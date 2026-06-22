# PERSONAL OPS V1

## Estado

- estado: activo en modo controlado
- canal principal: Telegram
- alcance: decisiones, prioridades, dudas y notas privadas
- publicacion automatica: no

## Proposito

Usar Hermes desde movil para descargar, ordenar y recuperar cosas personales u operativas que no son contenido publico.

Personal Ops V1 existe para reducir friccion mental, no para sustituir criterio humano ni para automatizar decisiones sensibles.

## Casos de uso permitidos

- capturar una decision personal o laboral para revisarla luego
- guardar una duda recurrente
- registrar una idea no publicable
- pedir priorizacion de la siguiente sesion de portatil
- convertir una captura privada en tarea o nota
- pedir un resumen privado de lo pendiente
- descargar una preocupacion o recordatorio en formato recuperable

## Casos de uso no permitidos

- publicar en redes
- mover secretos
- tocar `.env`
- tocar servicios
- automatizar decisiones sensibles
- borrar datos sin permiso
- convertir por defecto vida personal en contenido

## Formatos de salida validos

- nota privada
- tarea
- backlog
- revisar luego
- decision sugerida
- resumen corto

## Regla de formato movil

Cuando Hermes devuelva algo que luego vas a reutilizar, debe intentar que salga facil de copiar:

- listas cortas;
- una referencia por linea;
- ids o rutas aislados si hacen falta;
- evitar mezclar el dato util dentro de demasiado texto.

Si el canal lo permite, puede anadir botones de copia para ids o rutas reutilizables.
En Telegram esto ya quedo validado para listados de capturas.

## Regla principal

Si el usuario plantea algo como decision, duda, prioridad, tarea o nota personal, Hermes debe tratarlo primero como `Personal Ops`, no como `Content`.

Si la intencion no esta clara, Hermes puede hacer una sola pregunta corta para distinguir:

`Quieres guardarlo como nota privada, convertirlo en tarea o usarlo como contenido?`

## Flujo minimo

1. capturar desde Telegram
2. guardar fuera de Git si corresponde
3. devolver `id` o resumen corto
4. proponer una sola siguiente accion
5. recuperar despues desde portatil o Telegram si hace falta

## Regla de recuperacion humana

Personal Ops V1 debe ser usable sin obligarte a memorizar ids largos.

Formas validas de pedir recuperacion:

- `Recupera la ultima captura`
- `Dime mis ultimas 5 capturas`
- `Recupera la numero 2`
- `Recupera mi ultima decision`
- `Recupera la nota sobre prioridades del portatil`

Si hay ambiguedad, Hermes debe hacer una sola pregunta corta.

## Ejemplos de uso real

### Prioridad de sesion

```text
Captura movil

Tipo: decision personal
Texto: Estoy decidiendo que tarea hacer primero en el portatil esta semana.
Privacidad: no publicar
Formato sugerido: nota
```

### Duda recurrente

```text
Captura movil

Tipo: duda recurrente
Texto: No se si conviene abrir Personal Ops ya o esperar una semana mas.
Privacidad: no publicar
Formato sugerido: nota
```

### Recuperacion privada

```text
Recupera la captura <id> y devuelveme:
- resumen en 3 lineas
- decision sugerida
- sin convertirlo en contenido publico
```

## Criterio de exito

Personal Ops V1 funciona si:

1. permite capturar cosas privadas sin friccion;
2. ayuda a priorizar sin convertir todo en contenido;
3. devuelve salidas cortas y utiles;
4. mantiene la privacidad por defecto;
5. no invade Research, Content ni Builder.

## Limite

Personal Ops V1 ayuda a pensar y ordenar.

No decide por ti en temas sensibles ni reemplaza una revision humana cuando la situacion lo requiere.
