# SPEC FORMALIZACION - CAPTURA MOVIL

## Proposito

Definir el alcance minimo y las reglas operativas para decidir si `ciudadanoinusual-mobile-intake` puede pasar de skill candidata a skill oficial versionada.

Esta spec no oficializa la skill por si sola.

Sirve para responder tres preguntas:

- que debe hacer exactamente;
- que no debe hacer;
- y que pruebas minimas debe superar antes de entrar al repo como skill oficial.

## Estado de partida

La skill ya cumple estas evidencias:

- `3/3` capturas reales utiles;
- guardado privado fuera de Git;
- recuperacion real por `id`;
- conversion a borrador;
- `JUDGE.md` aplicado;
- registro en `JUDGE-REGISTRO.md`;
- recepcion de imagen, voz y PDF validada desde Telegram;
- entrada natural validada con foto + instruccion breve de guardado.

La skill ya no esta en incubacion temprana.

Su estado correcto ahora es:

- `candidata a formalizacion`

## Objetivo funcional

Permitir que Hermes reciba desde Telegram una situacion real, la guarde como captura privada con trazabilidad y la convierta despues en una pieza o nota solo si el usuario lo pide.

## Alcance oficial propuesto

La skill oficial debe cubrir solo estos flujos:

1. guardar captura privada;
2. recuperar o verificar captura;
3. resumir o decidir en privado;
4. convertir una captura en borrador si el usuario lo pide;
5. inspeccionar si una imagen, voz o documento fue recibido y donde quedo accesible.

## Fuera de alcance

La skill oficial no debe:

- publicar automaticamente;
- mover secretos;
- tocar `.env`;
- tocar servicios;
- instalar nada;
- convertir cualquier foto en contenido sin confirmacion;
- reemplazar flujos generales de research o builder;
- mezclar captura privada con automatizaciones recurrentes.

## Activadores de entrada aceptados

La skill debe activarse si detecta una intencion clara de captura en cualquiera de estas formas:

- `Captura movil` + texto libre;
- `guarda esto`;
- `guardame esto`;
- `esto es una captura`;
- `nota privada`;
- foto + contexto breve + instruccion de guardado;
- voz + instruccion explicita de guardado.

## Regla de prioridad de intencion

Si la intencion principal parece ser guardar una captura:

- primero guardar;
- despues transformar solo si el usuario lo pide.

No debe priorizar:

- descripcion visual;
- pulido de copy;
- conversion a post;
- ni sugerencias publicables

si antes no queda resuelto si el usuario queria capturar o convertir.

## Regla de aclaracion minima

Si la intencion no es clara, la skill debe hacer una sola pregunta corta:

`Quieres que lo guarde como captura privada o que lo convierta ahora en contenido?`

No debe hacer mas de una pregunta antes de decidir el flujo.

## Contrato de guardado

Cuando guarde una captura, debe preservar:

- `original_text` con el cuerpo real de la situacion;
- `privacy_flags` segun riesgo detectado;
- `suggested_format` segun peticion o inferencia prudente;
- `status: inbox`;
- `id`;
- `ruta real del almacen`.

Debe devolver solo los campos pedidos por el usuario.

## Contrato de recuperacion privada

Si el usuario pide recuperar o resumir en privado:

- usar `show`;
- no cambiar estado;
- no convertir a contenido salvo peticion explicita;
- devolver resumen o decision en lane privado.

Lane privado permitido:

- nota privada;
- tarea;
- backlog;
- revisar luego;
- descartar.

## Contrato de conversion

Si el usuario pide convertir una captura:

- respetar privacidad;
- no inventar;
- producir borrador breve y usable;
- aplicar `JUDGE.md` si se pide o si el flujo operativo lo exige;
- registrar decision cuando corresponda.

## Contrato de inspeccion de adjuntos

Si el usuario pregunta por un archivo, imagen o voz:

- decir si llego;
- decir como llego;
- devolver nombre si existe;
- devolver ruta exacta si existe cache accesible;
- no describir contenido si el usuario no lo pidio.

## Limites de tipos de archivo

El flujo ya valida:

- imagen: si;
- voz: si;
- PDF: si;
- `.asc`: no.

La skill oficial no debe prometer soporte universal de archivos.

Debe decir claramente cuando un tipo no es compatible con el flujo actual.

## Riesgos que la skill debe seguir controlando

- plantillas o placeholders guardados como `original_text`;
- confusion entre captura y redaccion;
- terceros identificables;
- ubicaciones exactas;
- logos de empresa;
- rutinas de desplazamiento;
- datos que conviertan una nota privada en exposicion publica.

## Criterio de oficializacion

La skill puede pasar a oficial versionada si cumple a la vez:

1. mantiene `3/3` capturas reales utiles sin errores graves;
2. la entrada natural ya no rompe el flujo de guardado;
3. no mezcla captura y contenido cuando la intencion es clara;
4. el alcance queda cerrado y no invade otros modos;
5. Erick aprueba versionarla.

## Criterio para no oficializar todavia

No debe pasar a oficial si:

- vuelve a desviar foto + texto libre a copy en vez de guardado;
- vuelve a guardar wrapper o plantilla como contenido real;
- necesita demasiadas aclaraciones para casos normales;
- o sigue mezclando demasiadas responsabilidades en una sola skill.

## Decision tomada

Se adopta `Plan B`.

La futura formalizacion no debe congelar una sola skill demasiado mezclada.

La direccion aprobada es separar en dos skills:

1. una skill de captura y recuperacion privada;
2. una skill de conversion ligera a contenido.

## Reparto propuesto

### Skill 1: captura privada

Responsabilidades:

- detectar intencion de captura;
- guardar en JSONL privado;
- recuperar por `id`;
- resumir en lane privado;
- inspeccionar si imagen, voz o documento llegaron y donde quedaron accesibles.

No debe:

- redactar posts por defecto;
- pulir copy sin peticion;
- saltar a contenido publico si el usuario queria guardar.

### Skill 2: conversion ligera

Responsabilidades:

- tomar una captura ya guardada;
- convertirla en nota, post, guion o borrador breve;
- aplicar privacidad;
- pasar por `JUDGE.md` cuando corresponda;
- registrar decision.

No debe:

- guardar nuevas capturas;
- tocar adjuntos o almacenamiento privado;
- asumir que cualquier captura debe volverse publicacion.

## Verificacion minima antes de ejecutar la separacion

Antes de versionar las skills oficiales, basta con:

- leer esta spec;
- mapear que partes actuales quedan en skill 1 y cuales en skill 2;
- confirmar nombres, limites y outputs minimos;
- y decidir si la skill remota actual sigue viva en `HERMES_HOME` hasta completar migracion.
