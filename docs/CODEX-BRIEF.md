# CODEX BRIEF

## Objetivo

Dar a futuras sesiones de Codex una foto comprimida, fiable y operativa de `Hermes_Ia` para evitar reinicios lentos, resúmenes repetidos y decisiones ya cerradas.

## Estado actual real

- Proyecto activo: `C:\Users\guill\Documents\Hermes_Ia`
- VPS: `hermes-01`
- Proveedor: `Hetzner`
- Plan: `CX33 x86`
- Región: `Nuremberg`
- Sistema: `Ubuntu 24.04.4 LTS`
- Instalación de Hermes: nativa
- Usuario operativo: `hermes`
- Backend actual: `local`
- Auth principal: `openai-codex`
- Modelo ligero validado: `gpt-5.4-mini`
- Fallback temporal: `OpenRouter`
- Sync local ↔ VPS: por Git, ya operativa
- Fase 0 documental: cerrada
- Fase 1: iniciada en modo controlado

## Norte estratégico

`Hermes_Ia` ya no es solo una instalación protegida.
La dirección actual es evolucionarlo de forma gradual hacia un sistema operativo personal de IA adaptado a la vida, aprendizaje y proyectos del usuario.

Inspiraciones útiles:

- Benjamin Cordero: visión amplia y mapa de madurez
- Fatz: operación práctica en VPS
- Gentleman Programming: estructura, perfiles, skills y método

No se copian sus stacks literalmente.
Se adaptan solo las piezas que aporten valor real a este proyecto.

## Regla de clasificación obligatoria

Cada idea nueva debe quedar en una de estas categorías:

1. operativo ahora
2. siguiente experimento seguro
3. futuro planificado
4. descartado por ahora

Si no cae claramente en una de esas cuatro, no se ejecuta.

## Reglas de seguridad vigentes

- no guardar secretos reales en Git
- no operar Hermes como `root` salvo bootstrap o recuperación
- no cambiar SSH, firewall o usuarios sin análisis explícito
- no instalar ni activar componentes nuevos sin objetivo, riesgo, alternativa, rollback y verificación
- si algo es riesgoso, no bloquearlo sin más: proponer una prueba mínima, aislada y reversible

## Qué sí se permite diseñar ahora

- usos oficiales de Hermes
- estructura documental y operativa
- flujos de trabajo local ↔ Git ↔ VPS ↔ Hermes
- experimentos pequeños de Research, Content y Builder
- criterios para futuras skills
- criterios para futuros perfiles o subagentes
- pruebas documentales o de prompt que no toquen configuración

## Qué no se permite instalar o activar todavía

- Docker
- cambio de `terminal.backend`
- cron
- Kanban
- perfiles reales o subagentes reales
- Playwright
- Telegram o Discord
- MCPs nuevos
- memoria externa tipo Engram
- `hermes doctor --fix`
- cambios en `.env`
- cambios en `TopoField` o `TopoTask`

## Decisión provisional root vs Docker

- `root`: solo para bootstrap, recuperación o administración puntual
- `hermes`: usuario normal de operación diaria
- Docker: permitido solo como línea futura de sandbox para Builder/código
- Docker no se instala ni se evalúa como cambio inmediato de backend

## Usos oficiales iniciales a definir

### 1. Hermes Research

Ámbitos esperados:

- IA y tecnología
- oportunidades en España
- FP, vivienda, topografía
- herramientas y aprendizaje

Regla:

- usar fuentes y análisis, no solo opinión rápida

### 2. Hermes Content

Ámbitos esperados:

- ideas
- hooks
- guiones
- posts
- ebooks
- contenido para `CiudadanoInusual`

Regla:

- convertir observación y research en piezas reutilizables

### 3. Hermes Builder

Ámbitos esperados:

- `Hermes_Ia`
- `TopoField`
- `TopoTask`
- scripts
- documentación
- código

Regla:

- en esta fase solo diseñar y preparar el método
- no tocar todavía `TopoField` ni `TopoTask`

## Siguiente experimento seguro recomendado

Definir por escrito los 3 usos oficiales iniciales de Hermes:

- Research
- Content
- Builder

Resultado esperado:

- un archivo o sección concreta con objetivo, entradas, salidas, límites y primer caso de uso de cada uno

## Futuro planificado

- skills solo cuando un flujo se repita varias veces
- perfiles o subagentes cuando los usos oficiales ya sean claros
- Docker backend como sandbox futuro para Builder
- memoria externa solo si la memoria actual se queda corta con evidencia real

## Descartado por ahora

- instalar Docker ya
- activar cron ya
- activar Kanban ya
- abrir dashboard o API pública
- mover el backend a Docker
- expandir el sistema a `TopoField` o `TopoTask` en esta fase

## Regla operativa para Codex

Priorizar cambios que produzcan:

- un archivo útil nuevo
- una mejora real de un archivo existente
- una decisión concreta registrada
- una verificación reproducible

Evitar:

- resúmenes repetidos
- prompts interminables
- meta-documentación sin salida operativa
