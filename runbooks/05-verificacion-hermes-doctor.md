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
