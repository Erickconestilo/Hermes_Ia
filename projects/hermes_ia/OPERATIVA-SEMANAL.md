# OPERATIVA SEMANAL

## Proposito

Separar la semana real en dos ritmos:

- movil: capturar, decidir rapido y publicar piezas simples;
- portatil: ordenar, editar, versionar, verificar y cerrar commits.

El objetivo es que `Hermes_Ia` avance aunque la mayor parte de la vida ocurra en la calle.

## Regla semanal

Cada semana debe dejar al menos una de estas evidencias:

- una captura movil revisada;
- una pieza publicada o lista para publicar;
- una mejora real del sistema editorial;
- una prueba de Mobile Ops;
- una decision registrada en roadmap, queue o bitacora.

## Dias de movil

Usar Telegram y `Modo calle` para:

- contar una situacion en bruto;
- mandar una foto o describirla;
- decidir si es post, guion, carrusel o nota privada;
- revisar privacidad;
- pedir una version corta publicable;
- guardar ideas que no se puedan trabajar en el momento.

No hacer desde movil:

- editar varios archivos del repo;
- resolver conflictos Git;
- tocar `.env`;
- cambiar gateway, cron, Docker, MCPs o servicios;
- publicar algo con datos sensibles sin revisar.

## Dia de portatil

Usar el portatil para:

- ordenar capturas buenas;
- editar imagenes o tapar datos;
- versionar publicables importantes;
- actualizar indices;
- aplicar Judge;
- hacer commit y push;
- revisar metricas de publicaciones.

## Flujo recomendado

1. Durante la semana: capturar ideas desde Telegram.
2. Marcar cada captura como `inbox`.
3. En portatil: revisar capturas y elegir una.
4. Convertirla en pieza.
5. Revisar privacidad.
6. Aplicar Judge.
7. Publicar manualmente o dejar lista.
8. Registrar aprendizaje.

## Checklist de cierre semanal

- `git status` limpio o pendiente explicado.
- Capturas privadas no versionadas.
- Si hubo publicacion, registrada en `publicaciones/INDICE-PUBLICACIONES.md`.
- Si hubo cambio operativo, commit y push a `origin` y `vps`.
- Siguiente accion concreta en `projects/hermes_ia/TAREAS.md`.

## Limite

No convertir cada semana en una reunion de estrategia.

Si no hay tiempo, hacer una captura buena y una revision de privacidad ya cuenta como avance.

