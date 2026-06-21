# GLOSARIO

## Objetivo

Reducir ambiguedades en la documentacion base de `Hermes_Ia`.

## Terminos

### Hermes_Ia

Proyecto piloto inicial donde se valida el sistema de trabajo con Hermes antes de escalarlo a otros proyectos.

### hermes

Usuario operativo del VPS y tambien nombre del agente CLI instalado de forma nativa en `/home/hermes`.

### Fase 1 controlada

Etapa actual del proyecto: Hermes ya funciona y Telegram Gateway esta operativo como canal movil controlado, pero no se activan todavia Docker, cron recurrente, MCPs ni memoria externa.

### openai-codex

Proveedor principal actual de Hermes autenticado con login de ChatGPT/Codex y usado para el trabajo normal del proyecto.

### OpenRouter fallback

Proveedor de respaldo que permanece configurado para Hermes solo si falla `openai-codex`; no es ya el proveedor principal.

### ritual de arranque

Rutina corta de inicio de sesion para leer contexto, confirmar el estado del proyecto y elegir una sola tarea pequena y util.
