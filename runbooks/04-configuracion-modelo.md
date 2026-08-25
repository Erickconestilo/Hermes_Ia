# 04 - Configuracion del modelo

## Objetivo

Mantener dos perfiles aislados, con un proveedor principal estable, fallback
controlado y un coste operativo entendible.

## Proveedores soportados y alcance

Hermes permite configurar proveedores compatibles mediante su configuracion de
modelo y fallback. En esta instalacion solo se han validado en uso real:

- `openai-codex` como proveedor principal.
- `openrouter` como proveedor compatible de fallback.

Esto no es una lista exhaustiva de todos los proveedores que Hermes puede
admitir. Cualquier proveedor adicional requiere una prueba separada.

## Configuracion final aplicada

| Perfil | Uso | Principal | Fallback | Backend |
|---|---|---|---|---|
| `default` | CiudadanoInusual | `gpt-5.6-terra` via `openai-codex` | `google/gemini-3.7-flash` via `openrouter` | `local` |
| `auscultacion` | apoyo tecnico de campo | `gpt-5.6-luna` via `openai-codex` | `google/gemini-3.7-flash` via `openrouter` | `local` |

Cada perfil tiene configuracion y secretos separados:

- `/home/hermes/.hermes/config.yaml` y `/home/hermes/.hermes/.env`
- `/home/hermes/.hermes/profiles/auscultacion/config.yaml` y
  `/home/hermes/.hermes/profiles/auscultacion/.env`

El saldo prepago de OpenRouter queda limitado operativamente a 5 EUR como tope
de emergencia. Es una medida de presupuesto, no un secreto ni una garantia de
que un proveedor externo interprete el limite de la misma forma.

## Base URL y compatibilidad

- `openai-codex` usa la base compatible del runtime:
  `https://chatgpt.com/backend-api/codex`.
- OpenRouter usa `https://openrouter.ai/api/v1`.
- Para Google AI Studio con cliente compatible OpenAI, la base correcta es
  `https://generativelanguage.googleapis.com/v1beta/openai`, no la API nativa
  `https://generativelanguage.googleapis.com/v1beta`.

La URL debe corresponder al formato de API que espera el cliente. Una URL nativa
de Google y una URL compatible OpenAI no son intercambiables.

## Orden operativo obligatorio

1. Configurar el perfil correcto y revisar la configuracion no sensible.
2. Verificar proveedor, modelo, base URL y credencial sin imprimir secretos.
3. Reiniciar el gateway del mismo perfil.
4. Comprobar el servicio correcto:
   - `hermes-gateway.service` para `default`.
   - `hermes-gateway-auscultacion.service` para `auscultacion`.
5. Probar una peticion minima desde el canal correspondiente.

No reiniciar el gateway de otro perfil como sustituto. Los perfiles son
instancias aisladas.

## Optimizacion final de Telegram

Ambos perfiles quedaron con `agent.max_turns: 20`.

En Telegram se desactivaron en ambos perfiles:

- `session_search`
- `browser`
- `bfl` (video generation / BFL FLUX 3 Video)

Ademas, `image_gen` se mantiene en `default` y esta desactivado en
`auscultacion`. Se conservaron `vision`, `file`, `memory`, `skills`, `todo`,
`clarify` y `web`.

## Rollback completo de las dos pasadas

El rollback se ejecuta por perfil y despues reinicia su gateway.

### `default`

```bash
/home/hermes/.local/bin/hermes config set agent.max_turns 60
/home/hermes/.local/bin/hermes tools enable --platform telegram session_search browser bfl delegation tts
/home/hermes/.local/bin/hermes gateway restart
```

### `auscultacion`

```bash
/home/hermes/.local/bin/hermes -p auscultacion config set agent.max_turns 150
/home/hermes/.local/bin/hermes -p auscultacion tools enable --platform telegram session_search browser bfl image_gen delegation tts code_execution computer_use cronjob
/home/hermes/.local/bin/hermes -p auscultacion gateway restart
```

Estos comandos restauran los limites y herramientas desactivados en ambas
pasadas. No modifican proveedores, modelos ni secretos.

## Nota sobre secretos

Las claves viven solo en los `.env` de cada perfil y nunca deben aparecer en
Git, chat, capturas ni salidas compartidas. Si una clave se expone, debe
rotarse.
## Historial temporal de proveedor

En una ventana anterior se probó `gemini-3.6-flash` vía Google AI Studio porque
`openai-codex` había devuelto `429 usage_limit_reached`. Esa transición fue
temporal y no representa la configuración final verificada actualmente.

También quedó validado que `gemini-3.7-flash` puede responder `503 high demand`
y que los errores de proveedor deben diagnosticarse antes de cambiar el perfil.
