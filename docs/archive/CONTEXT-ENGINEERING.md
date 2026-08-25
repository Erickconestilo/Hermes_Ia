# CONTEXT ENGINEERING - Hermes_Ia

## Propósito

Definir cómo Hermes construye, reduce y entrega contexto a agentes y modelos.

El contexto es un recurso caro.
Más contexto no siempre significa mejor resultado.

## Regla principal

Cada agente recibe solo el contexto mínimo necesario para hacer bien su trabajo.

`BOOTSTRAP.md` decide qué debe leerse al iniciar una sesión; este documento solo decide qué contexto adicional entra en una tarea concreta.

## Capas de contexto

### Constitución

Siempre disponible.

Archivos:

- `docs/governance/CONSTITUTION.md`
- `docs/governance/BOOTSTRAP.md`

### Gobernanza

Disponible cuando se toman decisiones de sistema.

Archivos:

- `ORCHESTRATOR.md`
- `AGENT-SPEC.md`
- `CODEX-OPERATING-POLICY.md`
- `LOOP-ENGINEERING.md`
- `MEMORY-ENGINEERING.md`

### Proyecto

Disponible según tarea.

Archivos:

- `README.md`
- `AGENTS.md`
- `ROADMAP-HERMES.md`
- `docs/CODEX-BRIEF.md`
- `projects/hermes_ia/TAREAS.md`

### Dominio

Disponible según agente.

Ejemplos:

- Content lee archivos de `content/ciudadanoinusual/`;
- Research lee `research/`;
- Builder lee scripts y docs técnicos;
- Mobile Ops lee contratos de captura;
- Financial Ops lee su propia política y registros futuros.

### Tarea

Contexto específico de la acción actual.

Debe incluir:

- objetivo;
- archivos afectados;
- restricciones;
- criterio de terminado;
- comandos de prueba.

## Reglas de reducción de contexto

Antes de pasar contexto a un agente:

1. eliminar ruido;
2. resumir duplicados;
3. priorizar fuente canónica;
4. incluir solo lo necesario;
5. mantener citas internas o rutas cuando aplique.

## Reglas de recuperación

Si falta contexto:

1. buscar primero en archivos canónicos;
2. revisar roadmap y tareas;
3. revisar contratos específicos;
4. revisar bitácora solo si hace falta;
5. preguntar al usuario solo si no puede inferirse.

## Anti-patrones

Evitar:

- pasar todo el repo a todos los agentes;
- repetir contexto ya conocido;
- convertir cada sesión en una auditoría completa;
- depender del chat como única fuente de verdad;
- crear documentos nuevos para decisiones menores.

## Criterio de buen contexto

Un buen paquete de contexto permite que el agente:

- entienda la tarea;
- no rompa la visión;
- sepa qué no tocar;
- produzca salida útil;
- pueda verificar resultado.
