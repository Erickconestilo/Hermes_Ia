# TAREAS

## Objetivo

Mantener una lista mínima, clara y útil de trabajo para el proyecto piloto `Hermes_Ia`.

## Siguiente tarea concreta

- completar la tercera captura real util desde Telegram para decidir si `ciudadanoinusual-mobile-intake` ya puede pasar de experimental activa a candidata a formalizacion

## Peticion minima de tarea

- archivo:
- cambio:
- verificacion:

## En curso

- usar a Hermes como lector de contexto del proyecto piloto
- usar a Hermes para priorizar la siguiente tarea pequena y util
- consolidar el flujo local ↔ Git ↔ VPS ↔ Hermes
- convertir el ritual de arranque en un habito de sesion
- usar `OPERATIVA-DIARIA.md` como referencia para ejecutar sin volver al bucle meta
- permitir confianza supervisada en tareas verdes y amarillas bajas de `Hermes Builder`
- usar `CiudadanoInusual` como banco operativo de contenido real: guiones, posts, carruseles y publicacion movil
- usar Telegram como canal movil de entrada, no como automatizacion sin control

## Pendientes cercanas

- consolidar Captura Movil V1 con 3 capturas reales utiles sin errores graves
- registrar limite real de archivos soportados desde Telegram separando PDF/imagen validos y tipos rechazados
- decidir si `Personal Ops V1` entra ya como siguiente uso estable desde Telegram
- preparar Personal Ops V1 solo despues de cerrar Mobile Ops V1 basico
- publicar o dejar lista una primera pieza real desde el flujo movil
- abrir Banco 2 con vida real expandida: pareja, convivencia, hogar, recados, comida, ocio simple y mini viajes
- seguir probando `Modo guion`, `Modo post` y `Modo carrusel` con situaciones reales
- medir que formatos son mas faciles de repetir sin quemarse
- mantener vivienda/credito/ayudas como investigacion personal, no como eje del contenido
- limpiar o respaldar la carpeta untracked `projects/hermes_ia/briefings/` del VPS si vuelve a bloquear un `git push vps`

## Decision provisional sobre PRD/RFC

- por ahora no aporta abrir un `PRD` o `RFC` completo
- si aporta mantener una evaluacion minima documentada
- motivo: el proyecto todavia esta consolidando uso practico basico, no una capa documental mas pesada
- condicion para reabrir la decision: cuando el flujo de uso con Hermes ya sea estable y aparezca una necesidad real de especificacion

## Bloqueos o dudas abiertas

- cuándo merece la pena activar fases posteriores como cron, skills o perfiles
- cuándo pasar de la sincronización manual selectiva a un flujo basado en Git remoto
- que piezas publicadas realmente conectan con audiencia

## Completadas recientes

- instalación base de Hermes validada
- OpenRouter operativo
- `openai-codex` autenticado y operativo como proveedor principal
- `gpt-5.4` validado como modelo principal por `openai-codex`
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
- envio de imagenes generadas a Telegram validado con `scripts/send-telegram-photo.py`
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
