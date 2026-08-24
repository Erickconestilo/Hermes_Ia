# Memoria

Indice corto de cambios importantes, para carga rapida de contexto por cualquier agente (Claude, Codex, Hermes).

Una linea por entrada, entre 40 y 150 caracteres. Menos de 40 no suele caber fecha + hecho concreto (queda ambiguo con el tiempo); mas de 150 deja de ser indice y empieza a duplicar la bitacora. El detalle completo va en `learning/bitacora.md`, esto solo apunta a el.

No sustituye la bitacora. No es lectura obligatoria de `BOOTSTRAP.md` (para no subir el peaje de lectura). Es referencia rapida opcional.

## Entradas

- 2026-08-08: SSH endurecido, `PasswordAuthentication no` activo. Detalle: bitacora.md
- 2026-08-08: Hermes Agent actualizado 0.16.0 -> 0.20.0 (20883 commits). Detalle: bitacora.md
- 2026-08-08: Hermes 0.20.0 trae panel web (`hermes dashboard`); apagado, no expuesto. Ver bitacora.
- 2026-08-08: Config Hermes migrada v29->v33; verify_on_stop corregido a "auto". Ver bitacora.
- 2026-08-21: F-03 validado: copia GPG externa y restauracion aislada con 1.427 mensajes, 41 sesiones y 11 capturas.
- 2026-08-21: F-01: tres simulaciones de riesgo bloqueadas; proteccion textual parcial, sin cierre semantico.
- 2026-08-21: VPS actualizado y reiniciado: kernel 6.8.0-138, sin actualizaciones estandar y gateway operativo.
- 2026-08-21: Retencion minima de capturas probada con datos sinteticos; sesiones, logs y backups siguen pendientes.
- 2026-08-21: Skill movil historica ausente del runtime; no se restaura sin decision y prueba reales.
- 2026-08-21: Verificador de secretos ya redactor valores: solo informa tipo, archivo y linea; prueba sintetica aprobada.
- 2026-08-21: Gobernanza reducida: BOOTSTRAP es único arranque; políticas secundarias remiten a fuentes canónicas.
- 2026-08-24: Video Telegram validado con fotogramas y transcripcion local; `video_analyze` nativo sigue desactivado.
- 2026-08-24: Shorts V1 implementado y probado en Linux sintetico; despliegue y cuatro pruebas reales por Telegram pendientes.
