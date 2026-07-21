#!/usr/bin/env bash
# Detector simple de secretos antes de commitear.
#
# No requiere instalar gitleaks ni ninguna herramienta nueva (AGENTS.md
# pide no instalar mas herramientas sin necesidad real). Es un grep con
# patrones conocidos sobre lo que esta en stage para el proximo commit.
#
# Uso manual:
#   bash scripts/verificar-secretos.sh
#
# Uso como hook (ver runbooks/02-seguridad.md para instalarlo):
#   se ejecuta solo, antes de cada `git commit`.
#
# Si encuentra algo sospechoso, termina con codigo != 0 y lista los
# archivos y lineas. No borra ni modifica nada.

set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

# Archivos que van a entrar en el proximo commit (staged), excluyendo
# los que ya se borraron (no tiene sentido escanear un archivo eliminado).
mapfile -t staged_files < <(git diff --cached --name-only --diff-filter=ACMR)

if [ "${#staged_files[@]}" -eq 0 ]; then
  echo "verificar-secretos: no hay archivos en stage, nada que revisar."
  exit 0
fi

found=0

# Patrones de secretos con forma reconocible.
# Cada patron: descripcion | regex extendida (grep -E)
patterns=(
  "clave OpenAI (sk-...)|sk-[A-Za-z0-9]{20,}"
  "token de GitHub (ghp_/gho_/ghu_/ghs_/ghr_)|gh[pousr]_[A-Za-z0-9]{30,}"
  "token de bot de Telegram|[0-9]{8,10}:AA[A-Za-z0-9_-]{30,}"
  "clave privada (RSA/OPENSSH/EC/DSA)|-----BEGIN (RSA |OPENSSH |EC |DSA |)PRIVATE KEY-----"
  "clave de acceso AWS|AKIA[0-9A-Z]{16}"
)

echo "verificar-secretos: revisando ${#staged_files[@]} archivo(s) en stage..."

for entry in "${patterns[@]}"; do
  desc="${entry%%|*}"
  regex="${entry#*|}"
  matches="$(git diff --cached -U0 -- "${staged_files[@]}" 2>/dev/null | grep -EnH -e "$regex" || true)"
  if [ -n "$matches" ]; then
    echo ""
    echo "POSIBLE SECRETO ($desc):"
    echo "$matches"
    found=1
  fi
done

# IPs publicas: en este repo la regla es no versionar la IP real del VPS,
# siempre usar el placeholder <HETZNER_VPS_IP>. Se excluyen direcciones
# de uso general que no son sensibles (loopback, sin sentido, comodines).
ip_matches="$(git diff --cached -U0 -- "${staged_files[@]}" 2>/dev/null \
  | grep -EnH -e '([0-9]{1,3}\.){3}[0-9]{1,3}' \
  | grep -Ev -e '0\.0\.0\.0|127\.0\.0\.1|255\.255\.255\.255|<HETZNER_VPS_IP>' || true)"
if [ -n "$ip_matches" ]; then
  echo ""
  echo "POSIBLE IP REAL VERSIONADA (deberia ser <HETZNER_VPS_IP> si es el VPS):"
  echo "$ip_matches"
  found=1
fi

if [ "$found" -eq 1 ]; then
  echo ""
  echo "verificar-secretos: encontrado algo que revisar arriba."
  echo "Si es un falso positivo, revisa igualmente antes de forzar el commit."
  exit 1
fi

echo "verificar-secretos: sin coincidencias. OK."
exit 0
