# CAPTURA - CiudadanoInusual

Consolida en un solo archivo lo que antes vivía repartido en `CONTRATO-CAPTURA-PRIVADA.md`, `CONTRATO-CONVERSION-LIGERA.md`, `SPEC-FORMALIZACION-CAPTURA-MOVIL.md` y `PLAN-SEPARACION-SKILLS-CAPTURA.md` (798 líneas entre los cuatro, para un script de ~200 líneas que ya funciona: `scripts/captura-movil.py`). Los cuatro decían en gran parte lo mismo en distintos momentos de la decisión; este archivo se queda con la version final de cada parte.

## Estado

- skills objetivo: `ciudadanoinusual-captura-privada` y `ciudadanoinusual-conversion-ligera`
- tipo: futuras skills oficiales versionadas
- origen: separación de la skill experimental `ciudadanoinusual-mobile-intake`
- estado actual: contratos cerrados; implementación oficial pendiente
- skill puente actual: `ciudadanoinusual-mobile-intake` no esta presente ni es detectable en `HERMES_HOME` desde la comprobacion real del 2026-08-21; no se restaura automaticamente

## Evidencia de partida

El flujo historico de la skill puente cumplio, con evidencia registrada en `learning/bitacora.md` y `JUDGE-REGISTRO.md`:

- `3/3` capturas reales útiles sin errores graves;
- guardado privado fuera de Git;
- recuperación real por `id`;
- conversión a borrador;
- `JUDGE.md` aplicado y registrado;
- recepción de imagen, voz y PDF validada desde Telegram;
- entrada natural validada con foto + instrucción breve de guardado.

Esa evidencia no prueba que siga instalada ni descubrible. Su estado actual es `ausente del runtime`; no puede considerarse candidata operativa hasta una nueva instalacion y prueba real.

## Decisión de arquitectura: Plan B

No se versiona una skill oficial monolítica. Se separa en dos:

1. **`ciudadanoinusual-captura-privada`** — guardar y recuperar.
2. **`ciudadanoinusual-conversion-ligera`** — convertir una captura ya guardada en borrador.

Motivo: mezclar guardado y redacción en una sola skill desviaba capturas simples hacia copy no pedido. Separar el guardado (que debe ser rápido y fiable) de la conversión (que debe ser deliberada) evita esa deriva.

## Regla de frontera entre las dos skills

Si el usuario quiere **guardar** algo → `ciudadanoinusual-captura-privada`.

Si el usuario quiere **convertir** algo ya guardado → `ciudadanoinusual-conversion-ligera`.

Si la intención no es clara, una sola pregunta y no más:

> ¿Quieres que lo guarde como captura privada o que lo convierta ahora en contenido?

---

## Skill 1 - `ciudadanoinusual-captura-privada`

### Propósito

Recibir desde Telegram una situación real, guardarla como captura privada con trazabilidad, y permitir recuperación fiable sin desviarse por defecto a redacción o publicación.

### Regla principal

Si la intención principal es guardar, prioriza captura y registro. No salta a copy, post, guion o carrusel salvo petición explícita posterior.

### Inputs aceptados

- `Captura movil` + texto libre; `guarda esto`; `guardame esto`; `esto es una captura`; `nota privada`;
- foto + contexto breve + instrucción de guardado;
- nota de voz + intención explícita de guardado;
- petición de recuperar una captura ya guardada;
- petición de confirmar si un adjunto llegó y dónde quedó accesible.

### Prioridad de intención

1. guardar captura
2. recuperar captura
3. inspeccionar adjunto
4. resumir en privado

No antes que eso: descripción visual libre, redacción publicable, análisis creativo, `JUDGE.md`.

### Output mínimo de guardado

`id`, `estado`, `privacy_flags`, `suggested_format`, ruta real del almacén.

Debe preservar `original_text` tal cual (sin wrappers ni plantillas), `status: inbox`, `privacy_flags` según riesgo detectado, `id` estable, ruta real del JSONL privado. Debe rechazar textos que parezcan plantilla o instrucciones del prompt.

### Output mínimo de recuperación privada

Resumen en 3 líneas + decisión sugerida.

Reglas:

- recuperación por `id`, última captura, posición reciente o referencia semántica corta;
- no cambia estado por defecto; no convierte a contenido salvo petición explícita; se mantiene en lane privado;
- el `id` es para el sistema — el usuario no debe depender de memorizarlo. Formas humanas válidas: `Recupera la ultima captura`, `Dime mis ultimas 5 capturas`, `Recupera la numero 2 de las ultimas 5`, `Recupera mi ultima decision`, `Recupera la del ramen`.

Resolución: si hay `id` explícito, usarlo; si dice "última", la más reciente; si pide "últimas N", lista humana corta (id, tipo, resumen en una línea — nunca volcado de JSON); si hay referencia semántica con una sola coincidencia razonable, usarla; si hay ambigüedad, una sola pregunta corta.

Salida para móvil: ids y rutas reutilizables en formato fácil de copiar, una línea por item, nunca escondidos dentro de párrafos largos.

Lane privado válido: nota privada, tarea, backlog, revisar luego, descartar.

### Output mínimo de inspección de adjuntos

`recibido`, `tipo`, `nombre`, `ruta`, `puedo leerlo o solo detectarlo`. No describe el contenido si no se pidió.

### Tipos de archivo soportados hoy

Imagen: válido. Voz: válido. PDF: válido. `.asc`: rechazado. No prometer soporte universal; si un tipo no está validado, decirlo claro.

### Límites duros

No debe: redactar posts por defecto, pulir copy, convertir una captura en pieza pública automáticamente, aplicar `JUDGE.md` salvo verificación puntual pedida, publicar en redes, tocar `.env`/secretos/servicios/paquetes/Docker/MCPs/Playwright/memoria externa, modificar Git como parte del guardado.

### Riesgos de privacidad a vigilar

Nombres reales, caras visibles, terceros identificables, logos de empresa, ubicaciones exactas, rutinas de desplazamiento, documentos o códigos visibles, datos personales o sensibles.

### Frontera con la skill 2

Termina su trabajo cuando la captura ya quedó guardada, la recuperación privada ya fue entregada, o la inspección del adjunto ya fue resuelta. Si el usuario quiere convertir una captura ya guardada, el flujo pasa a la skill 2.

---

## Skill 2 - `ciudadanoinusual-conversion-ligera`

### Propósito

Tomar una captura ya guardada y convertirla en un borrador usable sin saltar automáticamente a publicación ni mezclar el flujo con guardado privado.

### Regla principal

Produce un borrador claro, breve y usable. No guarda capturas nuevas ni altera el almacenamiento privado.

### Inputs aceptados

`convierte esta captura`, `hazme un borrador con esta captura`, `pasalo a post`, `pasalo a guion`, `pasalo a carrusel`, `recupera la captura <id> y conviertela`, o cualquier petición explícita de transformar una captura ya guardada.

### Prioridad de intención

1. leer captura existente
2. detectar formato pedido o recomendado
3. producir borrador
4. aplicar privacidad
5. aplicar `JUDGE.md` si el flujo lo pide

No antes: volver a guardar la captura, inspeccionar adjuntos como primera acción, publicar automáticamente, expandir el texto más de lo necesario.

### Pregunta de aclaración permitida

Solo si falta el formato de salida: `¿Quieres que lo convierta en nota, post, guion o carrusel?`. Si ya está claro por contexto o `suggested_format`, no preguntar.

### Output mínimo

Formato recomendado, riesgos de privacidad, borrador breve, puntuación Judge si aplica, decisión.

### Formatos permitidos

Nota privada, post, guion, carrusel, borrador breve no publicable. No asume que toda captura acaba publicada.

### Reglas de privacidad

Antes de entregar: revisar nombres reales, terceros identificables, logos de empresa, ubicaciones exactas, rutinas o datos sensibles. Si detecta riesgo: generalizar, marcarlo, o recomendar nota privada.

### Uso de JUDGE.md

Aplicar cuando el flujo operativo lo pida, el usuario lo pida, o la pieza esté a punto de considerarse válida para el banco. Si la nota es menor de 8/10, mejorar el borrador antes de darlo por bueno. Si el flujo lo pide, registrar en `JUDGE-REGISTRO.md` con decisión final y siguiente acción mínima. No toca Git salvo en un flujo ya pedido y con diff claro.

### Límites duros

No debe: guardar nuevas capturas, tocar el JSONL privado, cambiar estados en privado sin que el flujo lo pida, publicar automáticamente, tocar `.env`/secretos/servicios/paquetes/Docker/MCPs/Playwright/memoria externa, convertir cualquier idea en contenido público sin revisar privacidad.

### Frontera con la skill 1

Empieza solo cuando la captura ya existe o el usuario pide expresamente transformar algo ya guardado. Si el usuario todavía está intentando guardar algo nuevo, el flujo vuelve a la skill 1.

---

## Criterio de oficialización

Puede pasar a oficial versionada si cumple a la vez:

1. mantiene `3/3` capturas reales útiles sin errores graves;
2. la entrada natural ya no rompe el flujo de guardado;
3. no mezcla captura y contenido cuando la intención es clara;
4. el alcance queda cerrado y no invade otros modos;
5. Erick aprueba versionarla.

No debe oficializarse todavía si: vuelve a desviar foto + texto libre a copy en vez de guardado, vuelve a guardar wrapper o plantilla como contenido real, necesita demasiadas aclaraciones para casos normales, o sigue mezclando demasiadas responsabilidades en una sola skill.

## Orden de ejecución pendiente

1. ~~Versionar la spec y el plan~~ — hecho, consolidado en este archivo.
2. ~~Definir contrato final de la skill 1~~ — hecho, arriba.
3. ~~Definir contrato final de la skill 2~~ — hecho, arriba.
4. Decidir nombres finales y ubicación en el repo (los nombres de trabajo ya están fijados arriba, falta confirmarlos como definitivos).
5. Crear versión oficial mínima de la skill 1.
6. Probarla con una captura real.
7. Crear versión oficial mínima de la skill 2.
8. Probarla con una captura ya guardada.
9. Decidir si la skill puente de `HERMES_HOME` se archiva o se mantiene un ciclo más.

## Verificación mínima de que la separación quedó bien hecha

- una captura nueva entra por la skill 1 sin desviarse a redacción;
- una captura ya guardada entra por la skill 2 y sale como borrador usable;
- ninguna de las dos toca secretos, `.env`, servicios o Git sin diff claro;
- el usuario ya no necesita recordar una plantilla rígida para guardar algo desde móvil.

## Riesgos a vigilar durante la implementación

Duplicar lógica entre skills, dejar outputs inconsistentes, romper la prioridad de captura, mezclar de nuevo análisis visual y redacción en la skill 1, dejar demasiado pobre la skill 2 y obligar a rehacer manualmente cada borrador.
