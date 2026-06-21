# Bitácora

## 2026-06-11

- Se creó la estructura base del proyecto.
- Se fijó la decisión inicial: Hermes nativo en VPS Hetzner con usuario `hermes`.
- Se movió la transcripción del curso a [docs/curso-benjamin-hermes-transcripcion.md](/C:/Users/guill/Documents/Hermes_Ia/docs/curso-benjamin-hermes-transcripcion.md).
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
- El acceso correcto se consiguió con `ssh -i $HOME/.ssh/hermes_hetzner_ed25519 root@167.233.91.185`.
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
