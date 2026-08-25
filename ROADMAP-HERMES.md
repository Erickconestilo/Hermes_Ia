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

- Repo local: workspace local del proyecto
- VPS: `hermes-01` en Hetzner, Ubuntu 24.04, plan CX33 x86.
- Usuario operativo: `hermes`.
- Instalacion Hermes: nativa en `/home/hermes/.hermes`.
- Workspace VPS: `/home/hermes/workspace/Hermes_Ia`.
- Backend: `local`.
- Proveedores y modelos por perfil: ver [`docs/CODEX-BRIEF.md`](docs/CODEX-BRIEF.md#estado-de-proveedores-y-modelos-fuente-unica).
- Sincronizacion: Git local -> GitHub `origin` y VPS `vps`.
- Telegram Gateway: operativo como servicio de usuario `hermes-gateway.service`.
- Version Hermes Agent: `0.20.0` (actualizado el 2026-08-08 desde `0.16.0`; ver `learning/bitacora.md`). La migracion de config `v29 -> v33` y `agent.verify_on_stop = "auto"` quedaron ejecutados y verificados ese mismo dia.
- SSH del VPS endurecido el 2026-08-08: `PasswordAuthentication no` activo, `PermitRootLogin` ya estaba en `prohibit-password`. Pendiente aparte: `fail2ban`/`ufw`.
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
| Flujo movil extremo a extremo | Cerrado | captura privada -> recuperacion -> borrador -> Judge -> registro completados |
| Captura Movil V1 | Parcial | script versionado y pruebas historicas; skill experimental ausente del runtime el 2026-08-21 |
| Personal Ops V1 | Activo en modo controlado | `projects/hermes_ia/CAPTURA.md` y `projects/hermes_ia/TAREAS.md` |
| Empleo Ops V0 | Futuro experimento controlado; no operativo | contrato y prueba sintetica en `projects/hermes_ia/EMPLEO-OPS-V0.md` |
| Judge aplicado y registrado | Cerrado | `projects/hermes_ia/JUDGE-REGISTRO.md` con piezas reales evaluadas |
| Banco 2 | Iniciado | vida real, convivencia, hogar, comida, trayectos |
| Continuidad semanal | Abierta | falta rutina semanal estable |

## Track A: Plataforma y Mobile Ops

### Operativo ahora

- Hermes nativo en VPS.
- Estado vigente de proveedores y modelos: ver [`docs/CODEX-BRIEF.md`](docs/CODEX-BRIEF.md#estado-de-proveedores-y-modelos-fuente-unica).
- Telegram Gateway para hablar con Hermes desde movil.
- Envio de imagenes generadas a Telegram.
- Git como mecanismo de sincronizacion.
- Skills experimentales dentro de `HERMES_HOME` como incubadora de flujos repetibles de bajo riesgo.
- No hay skill puente activa actualmente: `ciudadanoinusual-mobile-intake` esta ausente de `HERMES_HOME` y no es detectable por Hermes.

### Siguiente experimento seguro

- Probar Hermes Creador con cinco entradas reales en lenguaje natural desde el movil.
- Validar que al menos cuatro queden bien encaminadas, con una correccion como maximo y sin errores graves de privacidad.
- Publicar manualmente al menos una pieza y registrar su resultado antes de ampliar comandos o skills.

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
| Telegram Gateway con texto, imagenes, archivos y voz | texto, imagen, voz y PDF validados; `.asc` rechazado | medio | experimento seguro si no toca secretos ni servicios |
| Comandos `/whoami` y `/status` | validados desde Telegram | bajo | permitidos con registro posterior |
| `/background` desde mensajeria | validado en tareas pequenas no destructivas | medio | permitido solo para tareas no destructivas y registradas |
| Skills experimentales | no hay una skill movil activa detectada; `ciudadanoinusual-mobile-intake` requiere decision explicita antes de restaurar o formalizar | bajo-medio | permitidas como incubadora con auditoria posterior |
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
| `ciudadanoinusual-mobile-intake` | ausente del runtime el 2026-08-21 | no disponible en `HERMES_HOME` | flujo historico de Captura Movil V1 y Modo Calle | decidir si se recupera de forma controlada o se sustituye por skills oficiales |

## Track B: CiudadanoInusual y feedback real

### Operativo ahora

- Comandos `guion`, `post`, `carrusel` (ver `projects/hermes_ia/content/ciudadanoinusual/COMANDOS.md`; sustituyen a los antiguos `Modo guion`/`Modo post`/`Modo carrusel`/`Modo calle`).
- Nivel 0 sin comando (mandar foto o nota y que Hermes decida) para uso en calle.
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

Este track ya puede usarse en modo controlado porque Mobile Ops V1 basico quedo cerrado.

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

### Estado activado

- activo en modo controlado;
- usa Telegram como entrada principal;
- no requiere skill nueva oficial todavia;
- se apoya en captura privada y recuperacion breve.

## Track D: Financial Ops — Empleo Ops V0

### Futuro planificado, no operativo

- El contrato minimo y su prueba documental sintetica estan diseñados en `projects/hermes_ia/EMPLEO-OPS-V0.md`.
- CareerOps, JobSync y cualquier herramienta externa permanecen en `NO-GO`.
- Los datos profesionales reales no se habilitan automáticamente: F-01 queda como mitigación parcial aceptada y F-10 mantiene alcance parcial; F-03 ya esta cerrado.
- F-01 Fase A: `PARTIAL ACEPTADA`; tres rutas concretas devuelven `user-deny`. La protección global del proceso host, sockets directos y dominios permitidos queda fuera de alcance; el cierre completo requeriría Docker, descartado por ahora.
- F-03: `CERRADO`; backup cifrado externo, checksum y restauracion aislada verificados el 2026-08-21.
- Este experimento pertenece a Financial Ops y no desplaza la prioridad vigente de Hermes Creador.

## Track E: Automatizacion controlada

### Futuro planificado

- Cron one-shot: futuro experimento seguro con permiso explicito.
- Background sessions: experimento seguro si la tarea es pequena, no destructiva y queda registrada.

### Rojo por ahora

- Cron recurrente sin permiso fuerte.
- Automatizaciones que toquen servicios, `.env`, secretos, Docker, MCPs, Playwright o memoria externa.
- Publicacion automatica en redes.

## Tareas actuales

1. Probar cinco entradas reales de Hermes Creador mediante lenguaje natural y sin obligar a recordar comandos.
2. Publicar manualmente al menos una pieza y registrar resultado a 24 horas y 7 dias.
3. Probar dos usos reales mas de `Personal Ops V1` y registrar si reduce friccion de portatil.

## Regla de cierre operativo

Un item no se considera cerrado por estar escrito en un markdown.

Se cierra solo cuando existen las cuatro piezas:

1. prueba real o decision ejecutada;
2. resultado observable;
3. registro corto en el archivo correcto;
4. conclusion operativa reutilizable.

Aplicacion practica:

- si falta prueba, sigue abierto;
- si falta evidencia o registro, sigue abierto;
- si ya hay evidencia suficiente, se cierra y sale de `TAREAS.md`;
- si no toca en esta fase, pasa a descartado por ahora, no a cerrado.

## Condiciones de cierre de Mobile Ops V1

Mobile Ops V1 queda cerrado solo cuando:

- Telegram permite capturar una idea desde movil.
- La captura queda guardada fuera de Git.
- Se puede recuperar despues desde portatil o VPS.
- Se convierte una captura en una pieza util.
- Se aplica Judge y se registra decision.
- Se publica o se deja lista una pieza con privacidad revisada.

Estado a 2026-06-21:

- todas las condiciones anteriores ya quedaron cumplidas en uso real;
- Mobile Ops V1 se considera cerrado;
- la skill historica supero `3/3`, pero actualmente esta ausente del runtime y no se formaliza ni restaura sin una necesidad demostrada.
- `/background` pequeno queda aceptado como experimento seguro para tareas no destructivas y registrables.

Estado historico a 2026-06-22, sustituido para runtime por la comprobacion del 2026-08-21:

- la recuperacion humana ya no depende solo de leer ids largos;
- Telegram ya muestra botones de copia para `ultimas 5 capturas` en el runtime real de Hermes;
- la mejora se documento como operativa-remota en `HERMES_HOME`; actualmente no hay skill detectable ni se puede asumir disponible.

## Decision de arquitectura ya tomada

Sobre `ciudadanoinusual-mobile-intake`:

- su funcion de puente fue una decision historica, pero esta ausente del runtime actual;
- no se restaura ni gana alcance nuevo sin aprobacion;
- no se versiona como skill oficial monolitica;
- la siguiente decision separada es instalar y probar una skill oficial minima o mantener el flujo en scripts y prompts manuales.

## Regla de decision

Si una idea nueva no mejora ejecucion real, captura movil, publicacion, verificacion o aprendizaje medible, vuelve al backlog.
