# 01 - Estado actual

## Objetivo

Tener una foto técnica breve y fiable del estado actual de `Hermes_Ia` sin tener que reconstruirla desde conversaciones o varios archivos dispersos.

## Infraestructura actual

- VPS: `hermes-01`
- proveedor: `Hetzner`
- plan: `CX33 x86`
- región: `Nuremberg`
- sistema operativo: `Ubuntu 24.04.4 LTS`

## Instalación validada

A fecha actual, ya se ha validado lo siguiente:

- acceso SSH al VPS
- actualización base del sistema
- creación del usuario `hermes` con `sudo`
- preparación de rutas de trabajo
- instalación nativa de Hermes como usuario `hermes`
- corrección del `PATH` en `/home/hermes/.profile`
- funcionamiento de:
  - `hermes --version`
  - `node --version`
- configuración de OpenRouter
- funcionamiento de Hermes con modelo principal y fallback

## Configuración actual del modelo

- proveedor operativo: `OpenRouter`
- modelo principal: `nex-agi/nex-n2-pro:free`
- fallback: `nvidia/nemotron-3-ultra-550b-a55b:free`

## Estado de credenciales

- OpenRouter está configurado mediante entorno local, sin documentar ni versionar la clave.
- `hermes doctor` ya valida `OpenRouter API`.

## Advertencias no bloqueantes

Quedan abiertas, pero no impiden el uso actual:

- `config.yaml` pendiente de migración de `v0` a `v29`
- Docker no instalado
- Playwright Chromium no instalado
- Telegram y Discord no instalados
- skills hub no inicializado

## Decisiones vigentes

- Hermes corre de forma nativa
- el usuario operativo es `hermes`
- el backend actual es `local`
- no se expone dashboard público
- no se expone API pública
- no se activa Telegram todavía
- no se activan MCPs todavía
- no se instala Playwright todavía salvo necesidad real

## Proyecto piloto actual

El único proyecto piloto inicial del sistema de trabajo con IA es:

- `Hermes_Ia`

Todavía no se extiende esta estructura a:

- `TopoField`
- `TopoTask`

## Estado de fase actual

- Fase 0 documental: cerrada
- Fase 1: iniciada en modo controlado

## Siguiente paso permitido en Fase 1

El siguiente paso permitido es de uso práctico básico:

- usar Hermes como asistente documental del proyecto piloto
- usar Hermes como ritual de arranque de sesión
- validar una primera acción pequeña y útil sin tocar configuración

## Qué no toca esta fase

Esta fase no incluye:

- `hermes doctor --fix`
- Docker
- Playwright
- cron
- Telegram
- memoria externa
- perfiles o subagentes
- cambios sobre otros proyectos
