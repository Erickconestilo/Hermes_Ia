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

## Banco 2: vida real expandida

- probar `Modo guion` con otra situacion real -> guion publicable si pasa privacidad y calidad -> guardar en `projects/hermes_ia/content/ciudadanoinusual/publicables/`
- vida compartida: pareja, convivencia, casa, cansancio y proyectos -> hooks + escenas + cierre humano -> guardar en `projects/hermes_ia/content/ciudadanoinusual/`
- dias libres que no son libres: limpieza, mercado, coche, recados y descanso real -> hooks + escenas + cierre util -> guardar en `projects/hermes_ia/content/ciudadanoinusual/`
- salida simple: una copa, paseo o mini viaje barato sin postureo -> hooks + esquema + cierre cercano -> guardar en `projects/hermes_ia/content/ciudadanoinusual/`
- comida en ruta episodio real -> aplicar ranking `/25` a una comida concreta -> guardar en `projects/hermes_ia/content/ciudadanoinusual/`
- guion publicable: convertir una pieza fuerte del banco inicial en guion corto -> hook + desarrollo + cierre -> guardar en `projects/hermes_ia/content/ciudadanoinusual/`

## Futuro: TopoBot como inspiracion

- no reactivar el TopoBot viejo por ahora
- conservar la idea: experiencia real de obra/topografia -> post LinkedIn / guion / contenido social
- futura integracion posible: `Modo LinkedIn Obra`, `Modo Foto a Post`, `Modo Video a Guion`
- Hermes_Ia debe ser el cerebro; un bot futuro solo seria interfaz de captura rapida

## Research personal / decisiones de vida

- vivienda, credito y ayudas publicas quedan como investigacion personal de referencia para decisiones futuras
- no son el eje del banco de contenido de `CiudadanoInusual`
- solo se convierten en contenido si el angulo conecta con vida real de trabajador, aprendizaje o toma de decisiones prudente

## Builder siguientes

- probar `/whoami` desde Telegram -> confirmar alcance real de permisos del bot -> registrar respuesta sin datos sensibles
- probar `/status` desde Telegram -> confirmar estado de sesion y gateway -> registrar resultado minimo
- probar envio de archivo desde Telegram a Hermes -> verificar recepcion sin versionar privados -> nota de resultado
- probar recepcion de imagen desde Telegram -> confirmar que Hermes puede verla o describirla -> nota de capacidad real
- probar nota de voz desde Telegram -> confirmar si transcribe o si requiere configuracion adicional -> registrar limite real
- probar `/background` con una tarea pequena no destructiva -> confirmar que devuelve resultado al chat -> registrar si queda como experimento seguro
- captura de decision personal -> guardar una decision breve fuera de Git -> recuperar y resumir sin convertirla en publicacion
- registro de idea no publicable -> capturar una idea privada -> clasificarla como nota, decision o backlog
- resumen semanal manual -> pedir desde Telegram un resumen de capturas recientes -> revisar en portatil
- priorizar tarea de portatil -> pedir a Hermes una sola tarea para la proxima sesion de laptop -> verificar que no sea publicacion por defecto
- briefing corto desde Telegram -> pedir research breve con fuentes o limites -> guardar resumen curado solo si aporta
- Builder seguro desde movil -> pedir mejora de script/doc/verificacion sin tocar servicios ni configuracion -> revisar diff en portatil
- validar Captura Movil V1 desde Telegram -> captura privada, recuperacion y conversion a borrador -> evidencia sin versionar datos privados
- crear `prompts/video.md` con plantillas para generacion, desarrollo y research de videos cortos -> guardar en `prompts/`
- limpiar o respaldar la carpeta untracked `projects/hermes_ia/briefings/` del VPS -> evitar conflictos de `git push vps` -> `git status --short` limpio en VPS
- `projects/hermes_ia/verificar-cambio.sh` -> probarlo en VPS cuando toque Builder -> salida de terminal limpia

## Personal Ops V1 siguientes

- captura de decision personal -> guardar decision, opciones y motivo fuera de Git -> recuperar resumen sin convertirlo en contenido
- duda recurrente -> guardar duda y contexto minimo -> revisar si vuelve a aparecer en la semana
- idea no publicable -> registrar como nota privada -> clasificar como tarea, decision o descarte
- resumen semanal manual -> pedir a Hermes sintesis de capturas revisadas -> validar que no inventa ni publica
- priorizar portatil -> elegir una sola tarea de laptop -> verificar que queda en `TAREAS.md` si procede

## Automatizacion controlada futura

- cron one-shot -> disenar prueba puntual con permiso explicito -> no activar hasta aprobar riesgo y rollback
- background pequeno -> ejecutar tarea no destructiva desde Telegram -> registrar resultado y limite

## No entra todavia

- cron recurrente
- cambios de configuracion del gateway de Telegram fuera de pruebas no destructivas
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
- content-09: dia en mi vida, topografia, estudio e IA -> hooks + escenas + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-10: topografia de campo y aprendizaje digital -> hooks + escenas + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-11: cosas que nadie cuenta de la topografia -> hooks + lista + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-12: drones, topografia y curiosidad tecnologica -> hooks + escenas + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-13: estudiar de noche sin romantizar el cansancio -> hooks + escenas + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-14: errores aprendiendo IA como principiante -> hooks + lista + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-15: estudiar desarrollo web trabajando -> hooks + lista + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-16: IA util para trabajador normal -> hooks + lista + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-17: falsa productividad -> hooks + lista + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-18: comer en ruta mientras se trabaja -> hooks + secciones + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-19: ranking de comida en ruta -> hooks + sistema de puntuacion + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`
- content-20: trayecto al trabajo en moto, bus o tren -> hooks + momentos + frase memorable -> guardado en `projects/hermes_ia/content/ciudadanoinusual/`

### Guiones publicables completados

- guion-01: ir al trabajo tambien cansa -> guardado en `projects/hermes_ia/content/ciudadanoinusual/publicables/`
- guion-02: viernes de faena y comida en ruta -> guardado en `projects/hermes_ia/content/ciudadanoinusual/publicables/`
- guion-03: calor, falta de respeto y faena -> guardado en `projects/hermes_ia/content/ciudadanoinusual/publicables/`

### Builder completado

- script de verificacion de cambios creado -> `projects/hermes_ia/verificar-cambio.sh`
- juez minimo de calidad creado -> `projects/hermes_ia/JUDGE.md`
- indice operativo creado -> `projects/hermes_ia/INDICE-OPERATIVO.md`
- Telegram Gateway operativo desde movil -> `runbooks/09-telegram-gateway.md`
- envio de imagenes generadas a Telegram -> `scripts/send-telegram-photo.py`
