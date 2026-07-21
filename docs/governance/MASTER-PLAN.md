# MASTER PLAN - Hermes_Ia

## Propósito

Este documento organiza la evolución de Hermes en fases.

No sustituye `ROADMAP-HERMES.md`.
Lo complementa desde la arquitectura de gobernanza.

## Norte

Hermes debe convertirse en un sistema operativo personal de IA gobernado por:

- Constitución;
- Orquestador;
- agentes especializados;
- contexto controlado;
- memoria curada;
- loops autónomos;
- evidencia real;
- control humano.

## Fase 0 - Gobernanza

Objetivo:

Crear la capa de gobierno antes de seguir implementando.

Archivos:

- `BOOTSTRAP.md`
- `CONSTITUTION.md`
- `ORCHESTRATOR.md`
- `AGENT-SPEC.md`
- `CONTEXT-ENGINEERING.md`
- `MEMORY-ENGINEERING.md`
- `LOOP-ENGINEERING.md`
- `CODEX-OPERATING-POLICY.md`
- `MODEL-SELECTION-POLICY.md`
- `EVOLUTION-POLICY.md`
- `MASTER-PLAN.md`

Criterio de terminado:

- documentos creados;
- README y AGENTS enlazan a BOOTSTRAP;
- Codex puede leerlos como fuente de verdad.

## Fase 1 - Hermes Creador mínimo

Estado (2026-07-21): en marcha, con avance real verificado, no cerrada.

Antes de esta fecha, la fase llevaba semanas marcada como "activa" sin evidencia de trabajo reciente (hallazgo 4.4 de `AUDITORIA-2026-07-21.md`). Lo que se resolvió hoy:

- rediseño de comandos completo, ver `projects/hermes_ia/content/ciudadanoinusual/COMANDOS.md` (Nivel 0 a Nivel 3);
- `AUDIENCIA.md` y `APRENDIZAJES.md` creados con patrones de voz y aprendizajes reales, no solo plan;
- `JUDGE-REGISTRO.md` calibrado con 24 evaluaciones reales y distribución 5-9 (antes daba 8/10 plano);
- se probó y se descartó el menú nativo de comandos de Telegram (`setMyCommands`) como solución a la fricción móvil — reemplaza en vez de fusionar el menú propio de Hermes Agent y se resetea en cada `hermes gateway restart` (detalle en `runbooks/10-telegram-comandos-nativos.md`); Nivel 0 (mandar contenido sin comando) quedó adoptado como la solución real.

Lo que sigue sin resolver, y por eso la fase no está cerrada:

- solo 1 de más de 20 piezas de contenido se ha publicado nunca; documentación adicional no resuelve esto, hace falta publicar de verdad;
- 12 de 18 piezas publicables siguen bloqueadas por edición visual/privacidad pendiente;
- `Hermes Creador mínimo` con Nivel 0 no se ha probado todavía en una situación real de calle.

Objetivo:

Reducir fricción para crear contenido.

Comandos humanos mínimos (plan original de esta fase; los nombres reales quedaron simplificados despues, ver `projects/hermes_ia/content/ciudadanoinusual/COMANDOS.md`):

- `¿Qué toca hoy?` -> hoy `hoy`
- `Vídeo` -> hoy `guion`
- `Historia` -> hoy `post` o Nivel 0
- `He publicado` -> hoy `publicado`

Debe hacer:

- decidir formato;
- pedir contexto mínimo;
- crear borrador;
- revisar privacidad;
- sugerir adaptación;
- registrar aprendizaje.

No debe:

- publicar automáticamente;
- pedir prompts largos;
- copiar tendencias;
- ignorar identidad.

Criterio de terminado (no cumplido aún):

- al menos una pieza publicada usando el flujo Nivel 0 completo, de idea a publicación;
- registro de esa publicación en `INDICE-PUBLICACIONES.md` con métricas reales.

## Fase 2 - Memoria creativa

Objetivo:

Aprender qué funciona para CiudadanoInusual.

Debe registrar:

- formato;
- tema;
- plataforma;
- resultado simple;
- sensación del usuario;
- aprendizaje.

Criterio de terminado:

- al menos 5 publicaciones registradas;
- aprendizajes útiles;
- recomendación de formatos repetibles.

## Fase 3 - Skills oficiales

Objetivo:

Formalizar la skill puente en piezas limpias.

Skills:

- `ciudadanoinusual-captura-privada`
- `ciudadanoinusual-conversion-ligera`

Criterio de terminado:

- ambas versionadas;
- probadas desde Telegram;
- skill puente archivada o congelada.

## Fase 4 - Financial Ops inicial

Objetivo:

Ayudar a ahorrar, detectar oportunidades y mejorar ingresos sin riesgos automáticos.

Primeras funciones:

- oportunidades de empleo;
- cupones;
- puntos;
- recompensas;
- gastos recurrentes;
- ideas de ingresos;
- research financiero prudente.

No debe:

- invertir;
- comprar;
- mover dinero;
- contratar;
- endeudar.

## Fase 5 - Hermes Programador

Objetivo:

Ayudar a Erick con FP, proyectos, GitHub y desarrollo web.

Agentes:

- Architect;
- Builder;
- QA;
- Research técnico;
- Documentation.

Criterio de terminado:

- mejora real en un proyecto;
- pruebas;
- documentación;
- aprendizaje reutilizable.

## Fase 6 - Autoevolución gobernada

Objetivo:

Mejorar skills, prompts, workflows y criterios usando evidencia.

Inspirado en:

- evolución de skills;
- pruebas;
- constraints;
- revisión humana.

No empezar aquí.

## No ahora

- Docker backend;
- cron recurrente;
- MCPs;
- Playwright;
- memoria externa;
- publicación automática;
- scraping agresivo;
- integraciones complejas con redes sociales;
- tocar otros proyectos;
- multiagentes persistentes sin pruebas.

## Criterio global de éxito

Hermes avanza si cada fase:

- reduce fricción;
- deja rastro;
- respeta privacidad;
- mejora decisiones;
- ayuda a crear, aprender o prosperar;
- no aumenta caos.
