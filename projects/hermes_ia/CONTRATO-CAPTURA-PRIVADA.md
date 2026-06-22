# CONTRATO FINAL - CIUDADANOINUSUAL CAPTURA PRIVADA

## Estado

- skill objetivo: `ciudadanoinusual-captura-privada`
- tipo: futura skill oficial versionada
- origen: separacion de la skill experimental `ciudadanoinusual-mobile-intake`
- estado actual: contrato cerrado; implementacion pendiente

## Proposito

Recibir desde Telegram una situacion real, guardarla como captura privada con trazabilidad y permitir recuperacion fiable sin desviarse por defecto a redaccion o publicacion.

## Regla principal

Si la intencion principal del usuario es guardar algo, esta skill debe priorizar captura y registro.

No debe saltar a copy, post, guion o carrusel salvo peticion explicita posterior.

## Inputs aceptados

La skill puede entrar si detecta cualquiera de estas formas:

- `Captura movil` + texto libre
- `guarda esto`
- `guardame esto`
- `esto es una captura`
- `nota privada`
- foto + contexto breve + instruccion de guardado
- nota de voz + intencion explicita de guardado
- peticion de recuperar una captura ya guardada
- peticion de confirmar si un adjunto llego y donde quedo accesible

## Prioridad de intencion

Orden de prioridad:

1. guardar captura
2. recuperar captura
3. inspeccionar adjunto
4. resumir en privado

No debe priorizar antes:

- descripcion visual libre
- redaccion publicable
- analisis creativo
- `JUDGE.md`

## Pregunta de aclaracion permitida

Si la intencion no es clara, solo puede hacer una pregunta:

`Quieres que lo guarde como captura privada o que lo convierta ahora en contenido?`

No debe hacer mas de una pregunta antes de decidir el flujo.

## Output minimo de guardado

Cuando guarda una captura, debe devolver:

- `id`
- `estado`
- `privacy_flags`
- `suggested_format`
- `ruta real del almacen`

## Reglas de guardado

Debe preservar:

- `original_text` con la situacion real, sin wrappers ni plantillas
- `status: inbox`
- `privacy_flags` segun riesgo detectado
- `suggested_format` segun peticion explicita o inferencia prudente
- `id` estable de captura
- ruta real del JSONL privado

Debe rechazar textos que parezcan plantilla o instrucciones del prompt.

## Output minimo de recuperacion privada

Si el usuario pide recuperar o resumir una captura ya guardada, debe devolver:

- `resumen en 3 lineas`
- `decision sugerida`

## Reglas de recuperacion privada

Debe:

- permitir recuperacion por `id`, por ultima captura, por posicion reciente o por referencia semantica corta
- no cambiar estado por defecto
- no convertir a contenido salvo peticion explicita
- mantenerse en lane privado

Regla de usabilidad:

- el `id` es para el sistema;
- el usuario no debe depender de memorizar ids largos para recuperar capturas recientes.

Formas validas de recuperacion humana:

- `Recupera la captura <id>`
- `Recupera la ultima captura`
- `Dime mis ultimas 5 capturas`
- `Dime mis ultimas 10 capturas`
- `Recupera la numero 2 de las ultimas 5`
- `Recupera mi ultima decision`
- `Recupera la del ramen`

Regla de resolucion:

- si hay `id`, usar ese;
- si el usuario dice `ultima`, usar la mas reciente;
- si el usuario pide `ultimas 5` o `ultimas 10`, devolver lista humana corta;
- si el usuario usa referencia semantica y hay una sola coincidencia razonable, usarla;
- si hay ambiguedad, hacer una sola pregunta corta.

Formato recomendado para listar recientes:

- `id`
- `tipo`
- `resumen en una linea`

La lista debe ser humana y corta, no un volcado largo de JSON.

Regla de salida para movil:

- cuando devuelva ids, rutas o referencias reutilizables, debe entregarlas en formato facil de copiar;
- priorizar una linea por item;
- si el contenido se va a reutilizar luego, preferir bloque simple o texto limpio antes que parrafo largo;
- no esconder el dato importante dentro de explicaciones largas.

Lane privado valido:

- nota privada
- tarea
- backlog
- revisar luego
- descartar

## Output minimo de inspeccion de adjuntos

Si el usuario pregunta por una imagen, voz o archivo, debe devolver:

- `recibido`
- `tipo`
- `nombre`
- `ruta`
- `puedo leerlo o solo detectarlo`

## Reglas de inspeccion de adjuntos

Debe:

- confirmar si el adjunto llego
- devolver ruta exacta si existe cache accesible
- decir si puede leer el contenido o solo detectarlo
- no describir el contenido si el usuario no lo pidio

## Tipos de archivo soportados hoy

- imagen: valido
- voz: valido
- PDF: valido
- `.asc`: rechazado

La skill no debe prometer soporte universal.

Si un tipo no entra en el flujo actual, debe decirlo claro.

## Limites duros

Esta skill no debe:

- redactar posts por defecto
- pulir copy
- convertir una captura en pieza publica automaticamente
- aplicar `JUDGE.md` salvo peticion puntual de verificacion
- publicar en redes
- tocar `.env`
- tocar secretos
- tocar servicios
- instalar paquetes
- tocar Docker, MCPs, Playwright o memoria externa
- modificar Git o el repo como parte del guardado

## Riesgos de privacidad que debe vigilar

- nombres reales
- caras visibles
- terceros identificables
- logos de empresa
- ubicaciones exactas
- rutinas de desplazamiento
- documentos o codigos visibles
- datos personales o sensibles

## Criterio de exito

La skill cumple su contrato si:

1. guarda sin perder el texto real;
2. no mete plantillas en `original_text`;
3. devuelve trazabilidad minima;
4. recupera por `id` y por formas humanas sin desviar a contenido;
5. inspecciona adjuntos sin inventar;
6. respeta privacidad y limites;
7. devuelve referencias en formato razonablemente copiable desde movil.

## Frontera con la skill 2

Esta skill termina su trabajo cuando:

- la captura ya quedo guardada; o
- la recuperacion privada ya fue entregada; o
- la inspeccion del adjunto ya fue resuelta.

Si el usuario quiere convertir una captura ya guardada en nota, post, guion o carrusel, el flujo debe pasar a `ciudadanoinusual-conversion-ligera`.

## Verificacion minima para dar este contrato por cerrado

- el archivo existe en el repo
- el proposito esta delimitado
- inputs y outputs minimos estan definidos
- limites y riesgos estan escritos
- la frontera con la segunda skill queda clara

## Siguiente accion despues de este contrato

Usar este contrato para redactar el contrato final de `ciudadanoinusual-conversion-ligera` o para implementar la version oficial minima de `ciudadanoinusual-captura-privada`.
