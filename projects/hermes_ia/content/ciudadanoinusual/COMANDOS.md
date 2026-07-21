# COMANDOS - CiudadanoInusual

## Proposito

Reducir la superficie de comandos de `Hermes Creador` a algo que se pueda usar cansado, con una mano y desde el movil.

Principio 4 de la Constitucion: *"si una funcion obliga al usuario a recordar demasiados pasos, la funcion esta mal disenada"*.

Este archivo aplica ese principio a los comandos.

---

## 1. El problema medido

Superficie actual repartida entre `HERMES-CREADOR.md`, `GUIA-RAPIDA-MODOS.md`, `MODO-CALLE.md` y los cuatro archivos de modo diario:

| # | Comando | Estructura que exige |
| --- | --- | --- |
| 1 | `¿Que toca hoy?` | libre |
| 2 | `Video` / `Vídeo` | `Situacion:` |
| 3 | `Historia` / `Story` / `Stories` | `Situacion:` |
| 4 | `He publicado` | `Canal:` + `Pieza:` + `Resultado:` |
| 5 | `Modo guion` | `Situacion:` |
| 6 | `Modo post` | `Contexto:` |
| 7 | `Modo carrusel` | `Tema o situacion:` |
| 8 | `Modo calle` | `Estoy desde el movil` + `Contexto rapido:` |
| 9 | `Captura dia a contenido` | `Hoy paso esto:` |
| 10 | `Evalua esta foto como referencia visual...` | parrafo de 6 lineas |
| 11 | `Revision de privacidad para publicar` | bloque estructurado |
| 12 | `python3 scripts/captura-movil.py add --text ... --tags ...` | flags de CLI |
| 13 | `python3 scripts/send-telegram-photo.py <ruta> "<caption>"` | ruta exacta |
| 14 | `captura-movil.py list / show / update-status / export-curated` | subcomandos |
| 15 | `/whoami`, `/status`, `/background` | ninguna |

Quince entradas, seis plantillas distintas, dos con acentos y signos de apertura, dos que exigen escribir Python desde el telefono.

### Las redundancias

No es solo que sean muchos. Es que **se solapan**:

- **`Video` y `Modo guion` hacen exactamente lo mismo**: guion de video vertical corto. Son el mismo comando con dos nombres.
- **`Historia` y `Modo post` se solapan**: ambos convierten una imagen o momento en texto corto.
- **Hay tres routers para el mismo problema**: `¿Que toca hoy?`, `Modo calle` y `Captura dia a contenido` existen los tres para cuando no sabes que formato usar.
- **`Revision de privacidad` no deberia existir como comando.** Es opcional, y el dia que se te olvide es el dia que publicas una matricula. Un control de seguridad que depende de recordarlo esta mal disenado.

---

## 2. La superficie nueva

### Nivel 0 - Sin comando (el caso normal)

**Mandas lo que sea. Hermes decide.**

Una foto. Una nota de voz. Un texto suelto. Sin estructura, sin plantilla, sin palabra clave.

Hermes debe responder siempre con:

1. si esto es contenido o nota privada;
2. formato recomendado y por que;
3. **riesgos de privacidad** (siempre, sin pedirlo);
4. una version usable ahora;
5. si conviene trabajarlo mejor luego en el portatil.

Esto cubre el 80% de los usos reales y sustituye a `Modo calle`, `Captura dia a contenido`, `Referencias visuales` y el enrutado de `Modo post` / `Modo guion` / `Modo carrusel`.

**Si no te acuerdas de nada de este archivo, manda la foto y ya.**

---

### Nivel 1 - Forzar formato (3 palabras)

Solo cuando ya sabes que quieres y no quieres que Hermes decida:

| Palabra | Que hace |
| --- | --- |
| `guion` | video vertical corto |
| `post` | caption para una foto o momento |
| `carrusel` | varias slides |

Uso: la palabra, salto de linea, y cuentas lo que pasó. Sin `Situacion:`, sin `Contexto:`, sin `Tema:`.

```text
guion

Hoy en la obra a 31 grados, empece a las 8 y no pare hasta las 4.
```

---

### Nivel 2 - Gestion (2 palabras)

| Palabra | Que hace |
| --- | --- |
| `hoy` | que conviene hacer hoy (una sola recomendacion editorial) |
| `publicado` | registrar una publicacion y su aprendizaje |

`publicado` no exige estructura. Cuentas lo que sea y Hermes pregunta solo lo que falte:

```text
publicado

Subi el post de la comida a Instagram, 40 likes y dos comentarios.
```

---

### Nivel 3 - Privado (1 palabra)

| Palabra | Que hace |
| --- | --- |
| `guarda` | nota privada. No es contenido y no debe convertirse en contenido. |

Hermes guarda la nota con `captura-movil.py` **por su cuenta** y devuelve el `id`. Tu no escribes Python desde el movil nunca.

---

## 3. Resumen: seis palabras

```
guion   post   carrusel   hoy   publicado   guarda
```

Todas en minuscula. Sin acentos. Sin signos. Sin plantilla. Maximo nueve caracteres.

Y la regla que las cubre todas: **si no te acuerdas de ninguna, manda la foto y ya.**

---

## 4. Reglas que Hermes debe cumplir siempre

Estas no son comandos. Son comportamiento permanente.

**La revision de privacidad es automatica.**
Nunca hay que pedirla. Se ejecuta en toda pieza que pueda acabar publicada, sin excepcion. Checklist interno: matriculas, caras de terceros, logos de empresa, ubicacion exacta, nombres, carteles, tickets, documentos, codigos, pantallas, detalles de obra o cliente, consentimiento si aparece otra persona.

**Los scripts los ejecuta Hermes, no el usuario.**
`captura-movil.py` y `send-telegram-photo.py` son herramientas internas. Si desde el movil hace falta guardar una captura o enviar una imagen, Hermes lo hace y devuelve el resultado. El usuario no escribe rutas ni flags.

**El lenguaje natural siempre funciona.**
`ultimas 5`, `numero 2`, `mi ultima decision`, `enseñame lo que tengo listo` deben seguir funcionando sin comando. Las seis palabras son atajos, no una sintaxis obligatoria.

**Si la entrada mezcla situacion real, broma y cansancio, es material creativo.**
No convertirla en tarea de Builder, script, automatizacion ni organizacion personal salvo peticion explicita. (Regla heredada de `HERMES-CREADOR.md`, sigue vigente.)

**Ante duda de formato, decidir y avanzar.**
No devolver un menu de opciones. Elegir uno, decir por que en una linea y dar la pieza.

---

## 5. Equivalencias: nada se pierde

| Antes | Ahora |
| --- | --- |
| `¿Que toca hoy?` | `hoy` |
| `Video` / `Vídeo` | `guion` |
| `Modo guion` | `guion` |
| `Historia` / `Story` / `Stories` | `post` o Nivel 0 |
| `Modo post` | `post` |
| `Modo carrusel` | `carrusel` |
| `Modo calle` | Nivel 0 (sin comando) |
| `Captura dia a contenido` | Nivel 0 (sin comando) |
| `Evalua esta foto como referencia visual...` | Nivel 0 (mandar la foto) |
| `Revision de privacidad para publicar` | automatico, siempre |
| `He publicado` | `publicado` |
| `captura-movil.py add ...` | `guarda` |
| `send-telegram-photo.py ...` | lo hace Hermes solo |
| `/whoami`, `/status`, `/background` | sin cambios (son del gateway) |

De quince entradas con seis plantillas a seis palabras sin plantilla.

---

## 6. Archivos que este documento sustituye

Para no repetir el problema que diagnostico la auditoria (el repo solo crece), este archivo **reemplaza** la superficie de comandos de:

- `GUIA-RAPIDA-MODOS.md`
- `MODO-CALLE.md`
- `MODO-POST-DIARIO.md`
- `MODO-GUION-DIARIO.md`
- `MODO-CARRUSEL-DIARIO.md`
- `CAPTURA-DIA-A-CONTENIDO.md`

Seis archivos por uno.

**No se han borrado.** Borrar funcionalidad existente requiere confirmacion explicita segun `docs/governance/BOOTSTRAP.md`. Quedan marcados como sustituidos, pendientes de tu aprobacion para eliminarlos.

Lo que **no** sustituye:

- `HERMES-CREADOR.md` mantiene su valor como contrato de comportamiento (que debe y que no debe hacer Hermes al responder, la regla anti-deriva Builder, la salida esperada de cada comando). Solo queda obsoleta su seccion de nombres de comando.
- `PROMPTS-EDICION-IMAGENES.md`, `REFERENCIAS-VISUALES.md` y los checklists siguen igual: son material de apoyo, no comandos.

---

## 7. Criterio de terminado

Esta redisenado bien cuando:

- puedes usar el sistema un martes a las 22:40, cansado, sin abrir ningun archivo;
- no hay ninguna plantilla que rellenar;
- la privacidad se revisa aunque no te acuerdes de pedirla;
- nunca escribes Python desde el telefono;
- y si te olvidas de todo, mandar una foto sigue funcionando.
