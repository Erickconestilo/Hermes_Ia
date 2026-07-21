# 11 - Rotación de tokens y claves

## Objetivo

Tener un procedimiento escrito para cuando un secreto se filtra o simplemente toca renovarlo, en vez de improvisar en caliente. Cubre los cuatro secretos reales que usa `Hermes_Ia` hoy: token de bot de Telegram, `OPENROUTER_API_KEY`, autenticación de `openai-codex`, y la clave SSH del VPS.

Motivo: señalado como hueco en `AUDITORIA-2026-07-21.md` — la higiene de secretos del repo es buena (nada versionado, `.gitignore` correcto, ahora además con `scripts/verificar-secretos.sh` como red de seguridad automática), pero no había ningún procedimiento de qué hacer el día que algo se filtra de verdad.

## Regla general antes de rotar cualquier cosa

1. Confirmar que realmente hace falta rotar (filtración real, sospecha razonable, o rotación preventiva programada).
2. Generar el secreto nuevo ANTES de revocar el viejo, cuando el proveedor lo permita — evita una ventana sin servicio.
3. Actualizar `/home/hermes/.hermes/.env` en el VPS con el valor nuevo.
4. Verificar que el servicio afectado sigue funcionando con el valor nuevo.
5. Solo entonces revocar el valor viejo en el proveedor.
6. Registrar en `learning/bitacora.md`: qué se rotó, por qué, y el resultado de la verificación. Nunca registrar el secreto en sí, solo el hecho de la rotación.

---

## Token de bot de Telegram

**Dónde vive:** `TELEGRAM_BOT_TOKEN` en `/home/hermes/.hermes/.env`.

**Riesgo si se filtra:** alguien puede enviar mensajes como el bot, leer comandos configurados, o interferir con el gateway. No da acceso al VPS en sí.

**Pasos:**

1. En Telegram, hablar con `@BotFather`.
2. `/mybots` → seleccionar el bot de Hermes → `API Token` → `Revoke current token`. BotFather genera uno nuevo automáticamente al revocar.
3. Copiar el token nuevo.
4. En el VPS: editar `/home/hermes/.hermes/.env` y reemplazar `TELEGRAM_BOT_TOKEN` por el valor nuevo.
5. `hermes gateway restart`.
6. Verificación: mandar `hola` al bot desde Telegram y confirmar respuesta (mismo test que `runbooks/09-telegram-gateway.md`).
7. El token viejo queda inválido automáticamente al revocarlo en el paso 2 — no hace falta ningún paso adicional de revocación.

**Rollback si algo falla:** si el gateway no responde tras el paso 5, revisar que no haya espacios o comillas accidentales al pegar el token nuevo en `.env`. El token viejo ya no sirve una vez revocado, así que no hay vuelta atrás — si el nuevo falla, hay que generar otro repitiendo el proceso.

---

## `OPENROUTER_API_KEY`

**Dónde vive:** `/home/hermes/.hermes/.env`, fallback del proveedor principal.

**Riesgo si se filtra:** uso no autorizado de la cuenta de OpenRouter, coste económico.

**Pasos:**

1. Entrar a [openrouter.ai](https://openrouter.ai), sección de API keys.
2. Crear una key nueva.
3. En el VPS: actualizar `OPENROUTER_API_KEY` en `/home/hermes/.hermes/.env`.
4. Verificar con `hermes doctor` que valida "OpenRouter API" (ver `runbooks/01-estado-actual.md`).
5. Volver a OpenRouter y revocar/borrar la key vieja.

**Rollback:** si `hermes doctor` falla con la key nueva, revisar que se copió completa y sin espacios antes de revocar la vieja.

---

## Autenticación de `openai-codex`

**Dónde vive:** gestionada por el propio `hermes`, no es una variable de `.env` de texto plano sino un estado de autenticación interno.

**Riesgo si se filtra:** depende de cómo esté implementada la sesión (token OAuth, API key); en general, acceso a la cuenta de OpenAI/Codex asociada.

**Pasos:**

1. En el VPS, como `hermes`: consultar la documentación oficial de `openai-codex` para el comando de logout/re-auth (típicamente algo como `codex auth logout` seguido de `codex auth login`, verificar el nombre exacto del comando instalado antes de ejecutar nada).
2. Volver a autenticar siguiendo el flujo oficial (probablemente un link OAuth a abrir desde el navegador).
3. Verificar con `hermes doctor` que "OpenAI Codex auth" sigue validando correctamente.
4. Si la sesión vieja no se invalida automáticamente al re-autenticar, revisar el panel de la cuenta OpenAI/Codex para revocar sesiones activas antiguas manualmente.

**Nota:** este es el secreto menos documentado de los cuatro porque nunca se ha rotado en la práctica. La primera vez que se ejecute este procedimiento, actualizar esta sección con los comandos exactos reales que funcionaron.

---

## Clave SSH del VPS (`hermes_hetzner_ed25519`)

**Dónde vive:** privada en `C:\Users\guill\.ssh\hermes_hetzner_ed25519` (local), pública en `~/.ssh/authorized_keys` del usuario `hermes` (y de `root` si aplica) en el VPS.

**Riesgo si se filtra la clave privada:** acceso completo al VPS como el usuario correspondiente. Es el secreto de mayor impacto de los cuatro.

**Pasos:**

1. Generar un par de claves nuevo en local:
   ```
   ssh-keygen -t ed25519 -f C:\Users\guill\.ssh\hermes_hetzner_nueva -C "hermes-vps-rotada-$(date +%Y%m%d)"
   ```
2. Copiar la clave **pública** nueva al VPS. Si todavía se puede entrar con la clave vieja:
   ```
   ssh -i C:\Users\guill\.ssh\hermes_hetzner_ed25519 hermes@<HETZNER_VPS_IP> "echo '<contenido-de-la-clave-publica-nueva>' >> ~/.ssh/authorized_keys"
   ```
3. **Antes de borrar nada**, verificar que la clave nueva entra: abrir una terminal distinta y probar `ssh -i C:\Users\guill\.ssh\hermes_hetzner_nueva hermes@<HETZNER_VPS_IP>`.
4. Solo si el paso 3 funciona: editar `~/.ssh/authorized_keys` en el VPS y quitar la línea de la clave vieja.
5. Actualizar el alias local `hermes` en `C:\Users\guill\.ssh\config` para que apunte al archivo de clave nuevo.
6. Actualizar `core.sshCommand` en la configuración de Git del repo si apunta a la ruta de la clave vieja (`git config core.sshCommand`).
7. Borrar el archivo de la clave privada vieja en local, o guardarlo fuera del alcance normal si se prefiere conservar un tiempo por si acaso.

**Rollback:** no borrar la clave vieja del VPS (paso 4) hasta confirmar que la nueva funciona (paso 3). Mismo principio que el endurecimiento SSH de este mismo runbook: nunca cerrar el único camino de entrada sin haber verificado el nuevo primero.

---

## Registro

Cada rotación real ejecutada debe dejar una entrada en `learning/bitacora.md` con: fecha, qué se rotó, motivo (filtración / rutina / sospecha), y resultado de la verificación. Nunca escribir el valor del secreto, ni el viejo ni el nuevo.
