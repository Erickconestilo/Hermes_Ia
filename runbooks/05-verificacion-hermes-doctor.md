# 05 - Verificación Hermes Doctor

## Objetivo

Confirmar que la instalación quedó funcional antes de añadir integraciones.

## Checks mínimos

- `hermes --version` responde
- `which hermes` apunta al binario esperado
- `hermes doctor` no reporta fallos críticos
- el usuario `hermes` tiene acceso a su `HOME`
- existe el workspace esperado

## Si algo falla

Registrar:

- comando ejecutado
- salida exacta
- usuario que lo ejecutó
- PATH
- versión de Ubuntu

## Verificación realizada

- `which hermes` resolvió a `/home/hermes/.local/bin/hermes`
- `hermes --version` respondió correctamente
- `hermes doctor` confirmó:
  - entorno Python correcto
  - instalación de Hermes consistente
  - `git`, `rg`, Node.js y `agent-browser` operativos
  - `OpenRouter API` configurada correctamente

## Advertencias no bloqueantes observadas

- `Config version outdated (v0 -> v29)`
- `docker not found (optional)`
- `Playwright Chromium not installed`
- paquetes opcionales de Telegram y Discord no instalados
- skills hub todavía no inicializado

## Interpretación correcta

- Estas advertencias no bloquean la fase actual porque:
  - el backend deseado sigue siendo `local`
  - no queremos Docker todavía
  - no queremos Playwright todavía salvo exigencia real
  - Telegram Gateway ya esta operativo; no queremos Discord ni cambios adicionales de mensajeria en esta etapa

## Pruebas funcionales posteriores

- Hermes respondió: `Estoy usando nex-agi/nex-n2-pro:free a través de OpenRouter.`
- Hermes confirmó:
  - identidad: `Hermes Agent`
  - backend: terminal Linux integrado
  - directorio de trabajo actual: `/home/hermes`

## Pendiente razonable

- Evaluar más adelante `hermes doctor --fix` para migrar el archivo de configuración sin mezclar esa tarea con la instalación base.
