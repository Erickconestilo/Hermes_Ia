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
- configuración de `openai-codex` con fallback `openrouter`
- funcionamiento de Hermes con el modelo principal y fallback finales
- sincronización manual local ↔ VPS mediante Git local ya operativa para documentación y runbooks de `Hermes_Ia`
- autenticación `openai-codex` validada en Hermes
- respuesta funcional validada con `gpt-5.6-terra` en el runtime el 2026-08-21
- Telegram Gateway configurado, autorizado solo para el usuario permitido y validado desde movil
- servicios de usuario `hermes-gateway.service` y
  `hermes-gateway-auscultacion.service` activos con `systemd` y `linger`
  habilitado
- Google AI Studio también se validó temporalmente mediante endpoint compatible
  con OpenAI durante una ventana de cuota agotada.
- el perfil `auscultacion` dispone de bot y gateway propios, aislados del perfil
  `default`

## Configuracion final de modelos

| Perfil | Proveedor principal | Modelo principal | Fallback | Base fallback |
|---|---|---|---|---|
| `default` | `openai-codex` | `gpt-5.6-terra` | `google/gemini-3.7-flash` | `openrouter` |
| `auscultacion` | `openai-codex` | `gpt-5.6-luna` | `google/gemini-3.7-flash` | `openrouter` |

Ambos perfiles usan backend terminal `local`, tienen `agent.max_turns: 20` y
mantienen sus configuraciones y `.env` aislados.

OpenRouter tiene un saldo prepago de 5 EUR definido como tope operativo de
emergencia. No se versionan claves ni credenciales.

## Estado final de Telegram

Telegram sigue limitado a uso móvil autorizado. En ambos perfiles se retiraron
de ese canal `session_search`, `browser` y `bfl`; `image_gen` solo queda en
`default`. Se conservan `vision`, `file`, `memory`, `skills`, `todo`,
`clarify` y `web`. La tabla completa y los rollbacks están en
`runbooks/04-configuracion-modelo.md`.

## Estado de credenciales

- `openai-codex` ya está autenticado en Hermes.
- OpenRouter se mantiene configurado como fallback mediante el entorno de cada
  perfil, sin documentar ni versionar la clave.
- La autenticacion de `openai-codex` y la credencial de OpenRouter se mantienen
  separadas por perfil.
- Telegram usa token guardado en `/home/hermes/.hermes/.env`, no versionado en Git.

La transición temporal a Google AI Studio por un `429` de cuota queda
registrada en `learning/bitacora.md`; no es el estado final actual.

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
