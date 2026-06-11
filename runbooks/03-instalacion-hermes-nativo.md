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

## Rollback esperado

Pendiente de documentar tras validar el método oficial exacto.
