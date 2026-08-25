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
- 2026-08-24: Shorts V1 desplegado con skill 0.2.0; faltan tres cortos y un largo reales por Telegram.
- 2026-08-25: Telegram optimizado: max_turns 20 y menos herramientas no usadas; gateways activos. Ver bitacora.
- 2026-08-25: Segunda pasada Telegram: session_search, browser y video fuera; image_gen solo en default. Ver bitacora.
- 2026-08-25: Perfiles finales: terra/luna por Codex y Gemini 3.7 fallback; Telegram recortado. Ver bitacora.
- 2026-08-25: Google: probar endpoint directo antes de atribuir un 503 o URL incorrecta a autenticacion. Ver bitacora.
- 2026-08-25: `default` y `auscultacion` pasan a Gemini 3.6 Flash vía Google AI Studio por cuota de Codex.
- 2026-08-25: Fase 1: retencion y secretos corregidos; suite unittest 51 OK y 10 omisiones explicadas. Ver bitacora.
- 2026-08-25: Fase 2: runbooks y estados corregidos; F-03 cerrado y proveedores centralizados en CODEX-BRIEF. Ver bitacora.
