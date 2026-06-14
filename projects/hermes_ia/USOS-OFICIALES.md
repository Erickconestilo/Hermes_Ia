# USOS OFICIALES

## Objetivo

Definir los 3 usos iniciales y oficiales de `Hermes` dentro de `Hermes_Ia` para salir de la fase de pura instalación y entrar en una fase de utilidad real.

## Regla de esta etapa

Estos usos quedan definidos a nivel operativo y documental.

Eso significa:

- sí se pueden diseñar
- sí se pueden probar con tareas pequeñas
- no se convierten todavía en perfiles reales
- no activan cron, Kanban, Docker ni memoria externa

## 1. Hermes Research

### Objetivo

Usar Hermes para investigar, filtrar y resumir información útil sobre:

- IA y tecnología
- herramientas y aprendizaje
- oportunidades en España
- FP, vivienda y crédito
- topografía y temas cercanos al trabajo del usuario

### Entradas

- preguntas concretas
- temas de interés
- artículos, vídeos, enlaces o notas
- dudas comparativas

### Salidas

- resúmenes claros
- listas de opciones
- análisis con riesgos y tradeoffs
- siguientes pasos de aprendizaje o decisión

### Límites

- no dar consejo legal, médico o financiero como si fuera profesional cerrado
- no decidir inversiones o compras sin análisis y fuentes
- no tratar rumores o vídeos como verdad final

### Primer caso de uso seguro

Preparar un briefing corto sobre una sola tendencia útil de IA o una sola oportunidad práctica en España, con fuentes y una conclusión accionable.

## 2. Hermes Content

### Objetivo

Usar Hermes para transformar ideas, observaciones y research en contenido útil para `CiudadanoInusual`.

### Entradas

- ideas sueltas
- temas investigados
- notas personales
- ángulos de contenido
- borradores de títulos o hooks

### Salidas

- hooks
- esquemas
- guiones cortos
- posts
- estructuras de ebook o piezas más largas

### Límites

- no producir contenido vacío solo para “publicar por publicar”
- no inventar experiencia propia que no exista
- no copiar formatos externos sin adaptación real

### Primer caso de uso seguro

Convertir una idea o reflexión ya existente en 3 hooks, 1 esquema de post y 1 cierre útil para `CiudadanoInusual`.

## 3. Hermes Builder

### Objetivo

Usar Hermes como apoyo técnico y operativo para:

- `Hermes_Ia`
- documentación
- scripts pequeños
- revisión de flujo de trabajo
- apoyo en código cuando toque

### Entradas

- archivos del repo
- tareas concretas
- errores o dudas de flujo
- ideas de automatización futura

### Salidas

- cambios documentales útiles
- propuestas de mejora pequeñas
- scripts simples
- aclaraciones técnicas
- planes cortos y ejecutables

### Límites

- no tocar todavía `TopoField`
- no tocar todavía `TopoTask`
- no cambiar configuración sensible sin revisión
- no instalar Docker ni cambiar `terminal.backend`

### Primer caso de uso seguro

Mejorar un archivo operativo del propio repo o crear una pieza documental con retorno real inmediato, verificable con `git diff`.

## Orden de despliegue recomendado

1. `Hermes Research`
2. `Hermes Content`
3. `Hermes Builder`

## Criterio de validación

Cada uso oficial se considera validado cuando:

- ya tuvo al menos una sesión útil real
- produjo una salida reutilizable
- no obligó a tocar configuración
- dejó un resultado verificable en archivo o en decisión registrada

## Qué no se activa todavía

- perfiles reales
- subagentes
- cron
- Kanban
- Docker backend
- memoria externa
