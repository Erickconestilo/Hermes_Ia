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
- sincronización manual local ↔ VPS mediante Git local ya operativa para documentación y runbooks de `Hermes_Ia`
- autenticación `openai-codex` validada en Hermes
- respuesta funcional validada con `gpt-5.4-mini`

## Configuración actual del modelo

- proveedor principal: `openai-codex`
- modelo activo para trabajo ligero: `gpt-5.4-mini`
- fallback temporal: `OpenRouter`
- modelo fallback actual: `nvidia/nemotron-3-ultra-550b-a55b:free`

## Estado de credenciales

- `openai-codex` ya está autenticado en Hermes.
- OpenRouter se mantiene configurado como fallback mediante entorno local, sin documentar ni versionar la clave.
- `hermes doctor` ya valida `OpenAI Codex auth` y `OpenRouter API`.

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

- usar Hermes como operador de arranque y priorización diaria del proyecto piloto
- pedir una sola tarea concreta, pequeña y útil que no esté ya hecha
- ejecutar tareas de documentación o coordinación solo si aportan valor real inmediato

## Flujo operativo real

- local: editar archivos, revisar `git diff`, hacer commit y `git push vps master`
- VPS: entrar por `ssh` como `hermes`, ir a `/home/hermes/workspace/Hermes_Ia` y abrir `hermes`
- Git ya no debe usarse con copias manuales archivo a archivo salvo incidencia excepcional

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
