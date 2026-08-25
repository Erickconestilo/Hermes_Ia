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
# Si encuentra algo sospechoso, termina con codigo != 0 y lista solo tipo,
# archivo y linea. Nunca imprime el contenido que coincidio. No borra ni
# modifica nada.

set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

# Archivos que van a entrar en el proximo commit (staged), excluyendo
# los que ya se borraron (no tiene sentido escanear un archivo eliminado).
mapfile -d '' -t staged_files < <(
  git -c core.quotePath=false diff --cached --name-only -z --diff-filter=ACMR
)

if [ "${#staged_files[@]}" -eq 0 ]; then
  echo "verificar-secretos: no hay archivos en stage, nada que revisar."
  exit 0
fi

found=0

# Muestra metadatos suficientes para localizar una coincidencia sin exponer
# el secreto o la IP que activo el detector.
report_match() {
  local kind="$1"
  local file="$2"
  local line="$3"

  printf 'POSIBLE %s: archivo=%q linea=%s\n' "$kind" "$file" "$line"
}

scan_staged_pattern() {
  local kind="$1"
  local regex="$2"
  local file line
  local -a lines

  for file in "${staged_files[@]}"; do
    # Se escanea el blob preparado para el commit, no el contenido sin guardar.
    # Se conserva solo el numero de linea antes de informar la coincidencia.
    mapfile -t lines < <(
      git show ":$file" 2>/dev/null \
        | grep -aEn -e "$regex" \
        | cut -d: -f1 \
        || true
    )

    for line in "${lines[@]}"; do
      report_match "$kind" "$file" "$line"
      found=1
    done
  done
}

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
  scan_staged_pattern "SECRETO tipo=$desc" "$regex"
done

# IPs publicas: en este repo la regla es no versionar la IP real del VPS,
# siempre usar el placeholder <HETZNER_VPS_IP>. Se excluyen direcciones
# de uso general que no son sensibles (loopback, sin sentido, comodines).
for file in "${staged_files[@]}"; do
  mapfile -t ip_lines < <(
    while IFS=: read -r line content; do
      has_real_ip=0
      while IFS= read -r ip; do
        case "$ip" in
          0.0.0.0|127.0.0.1|255.255.255.255|'<HETZNER_VPS_IP>') ;;
          *) has_real_ip=1; break ;;
        esac
      done < <(printf '%s\n' "$content" | grep -aoE '([0-9]{1,3}\.){3}[0-9]{1,3}' || true)
      if [ "$has_real_ip" -eq 1 ]; then
        printf '%s\n' "$line"
      fi
    done < <(
      git show ":$file" 2>/dev/null \
        | grep -aEn -e '([0-9]{1,3}\.){3}[0-9]{1,3}' \
        || true
    )
  )

  for line in "${ip_lines[@]}"; do
    report_match "IP REAL VERSIONADA" "$file" "$line"
    found=1
  done
done

if [ "$found" -eq 1 ]; then
  echo ""
  echo "verificar-secretos: encontrado algo que revisar arriba."
  echo "Si es un falso positivo, revisa igualmente antes de forzar el commit."
  exit 1
fi

echo "verificar-secretos: sin coincidencias. OK."
exit 0
