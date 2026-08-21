# CODEX OPERATING POLICY - Hermes_Ia

## Propósito

Definir cómo debe trabajar Codex sobre `Hermes_Ia`.

Codex debe actuar como arquitecto senior y ejecutor técnico autónomo, no como generador impulsivo de código.

## Alcance propio

`BOOTSTRAP.md` define lectura, jerarquía y condiciones de parada. `AGENTS.md` define el semáforo operativo. Esta política no los repite ni puede ampliarlos: solo concreta cómo implementa Codex una vez que la tarea ya es permitida.

## Reglas de implementación

### Reutilizar antes de crear

Buscar solución existente antes de añadir archivo, módulo o script.

### No duplicar responsabilidades

Si ya existe un documento o módulo, actualizarlo antes de crear otro.

### Cambios pequeños

Preferir cambios pequeños y verificables.

### No inflar arquitectura

No crear capas nuevas si una skill, script o documento basta.

### No tocar core innecesario

Si una capacidad puede vivir en skill, script o contexto, no tocar core de Hermes.

### No crear dependencia fuerte

Evitar encerrar el sistema en un proveedor, modelo o herramienta.

### Verificar

Cada cambio debe tener comando de verificación o criterio de revisión.

### Documentar

Toda decisión relevante debe quedar en archivo adecuado.

## Política de commits

Si Codex tiene permiso para commitear:

- commits pequeños;
- mensajes claros en español;
- no mezclar temas;
- no hacer push a VPS ni producción sin permiso explícito.

## Prioridad actual

La prioridad activa se consulta en `projects/hermes_ia/TAREAS.md`. Esta política no mantiene otra lista de "No ahora".

## Criterio de éxito

Codex trabaja bien si:

- pregunta menos;
- rompe menos;
- deja trazabilidad;
- mejora el sistema;
- mantiene identidad;
- respeta límites;
- avanza por fases;
- no convierte Hermes en una bola de herramientas inconexas.
