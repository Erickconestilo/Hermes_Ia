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

## Ejecución realizada

- Se accedió inicialmente al VPS como `root` usando clave SSH dedicada.
- Se creó el usuario `hermes` con `adduser hermes`.
- Se añadió `hermes` al grupo `sudo`.
- Se prepararon las rutas:
  - `/home/hermes/.hermes`
  - `/home/hermes/workspace`
- Se asignó ownership a `hermes:hermes` sobre esas rutas.
- Se validó el entorno de `hermes`:
  - `whoami` -> `hermes`
  - `HOME` -> `/home/hermes`
  - `pwd` -> `/home/hermes`
  - `sudo -l` correcto

## Resultado esperado alcanzado

- `root` queda reservado para bootstrap y recuperación.
- `hermes` queda listo para operar Hermes con `sudo` cuando haga falta.
- La estructura base del proyecto en el VPS ya coincide con la decisión arquitectónica.

## Verificaciones útiles

- `id hermes`
- `ls -ld /home/hermes /home/hermes/.hermes /home/hermes/workspace`
- `sudo -l` ejecutado como `hermes`

## Pendiente siguiente

- Validar el método oficial exacto de instalación de Hermes antes de ejecutarlo.
- Ejecutar la instalación como `hermes`, no como `root`.
