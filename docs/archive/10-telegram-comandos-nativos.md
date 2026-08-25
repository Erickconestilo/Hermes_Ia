# 10 - Comandos nativos y botones en Telegram (cerrado: no viable por el menu `/`)

## Resultado final (2026-07-21)

Este runbook documento un intento real que **no funciono como se esperaba** y quedo revertido. Se conserva completo porque el hallazgo tecnico es reutilizable si en el futuro se reconsidera.

**Conclusion:** no usar `setMyCommands` para publicitar los comandos de `Hermes Creador`. El menu `/` de Telegram es propiedad de Hermes Agent (gateway nativo) y se resetea en cada `hermes gateway restart` / `hermes update`, sobrescribiendo cualquier lista personalizada sin aviso. Mantenerlo habria significado volver a ejecutar el mismo `curl` despues de cada reinicio, para siempre — carga manual recurrente, justo lo contrario de lo que se buscaba.

**Solucion real adoptada:** el Nivel 0 de `projects/hermes_ia/content/ciudadanoinusual/COMANDOS.md` ("manda lo que sea, sin palabra clave, Hermes decide") ya resuelve la friccion de la calle sin depender de ningun registro de Telegram. Las seis palabras (`guion`, `post`, `carrusel`, `hoy`, `publicado`, `guarda`) siguen funcionando igual que siempre porque nunca dependieron del menu `/`: son texto plano interpretado por Hermes, no comandos de Telegram.

---

## Como se llego a esta conclusion

### Motivo original

Uso real reportado por Erick el 2026-07-21: incluso seis palabras generaron friccion en la calle ("me lie y termine aburriendome... es que hasta dificil de memorizar son"). Se propuso usar el menu nativo `/` de Telegram (tocar en vez de escribir) como solucion.

### Fase 1 ejecutada

Se registro el menu con `setMyCommands` (ver comando completo mas abajo). La API de Telegram confirmo el registro: `{"ok":true,"result":true}`, y `getMyCommands` inmediatamente despues devolvio los seis comandos correctamente.

### Lo que se rompio sin darnos cuenta

`setMyCommands` **sustituye** la lista completa del scope por defecto, no la amplia. Al registrar los seis, desaparecieron del menu tactil los ~24 comandos nativos de Hermes Agent (`/help`, `/status`, `/restart`, `/background`, `/approve`, `/rollback`, etc.).

Primera decision (parcial): aceptar la perdida del menu nativo, ya que esos comandos siguen funcionando escritos a mano aunque no aparezcan en el autocompletado.

### La prueba que cambio la decision

Erick reinicio el gateway (`hermes gateway restart`) para probar. Resultado: el menu volvio a mostrar los ~24 comandos nativos, y los seis de `Hermes Creador` desaparecieron. Verificado con `getMyCommands`, que devolvio la lista nativa completa, sin rastro de los seis.

**Conclusion tecnica confirmada:** el propio `hermes gateway` reafirma su lista de comandos nativos en cada arranque/reinicio (probablemente vía su propia llamada a `setMyCommands` al iniciar). Cualquier lista personalizada queda con vida util de "hasta el proximo restart".

### Decision final

Ante dos opciones — mantener el forcejeo (re-ejecutar el `curl` tras cada `restart`/`update`, indefinidamente) o abandonar el menu `/` como vector para los seis comandos — Erick eligio la segunda: restaurar el menu nativo de Hermes y apoyarse en el Nivel 0 de `COMANDOS.md` para la friccion de calle.

---

## Restaurar el menu nativo de Hermes

Ejecutar en el VPS si el menu `/` sigue mostrando solo los seis comandos de `Hermes Creador`:

```bash
source /home/hermes/.hermes/.env

curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/setMyCommands" \
  -H "Content-Type: application/json" \
  -d '{"commands":[{"command":"help","description":"Show available commands"},{"command":"new","description":"Start a new session (fresh session ID + history)"},{"command":"stop","description":"Kill all running background processes"},{"command":"status","description":"Show session info"},{"command":"resume","description":"Resume a previously-named session"},{"command":"sessions","description":"Browse and resume previous sessions"},{"command":"model","description":"Switch model for this session"},{"command":"debug","description":"Upload debug report (system info + logs) and get shareable links"},{"command":"restart","description":"Gracefully restart the gateway after draining active runs"},{"command":"update","description":"Update Hermes Agent to the latest version"},{"command":"commands","description":"Browse all commands and skills (paginated)"},{"command":"approve","description":"Approve a pending dangerous command"},{"command":"deny","description":"Deny a pending dangerous command"},{"command":"queue","description":"Queue a prompt for the next turn (doesn'"'"'t interrupt)"},{"command":"steer","description":"Inject a message after the next tool call without interrupting"},{"command":"background","description":"Run a prompt in the background"},{"command":"reasoning","description":"Manage reasoning effort and display"},{"command":"usage","description":"Show token usage and rate limits for the current session"},{"command":"platform","description":"Pause, resume, or list a failing gateway platform"},{"command":"profile","description":"Show active profile name and home directory"},{"command":"whoami","description":"Show your slash command access (admin / user)"},{"command":"start","description":"Acknowledge platform start pings without a reply"},{"command":"topic","description":"Enable or inspect Telegram DM topic sessions"},{"command":"retry","description":"Retry the last message (resend to agent)"},{"command":"undo","description":"Back up N user turns and re-prompt (default 1)"},{"command":"title","description":"Set a title for the current session"},{"command":"branch","description":"Branch the current session (explore a different path)"},{"command":"compress","description":"Compress conversation context (add '"'"'here [N]'"'"' to keep recent N turns)"},{"command":"rollback","description":"List or restore filesystem checkpoints"},{"command":"agents","description":"Show active agents and running tasks"}]}'
```

Verificar con `getMyCommands` (mismo patron que en los pasos anteriores) que devuelve la lista nativa completa.

En la practica, esto probablemente no hace falta ejecutarlo a mano: el propio `hermes gateway restart` ya lo hace por su cuenta, segun lo observado. Se deja aqui documentado por si algun dia el gateway no se reinicia solo y el menu se queda a medias.

---

## Que queda vigente para la friccion de la calle

`projects/hermes_ia/content/ciudadanoinusual/COMANDOS.md`, Nivel 0: mandar la foto, nota de voz o texto suelto, sin palabra clave. Hermes decide formato, revisa privacidad y da una version usable. No depende de Telegram, no se pierde en un reinicio, no hace falta recordar nada.

Las seis palabras (`guion`, `post`, `carrusel`, `hoy`, `publicado`, `guarda`) siguen disponibles como atajo cuando ya se sabe que se quiere, escribiendolas a mano. Nunca dependieron del menu `/` — eso fue exclusivamente el experimento fallido de este runbook.

---

## Fase 2 (botones tactiles) - re-evaluar bajo esta luz

La idea original de Fase 2 (botones bajo cada respuesta de Hermes, reutilizando el patron de "Copiar ID") sigue siendo tecnicamente distinta de este problema: esos botones se generan por mensaje, no como un registro estatico en Telegram, por lo que no deberian sufrir el mismo reseteo en cada restart.

Si en el futuro se retoma, verificar primero esa hipotesis con una prueba pequena antes de invertir mas tiempo, dado lo ocurrido aqui.

## Relacion con otros archivos

- `projects/hermes_ia/content/ciudadanoinusual/COMANDOS.md`: Nivel 0 es la solucion vigente para la friccion de calle.
- `runbooks/09-telegram-gateway.md`: comandos de referencia del gateway y precedente del patron de botones.
- `learning/bitacora.md`: registro cronologico completo del intento, el hallazgo y la decision final.
