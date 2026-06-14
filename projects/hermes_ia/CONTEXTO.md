# CONTEXTO

## Objetivo real de Hermes_Ia

Hermes_Ia no es solo un repositorio de documentación ni una instalación de Hermes.

Es el arnés personal de IA de Erick/CiudadanoInusual: una capa operativa que combina Hermes, modelos, memoria, skills, herramientas, scripts, permisos, flujos de trabajo y futuros subagentes para convertir la IA en un sistema práctico de investigación, creación de contenido, construcción técnica y apoyo personal.

La meta no es tener más prompts.
La meta es tener un sistema que piense, recuerde, ejecute, verifique y mejore conmigo.

## Estado actual

La infraestructura ya existe y Hermes ya funciona en el VPS.

Está validado:

- VPS en Hetzner
- instalación nativa
- usuario `hermes`
- backend `local`
- `openai-codex` autenticado como proveedor principal
- `gpt-5.4-mini` funcionando para trabajo ligero
- OpenRouter mantenido como fallback
- sincronización local ↔ VPS por Git ya operativa

Además:

- Fase 0 documental ya quedó cerrada en Git
- el proyecto ya tiene contexto base, estado actual y tareas mínimas
- Fase 1 ya comenzó en modo controlado

## Objetivo inmediato

Usar Hermes ahora como:

- operador de arranque y priorización diaria
- lector y organizador de Markdown del proyecto
- recuperador de contexto real antes de cada sesión
- ayuda para elegir una sola tarea concreta y útil
- apoyo práctico sin tocar configuración

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
- documentación operativa ya consolidada
- operativa diaria local ↔ Git ↔ VPS ↔ Hermes
- organización del estado técnico vigente
- uso práctico básico de Hermes dentro del proyecto

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

- un flujo operativo claro entre local, Git, VPS y Hermes
- capacidad de leer el contexto real del proyecto sin caer en tareas ya hechas
- capacidad de proponer una sola tarea pequeña y útil
- uso práctico inicial validado sin tocar configuración ni instalar más componentes
- una referencia corta de trabajo diario en `projects/hermes_ia/OPERATIVA-DIARIA.md`
