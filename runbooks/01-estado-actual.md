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
- configuración histórica de OpenRouter
- sincronización manual local ↔ VPS mediante Git local ya operativa para documentación y runbooks de `Hermes_Ia`
- autenticación `openai-codex` validada en Hermes
- respuesta funcional validada con `gpt-5.6-terra` en el runtime el 2026-08-21
- Google AI Studio validado como proveedor temporal mediante endpoint compatible con OpenAI
- perfiles `default` y `auscultacion` configurados con `gemini-3.6-flash` el 2026-08-25
- Telegram Gateway configurado y autorizado solo para el usuario permitido
- el perfil `auscultacion` dispone de bot y gateway propios, aislados del perfil `default`

## Configuración actual del modelo

- perfil `default`:
  - proveedor actual: `Google AI Studio` mediante compatibilidad OpenAI
  - modelo actual: `gemini-3.6-flash`
- perfil `auscultacion`:
  - proveedor actual: `Google AI Studio` mediante compatibilidad OpenAI
  - modelo actual: `gemini-3.6-flash`
- proveedor principal anterior: `openai-codex`
- modelo principal anterior: `gpt-5.6-terra`
- bloqueo actual del principal anterior: `429 usage_limit_reached` hasta el 2026-08-31

## Estado de credenciales

- Cada perfil mantiene su propio `.env` en `/home/hermes/.hermes/profiles/<perfil>/.env`; no se versionan secretos.
- La presencia de una credencial en `hermes auth list` no sustituye la comprobación del `.env` del perfil.
- `openai-codex` ya fue autenticado y validado antes del bloqueo por cuota.
- OpenRouter queda como integración histórica validada, no como proveedor activo actual.

## Advertencias no bloqueantes

Quedan abiertas, pero no impiden el uso actual:

- `config.yaml` migrado y validado como `v33`
- Docker no instalado
- Playwright Chromium no instalado
- Discord no instalado
- skills hub no inicializado
- Google AI Studio usa nivel gratuito y está sujeto a límites de tasa/cuota
- `hermes prompt-size` muestra aproximadamente 15K tokens de prompt fijo por mensaje

## Decisiones vigentes

- Hermes corre de forma nativa
- el usuario operativo es `hermes`
- el backend actual es `local`
- los perfiles son instancias aisladas y deben configurarse/reiniciarse explícitamente por perfil
- no se expone dashboard público
- no se expone API pública
- Telegram queda operativo solo como canal móvil autorizado
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
- cambios adicionales de Telegram fuera de los gateways ya validados
- memoria externa
- perfiles adicionales o subagentes sin necesidad demostrada
- cambios sobre otros proyectos
