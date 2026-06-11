# 02 - Usuario hermes y seguridad

## Objetivo

Crear un usuario dedicado `hermes` para ejecutar Hermes sin operar como `root`.

## Decisión

- `root` solo para bootstrap inicial y tareas administrativas puntuales.
- `hermes` como usuario de ejecución habitual.
- datos en `/home/hermes/.hermes`
- workspace en `/home/hermes/workspace`

## Beneficios

- Reduce impacto de errores operativos.
- Hace más legibles permisos y ownership.
- Simplifica backups del entorno del agente.

## Riesgos

- Si se configuran mal permisos o PATH, Hermes puede instalarse en una ubicación inesperada.
- Cambios de SSH o `sudoers` mal hechos pueden romper acceso.

## Pendiente

Documentar:

- creación del usuario
- pertenencia a grupos si hiciera falta
- permisos de directorios
- verificación de `HOME`, `PATH` y ownership
