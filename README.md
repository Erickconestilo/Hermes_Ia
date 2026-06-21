# Hermes IA

Repositorio de documentación y operación para evolucionar `Hermes Agent` en un VPS de Hetzner como arnés personal de IA de Erick/CiudadanoInusual.

La estrategia vigente sigue siendo simple, pero ya no es Fase 0:

- instalación nativa en Ubuntu
- usuario dedicado `hermes`
- sin Docker al inicio
- sin dashboard público
- sin API pública
- Telegram Gateway operativo como canal movil controlado
- sin MCPs ni Playwright en la fase inicial salvo requisito oficial

## Objetivo

Construir un sistema de trabajo con IA estable, entendible y fácil de auditar antes de añadir complejidad operativa.

## Prioridad actual

La prioridad inmediata del proyecto es `Hermes IA`.

Eso significa:

- mantener la instalación nativa estable y verificable
- usar Hermes para Research, Content, Builder y Mobile Ops
- producir contenido y aprendizaje real para `CiudadanoInusual`
- evaluar servicios complementarios solo cuando haya caso de uso claro

## Capacidad futura de la infraestructura

Tomamos en cuenta que un VPS de Hetzner también puede servir más adelante como base para:

- frontend y backend ligeros o medianos
- `PostgreSQL` / `PostGIS`
- `Redis`
- `Docker`
- una PaaS self-hosted como `Coolify` o `Dokploy`
- `Uptime Kuma`
- `Dozzle`
- `n8n`
- `GitHub Actions Runner`
- backups, snapshots y cron jobs

Esto no implica instalar todo desde el principio.

Regla operativa:

- no desplegar varias capas complejas el mismo día
- priorizar primero `Hermes IA`
- añadir el resto por fases y con documentación

## Principios

- Simplicidad primero: un sistema simple que funciona antes que un sistema flexible pero frágil.
- Seguridad mínima sensata: sin exponer servicios innecesarios y sin guardar secretos en archivos versionados.
- Documentación antes de automatización: cada decisión importante debe quedar escrita.
- Evolución por fases: primero instalación nativa; Docker backend queda para una fase posterior.
- Verificación oficial: los comandos de instalación deben contrastarse con documentación oficial antes de ejecutarse.

## Estructura

- [AGENTS.md](AGENTS.md)
- [.env.example](.env.example)
- [runbooks/](runbooks/)
- [learning/bitacora.md](learning/bitacora.md)
- [scripts/](scripts/)
- `logs/`
- `secrets/`

## Roadmap y Proyecto Piloto

La hoja de ruta principal del proyecto está en:

- [ROADMAP-HERMES.md](ROADMAP-HERMES.md)

El proyecto piloto inicial para construir el sistema de trabajo con Hermes es:

- [projects/hermes_ia/CONTEXTO.md](projects/hermes_ia/CONTEXTO.md)
- [projects/hermes_ia/OPERATIVA-DIARIA.md](projects/hermes_ia/OPERATIVA-DIARIA.md)

El estado técnico resumido de la instalación actual está en:

- [runbooks/01-estado-actual.md](runbooks/01-estado-actual.md)

Regla vigente de alcance:

- `Hermes_Ia` es el único proyecto piloto inicial.
- Todavía no se escala este sistema a `TopoField` ni `TopoTask`.
- No se activan Docker, Playwright, cron, MCPs ni memoria externa.
- Telegram Gateway ya está operativo, pero cambios adicionales de Telegram siguen siendo sensibles.

## Estado actual

Fase 0 documental: cerrada.

Fase 1: iniciada en modo controlado.

Estado validado dentro de esta fase:

- proveedor elegido: `Hetzner`
- servidor creado: `hermes-01`
- plan: `CX33`
- arquitectura: `x86`
- ubicación: `Nuremberg`
- imagen: `Ubuntu 24.04`
- acceso SSH validado
- usuario `hermes` creado
- Hermes instalado y operativo
- proveedor principal `openai-codex` con `gpt-5.4`
- OpenRouter configurado como fallback
- sincronización local ↔ VPS por Git ya operativa
- Telegram Gateway operativo desde móvil
- primera publicación externa asistida por Hermes registrada

La siguiente prioridad no es abrir Fase 2: es cerrar Mobile Ops V1 con captura móvil, privacidad, Judge y publicación/seguimiento.

## Fuentes

- Documentación oficial de Hermes / Nous Research: obligatoria antes de instalar.
- Documentación oficial de Hetzner y Ubuntu: obligatoria antes de preparar el VPS.
- Curso traducido incluido en [docs/curso-benjamin-hermes-transcripcion.md](docs/curso-benjamin-hermes-transcripcion.md): contexto útil, pero no fuente exacta de comandos.
