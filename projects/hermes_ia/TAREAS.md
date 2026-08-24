# TAREAS

## Objetivo

Mantener una lista mínima, clara y útil de trabajo para el proyecto piloto `Hermes_Ia`.

## Siguiente tarea concreta

- probar `Hermes Creador minimo` con una situacion real usando el Nivel 0 de `COMANDOS.md` (mandar foto o nota sin palabra clave) y verificar si de verdad reduce la friccion de calle que se reporto el 2026-07-21
- F-01 queda aceptado por ahora como mitigacion parcial verificada; no ampliar reglas sin un nuevo bloque de seguridad aprobado.

## Estado de pruebas en Windows

- Las 9 pruebas omitidas son esperadas: seis requieren `HERMES_AGENT_SOURCE` (checkout local de Hermes) y tres requieren privilegio de enlaces simbolicos no disponible en este Windows.

## Cerrado recientemente

- Migracion de config Hermes v29 -> v33 y correccion de `agent.verify_on_stop` a `"auto"`: ejecutado y verificado el 2026-08-08, ver `learning/bitacora.md`.
- Hermes Agent actualizado de 0.16.0 a 0.20.0 (20883 commits): ejecutado y verificado el 2026-08-08, ver `learning/bitacora.md`. Backup completo tomado antes de actualizar. Gateway reiniciado y probado en real por Telegram (mensaje + `/whoami`). Hallazgo: trae panel web (`hermes dashboard`), apagado y no expuesto, sin conflicto con la politica de "sin dashboard publico".
- endurecimiento SSH (`runbooks/02-seguridad.md`): ejecutado y verificado el 2026-08-08, ver `learning/bitacora.md`. `PasswordAuthentication no` activo; `PermitRootLogin` ya estaba correcto. Pendiente aparte y no bloqueante: `fail2ban`/`ufw`, requieren permiso explicito por ser cambio de sistema.

## Cierres operativos pendientes

### 1. Contrato final de captura privada y conversion ligera

- estado: cerrado
- evidencia: `projects/hermes_ia/CAPTURA.md` (consolida lo que antes eran 4 archivos: los contratos de captura privada y conversion ligera, mas la spec de formalizacion y el plan de separacion)
- resultado: el alcance, inputs, outputs, limites y frontera entre las dos skills ya quedaron definidos

### 2. Limite real de archivos soportados desde Telegram

- estado: cerrado
- evidencia: `runbooks/09-telegram-gateway.md`
- resultado: PDF, imagen, voz, video y `.asc` ya quedaron documentados con su estado real observado; el video usa preparacion local y no el analizador nativo no verificado

### 3. Decision sobre `Personal Ops V1`

- estado: cerrado
- evidencia: `projects/hermes_ia/PERSONAL-OPS-V1.md` y `ROADMAP-HERMES.md`
- resultado: Personal Ops V1 entra ya en modo controlado como uso movil privado no publicable

### 4. Formalizacion o incubacion extra de la skill remota

- estado: cerrado
- evidencia: `ROADMAP-HERMES.md` y `projects/hermes_ia/SKILLS-EXPERIMENTALES.md`
- resultado: la skill puente historica esta ausente de `HERMES_HOME`; el flujo sigue mediante scripts y lenguaje natural, sin restaurarla ni formalizarla hasta demostrar una necesidad real

## Peticion minima de tarea

- archivo:
- cambio:
- verificacion:

## En curso

- usar `Hermes Creador minimo` para decidir formato, revisar privacidad y preparar borradores de `CiudadanoInusual`
- usar a Hermes como lector de contexto del proyecto piloto
- usar a Hermes para priorizar la siguiente tarea pequena y util
- consolidar el flujo local ↔ Git ↔ VPS ↔ Hermes
- convertir el ritual de arranque en un habito de sesion
- usar `OPERATIVA-DIARIA.md` como referencia para ejecutar sin volver al bucle meta
- permitir confianza supervisada en tareas verdes y amarillas bajas de `Hermes Builder`
- usar `CiudadanoInusual` como banco operativo de contenido real: guiones, posts, carruseles y publicacion movil
- usar Telegram como canal movil de entrada, no como automatizacion sin control

## Pendientes cercanas

- probar cinco entradas reales de Hermes Creador con lenguaje natural, sin exigir palabras clave, y comprobar que al menos cuatro queden bien encaminadas sin errores graves de privacidad
- publicar manualmente al menos una de esas piezas y registrar resultado a 24 horas y 7 dias
- probar dos usos reales mas de `Personal Ops V1` y medir si reduce friccion de portatil
- abrir Banco 2 con vida real expandida: pareja, convivencia, hogar, recados, comida, ocio simple y mini viajes
- seguir probando `guion`, `post` y `carrusel` con situaciones reales
- medir que formatos son mas faciles de repetir sin quemarse
- mantener vivienda/credito/ayudas como investigacion personal, no como eje del contenido
- limpiar o respaldar la carpeta untracked `projects/hermes_ia/briefings/` del VPS si vuelve a bloquear un `git push vps`

## Decision provisional sobre PRD/RFC

- por ahora no aporta abrir un `PRD` o `RFC` completo
- si aporta mantener una evaluacion minima documentada
- motivo: el proyecto todavia esta consolidando uso practico basico, no una capa documental mas pesada
- condicion para reabrir la decision: cuando el flujo de uso con Hermes ya sea estable y aparezca una necesidad real de especificacion

## Empleo Ops V0 — futuro controlado

- estado: contrato sintetico diseñado y prueba documental `PASS`; no operativo
- evidencia unica: `projects/hermes_ia/EMPLEO-OPS-V0.md`
- herramientas externas: `NO-GO` actual para CareerOps, JobSync y equivalentes
- datos reales: bloqueados por F-01, F-03 y F-10 de `AUDITORIA-INTEGRAL-2026-08-11.md`
- F-01 Fase A: `PARTIAL`; los dos scripts versionados tienen correcciones probadas con fixtures ficticios, pero la ejecución genérica por terminal sigue abierta y nada se aplicó al runtime
- proxima accion posterior: revisar y, sólo con aprobación, aplicar de forma reversible los scripts y reglas candidatas; mantener F-01 abierto hasta probar protección global
- prioridad: no desplaza la siguiente tarea concreta ni la Fase 1 de Hermes Creador

## F-03 — Backup y restore verificable

- estado: `CERRADO`; respaldo externo cifrado y restauracion aislada verificados el 2026-08-21
- evidencia: `learning/bitacora.md` y `learning/MEMORIA.md`
- resultado: copia GPG AES-256 creada antes de salir del VPS, checksum coincidente y restauracion de mensajes, sesiones y capturas validada; no se incluyen secretos en Git

## Bloqueos o dudas abiertas

- si el uso real demuestra una necesidad suficiente para restaurar o versionar una skill de captura movil
- si dos usos reales adicionales de `Personal Ops V1` confirman que reduce friccion de portatil
- que piezas publicadas realmente conectan con audiencia

## Completadas recientes

- instalación base de Hermes validada
- OpenRouter operativo
- `openai-codex` autenticado y operativo como proveedor principal
- `gpt-5.6-terra` observado como modelo principal por `openai-codex` el 2026-08-21
- usos oficiales iniciales definidos: `Research`, `Content` y `Builder`
- `JUDGE.md` creado y regla minima de 8/10 adoptada para salidas validas
- guía operativa diaria creada para trabajo local ↔ VPS ↔ Hermes
- seis briefings reales de `Hermes Research` registrados
- banco inicial de veinte salidas reales de `Hermes Content` completado
- seis guiones publicables creados en `projects/hermes_ia/content/ciudadanoinusual/publicables/`
- seis posts visuales publicables creados
- seis carruseles publicables o casi publicables creados
- primera publicacion externa asistida por Hermes registrada
- Telegram Gateway operativo desde movil y persistido con `systemd`
- `/whoami` y `/status` validados desde Telegram
- recepcion de imagen y nota de voz validadas desde Telegram
- `/background` pequeno validado para tareas no destructivas
- primer flujo movil extremo a extremo cerrado: captura -> recuperacion -> borrador -> `JUDGE.md` -> registro
- recepcion de documento PDF desde Telegram validada con ruta accesible
- tercera captura real util guardada, convertida y evaluada con `JUDGE.md`
- `ciudadanoinusual-mobile-intake` alcanzo historicamente `3/3` capturas utiles, pero esta ausente del runtime desde la comprobacion del 2026-08-21
- entrada natural validada en uso real con foto + instruccion breve de guardado
- mini especificacion de formalizacion creada para decidir versionado oficial sin depender del chat
- decision de arquitectura tomada: futura formalizacion separada en captura privada y conversion ligera
- plan minimo de separacion creado para ejecutar la division sin romper Mobile Ops
- la skill puente se planifico para un ciclo adicional, pero no existe actualmente en `HERMES_HOME`; no restaurar sin una decision y prueba separadas
- `Personal Ops V1` activado en modo controlado para decisiones, prioridades y notas privadas
- recuperacion humana validada con `ultimas 5`, `numero 2` y `mi ultima decision`
- envio de imagenes generadas a Telegram validado con `scripts/send-telegram-photo.py`
- Mobile Ops V1 cerrado como ciclo base con evidencia real
- criterio de `/background` pequeno aceptado como experimento seguro no destructivo
- `Modo guion`, `Modo post` y `Modo carrusel` creados y probados
- guia rapida de modos, prompts de edicion y plan semanal creados
- linea de vivienda/credito/ayudas marcada como investigacion personal de referencia, no como centro de `CiudadanoInusual`
- script `projects/hermes_ia/verificar-cambio.sh` creado para `Hermes Builder`
- documentación técnica principal ampliada
- referencias externas y backlog futuro documentados
- roadmap base ya redactado
- Fase 0 documental cerrada en Git
- proyecto piloto sincronizado entre local y VPS por Git
- Hermes validado como lector de contexto y asistente documental básico
- evaluacion minima de PRD/RFC ya resuelta de forma provisional
- gobernanza V1 aprobada y publicada en `origin`
- `Hermes Creador minimo` creado como contrato operativo editorial para `CiudadanoInusual`

## No hacer todavía

- no tocar `TopoField`
- no tocar `TopoTask`
- no activar cron recurrente
- no activar cron one-shot sin permiso explicito
- no instalar más herramientas
- no introducir memoria externa
- no abrir fases de subagentes ni Kanban todavía

## Backlog cercano

- producir primeras piezas del Banco 2: vida compartida, dias libres y ocio simple
- priorizar formatos de videovlog, dia en mi vida, trabajo de campo, estudio nocturno, IA practica y humor realista
- convertir mejores fotos y situaciones reales en piezas publicadas o listas para publicar
- crear una rutina semanal de revision de resultados
- preparar futura evaluación de PRD y RFC cuando el uso práctico básico ya sea estable
