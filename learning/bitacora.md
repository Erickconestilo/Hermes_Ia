# Bitácora

## 2026-06-11

- Se creó la estructura base del proyecto.
- Se fijó la decisión inicial: Hermes nativo en VPS Hetzner con usuario `hermes`.
- Se movió la transcripción del curso a [docs/curso-benjamin-hermes-transcripcion.md](../docs/curso-benjamin-hermes-transcripcion.md).
- Se dejó explícito que esa transcripción sirve como contexto, no como fuente exacta de comandos.
- Queda pendiente validar comandos con documentación oficial antes de tocar el VPS.

## 2026-06-12

- Se reforzó que la prioridad inmediata del proyecto es `Hermes IA`.
- Se documentó que el VPS de Hetzner puede servir más adelante como base para frontend, backend, bases de datos, observabilidad y automatización.
- Se dejó explícito que esa expansión futura no debe instalarse de golpe.
- Se cerró la decisión de proveedor en favor de `Hetzner`.
- Se creó el servidor `hermes-01` con plan `CX33`, `x86`, `Nuremberg` y `Ubuntu 24.04`.
- Se validó el acceso SSH inicial al VPS.
- El acceso sin forzar identidad cayó a autenticación por contraseña, lo que confirmó que el cliente SSH local no estaba usando por defecto la clave correcta.
- El acceso correcto se consiguió con `ssh -i $HOME/.ssh/hermes_hetzner_ed25519 root@<HETZNER_VPS_IP>`.
- Se verificó el estado base del servidor con `whoami`, `hostnamectl`, `pwd` y `ls -la /root`.
- Resultado de la verificación: acceso como `root`, hostname `hermes-01`, `Ubuntu 24.04.4 LTS`, arquitectura `x86-64` y home `/root`.
- Se actualizó Ubuntu y se confirmó que no quedaron paquetes pendientes con `apt list --upgradable`.
- Se creó el usuario `hermes`.
- Se añadió `hermes` al grupo `sudo`.
- Se crearon `/home/hermes/.hermes` y `/home/hermes/workspace` con ownership correcto.
- Se validó el entorno de `hermes`: `HOME`, `pwd`, `sudo` y estructura base correctos.
- Se validó el método oficial de instalación CLI de Hermes y se eligió una ejecución conservadora como usuario `hermes`.
- Se ejecutó el instalador oficial con enfoque mínimo: sin `setup`, sin browser inicial y sin Playwright.
- El instalador dejó `uv`, Python 3.11, Node.js 22, `ripgrep` y `ffmpeg` operativos en el entorno de `hermes`.
- Primera incidencia real tras instalar: `hermes` no quedaba disponible en el `PATH` del shell.
- Se verificó que el binario existía y se corrigió el `PATH` en `/home/hermes/.profile` para incluir:
  - `/home/hermes/.local/bin`
  - `/home/hermes/.hermes/bin`
  - `/home/hermes/.hermes/node/bin`
- Tras esa corrección, `which hermes`, `hermes --version` y `node --version` respondieron correctamente.
- `hermes doctor` confirmó instalación funcional, con advertencias esperables por componentes opcionales no instalados.
- Se configuró `terminal.backend: local` como base actual.
- Se configuró Hermes para usar `OpenRouter` con:
  - principal `nex-agi/nex-n2-pro:free`
  - fallback `nvidia/nemotron-3-ultra-550b-a55b:free`
- Segunda incidencia real: la variable `OPENROUTER_API_KEY` quedó comentada en `.env`, por lo que Hermes no detectaba credenciales.
- Se corrigió el `.env` quitando el `#` de `OPENROUTER_API_KEY`.
- `hermes doctor` pasó a validar `OpenRouter API` correctamente.
- Primera prueba funcional exitosa: Hermes respondió usando `nex-agi/nex-n2-pro:free` a través de OpenRouter.
- Segunda prueba funcional exitosa: Hermes confirmó identidad, backend terminal Linux integrado y directorio de trabajo `/home/hermes`.
- Queda pendiente decidir con calma si conviene ejecutar `hermes doctor --fix` para migrar `config.yaml` de `v0` a `v29`.

## 2026-06-13

- Se cerró la idea de usar `Hermes_Ia` como proyecto piloto inicial del sistema de trabajo con IA.
- Se decidió no escalar todavía el flujo documental ni operativo a `TopoField` ni `TopoTask`.
- Se aprobó una Fase 0 centrada solo en estabilizar documentación y estado actual, sin tocar configuración ni instalar nuevas herramientas.
- Se dejó como siguiente objetivo ordenar el proyecto piloto con un contexto claro, un estado actual centralizado y una lista mínima de tareas.
- Se pospuso cualquier decisión sobre `hermes doctor --fix`, subagentes, cron, Telegram, memoria externa o nuevas interfaces hasta después de consolidar la base documental.

## Ritual de arranque de sesion

Rellenar al inicio de cada sesion sobre `Hermes_Ia`.

### Arranque

- Fecha:
- Estado actual en 3 lineas:
- Documentos leidos:
  - `README.md`
  - `runbooks/01-estado-actual.md`
  - `projects/hermes_ia/CONTEXTO.md`
  - `projects/hermes_ia/TAREAS.md`

### 5 preguntas fijas

1. ?Donde esta el proyecto ahora?
2. ?Cual es la siguiente accion pequena y ejecutable?
3. ?Que valor practico aporta esa accion?
4. ?Que no debo intentar todavia?
5. ?Que tendria que quedar hecho para que la sesion haya valido la pena?

### Cierre

- Accion elegida:
- Resultado:
- Pendiente para la proxima sesion:
- Limites respetados:

## Sesion de arranque - 2026-06-14

### Arranque

- Fecha: 2026-06-14
- Estado actual en 3 lineas:
  - `Hermes_Ia` ya tiene base documental y contexto tecnico minimo.
  - Hermes funciona en el VPS con OpenRouter y backend local.
  - La fase actual es de uso practico inicial, sin tocar configuracion.
- Documentos leidos:
  - `README.md`
  - `runbooks/01-estado-actual.md`
  - `projects/hermes_ia/CONTEXTO.md`
  - `projects/hermes_ia/TAREAS.md`

### 5 preguntas fijas

1. ?Donde esta el proyecto ahora?
   - En Fase 1 controlada, con infraestructura base y documentacion principal ya listas.
2. ?Cual es la siguiente accion pequena y ejecutable?
   - Usar una vez el ritual de arranque y dejar elegida una unica tarea pequena para la proxima sesion.
3. ?Que valor practico aporta esa accion?
   - Convierte Hermes en una herramienta operativa minima y deja trazabilidad del flujo.
4. ?Que no debo intentar todavia?
   - No tocar configuracion, VPS, Docker, cron, Telegram, MCPs, memoria externa ni otros proyectos.
5. ?Que tendria que quedar hecho para que la sesion haya valido la pena?
   - Ritual usado una vez, cierre breve registrado y siguiente accion pequena identificada.

### Cierre

- Accion elegida: registrar la primera sesion real de arranque.
- Resultado: ritual validado como primer uso practico de Hermes dentro de `Hermes_Ia`.
- Pendiente para la proxima sesion: elegir y ejecutar una primera tarea pequena de Fase 1 sin ampliar alcance.
- Limites respetados: no se toco configuracion, VPS ni otros proyectos.

## Sesion Telegram Gateway - 2026-06-21

### Arranque

- Objetivo: activar Telegram como canal movil para hablar con Hermes desde el telefono.
- Alcance autorizado: configurar bot, guardar token en `.env`, validar respuesta basica y dejar gateway persistente.
- Limites: no Docker, no cambio de backend, no MCPs, no Playwright, no memoria externa, no secretos en Git.

### Resultado

- Se creo un bot de Telegram para Hermes.
- El token se guardo directamente en `/home/hermes/.hermes/.env`.
- Se configuro allowlist para limitar el uso al usuario autorizado.
- Se instalo y activo el servicio de usuario `hermes-gateway.service`.
- Se habilito `systemd linger` para que el gateway sobreviva al cierre de SSH.
- Hermes respondio desde el movil al mensaje `hola`.

### Respuesta observada de Hermes

```text
Hola Erick, que necesitas
```

### Verificacion documental

Despues de actualizar la documentacion, se pidio a Hermes desde Telegram:

```text
Lee docs/CODEX-BRIEF.md y dime en 3 lineas que cambio hoy sobre Telegram.
```

Hermes respondio que el estado real ya incluye:

- backend local
- `openai-codex` como auth principal
- Telegram Gateway operativo desde movil
- `CiudadanoInusual` como sistema editorial activo
- cron, Kanban, Docker, perfiles y MCPs aun no activados

### Cierre

- Telegram pasa de futuro planificado a operativo ahora, solo como canal movil autorizado.
- Cambios adicionales de Telegram siguen siendo sensibles y requieren confirmacion.
- Documentacion especifica: `runbooks/09-telegram-gateway.md`.

## Sprint semanal 01 - 2026-06-21

- Se reconcilio el estado real del proyecto: Fase 0 cerrada, Fase 1 activa, Telegram Gateway operativo y `gpt-5.4` como modelo principal.
- Se creo `ROADMAP-HERMES.md` como fuente canonica de fases, tracks, tareas actuales y limites.
- Se corrigieron documentos que todavia trataban Telegram como futuro o mencionaban `gpt-5.4-mini` como modelo activo.
- Se actualizo el inventario editorial real: 6 research, 20 content base, 6 guiones, 6 posts, 6 carruseles y 1 publicacion registrada.
- Se creo `OPERATIVA-SEMANAL.md` para separar trabajo movil y trabajo de portatil.
- Se creo Captura Movil V1 con `projects/hermes_ia/CAPTURA-MOVIL.md` y `scripts/captura-movil.py`.
- Se valido el script de captura con prueba sintetica: add, list, show, update-status y export-curated usando `tmp/`.
- Queda pendiente la prueba real desde Telegram: capturar una idea desde movil, recuperarla, convertirla en pieza, aplicar Judge y publicar o dejar lista.

## Politica de autonomia progresiva - 2026-06-21

- Se cambia el criterio de "bloquear skills por defecto" a "permitir incubadora con auditoria posterior".
- Hermes puede crear skills experimentales dentro de `HERMES_HOME` si el flujo es repetible, util y de bajo riesgo.
- Se mantienen limites rojos: secretos, `.env`, servicios, cron recurrente, Docker, MCPs, Playwright, memoria externa y publicacion automatica.
- `ciudadanoinusual-mobile-intake` queda clasificada como skill experimental activa, no oficial.
- La condicion para formalizarla en el repo es superar 3 capturas reales sin errores graves.

## Consolidacion Mobile Ops - 2026-06-21

- Captura Movil V1 ya tuvo prueba real desde Telegram.
- La primera captura incluyo un placeholder accidental y se corrigio creando una captura limpia.
- Se amplio la validacion anti-plantillas para rechazar instrucciones del prompt antes de guardar.
- Se creo `projects/hermes_ia/SKILLS-EXPERIMENTALES.md` como indice de skills incubadas en `HERMES_HOME`.
- La skill `ciudadanoinusual-mobile-intake` no se borra: queda experimental activa para Captura Movil V1 y Modo Calle.
- La formalizacion queda condicionada a 3 capturas reales sin errores graves.

## Confianza supervisada - 2026-06-21

- Se ajusto la politica para evitar bloqueo preventivo sobre capacidades propias de Hermes.
- Acciones verdes: skills experimentales en `HERMES_HOME`, uso desde Telegram, capturas privadas, recuperacion de capturas, borradores, `JUDGE.md`, temporales y envio de archivos con scripts probados.
- Acciones con registro posterior: nueva skill experimental, archivo nuevo en `HERMES_HOME`, cambio de flujo, error corregido o automatizacion experimental no recurrente.
- Acciones rojas: secretos, `.env`, tokens, SSH, firewall, usuarios, `sudo`, servicios, cron recurrente, paquetes, Docker, MCPs, Playwright, memoria externa, publicacion automatica, borrados y cambios fuera de `Hermes_Ia`.
- La regla queda: Hermes puede expandirse en bajo riesgo si deja rastro; debe pedir permiso en alto riesgo.

## Alineacion con documentacion oficial Hermes - 2026-06-21

- La documentacion oficial confirma que el Gateway de Telegram soporta texto, imagenes, archivos, voz, comandos internos y sesiones en background.
- `/whoami` y `/status` pasan a experimento seguro porque solo verifican alcance y estado.
- `/background` pasa a experimento seguro solo para tareas pequenas, no destructivas y registradas.
- Cron oficial soporta tareas one-shot y recurrentes, pero en `Hermes_Ia` cron recurrente sigue rojo; una prueba one-shot queda como futuro con permiso.
- `AGENTS.md` queda confirmado como contexto operativo valido del proyecto, por lo que debe reflejar la politica real de confianza supervisada.
- La skill `ciudadanoinusual-mobile-intake` queda registrada como experimental activa, no oficial versionada.

## Roadmap fuera de publicaciones - 2026-06-21

- Se separa Mobile Ops de la produccion de contenido para evitar que todo avance termine en publicaciones.
- Se crea Track C: Personal Ops V1 para decisiones, dudas recurrentes, ideas no publicables, resumen semanal manual y priorizacion de portatil.
- Se crea Track D: Automatizacion controlada para distinguir background pequeno, cron one-shot futuro y cron recurrente rojo.
- Captura Movil V1 refuerza la validacion anti-plantillas con marcadores adicionales del prompt.
- La siguiente prioridad operativa es probar capacidades reales de Telegram y una captura personal no publicable antes de abrir mas contenido.

## Validacion real de capacidades Telegram - 2026-06-21

- `/whoami` quedo validado desde Telegram y devolvio alcance real del bot para el usuario actual.
- `/status` quedo validado y mostro sesion activa, ultima actividad y plataforma conectada.
- Captura Movil V1 ya guardo una captura privada real en JSONL fuera de Git y luego se recupero correctamente.
- La primera recuperacion fallo por la skill experimental `ciudadanoinusual-mobile-intake`, que se quedaba en trazas de herramientas; se ajusto la skill en `HERMES_HOME` y la sesion nueva de Telegram ya respondio bien.
- El parseo de metadata tambien se corrigio: `Privacidad: no publicar` pasa a `privacy_flags: ["no_publicar"]`.
- La recepcion de imagen desde Telegram quedo validada: Hermes confirma recepcion, describe breve, marca privacidad y recomienda formato.
- La nota de voz / STT quedo validada: Hermes confirma recepcion, resume fielmente y recomienda formato sin publicar.
- `/background` pequeno quedo validado para lecturas no destructivas; el unico ruido detectado fue desincronizacion previa del repo y eco raro de markdown en nombres de archivo.

## Cierre Mobile Ops V1 - 2026-06-21

- Se completo el primer flujo movil extremo a extremo con captura real, recuperacion en portatil/VPS, borrador util, aplicacion de `JUDGE.md`, registro y cambio de estado en JSONL.
- Se completo una segunda captura real con el mismo cierre operativo, dejando `2/3` para evaluar futura formalizacion de la skill experimental.
- La recepcion de imagen por Telegram ya no solo describe: tambien devuelve nombre y ruta accesible en cache.
- La recepcion de documento PDF por Telegram quedo validada con ruta accesible y lectura basica posterior.
- Quedo documentado un limite real del canal: archivos `.asc` rechazados por tipo no permitido.
- A partir de aqui, `Mobile Ops V1` queda cerrado; lo que sigue ya no es validar la base, sino consolidar la skill experimental y decidir el siguiente uso estable.

## Skill candidata a formalizacion - 2026-06-21

- `ciudadanoinusual-mobile-intake` supera la condicion de `3/3` capturas reales utiles sin errores graves.
- Pasa de `experimental activa` a `candidata a formalizacion`.
- No se marca todavia como skill oficial porque la entrada sigue siendo demasiado rigida para movil.
- Se define una mejora minima obligatoria: aceptar mejor texto libre, foto + contexto breve y nota de voz + intencion explicita de guardado.

## Validacion de entrada natural - 2026-06-21

- Se aplico un parche remoto en `HERMES_HOME` para priorizar guardado de captura cuando la intencion es clara.
- La skill ya acepta mejor `foto + instruccion breve de guardado` sin exigir plantilla completa.
- La ultima prueba real devolvio `id`, `estado`, `privacy_flags`, `suggested_format` y ruta del almacen, en vez de desviarse a descripcion o redaccion.
- El cuello de botella principal deja de ser la entrada natural y pasa a ser la decision de versionado oficial o no.

## Cierre de configuracion y optimizacion de Telegram - 2026-08-25

- Se confirmaron dos perfiles aislados: `default` para CiudadanoInusual con
  `gpt-5.6-terra` via `openai-codex`, y `auscultacion` con `gpt-5.6-luna` via
  `openai-codex`.
- Ambos perfiles usan `google/gemini-3.7-flash` via OpenRouter como fallback.
  El saldo prepago de OpenRouter queda fijado operativamente en 5 EUR como
  tope de emergencia.
- En la primera pasada, `agent.max_turns` bajo de 60 a 20 en `default` y de
  150 a 20 en `auscultacion`; se retiraron herramientas no usadas desde
  Telegram.
- En la segunda pasada se desactivaron `session_search`, `browser` y `bfl` en
  ambos perfiles; `image_gen` quedo solo en `default`.
- El prompt fijo total quedo en 42.710 B para `default` y 44.865 B para
  `auscultacion`, frente a 53.843 B y 58.119 B de linea base: reduccion
  acumulada de 20,7% y 22,8%. Los gateways quedaron activos despues de cada
  reinicio.
- Se resolvio una incidencia de Google AI Studio: una base URL nativa
  `/v1beta`, credenciales ausentes en el `.env` del perfil y saturacion de
  `gemini-3.7-flash` se presentaban como el mismo error de autenticacion.
- La practica corregida es probar primero con `curl` contra el endpoint
  compatible, despues configurar el perfil, reiniciar el gateway correcto y
  verificarlo. Las credenciales no se imprimen ni se versionan.

## Recuperacion humana con copia - 2026-06-22

- Se parcheo el gateway real de Telegram en `HERMES_HOME` para anadir botones de copia en respuestas con ids o rutas reutilizables.
- La primera prueba artificial funciono, pero la validacion real mostro que el flujo normal pasaba por `edit_message`, no solo por `send`.
- Tras extender el parche a `send`, `edit_message` y continuaciones, `Dime mis ultimas 5 capturas` mostro botones `Copiar ID 1..5` en Telegram.
- La mejora reduce una friccion real: ya no hace falta memorizar o copiar a mano ids largos desde movil.
- No se versiono en Git porque vive en el runtime real de Hermes bajo `HERMES_HOME`; queda documentado como mejora operativa validada.

## Friccion real de comandos en la calle - 2026-07-21

- Uso real reportado: incluso la superficie reducida de seis palabras (`guion post carrusel hoy publicado guarda`) genero friccion en movil. Cita textual: "me lie y termine aburriendome... es que hasta dificil de memorizar son".
- Diagnostico: el problema no es la cantidad de palabras, es depender de memorizar cualquier cosa estando cansado y en la calle.
- Decision: construir menu nativo `/` de Telegram (Fase 1) y botones tactiles en las respuestas de Hermes Creador (Fase 2), reutilizando el patron ya probado de botones `Copiar ID` de la sesion "Recuperacion humana con copia" (2026-06-22).
- Clasificacion: zona roja segun `AGENTS.md` (cambio de configuracion del gateway de Telegram).
- **Permiso explicito concedido por Erick el 2026-07-21**, en conversacion directa, al elegir la opcion "botones reales en Telegram" sobre la alternativa de solo simplificar el documento.
- Plan completo, riesgo, rollback y pasos: `runbooks/10-telegram-comandos-nativos.md`.
- Pendiente de ejecucion: esta sesion no tiene acceso SSH al VPS. La Fase 1 (registrar el menu con `setMyCommands`) es de bajo riesgo y se puede ejecutar en minutos. La Fase 2 (botones) requiere localizar y extender el parche existente de `HERMES_HOME`.

## Fase 1 ejecutada - 2026-07-21

- Erick ejecuto en el VPS el `curl` de `setMyCommands` de `runbooks/10-telegram-comandos-nativos.md`.
- Respuesta de la API de Telegram: `{"ok":true,"result":true}`.
- Los seis comandos (`hoy`, `guion`, `post`, `carrusel`, `publicado`, `guarda`) quedaron registrados en el menu nativo del bot.
- Pendiente de confirmar: que el menu aparece al pulsar `/` en el chat desde el movil, y que tocar cada comando responde igual que escribir la palabra a mano (Paso 4 del runbook). Si `/hoy` no se comporta igual que `hoy`, hace falta el ajuste de alias descrito en ese paso.
- Fase 2 (botones tactiles) sigue pendiente, sin ejecutar.

### Verificacion y hallazgo - 2026-07-21

- Video enviado por Erick mostro el menu `/` con los ~24 comandos nativos de Hermes Agent (`/help`, `/status`, `/restart`, `/background`, etc.), sin los seis nuevos. Sospecha inicial: sobrescritura por el gateway.
- `getMyCommands` ejecutado despues confirmo que los seis SI estan registrados en Telegram: `{"ok":true,"result":[hoy, guion, post, carrusel, publicado, guarda]}`.
- Diagnostico correcto: `setMyCommands` reemplazo la lista nativa de Hermes por los seis nuevos (no fusiona, sustituye). El video probablemente reflejaba cache del cliente de Telegram antes del refresco, o el estado justo antes del reemplazo.
- Decision de Erick: dejar el menu solo con los seis comandos de `Hermes Creador`. Los comandos nativos de Hermes siguen funcionando igual si se escriben a mano; solo dejan de aparecer en el autocompletado `/`.
- Riesgo abierto sin confirmar: si `hermes gateway restart` o `hermes update` re-registran la lista nativa por su cuenta, sobrescribiendo los seis sin aviso. Verificar tras el proximo restart o update; si se pierden, repetir el mismo `curl`.
- Detalle completo en `runbooks/10-telegram-comandos-nativos.md`, seccion "Hallazgo real".

### Cierre del experimento - 2026-07-21

- Erick ejecuto `hermes gateway restart` para probar la persistencia. Resultado: el menu volvio a mostrar los ~24 comandos nativos de Hermes; los seis de `Hermes Creador` desaparecieron. `getMyCommands` lo confirmo.
- Confirmado: el riesgo que quedo anotado como abierto se materializo. `hermes gateway` reafirma su propia lista de comandos en cada arranque/reinicio.
- Decision final de Erick: no mantener el forcejeo contra el reinicio del gateway. Se abandona el uso del menu `/` de Telegram como vector para los seis comandos.
- El propio `hermes gateway restart` ya dejo el menu nativo restaurado por su cuenta; no hizo falta ninguna accion manual adicional.
- Solucion adoptada para la friccion de calle: Nivel 0 de `COMANDOS.md` (mandar la foto o nota sin palabra clave). No depende de Telegram, no se pierde en reinicios.
- `runbooks/10-telegram-comandos-nativos.md` reescrito para reflejar el cierre: documenta el intento completo como hallazgo tecnico util, deja el comando de restauracion del menu nativo por si hiciera falta en el futuro, y marca la Fase 2 (botones) como pendiente de re-evaluar bajo esta misma logica antes de invertir tiempo en ella.

## Backup y restore verificados - 2026-07-21

- Ejecutado en el VPS siguiendo `runbooks/06-backup-restore.md`.
- Backup: `tar -czf .../hermes-backup-20260721-195322.tar.gz -C /home/hermes .hermes workspace`. Resultado: 1.7G, con aviso no fatal `tar: .hermes: file changed as we read it` (archivo modificado en vivo durante la compresion, esperable con el gateway corriendo; no impidio crear el backup).
- Restore de verificacion en `/home/hermes/restore-test/` (ruta temporal, sin tocar `/home/hermes` real): extraccion completa de `.hermes` y `workspace`.
- Verificacion critica: `capturas.jsonl` (el unico dato del sistema sin copia en Git) se recupero y confirmo con `test -f` + `echo "CAPTURAS OK"`.
- Carpeta de prueba borrada despues de verificar (`rm -rf /home/hermes/restore-test`).
- Resultado: **el backup ya no es una suposicion, es un hallazgo verificado**. Cierra el hallazgo de seguridad "backup/restore nunca probado" de `AUDITORIA-2026-07-21.md`.
- Pendiente menor: se limpio despues a un solo backup (se borro el mas viejo, `195114`); sigue pendiente decidir politica de retencion y destino externo del `.tar.gz` (segun `runbooks/06-backup-restore.md`).

## Endurecimiento SSH bloqueado por falta de contrasena sudo - 2026-07-21

- Se intento el paso 1 de `runbooks/02-seguridad.md` (copia de `/etc/ssh/sshd_config` con `sudo cp`).
- Bloqueo: Erick no tiene a mano la contrasena de `sudo` del usuario `hermes` (distinta de la clave SSH usada para conectar).
- Ningun cambio se aplico: el comando se cancelo en el prompt de contrasena antes de ejecutarse. `sshd_config` sigue intacto, sin riesgo.
- Pendiente para la proxima sesion: localizar o resetear la contrasena de `sudo` de `hermes` antes de retomar el endurecimiento SSH. Sin eso, el runbook no se puede ejecutar.

## Endurecimiento SSH ejecutado y verificado - 2026-08-08

- Bloqueo de la sesion anterior resuelto: Erick recupero la contrasena de `sudo` de `hermes`.
- Ejecutado `runbooks/02-seguridad.md` paso a paso desde PowerShell -> `ssh hermes` -> VPS, sin cerrar la sesion hasta verificar.
- Paso 1: backup creado, `/etc/ssh/sshd_config.bak-20260808`.
- Paso 2 (estado previo): `permitrootlogin without-password` (ya correcto, sin cambio necesario), `passwordauthentication yes` (unico cambio real pendiente), `port 22` (sin cambio).
- Paso 3: confirmado login por clave antes de tocar nada (`grep -c "ssh-" ~/.ssh/authorized_keys` -> `1`).
- Paso 4: verificado que no existe override en `/etc/ssh/sshd_config.d/` (sin archivo de cloud-init tocando `PasswordAuthentication`); el `yes` efectivo venia del default de OpenSSH con la linea comentada. Cambio aplicado con `sed` sobre la linea 66: `#PasswordAuthentication yes` -> `PasswordAuthentication no`.
- Paso 5: `sudo sshd -t` sin errores de sintaxis.
- Paso 6: `sudo systemctl restart ssh`.
- Paso 7 (verificacion obligatoria): segunda conexion `ssh hermes` desde ventana nueva de PowerShell, sin cerrar la original. Entro por clave sin pedir contrasena. Verificado con exito.
- Paso 8: sesion original cerrada tras confirmar el paso 7.
- Resultado: `PasswordAuthentication no` activo; `PermitRootLogin` ya estaba en modo seguro desde antes de esta sesion. Cierra el hallazgo "endurecimiento SSH pendiente de ejecutar y verificar" de `runbooks/02-seguridad.md` y el Hallazgo relacionado de `AUDITORIA-2026-07-21.md`.
- Detectado durante la ejecucion, sin tocar por estar fuera de alcance: el VPS reporta `*** System restart required ***` y actualizaciones pendientes (6 inmediatas + 13 via ESM Apps). Ningun paquete se actualizo ni se reinicio el servidor en esta sesion.
- Verificacion adicional que el propio runbook marca como no bloqueante sigue sin ejecutar: `fail2ban` y `ufw`. Son cambios de sistema (zona roja de `AGENTS.md`), requieren permiso explicito aparte de este cierre.

## Hermes Agent actualizado de 0.16.0 a 0.20.0 - 2026-08-08

- Motivo: la instalacion estaba 20883 commits detras de `origin/main` (sin actualizar desde la instalacion inicial en junio).
- Ejecutado desde `hermes` por SSH: `hermes update --check` (confirmo el atraso) -> `hermes update --backup` (snapshot completo previo en `~/.hermes/backups/pre-update-2026-08-08-105353.zip`, 105.8 MB).
- Cambios locales sin commitear en el codigo fuente de `hermes-agent` (no en config, no en datos) se dejaron en git stash sin reaplicar (`git stash apply 7fcd89348a81b6a0a2bac1e4113c2fbe39d40816` si algun dia hacen falta) por no haber constancia de que fueran ediciones intencionales.
- Dependencias Python y Node actualizadas sin errores. Skills sincronizadas: `default: +7 new, ↑2 updated, ~2 user-modified` (las 2 personalizaciones locales se respetaron).
- `hermes doctor` post-update: sin errores criticos. Un hallazgo real pendiente: config `v29 -> v33` desactualizada (`hermes doctor --fix` la migraria, pero es zona roja de `AGENTS.md` -- queda fuera de este cierre, requiere permiso aparte). El resto de avisos (Docker, agent-browser, API keys de Discord/web search, vulnerabilidades npm de build-tool) son estado esperado por decision ya tomada en `ROADMAP-HERMES.md`, no regresiones nuevas.
- Hallazgo durante el cierre: `hermes update` actualizo el codigo en disco pero no reinicio el proceso del gateway en ejecucion (seguia corriendo el PID de hace 2 semanas con la version vieja). Paso adicional no documentado en el runbook local: `hermes gateway restart` fue necesario para que el Telegram Gateway cargara la version nueva.
- Verificacion real, no solo de logs: Erick probo el bot desde Telegram (mensaje normal + `/whoami`) y respondio correctamente tras el reinicio.
- Resultado: `hermes --version` -> `0.20.0 (2026.8.3)`. Gateway activo con PID nuevo desde 2026-08-08 10:59:39 UTC.
- Pendiente para otra sesion, no bloqueante: migracion de config v29->v33 (`hermes doctor --fix`, zona roja, pide permiso aparte); vulnerabilidades npm de build-tool en `agent-browser`/`web`/`ui-tui` (bajo impacto, runtime no afectado).

### Hallazgo - Hermes 0.20.0 trae panel web (`hermes dashboard`) - 2026-08-08

- La actualizacion incluye un dashboard web completo (chat, config, modelos, sesiones, cron, canales, analiticas). Confirmado en documentacion oficial de Nous Research.
- Estado actual: no esta corriendo, no se expone. El `update` solo genero los archivos estaticos (`web_dist`), no un servidor activo.
- Por defecto se ata a `127.0.0.1:9119` (solo accesible desde el propio VPS, sin login). Atarlo a `0.0.0.0` exige configurar usuario/contrasena u OAuth o el propio Hermes se niega a arrancar -- no se puede exponer por accidente.
- Coincide con la decision ya vigente en `AGENTS.md`/`README.md`: sin dashboard publico. No se activo nada.
- Forma segura de probarlo si hace falta: tunel SSH (`ssh -L 9119:127.0.0.1:9119 hermes` + `hermes dashboard --no-open` en el VPS), nunca abrir el puerto directamente.

## Migracion de config Hermes v29 -> v33 - 2026-08-08

- Backup previo: `~/.hermes/config.yaml.bak-20260808`.
- `hermes config check`: `Required` vacio, nada obligatorio faltaba. La lista larga de `Optional` es el catalogo completo de integraciones no usadas (Discord, Slack, WhatsApp, etc.), esperado en `○`.
- `hermes config migrate`: aplicado sin fricción. Dos avisos revisados:
  - `agent.verify_on_stop` quedo en `false` tras la migracion (Hermes no exige verificar codigo editado antes de dar por terminada una respuesta). Corregido a `"auto"` (activo en CLI/TUI, apagado en mensajeria) con `hermes config set agent.verify_on_stop auto` -- mas alineado con el principio de evidencia antes que intuicion.
  - Warnings de toolset desconocido para `teams` y `google_chat`: sin impacto, plataformas no usadas ni configuradas.
- Verificado con `hermes doctor`: `Config version up to date (v33)`, sin aviso de `verify_on_stop`. Quedan 4 avisos menores ya conocidos (vulnerabilidades npm de build-tool, API keys opcionales sin configurar) -- ninguno nuevo ni bloqueante.

## F-03 backup externo cifrado y restauracion verificada - 2026-08-21

- Se creo una copia de configuracion, datos operativos y workspace en el VPS sin detener el gateway.
- La copia se cifro con GPG AES-256 antes de transferirla fuera del VPS; el checksum coincide en origen y destino.
- La restauracion aislada valido 1.427 mensajes, 41 sesiones y 11 capturas; JSONL valido y directorio temporal eliminado.
- No se modificaron servicios, paquetes ni configuracion. Tras autorizacion explicita, el TAR sin cifrar se elimino; se conserva solo la copia GPG y la copia externa.

## F-01 despliegue parcial de approvals.deny - 2026-08-21

- Se respaldo `config.yaml` con permisos 600 y se desplegaron tres reglas para cargas directas con `curl`; `hermes config check` valido la configuracion.
- La simulacion seca de `curl --data-binary @...` devolvio `user-deny` con codigo 3, sin ejecutar trafico ni leer archivos reales.
- La primera simulacion de destinatario Telegram arbitrario y de exportacion hacia `~/.ssh/authorized_keys` devolvio `allow`; se corrigio con dos reglas explicitas adicionales, tras nuevo backup privado de config.
- Repeticion real: las tres simulaciones de riesgo devolvieron `user-deny` con codigo 3; lectura local y `curl` sin carga siguieron en `allow` con codigo 0.
- El resultado cubre esas rutas textuales concretas. F-01 sigue siendo una mitigacion parcial: no constituye control semantico ni habilita datos reales.
- Decision de alcance: se acepta esta proteccion limitada por ahora; cualquier ampliacion requerira un bloque de seguridad separado.

## Mantenimiento del VPS y reinicio controlado - 2026-08-21

- Se actualizaron 26 paquetes estandar de Ubuntu; no se instalaron ni eliminaron paquetes y no se activo Ubuntu Pro/ESM.
- El VPS se reinicio de forma controlada para cargar el kernel `6.8.0-138-generic`; ya no existe marcador de reinicio pendiente ni actualizaciones estandar pendientes.
- Tras el arranque, `hermes-gateway.service` quedo activo y Hermes conserva la version `0.20.0`.

## F-10 retencion minima de capturas privadas - 2026-08-21

- Se definio `RETENCION-DATOS.md` para capturas privadas: 30 dias descartadas, 90 inbox/reviewed y 180 convertidas; cualquier borrado exige revision previa y `--apply` explicito.
- Se anadio `scripts/retencion-datos.py`, que no muestra cuerpos privados y queda en revision por defecto; no se ejecuto contra el almacen real.
- Dos pruebas sinteticas pasaron: `--dry-run` no modifica el JSONL y `--apply` elimina solo registros vencidos de un directorio temporal.
- Sesiones, logs, adjuntos y backups siguen fuera de este alcance; F-10 general no se declara cerrado.

## Reconciliacion de skill movil - 2026-08-21

- Evidencia real en VPS: la ruta de `ciudadanoinusual-mobile-intake` no existe, falta `SKILL.md` y `hermes skills list` no la detecta.
- No se restauro ni creo ninguna skill. Se corrigieron los documentos operativos para no tratar una capacidad historica como runtime activo.

## F-08 salida segura del verificador de secretos - 2026-08-21

- `scripts/verificar-secretos.sh` conserva la deteccion sobre archivos en stage, pero ya no imprime coincidencias ni contenido sensible.
- Prueba sintetica: una clave OpenAI simulada y una IP de documentacion activan el fallo y solo muestran tipo, archivo y linea.

## Consolidacion de gobernanza - 2026-08-21

- Se eliminó `CODEX-KICKOFF.md`: duplicaba el arranque que ya gobierna `BOOTSTRAP.md`.
- Los documentos de políticas secundarias ahora referencian la fuente canónica de permisos, contexto, memoria, modelos, agentes, loops y roadmap en lugar de repetirla.

## Analisis de video desde Telegram - 2026-08-24

- La ruta nativa `video_analyze` se desactivo tras devolver falsos exitos cuando el proveedor auxiliar rechazo la peticion.
- Se anadio `scripts/preparar-video-social.py`: valida videos de hasta 50 MB, extrae una hoja de nueve fotogramas y transcribe el audio localmente con `faster-whisper`.
- La prueba sintetica completo preparacion y analisis visual; la prueba real recibio un MP4 desde Telegram, lo guardo en cache privada y devolvio el analisis al movil.
- El video completo no se publica ni se envia al proveedor visual; Hermes analiza la hoja de fotogramas y usa la transcripcion privada como contexto.

## CiudadanoInusual Shorts V1 - motor privado - 2026-08-24

- Se implemento `scripts/video-social.py` con ingesta privada, checksum del original, analisis local, planes versionados, A/B/C, aprobacion, export, estado, descarte sin borrado y retencion solo `dry-run`.
- Limites aplicados: cortos de hasta 60 segundos y 100 MB; largos de hasta 15 minutos y 1 GB; salidas de hasta 60 segundos, zoom `1.00-1.35` y maximo tres bloques de texto.
- Una prueba sintetica real en Linux completo ingesta, analisis, A/B/C y aprobacion de B; el checksum del original no cambio y el export coincidio con la preview aprobada.
- Un video sintetico de 66 segundos completo ingesta, analisis, hoja de 16 fotogramas y deteccion de escenas. La seleccion de tres momentos sigue siendo responsabilidad narrativa de Hermes.
- El motor no publica, no borra y no instala dependencias. La integracion de lenguaje natural y entrega A/B/C ya esta desplegada; sigue pendiente probarla con tres cortos y un video largo reales.
- Despliegue posterior: commits `15a357c` y `25f9744` sincronizados con VPS; 12 pruebas especificas correctas en Linux. La skill experimental `ciudadanoinusual-social-video` se actualizo de 0.1.0 a 0.2.0, quedo habilitada y conserva backup privado de la version anterior.
- No se reinicio el gateway ni se cambio configuracion. La entrega real A/B/C y las respuestas naturales siguen pendientes de prueba con material del usuario.

## Reduccion de coste fijo de Telegram - 2026-08-25

- `max_turns` quedo en 20 para `default` y `auscultacion` (antes 60 y 150).
- Telegram desactivo `delegation` y `tts` en ambos perfiles; Auscultacion tambien desactivo `code_execution`, `computer_use` y `cronjob`.
- Los gateways de ambos perfiles reiniciaron y quedaron activos; `vision`, `file`, `memory`, `skills`, `todo` y `clarify` se conservaron.
- El prompt fijo total se redujo 8,3% en `default` y 11,4% en `auscultacion`; los esquemas solos bajaron 16,8% y 21,3%. El bloque de sistema cambio por un ajuste concurrente de modelos y no se atribuye a esta optimizacion.

## Segunda pasada de reduccion de coste fijo de Telegram - 2026-08-25

- En Telegram se desactivaron `session_search`, `browser` y `bfl` en ambos perfiles; `image_gen` se mantuvo en `default` y se desactivo en `auscultacion`.
- Los esquemas medidos bajaron de 31.228 a 24.769 B en `default` y de 31.250 a 24.791 B en `auscultacion`; `browser` y `bfl` ya no contribuian al JSON fijo medido, pero quedaron fuera por alcance operativo.
- El prompt fijo total quedo en 42.710 B y 44.865 B, una reduccion adicional de 13,5% y 12,9% frente a la primera pasada; desde la linea base inicial, el ahorro acumulado es 20,7% y 22,8%.
- Ambos gateways reiniciaron y quedaron activos. Telegram conserva `web`, `vision`, `file`, `memory`, `skills`, `todo` y `clarify`; la recuperacion de sesiones antiguas queda para la CLI.

## Cambio temporal a Google AI Studio - 2026-08-25

- Motivo: `gpt-5.6-terra` vía `openai-codex` quedó bloqueado por `429 usage_limit_reached` hasta el 2026-08-31; se necesitaba continuidad operativa sin tocar el resto del sistema.
- Cambio: perfiles `default` y `auscultacion` configurados con `gemini-3.6-flash` vía Google AI Studio; cada perfil mantiene configuración, `.env` y gateway aislados.
- Coste estimado: `0 €` mientras el uso permanezca dentro del nivel gratuito de Google AI Studio; sujeto a límites de tasa y cuota.
- Ventajas: proveedor alternativo operativo; `gemini-3.6-flash` respondió correctamente; la integración compatible con OpenAI permite mantener el flujo de Hermes.
- Riesgos: nivel gratuito con rate limits; `gemini-3.7-flash` devolvió `503` por alta demanda; cada mensaje arrastra ~15K tokens de prompt fijo según `hermes prompt-size`, lo que acelera el consumo de cuota.
- Diagnóstico aprendido: `Provider authentication failed` no distingue falta de credenciales de saturación; verificar primero el `.env` del perfil y hacer `curl` directo al endpoint antes de cambiar configuración.
- Rollback: backup previo `hermes-backup-2026-08-25-084745.zip`; a partir del 2026-08-31 comprobar la recuperación de cuota y revertir ambos perfiles a `openai-codex` si vuelve a responder, reiniciando después el gateway correcto de cada perfil.
- Base URL validada para Google AI Studio en Hermes: `https://generativelanguage.googleapis.com/v1beta/openai`; `/v1beta` sin `/openai` no sirve para esta integración.

## Fase 2 - correccion de documentos de estado - 2026-08-25

- Se corrigieron exposicion real de Telegram, rotacion por perfil, cierre verificable de F-03, estado de F-01 como mitigacion parcial y referencias al bloque canonico de proveedores en `docs/CODEX-BRIEF.md`.

## Fase 3 - perfiles aislados - 2026-08-25

- Se documentaron los dos perfiles y gateways, el diagnostico de 429 y la restauracion con ambos perfiles y unidades; no hubo cambios de runtime.

## Fase 1 - correcciones de retencion y secretos - 2026-08-25

- La retencion identifica objetos expirados por identidad, evitando borrar registros validos con IDs duplicados y eliminando tambien registros sin ID.
- El verificador de secretos soporta nombres Unicode, blobs binarios y lineas con IP permitida junto a IP real; se ampliaron las pruebas para GitHub, claves privadas y AWS sin filtrar valores.
- La suite reproducible queda en `python -m unittest discover -s tests -t .`: 51 pruebas correctas y 10 omisiones esperadas en Windows o por dependencia externa.

## Fase 4 - consolidacion documental - 2026-08-25

- Se archivaron 14 documentos historicos sin perdida; se rescataron taxonomia activa, Judge, commits, contexto, Docker y estados.
- Dominios activos por ejecucion real: Creador, Research, Mobile Ops y Personal Ops. Programador, Financial Ops, Operador, Builder, Arquitectura e Inspiration quedan fuera.
- Se unifico la taxonomia del JSONL de capturas con `VALID_STATUSES`: `inbox`, `reviewed`, `converted` y `discarded`.
- Metrica de cierre: 123 archivos Markdown recursivos y 109 activos fuera de `docs/archive/`.
