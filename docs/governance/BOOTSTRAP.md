# BOOTSTRAP - Hermes_Ia

## Propósito

Este archivo es el punto de entrada obligatorio para cualquier agente, modelo, herramienta o sesión de trabajo que vaya a operar sobre `Hermes_Ia`.

Antes de modificar el repositorio, Codex, OpenCode, Hermes, un agente especializado o cualquier asistente debe leer este archivo y respetar el orden de lectura indicado.

`Hermes_Ia` no debe tratarse como un proyecto de código aislado. Es el arnés personal de IA de Erick/CiudadanoInusual.

## Orden obligatorio de lectura

Antes de actuar, leer en este orden:

1. `docs/governance/CONSTITUTION.md`
2. `docs/governance/ORCHESTRATOR.md`
3. `docs/governance/CODEX-OPERATING-POLICY.md`
4. `docs/governance/MASTER-PLAN.md`
5. `AGENTS.md`
6. `ROADMAP-HERMES.md`
7. `docs/CODEX-BRIEF.md`
8. `projects/hermes_ia/TAREAS.md`
9. Archivos específicos de la tarea actual.

Si hay conflicto entre documentos, prevalece este orden:

1. Constitución.
2. Política operativa de Codex.
3. Roadmap.
4. `AGENTS.md`.
5. Documentación específica.

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

Codex debe parar y pedir confirmación solo si va a:

- borrar funcionalidad existente;
- sustituir arquitectura base;
- tocar `.env`, secretos, SSH, firewall, usuarios, `sudo` o servicios;
- activar Docker, cron recurrente, MCPs, Playwright o memoria externa;
- publicar en redes;
- mover dinero o ejecutar decisiones financieras;
- tocar `TopoField` o `TopoTask`;
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
