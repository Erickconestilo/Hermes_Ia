# 11 - Rotacion de tokens y claves

## Objetivo

Rotar secretos sin mezclar los perfiles `default` y `auscultacion`, sin escribir valores en Git y verificando el gateway correcto despues de cada cambio.

## Regla general

1. Generar el secreto nuevo antes de revocar el anterior cuando el proveedor lo permita.
2. Actualizar solo el `.env` del perfil que usa ese secreto.
3. Mantener permisos restrictivos y no imprimir el valor.
4. Reiniciar y verificar el servicio del perfil afectado.
5. Revocar el secreto anterior solo despues de validar el nuevo.
6. Registrar el hecho en `learning/bitacora.md`, nunca el valor.

## Perfiles y servicios

| Perfil | Configuracion | Gateway |
| --- | --- | --- |
| `default` | `/home/hermes/.hermes/.env` | `hermes-gateway.service` |
| `auscultacion` | `/home/hermes/.hermes/profiles/auscultacion/.env` | `hermes-gateway-auscultacion.service` |

Usar siempre `hermes -p <perfil>` o el wrapper del perfil para comprobar el estado correcto. No asumir que cambiar el `.env` principal actualiza `auscultacion`.

## Inventario de secretos

- `TELEGRAM_BOT_TOKEN`: `.env` del perfil cuyo bot se rota.
- `OPENROUTER_API_KEY`: `.env` de cada perfil que lo use.
- `GOOGLE_API_KEY`: `.env` de cada perfil que use Google AI Studio o el fallback correspondiente.
- `FAL_KEY`: `.env` del perfil que use generacion de imagenes.
- Autenticacion `openai-codex`: estado de autenticacion interno del perfil, no un valor para copiar al repositorio.
- Clave SSH del VPS: privada en el equipo local y publica en `authorized_keys` del VPS.

## Telegram

1. Revocar y generar el token desde `@BotFather`.
2. Escribirlo en el `.env` del perfil correcto con permisos `600`.
3. Reiniciar solo el gateway correspondiente:

```bash
hermes gateway restart
hermes gateway status
hermes -p auscultacion gateway restart
hermes -p auscultacion gateway status
```

4. Enviar `hola` desde el movil y confirmar respuesta.

Rollback: el token anterior deja de ser valido al revocarlo; si el nuevo falla, generar otro y repetir. No existe rollback al token revocado.

## OpenRouter, Google AI Studio y FAL

1. Crear una clave nueva en el proveedor.
2. Actualizar la variable en el `.env` del perfil afectado.
3. Comprobar con `hermes -p <perfil> doctor` o una peticion inocua del perfil.
4. Reiniciar y verificar `hermes-gateway.service` o `hermes-gateway-auscultacion.service`.
5. Revocar la clave antigua.

Rollback: conservar la clave anterior hasta comprobar el nuevo flujo; si ya fue revocada, generar una nueva en el proveedor.

## Autenticacion openai-codex

Gestionarla con el flujo oficial de autenticacion del perfil. Verificar primero el comando disponible y ejecutar logout/login solo en el perfil afectado. Comprobar despues `hermes -p <perfil> doctor` y su gateway.

Rollback: repetir la autenticacion oficial con una sesion valida; no copiar tokens de autenticacion entre perfiles.

## Clave SSH del VPS

1. Generar una clave nueva en el equipo local.
2. Añadir la clave publica al `authorized_keys` del usuario `hermes`.
3. Probar una segunda conexion con la clave nueva.
4. Solo entonces retirar la clave antigua y actualizar el alias local.

Rollback: conservar la clave antigua hasta verificar la nueva; si se retiro, añadir de nuevo su clave publica desde una sesion aun abierta o mediante el acceso administrativo autorizado.

## Rotacion tras incidente

1. Tratar el secreto como comprometido y no esperar a confirmar el alcance.
2. Revocar primero en el proveedor, salvo que se necesite una ventana controlada para evitar caida.
3. Generar un valor nuevo y actualizar todos los perfiles donde aparecia el secreto.
4. Reiniciar y verificar cada gateway afectado por separado.
5. Revisar Git, logs y sesiones para retirar copias expuestas sin imprimirlas.
6. Revisar permisos, allowlists y destinos autorizados.
7. Registrar fecha, secreto afectado, alcance, verificacion y acciones pendientes sin escribir el valor.

## Registro

Toda rotacion real debe dejar una entrada breve en `learning/bitacora.md`. Nunca escribir el secreto viejo, el nuevo, tokens, cookies ni credenciales.
