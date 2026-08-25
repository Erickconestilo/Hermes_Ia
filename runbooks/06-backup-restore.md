# 06 - Backup y restore

## Objetivo

Respaldar el estado mínimo de Hermes sin mezclar secretos en el repositorio.

## Alcance inicial

- `/home/hermes/.hermes`
- `/home/hermes/workspace`
- `/home/hermes/.config/systemd/user` (unidades de gateway, sin activarlas al restaurar)

## Reglas

- no guardar backups con secretos dentro del repositorio
- no versionar dumps con tokens o claves
- documentar nombre, fecha y origen del backup

## Backup

Ejecutar como usuario `hermes` en el VPS. Genera un tar comprimido con fecha en el nombre, fuera del repositorio Git.

```bash
mkdir -p /home/hermes/backups
FECHA="$(date +%Y%m%d-%H%M%S)"
tar -czf "/home/hermes/backups/hermes-backup-${FECHA}.tar.gz" \
  -C /home/hermes .hermes workspace .config/systemd/user
ls -lh /home/hermes/backups/
```

Notas:

- el tar incluye `/home/hermes/.hermes/.env` (con el token real de Telegram) y `/home/hermes/.hermes/data/ciudadanoinusual/capturas.jsonl`. El archivo resultante es sensible: no debe subirse a Git, ni a un servicio en la nube sin cifrar, ni compartirse por Telegram.
- copiar el `.tar.gz` fuera del VPS periódicamente (por ejemplo a un portátil o a un storage cifrado) es responsabilidad manual hasta que exista una politica de retención. No hay backup real si solo vive en el mismo servidor que falla.

## Restore (procedimiento de verificación)

Objetivo: comprobar que un backup existente realmente se puede restaurar, sin tocar el `hermes` en producción.

Riesgo: bajo si se restaura en una ruta temporal distinta de `/home/hermes`. Alto si se restaura sobre `/home/hermes` en caliente.

Alternativa más segura: restaurar siempre primero en una ruta temporal (`/home/hermes/restore-test/`) y comparar antes de reemplazar nada real.

Pasos:

```bash
# 1. Elegir el backup a probar
BACKUP="/home/hermes/backups/hermes-backup-<FECHA>.tar.gz"

# 2. Restaurar en una ruta temporal, nunca sobre /home/hermes directamente
mkdir -p /home/hermes/restore-test
tar -xzf "$BACKUP" -C /home/hermes/restore-test

# 3. Verificar que el contenido esperado existe
ls /home/hermes/restore-test/.hermes
ls /home/hermes/restore-test/workspace
test -f /home/hermes/restore-test/.hermes/data/ciudadanoinusual/capturas.jsonl && echo "capturas.jsonl OK"
test -f /home/hermes/restore-test/.hermes/.env && echo ".env OK"

# 3b. Verificar ambos perfiles sin leer el contenido de sus secretos
test "$(stat -c '%a' /home/hermes/restore-test/.hermes/.env)" = "600" && echo "default .env mode OK"
test -f /home/hermes/restore-test/.hermes/profiles/auscultacion/.env && echo "auscultacion .env OK"
test "$(stat -c '%a' /home/hermes/restore-test/.hermes/profiles/auscultacion/.env)" = "600" && echo "auscultacion .env mode OK"

# 3c. Verificar que las dos unidades se restauraron como archivos
test -f /home/hermes/restore-test/.config/systemd/user/hermes-gateway.service && echo "default unit OK"
test -f /home/hermes/restore-test/.config/systemd/user/hermes-gateway-auscultacion.service && echo "auscultacion unit OK"

# 4. Verificar que capturas.jsonl es JSON valido linea a linea
python3 -c "
import json
path = '/home/hermes/restore-test/.hermes/data/ciudadanoinusual/capturas.jsonl'
with open(path, encoding='utf-8') as f:
    n = 0
    for line in f:
        line = line.strip()
        if not line:
            continue
        json.loads(line)
        n += 1
print(f'{n} capturas validas')
"

# 5. Limpiar la prueba
rm -rf /home/hermes/restore-test
```

Rollback: el paso 5 es el propio rollback; la prueba nunca toca `/home/hermes/.hermes` ni `/home/hermes/workspace` reales.

La comprobacion anterior valida presencia, permisos y archivos de unidad
restaurados. No ejecuta `systemctl`, no instala las unidades y no activa ningun
gateway. El estado de los servicios en produccion se comprueba aparte con
`systemctl --user is-active` para cada unidad.

Verificación de que la sesión sirvió: registrar en `learning/bitacora.md` la fecha, el nombre del backup probado, si `capturas.jsonl` fue válido, y si algo faltaba respecto a lo esperado.

## Pendiente

- definir cadencia de backup (cron one-shot manual por ahora; cron recurrente sigue siendo rojo según `AGENTS.md`)
- decidir destino externo del `.tar.gz` (fuera del VPS) y si conviene cifrarlo antes de moverlo
