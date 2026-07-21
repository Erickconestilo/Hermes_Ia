# 10 - Comandos nativos y botones en Telegram

## Objetivo

Eliminar la memorizacion de comandos en el uso movil de `Hermes Creador`. Hoy hace falta recordar palabras (`guion`, `post`, `carrusel`, `hoy`, `publicado`, `guarda`). El objetivo es que en la calle no haga falta recordar nada: se pulsa `/` y Telegram muestra el menu, o se pulsa un boton en la propia respuesta de Hermes.

Motivo: uso real registrado en `learning/bitacora.md` — el sistema de palabras genero fricción y abandono ("me lie y termine aburriendome"). Un menu nativo y botones tactiles no se olvidan porque no hace falta recordarlos: los ensena la propia interfaz.

## Por que es zona roja

`AGENTS.md` clasifica "cambios en la configuracion del gateway de Telegram fuera de pruebas no destructivas" como rojo: requiere permiso explicito previo. `QUEUE.md` lo lista en "no entra todavia".

**Permiso concedido:** 2026-07-21, en conversacion directa con Erick, al elegir explicitamente la opcion "botones reales en Telegram" frente a la alternativa de solo simplificar el documento. Registrar esta fecha en `learning/bitacora.md` al ejecutar.

## Por que no se ejecuta desde aqui

Esta sesion de trabajo no tiene acceso SSH al VPS `hermes-01`. Los pasos de este runbook deben ejecutarse tu, o en una sesion futura con acceso al VPS. Este documento deja todo listo para copiar y pegar.

## Riesgo y rollback

Riesgo: bajo en la Fase 1 (es una llamada a la API de Telegram, reversible al instante). Riesgo: medio en la Fase 2 (toca codigo del gateway en `HERMES_HOME`, que ya se ha editado antes con exito segun `runbooks/09-telegram-gateway.md`, seccion "Recuperacion humana con copia").

Rollback Fase 1: volver a llamar `setMyCommands` con una lista vacia, o con la lista anterior.
Rollback Fase 2: restaurar la copia del archivo de gateway hecha antes de editar (paso 0 de la Fase 2).

---

## Fase 1 - Menu nativo `/` (hacer primero, es la de menor riesgo)

Telegram permite registrar una lista de comandos que aparece al pulsar el icono `/` o el boton de menu del chat. El usuario no escribe nada: toca `/`, ve la lista con descripcion, y elige.

Esto no cambia como Hermes interpreta el texto. `/hoy` sigue siendo simplemente el texto `/hoy` cuando llega a Hermes — el `/` inicial es una convencion de Telegram para mostrar el menu, no magia adicional. Por eso este primer paso es seguro: en el peor caso, si Hermes no reconoce el `/` inicial, basta con que la palabra despues de la barra siga funcionando igual que hoy (`hoy`, `guion`, etc.), y se ajusta la deteccion en el prompt/skill si hace falta.

### Paso 1 - Conectar al VPS

```bash
ssh -i $HOME/.ssh/hermes_hetzner_ed25519 hermes@<HETZNER_VPS_IP>
cd /home/hermes/workspace/Hermes_Ia
source /home/hermes/.profile
```

### Paso 2 - Registrar el menu de comandos

Ejecutar en el VPS, donde ya vive el token real:

```bash
source /home/hermes/.hermes/.env

curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/setMyCommands" \
  -H "Content-Type: application/json" \
  -d '{
    "commands": [
      {"command": "hoy", "description": "Que toca hoy - una recomendacion editorial"},
      {"command": "guion", "description": "Convertir en guion de video corto"},
      {"command": "post", "description": "Convertir en post o caption"},
      {"command": "carrusel", "description": "Convertir en carrusel"},
      {"command": "publicado", "description": "Registrar una publicacion real"},
      {"command": "guarda", "description": "Nota privada, no es contenido"}
    ]
  }'
```

Respuesta esperada: `{"ok":true,"result":true}`.

### Paso 3 - Verificar en el telefono

Abrir el chat de Telegram con el bot, pulsar el icono `/` o escribir `/`. Debe aparecer la lista de seis comandos con su descripcion, tocable sin escribir nada mas.

### Paso 4 - Probar cada comando real

Tocar `/hoy` desde el menu (no escribirlo a mano) y confirmar que Hermes responde igual que si se hubiera escrito `hoy`. Repetir con `/guion`, `/post`, `/carrusel`, `/publicado`, `/guarda`.

Si alguno falla porque Hermes no reconoce el `/` inicial: la correccion es que la skill/prompt de enrutado trate `/hoy`, `/guion`, etc. como alias exactos de `hoy`, `guion`, etc. (quitar la barra antes de interpretar). Esto se ajusta en el mismo lugar donde ya se corrigio el parseo de `Privacidad: no publicar` (ver incidencia "Skill experimental que se quedaba en trazas de herramientas" en `runbooks/09-telegram-gateway.md`).

### Registrar en bitacora

Al terminar la Fase 1, anadir entrada en `learning/bitacora.md` con: fecha, comandos registrados, resultado de la prueba del paso 4, y si hizo falta el ajuste de alias.

---

## Fase 2 - Botones tactiles en la respuesta (hacer despues, mas trabajo)

Objetivo: cuando Hermes propone un formato ("esto parece un post"), la respuesta incluye botones para confirmar o cambiar, en vez de tener que escribir la palabra correcta.

Ejemplo de lo que deberia verse en el chat:

```text
Hermes: Esto tiene pinta de post — foto de comida en ruta, sin
identificadores visibles.

[ Usar como post ]  [ Prefiero guion ]  [ Prefiero carrusel ]  [ Guardar privado ]
```

### Por que esto ya es posible en este proyecto

`runbooks/09-telegram-gateway.md`, seccion "Recuperacion humana con copia" (2026-06-22), registra que ya se parcheo el gateway real en `HERMES_HOME` para anadir botones `Copiar ID 1..5` a las respuestas de recuperacion de capturas. La capacidad tecnica ya existe y ya funciono en produccion. Esto no es un experimento nuevo: es extender un patron ya probado a un caso de uso distinto.

### Por que este runbook no trae el diff exacto

El parche vive en `HERMES_HOME` en el VPS, fuera de este repositorio Git (igual que el resto de la capa de runtime de Hermes). Esta sesion no tiene visibilidad de ese archivo. Los pasos siguientes son el procedimiento, no el codigo final.

### Paso 0 - Copia de seguridad

Antes de tocar nada, localizar el archivo que ya anade los botones de `Copiar ID` y copiarlo:

```bash
# el nombre exacto depende de como quedo organizado HERMES_HOME;
# buscar por el texto de los botones ya conocidos
grep -rl "Copiar ID" /home/hermes/.hermes/ 2>/dev/null
```

Copiar el archivo encontrado con sufijo de fecha antes de editar.

### Paso 1 - Entender el patron existente

Leer como esta construido el teclado de botones de `Copiar ID` (probablemente un `inline_keyboard` de la API de Telegram, con filas de botones y un `callback_data` por boton). Ese mismo mecanismo es el que hay que reutilizar.

### Paso 2 - Anadir el teclado a las respuestas de `Hermes Creador`

Cuando la skill de contenido (la que hoy interpreta `guion`/`post`/`carrusel`/Nivel 0) propone un formato, adjuntar un `inline_keyboard` con las opciones relevantes. Cada boton debe llevar en su `callback_data` la accion exacta (equivalente a que el usuario hubiera escrito esa palabra).

### Paso 3 - Manejar la pulsacion del boton

El gateway debe recibir el `callback_query` cuando se pulsa un boton y tratarlo exactamente como si el usuario hubiera escrito el texto correspondiente (`post`, `guion`, `carrusel`, `guarda`). Si el patron de `Copiar ID` ya resuelve un `callback_query`, extender esa misma funcion en vez de crear una nueva.

### Paso 4 - Probar en real

Mandar una foto sin comando, confirmar que la respuesta trae botones, pulsar uno y confirmar que Hermes actua igual que si se hubiera escrito la palabra.

### Rollback

Restaurar el archivo copiado en el Paso 0 y reiniciar el gateway:

```bash
hermes gateway restart
```

### Registrar en bitacora

Fecha, que boton se probo, resultado, y si el `callback_data` quedo documentado en `SKILLS-EXPERIMENTALES.md` (si el cambio vive como skill) o directamente en este runbook (si es del gateway base).

---

## Como queda el uso una vez hecho esto

Antes (hoy, sin este cambio): memorizar seis palabras o escribirlas mal y perder la respuesta.

Despues de la Fase 1: pulsar `/`, ver la lista, tocar una.

Despues de la Fase 2: ni siquiera eso — mandar la foto o la nota, y tocar el boton que Hermes ya propuso.

El Nivel 0 de `COMANDOS.md` ("manda lo que sea, Hermes decide") sigue siendo el camino principal. Este runbook no lo sustituye: lo hace mas facil de confirmar o corregir sin escribir nada.

## Relacion con otros archivos

- `projects/hermes_ia/content/ciudadanoinusual/COMANDOS.md`: las seis palabras siguen validas como respaldo (escritorio, o si el menu nativo falla).
- `runbooks/09-telegram-gateway.md`: precedente tecnico del parche de botones y comandos de referencia del gateway.
- `projects/hermes_ia/SKILLS-EXPERIMENTALES.md`: si el cambio de Fase 2 se implementa como skill, registrarlo ahi.
