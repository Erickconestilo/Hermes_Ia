# PLAN MINIMO - SEPARACION DE SKILLS MOBILE OPS

## Objetivo

Separar la futura formalizacion de `ciudadanoinusual-mobile-intake` en dos skills oficiales mas limpias:

1. una skill de captura y recuperacion privada;
2. una skill de conversion ligera a contenido.

Este plan no ejecuta la separacion.

Solo define como hacerla sin romper el flujo ya validado.

## Decision de arquitectura

Se mantiene `Plan B`.

No se versionara una skill oficial monolitica.

La separacion propuesta es:

- `ciudadanoinusual-captura-privada`
- `ciudadanoinusual-conversion-ligera`

## Skill 1 - `ciudadanoinusual-captura-privada`

### Proposito

Recibir desde Telegram una situacion real y guardarla con privacidad, trazabilidad y recuperacion fiable.

### Responsabilidades

- detectar intencion de captura;
- guardar en JSONL privado;
- devolver `id`, `estado`, `privacy_flags`, `suggested_format` y `ruta real del almacen` cuando proceda;
- recuperar por `id`;
- resumir en lane privado;
- inspeccionar si una imagen, voz o PDF fue recibido y donde quedo accesible.

### No debe hacer

- redactar posts por defecto;
- pulir copy;
- convertir una captura en publicacion;
- aplicar `JUDGE.md` salvo verificacion muy puntual pedida por el usuario;
- cambiar estado sin peticion o flujo documentado.

### Output minimo esperado

Guardado:

- `id`
- `estado`
- `privacy_flags`
- `suggested_format`
- `ruta real del almacen`

Recuperacion privada:

- `resumen en 3 lineas`
- `decision sugerida`

Inspeccion de adjunto:

- `recibido`
- `tipo`
- `nombre`
- `ruta`
- `puedo leerlo o solo detectarlo`

## Skill 2 - `ciudadanoinusual-conversion-ligera`

### Proposito

Tomar una captura ya guardada y convertirla en borrador usable sin saltar automaticamente a publicacion.

### Responsabilidades

- leer una captura ya existente;
- proponer formato recomendado;
- producir nota, post, guion o borrador breve;
- aplicar privacidad;
- pasar por `JUDGE.md` cuando el flujo lo pida;
- registrar decision en `JUDGE-REGISTRO.md` si corresponde.

### No debe hacer

- guardar capturas nuevas;
- leer adjuntos directamente como primera accion;
- modificar almacenamiento privado;
- publicar automaticamente;
- asumir que toda captura debe volverse contenido.

### Output minimo esperado

- `formato recomendado`
- `riesgos de privacidad`
- `borrador breve`
- `puntuacion Judge`
- `decision`

## Regla de frontera entre skills

Si el usuario quiere **guardar** algo:

- entra `ciudadanoinusual-captura-privada`

Si el usuario quiere **convertir** algo ya guardado:

- entra `ciudadanoinusual-conversion-ligera`

Si la intencion no es clara:

- se hace una sola pregunta:
  - `Quieres que lo guarde como captura privada o que lo convierta ahora en contenido?`

## Estado de la skill remota actual

Durante la migracion:

- la skill actual en `HERMES_HOME` sigue viva;
- no se borra;
- no se congela todavia;
- actua como skill puente hasta que las dos nuevas queden definidas y probadas.

## Orden de ejecucion recomendado

1. versionar la spec y este plan;
2. definir contrato final de la skill 1;
3. definir contrato final de la skill 2;
4. decidir nombres finales y ubicacion en el repo;
5. crear version oficial minima de la skill 1;
6. probarla con una captura real;
7. crear version oficial minima de la skill 2;
8. probarla con una captura ya guardada;
9. decidir si la skill puente de `HERMES_HOME` se archiva o se mantiene un ciclo mas.

## Verificacion minima de la separacion

La separacion se considera bien ejecutada solo si:

- una captura nueva entra por la skill 1 sin desviarse a redaccion;
- una captura ya guardada entra por la skill 2 y sale como borrador usable;
- ninguna de las dos toca secretos, `.env`, servicios o Git sin diff claro;
- el usuario ya no necesita recordar una plantilla rigida para guardar algo desde movil.

## Riesgos a vigilar

- duplicar logica entre skills;
- dejar outputs inconsistentes;
- romper la prioridad de captura;
- mezclar de nuevo analisis visual y redaccion en la skill 1;
- dejar demasiado pobre la skill 2 y obligar a rehacer manualmente cada borrador.

## Siguiente accion concreta

Usar este plan para redactar el contrato final de `ciudadanoinusual-captura-privada`.
