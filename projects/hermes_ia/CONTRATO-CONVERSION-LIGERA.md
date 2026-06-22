# CONTRATO FINAL - CIUDADANOINUSUAL CONVERSION LIGERA

## Estado

- skill objetivo: `ciudadanoinusual-conversion-ligera`
- tipo: futura skill oficial versionada
- origen: separacion de la skill experimental `ciudadanoinusual-mobile-intake`
- estado actual: contrato cerrado; implementacion pendiente

## Proposito

Tomar una captura ya guardada y convertirla en un borrador usable sin saltar automaticamente a publicacion ni mezclar el flujo con guardado privado.

## Regla principal

Si la intencion principal del usuario es convertir una captura ya existente en nota, post, guion o carrusel, esta skill debe producir un borrador claro, breve y usable.

No debe guardar capturas nuevas ni alterar el almacenamiento privado.

## Inputs aceptados

La skill puede entrar si detecta cualquiera de estas formas:

- `convierte esta captura`
- `hazme un borrador con esta captura`
- `pasalo a post`
- `pasalo a guion`
- `pasalo a carrusel`
- `recupera la captura <id> y conviertela`
- peticion explicita de transformar una captura ya guardada

## Prioridad de intencion

Orden de prioridad:

1. leer captura existente
2. detectar formato pedido o recomendado
3. producir borrador
4. aplicar privacidad
5. pasar por `JUDGE.md` si el flujo lo pide

No debe priorizar antes:

- volver a guardar la captura
- inspeccionar adjuntos como primera accion
- publicar automaticamente
- expandir el texto mas de lo necesario

## Pregunta de aclaracion permitida

Si falta solo el formato de salida, puede hacer una sola pregunta corta:

`Quieres que lo convierta en nota, post, guion o carrusel?`

Si el formato ya esta claro por el contexto o por `suggested_format`, no debe preguntar.

## Output minimo

Cuando convierte una captura, debe devolver:

- `formato recomendado`
- `riesgos de privacidad`
- `borrador breve`
- `puntuacion Judge` si aplica
- `decision`

## Reglas de conversion

Debe:

- partir de una captura ya existente
- respetar `original_text`
- no inventar detalles
- conservar el angulo real de la situacion
- mantener el tono pedido o el tono base de `CiudadanoInusual`
- producir una salida breve y reutilizable

## Formatos permitidos

- nota privada
- post
- guion
- carrusel
- borrador breve no publicable

No debe asumir que toda captura acaba publicada.

## Reglas de privacidad

Antes de entregar el borrador debe:

- revisar si hay nombres reales
- revisar terceros identificables
- revisar logos de empresa
- revisar ubicaciones exactas
- revisar rutinas o datos sensibles

Si detecta riesgo, debe:

- generalizar;
- marcarlo;
- o recomendar `nota privada`

segun el caso.

## Uso de `JUDGE.md`

Debe aplicar `JUDGE.md` cuando:

- el flujo operativo lo pida;
- el usuario lo pida;
- o la pieza este a punto de considerarse valida para el banco.

Si la nota es menor de `8/10`, debe mejorar el borrador antes de darlo por bueno.

## Registro

Si el flujo operativo lo pide, debe:

- registrar la evaluacion en `projects/hermes_ia/JUDGE-REGISTRO.md`
- dejar decision final
- dejar siguiente accion minima

No debe tocar Git ni cambiar archivos del repo salvo en un flujo ya pedido y con diff claro.

## Limites duros

Esta skill no debe:

- guardar nuevas capturas
- tocar el JSONL privado
- cambiar estados en privado sin que el flujo lo pida
- publicar automaticamente
- tocar `.env`
- tocar secretos
- tocar servicios
- instalar paquetes
- tocar Docker, MCPs, Playwright o memoria externa
- convertir cualquier idea en contenido publico sin revisar privacidad

## Criterio de exito

La skill cumple su contrato si:

1. toma una captura ya guardada;
2. la convierte sin inventar;
3. respeta privacidad;
4. produce un borrador usable;
5. aplica `JUDGE.md` cuando toca;
6. no invade el trabajo de la skill de captura privada.

## Frontera con la skill 1

Esta skill empieza solo cuando la captura ya existe o el usuario pide expresamente transformar algo ya guardado.

Si el usuario todavia esta intentando guardar algo nuevo, el flujo debe volver a `ciudadanoinusual-captura-privada`.

## Verificacion minima para dar este contrato por cerrado

- el archivo existe en el repo
- el proposito esta delimitado
- inputs y outputs minimos estan definidos
- el uso de privacidad y `JUDGE.md` queda claro
- la frontera con la skill de captura privada queda cerrada

## Siguiente accion despues de este contrato

Decidir si ambas skills ya pasan a implementacion minima oficial o si la skill experimental en `HERMES_HOME` debe vivir un ciclo mas como puente.
