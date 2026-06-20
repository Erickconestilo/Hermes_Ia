# MODO POST DIARIO

## Uso rapido

Escribir:

```text
Modo post

Contexto:
[cuento que aparece en la foto, video o momento]
```

## Objetivo

Convertir una foto, video corto o momento del dia en un caption publicable para `CiudadanoInusual`.

No reemplaza a `Modo guion`. Este modo sirve cuando hay una imagen, clip o escena concreta y se quiere acompanarla con texto.

## Plantilla completa

```text
Modo post

Contexto:
[cuento que aparece en la foto, video o momento]

Objetivo:
Convierte esto en un post publicable para CiudadanoInusual.

Primero revisa:
- si hay una idea publicable o solo una nota privada;
- que dato sensible conviene ocultar;
- que tono encaja mejor;
- si falta contexto importante.

Privacidad:
Si aparecen nombres reales, caras de terceros, empresa, ubicacion exacta, matriculas, tickets, precios privados o datos sensibles, preguntame antes de usarlos.

Devuelve:
- caption corto;
- caption medio;
- caption mas personal;
- texto alternativo para accesibilidad;
- hashtags opcionales;
- advertencias de privacidad si aplica.

Tono:
Realista, cercano, con humor ligero, sin postureo y sin motivacion barata.

Reglas:
- no crees archivos;
- no edites el repo;
- no hagas commit;
- no inventes detalles;
- devuelve solo el contenido final en pantalla.
```

## Cuándo usarlo

- foto de comida en ruta
- foto de trayecto
- foto de trabajo de campo sin datos sensibles
- captura de estudio o aprendizaje
- imagen de herramienta, mochila, casco o libreta
- momento de hogar, recado, mercado o descanso

## Cuándo no usarlo

- si la historia necesita narracion, usar `Modo guion`
- si la idea es educativa en varias partes, usar futuro `Modo carrusel`
- si no hay historia ni imagen clara, guardar como nota privada

## Salida esperada

### Caption corto

Texto de 1-2 lineas para publicar rapido.

### Caption medio

Texto de 3-6 lineas con contexto, humor o reflexion.

### Caption mas personal

Texto mas humano, con voz propia y una idea clara.

### Texto alternativo

Descripcion breve de la imagen o video para accesibilidad.

### Hashtags opcionales

Solo si aportan contexto. No llenar el post de etiquetas genericas.

### Privacidad

Avisar si conviene tapar, ocultar o generalizar algun dato antes de publicar.
