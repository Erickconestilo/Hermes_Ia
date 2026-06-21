# Backlog futuro de Hermes

## Objetivo

Recoger ideas, funciones y posibles evoluciones de Hermes que surgen en vídeos, conversaciones y exploración personal, sin convertirlas automáticamente en trabajo inmediato.

## Regla de uso

Este backlog es un espacio de discusión técnica futura.

No implica:

- aprobación automática
- prioridad inmediata
- implementación en la siguiente sesión

Cada idea debe volver a discutirse antes de entrar en fase operativa.

Pero tampoco debe tratarse como un cementerio de ideas.

Si una idea muestra valor claro y puede probarse con bajo riesgo, puede pasar de backlog a experimento seguro.

## Prioridad actual del proyecto

Antes de abrir nuevas líneas, sigue vigente esta base:

- instalación nativa estable
- usuario `hermes`
- backend `local`
- documentación clara
- pocos puntos de fallo
- autonomía controlada en tareas de bajo riesgo

## Ideas futuras a revisar

### 1. Profiles / subagentes especializados

Valor:

- alto

Para qué podría servir:

- separar research, contenido, builder/código y seguimiento personal
- reducir mezcla de contexto
- especializar tono, instrucciones y criterios por tarea

Complejidad:

- media

Riesgo:

- medio

Fase sugerida:

- próxima fase útil después de consolidar la base

### 2. Cron / tareas programadas

Valor:

- muy alto

Para qué podría servir:

- briefing semanal de IA
- ideas de contenido
- seguimiento de precios VPS
- resúmenes automáticos de la bitácora

Complejidad:

- media

Riesgo:

- medio

Fase sugerida:

- alta prioridad futura

### 3. Kanban interno de Hermes

Valor:

- alto

Para qué podría servir:

- convertir ideas en tareas visibles
- repartir trabajo futuro entre agentes o perfiles
- organizar backlog interno sin perder contexto

Complejidad:

- media

Riesgo:

- medio

Fase sugerida:

- después de cron o en paralelo si el uso real lo justifica

### 4. Skills oficiales seleccionadas

Valor:

- medio-alto

Para qué podría servir:

- encapsular tareas repetitivas reales
- convertir flujos útiles en procedimientos reutilizables

Complejidad:

- media

Riesgo:

- medio

Notas:

- no cargar skills por colección
- instalar solo si hay una tarea repetitiva clara
- pasar a skill cuando un flujo ya haya demostrado repetición y retorno real

### 5. Telegram Gateway

Valor:

- alto

Para qué podría servir:

- hablar con Hermes desde móvil
- recibir salidas de tareas programadas
- usar Hermes como asistente persistente fuera del VPS

Complejidad:

- media

Riesgo:

- medio

Estado actual:

- gateway basico ya operativo en Fase 1
- cambios adicionales siguen siendo sensibles

Siguiente evaluacion:

- matriz de capacidades reales desde Telegram
- Captura Movil V1
- una prueba manual antes de cualquier cron recurrente

### 6. Mejora de memoria

Valor:

- medio

Para qué podría servir:

- mejor continuidad entre sesiones
- mejor seguimiento de temas largos
- más calidad en research persistente

Complejidad:

- media-alta

Riesgo:

- medio

Notas:

- solo vale la pena si la memoria actual se queda corta en uso real

### 7. WebUI privada con Caddy + HTTPS + auth

Valor:

- medio-alto

Para qué podría servir:

- acceso más cómodo desde móvil, casa y oficina
- interfaz más parecida a producto

Complejidad:

- alta

Riesgo:

- alto

Notas:

- mejor como fase deliberada, no como impulso
- estudiar antes dominio, DNS, auth y exposición pública

### 8. Tailscale para acceso privado

Valor:

- alto

Para qué podría servir:

- acceso remoto privado sin exponer servicios públicamente
- paso intermedio antes de publicar interfaces web

Complejidad:

- media

Riesgo:

- medio-bajo

Fase sugerida:

- antes que exponer una WebUI pública si se quiere acceso remoto

### 9. Goose como complemento o laboratorio

Valor:

- medio

Para qué podría servir:

- comparar filosofías de agentes
- probar recipes o workflows alternativos
- usarlo como laboratorio separado

Complejidad:

- alta

Riesgo:

- alto por dispersión

Fase sugerida:

- backlog lejano

### 10. Computer Use

Valor:

- llamativo, pero incierto para el caso actual

Para qué podría servir:

- automatizar interfaces humanas
- manipular apps sin APIs ni CLI claras

Complejidad:

- alta

Riesgo:

- alto

Juicio actual:

- útil como laboratorio o demo potente
- no prioritario para la fase actual
- más frágil y difícil de depurar que cron, profiles o Telegram

### 11. MCPs avanzados y flujos visuales

Valor:

- variable según caso

Ejemplos:

- Blender
- generación visual
- pipelines complejos de contenido

Complejidad:

- alta

Riesgo:

- alto

Fase sugerida:

- muy posterior

## Usos oficiales que más sentido tienen para este proyecto

### A. Hermes Research

Posibles temas:

- IA y agentes
- VPS y proveedores
- crédito e hipoteca
- topografía y oportunidades

### B. Hermes Content

Posibles salidas:

- ideas de vídeos
- hooks
- estructuras
- resúmenes de bitácora convertidos en contenido

### C. Hermes Builder

Posibles funciones:

- apoyo en código
- documentación
- scripts pequeños
- automatización técnica útil

## Qué me parece bien del método actual del proyecto

- explorar ideas antes de implementarlas
- discutir vídeos y tendencias en reuniones técnicas
- usar la curiosidad como radar, no como gatillo de cambios

## Riesgo principal del método

- confundir exploración con prioridad

## Regla propuesta para futuras reuniones

Cada idea nueva debe clasificarse así:

1. inspiración
2. backlog
3. fase próxima
4. implementación aprobada

Si no se clasifica, no entra en ejecución.

## Plan elaborado futuro inspirado en Gentleman

## Objetivo del plan

Tomar ideas útiles del enfoque de Gentleman y traducirlas a una hoja de ruta compatible con Hermes y con la estrategia conservadora de este proyecto.

## Principio de adaptación

No se copiará el stack de Gentleman tal cual.

Se adaptarán únicamente las partes que:

- aporten valor claro
- encajen con Hermes
- tengan coste de mantenimiento razonable
- no rompan la base actual

## Fase G1: Consolidar usos oficiales de Hermes

Objetivo:

- definir para qué va a trabajar Hermes antes de añadir nuevas capas

Usos oficiales propuestos:

- `Hermes Research`
- `Hermes Content`
- `Hermes Builder`

Valor:

- muy alto

Complejidad:

- baja

Riesgo:

- bajo

Condición de cierre:

- cada uso debe tener una descripción clara, una entrada, una salida y una utilidad real

## Fase G2: Profiles / subagentes especializados

Objetivo:

- separar contextos y estilos de trabajo

Aplicación futura:

- perfil de investigación
- perfil creativo
- perfil técnico
- perfil de seguimiento personal o financiero

Valor:

- alto

Complejidad:

- media

Riesgo:

- medio

Comentario:

- esta es la idea más transferible y más útil del material de Gentleman

## Fase G3: Cron con una automatización útil

Objetivo:

- validar automatización persistente con una sola tarea bien elegida

Primeros candidatos:

- briefing semanal de IA y agentes
- resumen semanal de `learning/bitacora.md`
- ideas de contenido semanales

Valor:

- muy alto

Complejidad:

- media

Riesgo:

- medio

Regla:

- no activar varias tareas a la vez al principio

## Fase G4: Skills a partir de repetición real

Objetivo:

- encapsular tareas repetitivas que ya hayan demostrado utilidad

Ejemplos posibles:

- generar ideas de vídeos
- transformar bitácora en borrador de contenido
- revisar estado de Hermes y del VPS
- preparar un informe semanal de research

Valor:

- alto

Complejidad:

- media

Riesgo:

- medio

Regla:

- una skill no se crea por entusiasmo, sino por repetición comprobada

## Fase G5: Kanban interno de Hermes

Objetivo:

- pasar de ideas sueltas a una gestión visible de tareas

Posible valor:

- triage de ideas
- asignación futura a perfiles
- control del trabajo pendiente

Valor:

- medio-alto

Complejidad:

- media

Riesgo:

- medio

Comentario:

- útil cuando ya exista más de un flujo persistente y no antes

## Fase G6: Mejora de memoria solo si hay dolor real

Objetivo:

- evaluar una capa extra de memoria si la memoria actual de Hermes se queda corta

Señales que justificarían estudiarlo:

- pérdida frecuente de contexto útil
- compactaciones pobres
- continuidad débil en research de largo plazo

Valor:

- medio

Complejidad:

- media-alta

Riesgo:

- medio-alto

Comentario:

- aquí podría entrar algo tipo Engram u otra solución comparable, pero solo con evidencia de necesidad

## Fase G7: Routing de modelos por tarea

Objetivo:

- usar distintos modelos según el tipo de trabajo

Ejemplo conceptual:

- research con un modelo
- creatividad con otro
- debugging o testing con otro

Valor:

- medio-alto

Complejidad:

- alta

Riesgo:

- alto

Comentario:

- potente, pero claramente posterior a tener tareas diferenciadas de verdad

## Fase G8: UI y acceso remoto más avanzados

Objetivo:

- decidir cómo acceder a Hermes de forma más cómoda

Opciones futuras:

- Telegram
- Tailscale
- WebUI privada
- Caddy + HTTPS + auth

Valor:

- variable

Complejidad:

- media-alta

Riesgo:

- medio-alto

Comentario:

- no es prioridad mientras la utilidad del sistema no esté consolidada

## Cosas del enfoque de Gentleman que sí adoptamos como criterio

- pensar Hermes como sistema y no solo como chat
- separar funciones por perfiles
- automatizar solo lo que ya demuestra valor
- factorizar tareas repetitivas en skills
- aceptar que no existe un único mejor modelo para todo

## Cosas del enfoque de Gentleman que no adoptamos todavía

- entusiasmo tipo “la IA puede hacer todo” como regla operativa
- capas avanzadas de memoria sin necesidad demostrada
- complejidad excesiva en el enrutado de modelos
- trasladar su stack entero a este proyecto
- mezclar demasiadas innovaciones en una sola fase

## Preguntas para futuras reuniones

1. ¿Qué uso oficial de Hermes ya demostró valor real?
2. ¿Qué tarea repetimos tanto que merece una skill?
3. ¿Qué automatización concreta justifica activar cron?
4. ¿La memoria actual de Hermes ya nos limita o todavía no?
5. ¿Estamos optimizando por utilidad o por fascinación técnica?
