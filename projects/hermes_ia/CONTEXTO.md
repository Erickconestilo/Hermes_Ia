# CONTEXTO

## Propósito

`Hermes_Ia` es el proyecto piloto inicial para construir un sistema real de trabajo con IA usando `Hermes` como núcleo principal.

No es todavía un sistema multi-proyecto ni un laboratorio de todas las herramientas posibles.
Es la base desde la que se validará el método de trabajo.

## Estado actual

La infraestructura ya existe y Hermes ya funciona en el VPS.

Está validado:

- VPS en Hetzner
- instalación nativa
- usuario `hermes`
- backend `local`
- OpenRouter operativo
- modelo principal y fallback funcionando

Además:

- Fase 0 documental ya quedó cerrada en Git
- el proyecto ya tiene contexto base, estado actual y tareas mínimas
- Fase 1 ya comenzó en modo controlado

## Objetivo inmediato

Usar Hermes ahora como:

- asistente documental
- lector y organizador de Markdown
- recuperador de contexto del proyecto
- apoyo para pensar mejor los siguientes pasos
- ritual de arranque de sesión

## Límites actuales

En esta fase no se debe asumir todavía que Hermes será:

- sistema multiagente completo
- gestor de varios proyectos a la vez
- pipeline con cron
- interfaz pública
- sistema con memoria externa
- orquestador de herramientas complejas

## Alcance actual

El alcance actual se limita a:

- `Hermes_Ia`
- documentación
- organización del estado técnico
- preparación de una base sólida para fases posteriores

Quedan fuera por ahora:

- `TopoField`
- `TopoTask`

## Herramientas permitidas en esta fase

- Markdown
- Git
- documentación local
- Hermes como asistente de contexto y organización

## Qué no debe tocar todavía Hermes

Hermes no debe tomar todavía decisiones automáticas sobre:

- configuración sensible
- despliegues
- cron
- integraciones de mensajería
- cambios sobre otros proyectos
- nuevas herramientas no aprobadas

## Resultado esperado de esta fase

Al terminar esta fase, el proyecto debe tener:

- un ritual simple y repetible de arranque de sesión con Hermes
- capacidad de leer el contexto real del proyecto
- capacidad de proponer la siguiente tarea pequeña y útil
- uso práctico inicial validado sin tocar configuración
