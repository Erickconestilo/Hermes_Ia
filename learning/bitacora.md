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
