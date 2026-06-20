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

- ayudas vivienda Cataluna / Espana para perfil trabajador -> investigacion con fuentes oficiales vigentes -> guardar en `projects/hermes_ia/research/`
- oportunidad laboral en topografia + IA aplicada -> briefing con fuentes y salida accionable -> guardar en `projects/hermes_ia/research/`

## Content siguientes

- `briefing-05-vivienda-credito-espana-perfil-trabajador.md` -> convertir en version mas cercana a voz `CiudadanoInusual` si la salida 06 no llega a 8/10 -> guardar mejora en `projects/hermes_ia/content/ciudadanoinusual/`
- una idea personal de aprendizaje con IA -> convertir en hooks + esquema + cierre -> guardar en `projects/hermes_ia/content/ciudadanoinusual/`
- preparar pieza 07 del banco de 20 -> salida Content validada por `JUDGE.md` -> guardar en `projects/hermes_ia/content/ciudadanoinusual/`

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

### Content completado

- content-01: IA en pymes de servicios -> hooks + esquema + cierre -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-02: FP y microcredenciales -> hooks + esquema + cierre -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-03: productividad en Windows -> hooks + esquema + cierre -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-04: IA en pymes/back-office -> hooks + esquema + cierre -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-05: FP, topografia, construccion y datos -> hooks + esquema + cierre -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-06: vivienda, credito y contrato indefinido -> hooks + esquema + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`

### Builder completado

- script de verificacion de cambios creado -> `projects/hermes_ia/verificar-cambio.sh`
- juez minimo de calidad creado -> `projects/hermes_ia/JUDGE.md`
- indice operativo creado -> `projects/hermes_ia/INDICE-OPERATIVO.md`
