# QUEUE

## Proposito

Mantener una cola simple de produccion para `Hermes_Ia`.

Este archivo responde una pregunta: que hacemos despues sin volver a reconstruir todo el contexto.

## Regla de uso

Cada item debe tener:

- tema o archivo
- salida esperada
- verificacion

Si no se puede verificar, no entra en la cola.

## Research siguientes

- dia en mi vida: trabajador de topografia que estudia desarrollo web y aprende IA -> briefing de angulos, escenas y riesgos de privacidad -> guardar en `projects/hermes_ia/research/`
- videovlog de trabajo/estudio/IA para `CiudadanoInusual` -> briefing de formatos virales realistas -> guardar en `projects/hermes_ia/research/`
- oportunidad laboral en topografia + IA aplicada -> briefing con fuentes y salida accionable -> guardar en `projects/hermes_ia/research/`
- IA practica para trabajador con poco tiempo -> briefing con fuentes, riesgos y rutina aplicable -> guardar en `projects/hermes_ia/research/`

## Content siguientes

- pieza 09: dia en mi vida, trabajo, estudio e IA -> hooks + escenas + cierre humano -> guardar en `projects/hermes_ia/content/ciudadanoinusual/`
- pieza 10: trabajo de campo/topografia + aprendizaje digital -> hooks + esquema de videovlog -> guardar en `projects/hermes_ia/content/ciudadanoinusual/`
- una idea personal de aprendizaje con IA -> convertir en hooks + esquema + cierre -> guardar en `projects/hermes_ia/content/ciudadanoinusual/`
- convertir un briefing existente en guion corto de video -> salida con hook, desarrollo y cierre -> guardar en `projects/hermes_ia/content/ciudadanoinusual/`

## Research personal / decisiones de vida

- vivienda, credito y ayudas publicas quedan como investigacion personal de referencia para decisiones futuras
- no son el eje del banco de contenido de `CiudadanoInusual`
- solo se convierten en contenido si el angulo conecta con vida real de trabajador, aprendizaje o toma de decisiones prudente

## Builder siguientes

- crear `prompts/video.md` con plantillas para generacion, desarrollo y research de videos cortos -> guardar en `prompts/`
- limpiar o respaldar la carpeta untracked `projects/hermes_ia/briefings/` del VPS -> evitar conflictos de `git push vps` -> `git status --short` limpio en VPS
- `projects/hermes_ia/verificar-cambio.sh` -> probarlo en VPS cuando toque Builder -> salida de terminal limpia

## No entra todavia

- cron
- Telegram
- Docker backend
- perfiles reales
- subagentes
- memoria externa
- cambios sobre `TopoField`
- cambios sobre `TopoTask`

## Completado

### Research completado

- briefing-01: IA en pymes de servicios en Espana -> briefing con fuentes y conclusion accionable -> guardado en `projects/hermes_ia/research/briefing-01-pymes-ia-espana.md`
- briefing-02: FP modular y microcredenciales -> briefing con fuentes y lectura practica -> guardado en `projects/hermes_ia/research/briefing-02-fp-microcredenciales-espana.md`
- briefing-03: IA practica para productividad personal en Windows -> briefing con fuentes, riesgos y conclusion accionable -> guardado en `projects/hermes_ia/research/briefing-03-ia-productividad-windows.md`
- briefing-04: oportunidades de FP vinculadas a topografia, construccion o datos -> briefing con fuentes oficiales y lectura practica -> guardado en `projects/hermes_ia/research/briefing-04-fp-topografia-construccion-datos.md`
- briefing-05: vivienda y credito en Espana para perfil trabajador -> briefing con fuentes, ayudas publicas y prudencia financiera -> guardado en `projects/hermes_ia/research/briefing-05-vivienda-credito-espana-perfil-trabajador.md`
- briefing-06: ayudas de vivienda en Cataluna/Espana -> briefing con fuentes oficiales y separacion activo/vigilar -> guardado en `projects/hermes_ia/research/briefing-06-ayudas-vivienda-cataluna-espana.md`

### Content completado

- content-01: IA en pymes de servicios -> hooks + esquema + cierre -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-02: FP y microcredenciales -> hooks + esquema + cierre -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-03: productividad en Windows -> hooks + esquema + cierre -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-04: IA en pymes/back-office -> hooks + esquema + cierre -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-05: FP, topografia, construccion y datos -> hooks + esquema + cierre -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-06: vivienda, credito y contrato indefinido -> hooks + esquema + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-07: ayudas de vivienda para trabajadores -> hooks + esquema + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-08: prestamo, aval y subvencion en vivienda -> hooks + esquema + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`

### Builder completado

- script de verificacion de cambios creado -> `projects/hermes_ia/verificar-cambio.sh`
- juez minimo de calidad creado -> `projects/hermes_ia/JUDGE.md`
- indice operativo creado -> `projects/hermes_ia/INDICE-OPERATIVO.md`
