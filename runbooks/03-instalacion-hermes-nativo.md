# 03 - Instalación Hermes nativo

## Objetivo

Instalar Hermes con el método oficial y más simple posible sobre Ubuntu, ejecutándolo como usuario `hermes`.

## Restricciones actuales

- No Docker al inicio
- no `--yolo`
- no dashboard público
- no API pública
- no MCPs al inicio
- no Playwright salvo exigencia oficial

## Lo que validaremos antes

- comando oficial vigente de instalación
- dependencias reales mínimas
- ubicación esperada del binario
- compatibilidad con Ubuntu LTS

## Nota oficial ya validada

La documentación oficial de Hermes publica un camino CLI para Linux sin Hermes Desktop:

- `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`

Además, el instalador oficial expone flags relevantes que encajan con esta estrategia:

- `--skip-setup`
- `--skip-browser`
- `--no-playwright`
- `--no-skills`
- `--hermes-home`

Esto no implica que debamos usarlos todos; solo deja constancia de que existen en el instalador oficial actual.

## Verificación esperada

- `hermes --version`
- `which hermes`
- `hermes doctor`

## Ejecución realizada

- La instalación se ejecutó como usuario `hermes`, no como `root`.
- Se usó el instalador oficial con flags alineados con la decisión del proyecto:
  - `--skip-setup`
  - `--skip-browser`
  - `--no-playwright`
  - `--hermes-home /home/hermes/.hermes`
- Resultado observado del instalador:
  - `uv` instalado en `/home/hermes/.hermes/bin`
  - Python `3.11.15` instalado
  - Node.js `22.22.3` instalado en `~/.hermes/node`
  - `git` detectado
  - `ripgrep` y `ffmpeg` instalados como dependencias opcionales útiles

## Incidencia encontrada

- Tras instalar, `hermes` no quedaba accesible desde el shell normal.
- La causa no fue una instalación rota, sino un `PATH` incompleto.
- Se verificó que el binario y el entorno virtual sí existían en `~/.hermes/hermes-agent/venv/bin` y `~/.local/bin`.

## Corrección aplicada

- Se añadió a `/home/hermes/.profile`:

```bash
export PATH="$HOME/.local/bin:$HOME/.hermes/bin:$HOME/.hermes/node/bin:$PATH"
```

- Después de recargar el perfil:
  - `which hermes` -> `/home/hermes/.local/bin/hermes`
  - `hermes --version` correcto
  - `which node` correcto
  - `node --version` correcto

## Resultado alcanzado

- Hermes quedó instalado de forma nativa bajo `/home/hermes/.hermes`.
- El usuario operativo sigue siendo `hermes`.
- No se instaló Docker, Playwright ni integraciones externas innecesarias en esta fase.

## Rollback esperado

- Si hubiera que deshacer la instalación, el punto principal a revisar es `/home/hermes/.hermes` y las líneas añadidas al `PATH` del usuario `hermes`.
- No ejecutar rollback destructivo sin snapshot o backup previo si ya existen sesiones o configuración útil.
