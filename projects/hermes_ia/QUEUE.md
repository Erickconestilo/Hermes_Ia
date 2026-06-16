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

- IA practica para productividad personal en Windows -> briefing con fuentes, riesgos y conclusion accionable -> guardar en `projects/hermes_ia/research/`
- oportunidades de FP vinculadas a topografia, construccion o datos -> briefing con fuentes oficiales y lectura practica -> guardar en `projects/hermes_ia/research/`
- vivienda y credito en Espana para perfil trabajador -> briefing prudente con riesgos y fuentes -> guardar en `projects/hermes_ia/research/`

## Content siguientes

- `briefing-01-pymes-ia-espana.md` -> convertir en post corto para `CiudadanoInusual` -> guardar en `projects/hermes_ia/content/ciudadanoinusual/`
- `briefing-02-fp-microcredenciales-espana.md` -> convertir en guion breve de video -> guardar en `projects/hermes_ia/content/ciudadanoinusual/`
- una idea personal de aprendizaje con IA -> convertir en hooks + esquema + cierre -> guardar en `projects/hermes_ia/content/ciudadanoinusual/`

## Builder siguientes

- `projects/hermes_ia/verificar-cambio.sh` -> probarlo en VPS y confirmar que no deja cambios fuera de `projects/hermes_ia` -> salida de terminal limpia
- `projects/hermes_ia/JUDGE.md` -> usarlo para puntuar `Research 02` y decidir si pasa de 8/10 -> registrar resultado si hace falta
- `projects/hermes_ia/INDICE-OPERATIVO.md` -> agregar referencia a `QUEUE.md` si demuestra uso real -> `git diff` de una sola linea

## No entra todavia

- cron
- Telegram
- Docker backend
- perfiles reales
- subagentes
- memoria externa
- cambios sobre `TopoField`
- cambios sobre `TopoTask`
