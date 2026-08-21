# BOOTSTRAP - Hermes_Ia

## Propósito

Este archivo es el punto de entrada obligatorio para cualquier agente, modelo, herramienta o sesión de trabajo que vaya a operar sobre `Hermes_Ia`.

Antes de modificar el repositorio, Codex, OpenCode, Hermes, un agente especializado o cualquier asistente debe leer este archivo y respetar el orden de lectura indicado.

`Hermes_Ia` no debe tratarse como un proyecto de código aislado. Es el arnés personal de IA de Erick/CiudadanoInusual.

## Orden obligatorio de lectura

Núcleo minimo, siempre, para cualquier tarea por pequeña que sea:

1. `docs/governance/CONSTITUTION.md` — las leyes.
2. `AGENTS.md` — el semáforo verde/amarillo/rojo de autonomía.
3. `docs/CODEX-BRIEF.md` — foto comprimida del estado real actual.
4. `projects/hermes_ia/TAREAS.md` — qué toca hacer ahora.

Con estos cuatro ya se puede actuar en la mayoría de tareas locales, reversibles y documentales.

Lectura condicional, solo si la tarea la necesita:

- `docs/governance/ORCHESTRATOR.md` — si la tarea implica coordinar varios dominios o agentes especializados.
- `docs/governance/AGENT-SPEC.md` — si se crea, cambia o evalúa un contrato de agente.
- `docs/governance/CODEX-OPERATING-POLICY.md` — si se opera específicamente como Codex y hay dudas de implementación o commit.
- `docs/governance/MASTER-PLAN.md` y `ROADMAP-HERMES.md` — si la tarea toca la fase actual, el plan por fases o una decisión de roadmap.
- `CONTEXT-ENGINEERING.md`, `MEMORY-ENGINEERING.md`, `LOOP-ENGINEERING.md`, `MODEL-SELECTION-POLICY.md` o `EVOLUTION-POLICY.md` — solo si la tarea afecta directamente a esa responsabilidad.
- Archivos específicos de la tarea actual — siempre, al final, sea cual sea la tarea.

Esta reducción (2026-07-21) responde al propio Principio 4 de la Constitución: "si una función obliga al usuario a recordar demasiados pasos, la función está mal diseñada". El orden anterior exigía leer 9 documentos (~1.400 líneas) antes de tocar nada, incluso para un cambio trivial. `docs/CODEX-BRIEF.md` ya resume lo esencial de `MASTER-PLAN.md`, `ROADMAP-HERMES.md` y el estado operativo, por eso puede sustituirlos como lectura obligatoria por defecto.

Si hay conflicto entre documentos, prevalece este orden:

1. Constitución.
2. `AGENTS.md` para permisos, semáforo y límites operativos.
3. `CODEX-OPERATING-POLICY.md` para la forma de implementar y commitear con Codex.
4. `ROADMAP-HERMES.md` y `MASTER-PLAN.md` para estado y dirección por fases.
5. Documentación específica de la tarea.

La Constitución no puede contradecirse. `AGENTS.md` es la fuente única de límites operativos; ningún documento de ejecución puede ampliarlos. El roadmap describe estado, no autoriza acciones rojas.

## Regla principal

No ejecutar cambios por entusiasmo.

Cada cambio debe responder a una de estas preguntas:

- ¿Reduce carga mental?
- ¿Mejora capacidad de crear, aprender, decidir o prosperar?
- ¿Hace más claro, seguro o mantenible el sistema?
- ¿Ayuda a publicar, medir, aprender o evolucionar?
- ¿Respeta la identidad de CiudadanoInusual?

Si la respuesta es no, mover a backlog o `No ahora`.

## Modo de trabajo por defecto

Codex debe trabajar con autonomía por defecto.

Eso significa:

- leer antes de modificar;
- inferir decisiones menores;
- reutilizar antes de crear;
- documentar cada decisión relevante;
- avanzar por fases;
- verificar antes de dar por terminado;
- no detenerse por dudas pequeñas.

## Cuándo debe detenerse

Codex debe parar y pedir confirmación si la acción entra en la zona roja definida en `AGENTS.md` (sección "Autonomía operativa"). Esa lista vive solo allí.

Además de la zona roja operativa, deben pararse por separado las decisiones de producto o arquitectura — estas no viven en el semáforo de `AGENTS.md` porque no son acciones del día a día:

- borrar funcionalidad existente;
- sustituir arquitectura base;
- mover dinero o ejecutar decisiones financieras;
- cambiar la visión de Hermes;
- crear una dependencia fuerte con una herramienta o proveedor;
- no poder inferir una decisión de producto sin riesgo.

## Cuándo NO debe preguntar

No debe preguntar si la decisión es:

- local;
- reversible;
- documental;
- pequeña;
- alineada con la Constitución;
- verificable;
- sin secretos;
- sin cambios de sistema;
- sin impacto en producción.

En esos casos debe decidir, dejar rastro y continuar.

## Resultado esperado de una sesión útil

Una sesión útil termina con al menos uno de estos resultados:

- documento mejorado;
- script verificado;
- decisión registrada;
- deuda técnica reducida;
- flujo más simple;
- prueba ejecutada;
- siguiente paso claro.

## No olvidar

Hermes no es un chatbot.

Hermes es un sistema operativo personal de IA.

Los modelos son motores intercambiables.
La identidad, memoria, reglas y dirección viven en el repositorio y en la gobernanza.
