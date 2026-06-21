# ROADMAP HERMES

## Proposito

Este archivo es la fuente canonica para saber donde esta `Hermes_Ia`, que esta cerrado, que sigue abierto y que no se debe activar todavia.

No sustituye los runbooks tecnicos. Sirve para tomar decisiones sin volver a reconstruir el proyecto desde conversaciones.

## Mision

Convertir Hermes en el arnes personal de IA de Erick/CiudadanoInusual:

- Research: investigar oportunidades, tecnologia, IA, FP, vivienda, topografia y decisiones personales con fuentes y riesgos.
- Content: transformar vida real, trabajo, estudio, fotos y notas en piezas publicables para CiudadanoInusual.
- Builder: mejorar `Hermes_Ia` con scripts, documentacion y verificaciones utiles.
- Mobile Ops: usar Telegram como canal operativo desde el movil cuando no hay portatil.

## Estado tecnico actual

- Repo local: `C:\Users\guill\Documents\Hermes_Ia`
- VPS: `hermes-01` en Hetzner, Ubuntu 24.04, plan CX33 x86.
- Usuario operativo: `hermes`.
- Instalacion Hermes: nativa en `/home/hermes/.hermes`.
- Workspace VPS: `/home/hermes/workspace/Hermes_Ia`.
- Backend: `local`.
- Proveedor principal: `openai-codex`.
- Modelo principal: `gpt-5.4`.
- Fallback: OpenRouter.
- Sincronizacion: Git local -> GitHub `origin` y VPS `vps`.
- Telegram Gateway: operativo como servicio de usuario `hermes-gateway.service`.
- Imagenes generadas: envio a Telegram mediante `scripts/send-telegram-photo.py`.

## Estado por fases y evidencias

| Area | Estado | Evidencia |
| --- | --- | --- |
| Fase 0 documental e infraestructura | Cerrada | README, runbooks base, bitacora y commits iniciales |
| G1 Research / Content / Builder | Cerrada | `projects/hermes_ia/USOS-OFICIALES.md` |
| Research base | Cerrada | 6 briefings en `projects/hermes_ia/research/` |
| Banco inicial Content 20/20 | Cerrado | 20 salidas base en `projects/hermes_ia/content/ciudadanoinusual/` |
| Judge definido | Cerrado | `projects/hermes_ia/JUDGE.md` |
| Telegram Gateway basico | Cerrado | `runbooks/09-telegram-gateway.md` y respuesta desde movil |
| Envio de imagenes por Telegram | Cerrado | `scripts/send-telegram-photo.py` probado |
| Publicacion externa | Abierta | 1 publicacion LinkedIn registrada |
| Telegram operativo base | Cerrado | `/whoami`, `/status`, imagen, voz y `/background` pequeno validados |
| Flujo movil extremo a extremo | Abierto | falta captura movil -> pieza -> judge -> publicacion |
| Captura Movil V1 | Operativa | prueba real desde Telegram; placeholder corregido; skill experimental ajustada; validacion anti-plantillas |
| Judge aplicado y registrado | Abierto | falta registro minimo de evaluaciones reales |
| Banco 2 | Iniciado | vida real, convivencia, hogar, comida, trayectos |
| Continuidad semanal | Abierta | falta rutina semanal estable |

## Track A: Plataforma y Mobile Ops

### Operativo ahora

- Hermes nativo en VPS.
- `openai-codex` con `gpt-5.4`.
- OpenRouter como fallback.
- Telegram Gateway para hablar con Hermes desde movil.
- Envio de imagenes generadas a Telegram.
- Git como mecanismo de sincronizacion.
- Skills experimentales dentro de `HERMES_HOME` como incubadora de flujos repetibles de bajo riesgo.
- Skill `ciudadanoinusual-mobile-intake` como experimental activa.

### Siguiente experimento seguro

- Completar el primer flujo movil extremo a extremo: captura privada -> recuperacion -> borrador -> `JUDGE.md`.
- Probar recepcion de archivo desde Telegram para confirmar limite real del canal movil.
- Operativa semanal: decidir que se hace desde movil y que se reserva para portatil.

### Futuro planificado

- Formalizar skills oficiales versionadas solo cuando un flujo se repita varias veces y supere auditoria.
- Perfiles/subagentes cuando Research, Content, Builder y Judge ya tengan uso estable.
- Cron con una sola tarea no recurrente antes de cualquier automatizacion persistente.
- Docker solo como sandbox futuro para Builder fuerte.

### Descartado por ahora

- Docker como backend actual.
- MCPs.
- Playwright.
- Memoria externa.
- Kanban.
- Dashboard o API publica.
- Automatizaciones recurrentes sin prueba manual previa.

## Alineacion con capacidades oficiales de Hermes

| Capacidad oficial | Estado real en `Hermes_Ia` | Riesgo | Politica local |
| --- | --- | --- | --- |
| Telegram Gateway con texto, imagenes, archivos y voz | texto, imagen recibida y voz validados; archivo aun pendiente | medio | experimento seguro si no toca secretos ni servicios |
| Comandos `/whoami` y `/status` | validados desde Telegram | bajo | permitidos con registro posterior |
| `/background` desde mensajeria | validado en tareas pequenas no destructivas | medio | permitido solo para tareas no destructivas y registradas |
| Skills experimentales | `ciudadanoinusual-mobile-intake` creada en `HERMES_HOME` | bajo-medio | permitidas como incubadora con auditoria posterior |
| Toolsets amplios por plataforma | disponibles segun instalacion | variable | usar solo capacidades necesarias; Docker/MCPs/Playwright siguen rojos |
| Cron one-shot y recurrente | no activo | medio-alto | one-shot futuro con permiso; recurrente sigue rojo |
| Context files `AGENTS.md` | activo como politica del repo | bajo | mantener actualizado y conciso |

## Incubadora de skills y confianza supervisada

Hermes puede crear y usar skills experimentales dentro de `HERMES_HOME` cuando detecte un flujo repetible y de bajo riesgo.

Regla principal: Hermes puede expandirse en bajo riesgo si deja rastro. Hermes debe pedir permiso en alto riesgo.

Indice detallado: `projects/hermes_ia/SKILLS-EXPERIMENTALES.md`.

Condiciones:

- no tocar secretos, `.env` ni servicios;
- no activar cron recurrente;
- no instalar paquetes;
- no tocar Docker, MCPs, Playwright ni memoria externa;
- no publicar en redes;
- no hacer cambios destructivos;
- no modificar el repo sin diff claro;
- dejar registro de que creo, donde vive y para que sirve.

| Skill | Estado | Ubicacion | Proposito | Condicion para formalizar |
| --- | --- | --- | --- | --- |
| `ciudadanoinusual-mobile-intake` | experimental activa | `HERMES_HOME` | Captura Movil V1, Modo Calle y flujo Telegram para CiudadanoInusual | superar 3 capturas reales utiles sin errores graves y sin tocar Git/servicios/secretos sin permiso |

## Track B: CiudadanoInusual y feedback real

### Operativo ahora

- Modo guion.
- Modo post.
- Modo carrusel.
- Modo calle.
- Indice de publicables.
- Indice de publicaciones.
- Revision de privacidad antes de publicar.

### Inventario real actual

- Research: 6 briefings.
- Content base: 20 salidas.
- Guiones publicables: 6.
- Posts visuales: 6.
- Carruseles: 6.
- Formatos recurrentes: 1.
- Publicaciones registradas: 1.

### Siguiente experimento seguro

- Publicar y medir piezas simples con baja friccion.
- Usar Telegram para capturar ideas desde la calle.
- Registrar metricas basicas de 24h y 7d cuando haya publicaciones.
- Aplicar Judge solo a piezas concretas, no a todo el banco de golpe.

### Futuro planificado

- Banco 2 con vida real expandida: pareja, convivencia, hogar, dias libres, recados, comida, ocio y mini viajes.
- Versiones LinkedIn de experiencias de obra/topografia.
- Reciclaje de piezas cuando haya suficiente material publicado.

### Descartado por ahora

- Convertir vivienda/credito/ayudas en eje central del canal.
- Publicar capturas ajenas como contenido propio.
- Publicar datos de obra, empresa, cliente, ubicacion exacta o terceros sin revision.

## Track C: Personal Ops V1

### Objetivo

Usar Hermes desde movil no solo para contenido, sino para vida, decisiones y trabajo personal.

### Futuro inmediato

Este track empieza despues de cerrar Mobile Ops V1 basico.

Funciones iniciales:

- capturar decisiones;
- guardar dudas recurrentes;
- registrar ideas no publicables;
- resumir semana manualmente;
- priorizar proxima sesion de portatil;
- convertir capturas en tareas;
- ayudar a elegir siguiente accion sin quedar bloqueado.

### Limite

Personal Ops no publica, no toca secretos, no automatiza decisiones sensibles y no sustituye criterio humano.

## Track D: Automatizacion controlada

### Futuro planificado

- Cron one-shot: futuro experimento seguro con permiso explicito.
- Background sessions: experimento seguro si la tarea es pequena, no destructiva y queda registrada.

### Rojo por ahora

- Cron recurrente sin permiso fuerte.
- Automatizaciones que toquen servicios, `.env`, secretos, Docker, MCPs, Playwright o memoria externa.
- Publicacion automatica en redes.

## Tareas actuales

1. Probar envio de archivo desde Telegram y registrar limite real sin versionar privados.
2. Completar validacion de Captura Movil V1 hasta 3 capturas reales utiles sin errores graves.
3. Convertir una captura movil en borrador, aplicar `JUDGE.md` y registrar decision.
4. Decidir si `Personal Ops V1` entra ya como siguiente uso oficial de movil.
5. Registrar el criterio final sobre `/background` pequeno como experimento seguro.

## Condiciones de cierre de Mobile Ops V1

Mobile Ops V1 queda cerrado solo cuando:

- Telegram permite capturar una idea desde movil.
- La captura queda guardada fuera de Git.
- Se puede recuperar despues desde portatil o VPS.
- Se convierte una captura en una pieza util.
- Se aplica Judge y se registra decision.
- Se publica o se deja lista una pieza con privacidad revisada.

## Regla de decision

Si una idea nueva no mejora ejecucion real, captura movil, publicacion, verificacion o aprendizaje medible, vuelve al backlog.
