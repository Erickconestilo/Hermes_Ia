# MODEL SELECTION POLICY - Hermes_Ia

## Propósito

Definir cómo Hermes debe elegir modelos y proveedores.

Hermes no debe depender de un único modelo.

Los modelos son motores intercambiables.

## Principio principal

Usar el modelo más barato que pueda resolver bien la tarea, y reservar modelos potentes para decisiones críticas.

## Herramientas consideradas

### ChatGPT / Codex

Útil para:

- arquitectura;
- razonamiento;
- planificación;
- auditorías;
- diseño de sistema;
- tareas críticas.

### OpenCode

Útil como agente de desarrollo o interfaz de programación asistida.

Puede actuar como ejecutor técnico bajo las reglas de Hermes.

### OpenRouter

Útil como capa de acceso a múltiples modelos.

Permite seleccionar modelos según coste, calidad y tarea.

## Política recomendada

No elegir entre OpenCode y OpenRouter como si fueran equivalentes.

OpenCode puede ser herramienta/agente.
OpenRouter puede ser proveedor/capa de modelos.

La combinación correcta puede ser:

```text
Hermes Orchestrator
  -> OpenCode / Codex como agente ejecutor
  -> OpenRouter como capa de modelos
  -> modelo elegido según coste/riesgo/tarea
```

## Niveles de tarea

### Bajo riesgo

Ejemplos:

- reformatear Markdown;
- resumir archivos;
- clasificar ideas;
- generar borradores simples;
- revisar estilo.

Modelo:

- barato;
- rápido;
- suficiente.

### Riesgo medio

Ejemplos:

- editar scripts;
- modificar flujo;
- crear skill;
- analizar contenido sensible;
- estructurar agentes.

Modelo:

- calidad media-alta.

### Riesgo alto

Ejemplos:

- arquitectura;
- decisiones de seguridad;
- cambios de sistema;
- diseño financiero;
- refactor importante;
- planificación multiagente.

Modelo:

- máximo razonamiento disponible.

## Regla financiera

No gastar más por costumbre.

Gastar más solo si:

- reduce riesgo;
- ahorra tiempo real;
- evita errores caros;
- mejora arquitectura;
- resuelve una decisión difícil.

## Registro

Si se cambia proveedor o modelo principal, registrar:

- motivo;
- coste estimado;
- ventajas;
- riesgos;
- rollback;
- fecha.

## Criterio de éxito

La selección de modelo funciona si Hermes mantiene calidad, reduce coste y no queda atado a un proveedor.
