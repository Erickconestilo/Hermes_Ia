# 04 - Configuración del modelo

## Objetivo

Configurar el proveedor de modelo de forma estable, reversible y sin versionar secretos.

## Proveedores validados en este entorno

- `openai-codex`: autenticado y usado con `gpt-5.6-terra` hasta agotar cuota.
- `OpenRouter`: validado previamente como capa de modelos.
- `Google AI Studio`: validado mediante su endpoint compatible con OpenAI.

Para Google AI Studio, la Base URL funcional en Hermes es `https://generativelanguage.googleapis.com/v1beta/openai`; `/v1beta` sin `/openai` corresponde a la API nativa y no funciona con esta integración.

## Estado desde 2026-08-25

- Perfil `default`: `gemini-3.6-flash` vía Google AI Studio.
- Perfil `auscultacion`: `gemini-3.6-flash` vía Google AI Studio.
- Principal anterior: `gpt-5.6-terra` / `openai-codex`, bloqueado por `429 usage_limit_reached` hasta el 2026-08-31.
- Backup previo: `hermes-backup-2026-08-25-084745.zip`.

## Notas operativas

1. Los perfiles son instancias aisladas: cada uno tiene configuración, `/home/hermes/.hermes/profiles/<perfil>/.env` y gateway propios. Todo comando de configuración necesita `-p <perfil>` o actúa sobre `default`.
2. `hermes auth list` puede mostrar una credencial que el perfil no tiene realmente; la fuente de verdad es el `.env` del perfil.
3. Orden obligatorio: configurar primero y reiniciar después el gateway del perfil correcto (`hermes-gateway-<perfil>.service`, no asumir `hermes-gateway.service`).
4. `Provider authentication failed` no identifica la causa: puede ocultar un `503` de saturación o credenciales ausentes. Diagnosticar primero con `curl` directo al endpoint.
5. `gemini-3.7-flash` devolvió `503` por alta demanda; `gemini-3.6-flash` funcionó. `gemini-2.5-flash` no está disponible para usuarios nuevos en este entorno.
6. La integración de Google AI Studio se hace por la capa compatible con OpenAI; por eso la Base URL debe terminar en `/v1beta/openai`.

## Riesgos actuales

- Google AI Studio está en nivel gratuito y sujeto a límites de tasa/cuota.
- `hermes prompt-size` muestra ~15K tokens de prompt fijo por mensaje; ese coste de contexto contribuye al consumo rápido de cuota.
- No guardar API keys, tokens ni `.env` en Git.

## Historial mínimo

La primera etapa usó OpenRouter con `nex-agi/nex-n2-pro:free` y fallback `nvidia/nemotron-3-ultra-550b-a55b:free`. Después se validó `openai-codex`; el cambio a Gemini es temporal por agotamiento de cuota del proveedor principal.
