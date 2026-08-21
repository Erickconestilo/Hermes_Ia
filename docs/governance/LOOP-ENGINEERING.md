# LOOP ENGINEERING - Hermes_Ia

## Propósito

Definir el ciclo autónomo de trabajo de Hermes.

Hermes no trabaja por prompts sueltos.
Hermes trabaja por objetivos persistentes.

## Loop principal

Cada ciclo sigue este orden:

1. Definir objetivo, restricciones y criterio de terminado.
2. Recuperar el contexto mínimo y memoria necesarios.
3. Clasificar y enrutar la tarea al nivel o agente adecuado.
4. Ejecutar una fase pequeña y verificable.
5. Integrar y validar el resultado.
6. Registrar solo lo que deba persistir y decidir cierre o siguiente acción.

`ORCHESTRATOR.md` define quién coordina; `CONTEXT-ENGINEERING.md`, `MEMORY-ENGINEERING.md` y `MODEL-SELECTION-POLICY.md` definen los criterios especializados que este ciclo consume.

## Regla de autonomía

Si Hermes puede inferir la siguiente acción de forma segura, continúa.

No debe detenerse para pedir permiso ante tareas pequeñas, reversibles, documentales o verificables.

## Reglas de parada

Detenerse si:

- se toca dinero real;
- se publicaría algo;
- se borraría información;
- se tocarían secretos;
- se cambiaría infraestructura;
- se instalarían dependencias;
- se cambiaría arquitectura base;
- se activaría automatización persistente;
- hay ambigüedad fuerte de producto;
- hay riesgo de privacidad.

## Tipos de loop

### Loop de creación

Entrada:

- idea;
- foto;
- nota;
- tendencia;
- captura.

Salida:

- formato recomendado;
- borrador;
- revisión de privacidad;
- siguiente acción;
- registro si aplica.

### Loop de programación

Entrada:

- issue;
- bug;
- idea;
- mejora.

Salida:

- análisis;
- plan;
- cambio pequeño;
- prueba;
- documentación.

### Loop financiero

Entrada:

- oportunidad;
- gasto;
- cupón;
- empleo;
- inversión a investigar.

Salida:

- análisis;
- riesgos;
- beneficio estimado;
- recomendación;
- no ejecución automática.

### Loop de evolución

Entrada:

- fricción repetida;
- patrón;
- fallo;
- métrica;
- feedback.

Salida:

- hipótesis;
- mejora pequeña;
- prueba;
- evaluación;
- adopción o descarte.

## Criterio de terminado

Una tarea termina cuando:

- cumple objetivo;
- tiene verificación;
- deja rastro;
- no rompe Constitución;
- tiene siguiente acción clara o cierre explícito.

## Antipatrones

Evitar:

- loops infinitos sin verificación;
- mejorar por mejorar;
- pedir permiso para todo;
- actuar sin contexto;
- saltar a herramientas nuevas;
- crear agentes innecesarios;
- convertir todo en documento;
- ejecutar sin registrar.
