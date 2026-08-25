# MEMORY ENGINEERING - Hermes_Ia

## Propósito

Definir qué debe recordar Hermes, dónde debe recordarlo y cuándo debe olvidar o consolidar.

La memoria no es acumular todo.
La memoria es conservar lo que mejora decisiones futuras.

Este documento define persistencia, selección de contexto, consolidación y olvido.

## Seleccion de contexto

Cada tarea recibe solo el contexto mínimo necesario. Antes de pasarlo a Hermes
se elimina ruido, se resumen duplicados, se prioriza la fuente canónica y se
mantienen rutas o citas internas cuando hagan falta.

Las capas son: Constitución y bootstrap; gobernanza si la tarea es de sistema;
proyecto según el objetivo; dominio según el trabajo; y tarea con objetivo,
archivos, restricciones, verificación y criterio de terminado.

Si falta contexto, buscar primero en fuentes canónicas, después en roadmap y
tareas, luego en contratos específicos y finalmente en la bitácora. No pasar
todo el repositorio a todos los agentes ni crear documentos nuevos para dudas
menores.

## Tipos de memoria

### Memoria constitucional

Contiene misión, principios y límites.

Ubicación:

- `docs/governance/CONSTITUTION.md`

Es estable y cambia poco.

### Memoria de proyecto

Contiene estado, roadmap, tareas y decisiones técnicas.

Ubicación:

- `ROADMAP-HERMES.md`
- `AGENTS.md`
- `docs/CODEX-BRIEF.md`
- `projects/hermes_ia/TAREAS.md`
- runbooks relevantes.

### Memoria compartida entre agentes

Indice corto de cambios importantes, comun a Claude, Codex y Hermes: una sola fuente rapida para no reconstruir contexto cada vez desde cero ni depender de que cada agente lea toda la bitacora.

Ubicacion:

- `learning/MEMORIA.md`

Regla: una linea por entrada, entre 40 y 150 caracteres (fecha + hecho concreto). No sustituye `learning/bitacora.md`, solo apunta a ella. No es lectura obligatoria de `BOOTSTRAP.md`, es referencia rapida opcional.

### Memoria operativa

Contiene lo que está activo ahora.

Ubicación:

- `projects/hermes_ia/TAREAS.md`
- archivos de trabajo actuales.

### Memoria privada

Contiene capturas, decisiones personales y notas privadas.

Ubicación fuera de Git:

```text
/home/hermes/.hermes/data/ciudadanoinusual/
```

No se versiona.

### Memoria creativa curada

Contiene aprendizajes de contenido que sí pueden guardarse.

Ubicación futura sugerida:

```text
projects/hermes_ia/content/ciudadanoinusual/MEMORIA-CREATIVA.md
```

Debe incluir solo información revisada, no datos privados crudos.

### Memoria financiera

Contiene oportunidades, aprendizajes, reglas y decisiones financieras revisadas.

Ubicación futura sugerida:

```text
projects/hermes_ia/financial_ops/
```

No debe contener credenciales bancarias, datos sensibles o movimientos automáticos.

## Qué merece recordarse

Algo merece entrar en memoria si:

- se repite;
- reduce fricción;
- mejora decisiones;
- evita errores futuros;
- representa identidad;
- tiene evidencia;
- afecta arquitectura;
- sirve para medir progreso.

## Qué no merece recordarse

No entra en memoria permanente:

- ocurrencias aisladas;
- datos privados crudos;
- emociones momentáneas sin decisión;
- métricas sin interpretación;
- ideas externas no evaluadas;
- prompts largos sin uso real.

## Proceso de consolidación

1. Captura.
2. Revisión.
3. Clasificación.
4. Depuración.
5. Registro en ubicación correcta.
6. Eliminación o archivo del ruido.

## Reglas de privacidad

Por defecto, tratar como privado:

- caras;
- nombres;
- ubicaciones;
- empresa;
- clientes;
- rutinas;
- documentos;
- facturas;
- dinero;
- conversaciones;
- capturas de pantalla;
- datos personales.

## Regla de olvido

Hermes debe poder olvidar o archivar.

Si una memoria:

- no se usa;
- crea ruido;
- confunde;
- quedó obsoleta;
- contradice documentos canónicos;

debe archivarse o actualizarse.

## Criterio de buena memoria

Una memoria es buena si ayuda a Hermes a decidir mejor con menos preguntas al usuario.
