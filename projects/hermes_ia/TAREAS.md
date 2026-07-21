# TAREAS

## Objetivo

Mantener una lista mínima, clara y útil de trabajo para el proyecto piloto `Hermes_Ia`.

## Siguiente tarea concreta

- probar `Hermes Creador minimo` con una situacion real usando el Nivel 0 de `COMANDOS.md` (mandar foto o nota sin palabra clave) y verificar si de verdad reduce la friccion de calle que se reporto el 2026-07-21

## Cierres operativos pendientes

### 1. Contrato final de captura privada

- estado: cerrado
- evidencia: `projects/hermes_ia/CONTRATO-CAPTURA-PRIVADA.md`
- resultado: el alcance, inputs, outputs, limites y frontera con la skill 2 ya quedaron definidos

### 2. Limite real de archivos soportados desde Telegram

- estado: cerrado
- evidencia: `runbooks/09-telegram-gateway.md`
- resultado: PDF, imagen, voz y `.asc` ya quedaron documentados con su estado real observado

### 3. Decision sobre `Personal Ops V1`

- estado: cerrado
- evidencia: `projects/hermes_ia/PERSONAL-OPS-V1.md` y `ROADMAP-HERMES.md`
- resultado: Personal Ops V1 entra ya en modo controlado como uso movil privado no publicable

### 4. Formalizacion o incubacion extra de la skill remota

- estado: cerrado
- evidencia: `ROADMAP-HERMES.md` y `projects/hermes_ia/SKILLS-EXPERIMENTALES.md`
- resultado: la skill sigue un ciclo mas en `HERMES_HOME` solo como puente, sin ganar alcance nuevo y con retirada prevista tras probar las dos skills oficiales minimas

### 5. Contrato final de conversion ligera

- estado: cerrado
- evidencia: `projects/hermes_ia/CONTRATO-CONVERSION-LIGERA.md`
- resultado: el alcance, inputs, outputs, privacidad, Judge y frontera con la skill 1 ya quedaron definidos

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

- ejecutar una prueba real de cada comando: `¿Qué toca hoy?`, `Video`, `Historia` y `He publicado`
- probar dos usos reales mas de `Personal Ops V1` y medir si reduce friccion de portatil
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

- cuando versionar oficialmente la skill derivada de captura movil
- si `Personal Ops V1` debe entrar ya o esperar una semana mas de uso real
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
- tercera captura real util guardada, convertida y evaluada con `JUDGE.md`
- `ciudadanoinusual-mobile-intake` ya pasa a candidata a formalizacion tras `3/3` capturas reales utiles
- entrada natural validada en uso real con foto + instruccion breve de guardado
- mini especificacion de formalizacion creada para decidir versionado oficial sin depender del chat
- decision de arquitectura tomada: futura formalizacion separada en captura privada y conversion ligera
- plan minimo de separacion creado para ejecutar la division sin romper Mobile Ops
- skill puente `ciudadanoinusual-mobile-intake` mantenida un ciclo mas en `HERMES_HOME` con alcance congelado
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
