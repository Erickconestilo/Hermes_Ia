# APRENDIZAJES - CiudadanoInusual

## Proposito

Registrar que funciona y que no, con evidencia.

El Principio 6 de la Constitucion dice "evidencia antes que intuicion". Este archivo es donde vive esa evidencia. Sin el, `Hermes Creador` optimiza a ciegas.

Regla: aqui solo entra lo que se puede sostener con un dato, un recuento o una observacion concreta. Las opiniones sin respaldo van a `AUDIENCIA.md` como hipotesis, no aqui.

---

## Parte 1 - Meta-aprendizajes del sistema

Estos no vienen de publicar. Vienen de auditar el propio inventario, y son demostrables hoy.

### Meta-aprendizaje 1 - Se produce video, se publica texto

**Evidencia:** de 18 piezas publicables, 6 son guiones de video vertical. Publicados: 0.
La unica publicacion real (`linkedin-01-hermes-ia-vps`) es texto largo con una captura de pantalla.

**Lectura:** el sistema produce mayoritariamente el formato que no publicas. El video exige grabar, editar y aparecer en camara — tres fricciones que el texto no tiene. La produccion esta desalineada con la ejecucion real.

**Decision derivada:** no producir mas guiones hasta decidir conscientemente si vas a grabar. Si la respuesta es no por ahora, el esfuerzo se reasigna a post y carrusel.

**Fecha:** 2026-07-21. **Estado:** confirmado por inventario, pendiente de decision.

---

### Meta-aprendizaje 2 - El cuello de botella no es crear: es publicar

**Evidencia:** 6 briefings + 20 piezas de content + 18 publicables producidos entre el 11 y el 28 de junio. Publicaciones registradas en ese periodo y hasta hoy: 1.
Tasa de conversion de publicable a publicado: aproximadamente 5%.

**Lectura:** todo el sistema (modos, plantillas, JUDGE, indices) esta optimizado para la fase de creacion, que ya funciona sobrada. La fase de publicacion no tiene ni un solo mecanismo dedicado. `QUEUE.md` tiene unos 15 items pendientes de crear y cero de publicar.

**Decision derivada:** la unica metrica de los proximos 30 dias es publicaciones reales por semana. No piezas creadas.

**Fecha:** 2026-07-21. **Estado:** confirmado.

---

### Meta-aprendizaje 3 - El bloqueo real es visual, no editorial

Este es el hallazgo menos evidente y probablemente el mas importante.

**Evidencia:** clasificacion de las 18 piezas publicables segun `AUDITORIA-PUBLICABLES.md`:

| Estado | Piezas | Cantidad |
| --- | --- | --- |
| Listas para publicar ya | post-04, guion-01, guion-02, guion-06 | 4 |
| Bloqueadas por edicion de imagen | post-01, 02, 03, 05, 06; carrusel-01, 02, 06 | 8 |
| Bloqueadas por falta de fotos propias | carrusel-03, 04, 05 | 3 |
| Bloqueadas por sensibilidad / consentimiento | guion-03 | 1 |

**12 de 18 piezas estan bloqueadas por trabajo visual**, no por trabajo de escritura. Tapar matriculas, recortar logos, conseguir fotos propias.

**Lectura:** el texto esta resuelto y sobra. Lo que falta es un flujo de imagen: capturar fotos utiles durante la jornada, y editarlas para privacidad de forma rapida. Ningun documento del repositorio aborda esto. `PROMPTS-EDICION-IMAGENES.md` existe pero es para generar, no para sanear.

**Decision derivada:** la mejora de mayor retorno del sistema no es otra skill de texto. Es un flujo simple de "foto -> tapar lo sensible -> lista". Y a corto plazo: empezar publicando las 4 piezas que no requieren nada.

**Fecha:** 2026-07-21. **Estado:** confirmado por inventario.

---

### Meta-aprendizaje 4 - La marca se encontro en la pieza 09

**Evidencia:** las piezas 01-08 derivan de briefings de Research (IA en pymes, FP, vivienda, ayudas). Voz de analista, segunda persona, sin escenas, casi ninguna con frase memorable.
Las piezas 09-20 derivan de vida vivida. Primera persona, escenas concretas, todas con frase memorable.

**Lectura:** hay un cambio de voz identificable a mitad del banco. Las primeras 8 podria haberlas escrito cualquiera con las mismas fuentes.

**Decision derivada:** el contenido derivado de research solo se convierte en pieza si pasa por experiencia propia. Detalle completo en `AUDIENCIA.md`, seccion 1.

**Fecha:** 2026-07-21. **Estado:** confirmado por lectura del banco.

---

### Meta-aprendizaje 5 - Sin datos, JUDGE no discrimina

**Evidencia:** 5 evaluaciones registradas en `JUDGE-REGISTRO.md`. Notas: 8, 8, 8, 8, 8. Decisiones: valida, valida, valida, valida, valida.

**Lectura:** un juez cuya distribucion de notas es constante no aporta informacion. El umbral de 8/10 no esta filtrando nada porque nunca se evalua algo que se descarte.

**Decision derivada:** evaluar tambien piezas que se rechazan, y registrar al menos un suspenso. Si en 10 evaluaciones no hay ninguna por debajo de 8, el criterio esta roto y hay que recalibrarlo.

**Fecha:** 2026-07-21. **Estado:** confirmado.

---

## Parte 2 - Aprendizajes por publicacion

Aqui va lo que se aprende de publicar de verdad. Ahora mismo hay una sola entrada.

### Publicacion 01 - LinkedIn, 2026-06-21

**Pieza:** `publicaciones/linkedin-01-hermes-ia-vps.md`
**Canal:** LinkedIn
**Formato:** texto largo + captura de pantalla
**Territorio:** IA y aprendizaje sin humo
**JUDGE:** 8/10

**Datos de recepcion:** ninguno registrado. El seguimiento sigue diciendo "revisar impresiones, reacciones y comentarios" un mes despues.

**Aprendizaje disponible:** ninguno solido. Sin datos no hay aprendizaje, solo intuicion.

**Lo unico observable:** el tono "menos magia, mas criterio / menos promesa, mas proceso" es coherente con el Patron A de la voz descrito en `AUDIENCIA.md`. La pieza es fiel a la marca. Si conecto o no, se desconoce.

**Accion pendiente:** entrar en LinkedIn, mirar las metricas reales de esa publicacion y rellenar la fila. Es una tarea de 5 minutos que lleva un mes bloqueando todo el bucle de evidencia del sistema.

---

## Parte 3 - Como registrar una publicacion

Cuando publiques algo, anade una entrada aqui con esta estructura. No hace falta que sea larga.

```text
### Publicacion NN - <canal>, <fecha>

**Pieza:** <archivo>
**Canal:** <LinkedIn / Instagram / TikTok / Shorts>
**Formato:** <texto / post+foto / carrusel / video>
**Territorio:** <oficio real / cansancio honesto / IA sin humo / comida en ruta>

**Datos a las 48h:** impresiones, reacciones, comentarios, guardados, compartidos
**Datos a los 7 dias:** los mismos

**Que funciono:**
**Que no funciono:**
**Cuanto costo producirla:** <tiempo real, incluida edicion de imagen>
**¿Repetiria el formato?:**
```

El campo de coste de produccion importa tanto como el de resultado. Un formato que funciona bien pero te quema no es repetible, y la Constitucion (Principio 11) lo prohibe explicitamente.

---

## Parte 4 - Hipotesis abiertas

Cosas que `AUDIENCIA.md` afirma y que aun no estan demostradas. Cada publicacion deberia confirmar o desmentir alguna.

| # | Hipotesis | Como se comprueba | Estado |
| --- | --- | --- | --- |
| H1 | La audiencia primaria (trabajador de oficio que estudia) existe en tus canales | comentarios y perfiles de quien interactua | sin datos |
| H2 | LinkedIn responde mejor al territorio "oficio real" que Instagram | publicar la misma idea adaptada en ambos | sin datos |
| H3 | El territorio "cansancio honesto" conecta y no resulta deprimente | ratio de guardados y comentarios en 3 piezas del territorio | sin datos |
| H4 | El ranking de comida `/25` funciona como formato recurrente | publicar 3 episodios y ver si crece | sin datos |
| H5 | La anti-epica es el diferenciador real | comentarios que mencionen honestidad, realidad o identificacion | sin datos |
| H6 | El video no se va a producir por friccion real, no por falta de guiones | observar 30 dias si se graba alguno | sin datos |

Regla: no anadir hipotesis nuevas hasta cerrar al menos dos de estas.

---

## Regla de mantenimiento

Este archivo solo tiene valor si se actualiza al publicar, no al planificar.

Si pasan 30 dias sin una entrada nueva en la Parte 2, el problema no es este archivo: es que no se esta publicando. En ese caso la accion no es mejorar el documento, es publicar algo.
