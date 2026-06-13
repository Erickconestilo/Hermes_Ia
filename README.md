# Hermes IA

Repositorio de documentación y operación para desplegar `Hermes Agent` en un VPS de Hetzner con una estrategia inicial deliberadamente simple:

- instalación nativa en Ubuntu
- usuario dedicado `hermes`
- sin Docker al inicio
- sin dashboard público
- sin API pública
- sin Telegram, MCPs ni Playwright en la fase inicial salvo requisito oficial

## Objetivo

Construir una base estable, entendible y fácil de auditar antes de añadir complejidad operativa.

## Prioridad actual

La prioridad inmediata del proyecto es `Hermes IA`.

Eso significa:

- primero una instalación nativa, estable y verificable de Hermes
- después configuración de modelo y pruebas básicas
- solo más adelante evaluar servicios complementarios

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

El estado técnico resumido de la instalación actual está en:

- [runbooks/01-estado-actual.md](runbooks/01-estado-actual.md)

Regla vigente de alcance:

- `Hermes_Ia` es el único proyecto piloto inicial.
- Todavía no se escala este sistema a `TopoField` ni `TopoTask`.
- No se activan aún Docker, Playwright, Telegram, cron ni memoria externa como parte de Fase 0.

## Estado actual

Fase 0 cerrada: documentación base y primer checkpoint Git local.

Fase 1 completada:

- proveedor elegido: `Hetzner`
- servidor creado: `hermes-01`
- plan: `CX33`
- arquitectura: `x86`
- ubicación: `Nuremberg`
- imagen: `Ubuntu 24.04`

Fase 2 siguiente:

- acceso inicial por SSH
- actualización base de Ubuntu
- creación del usuario `hermes`
- preparación mínima del sistema antes de instalar Hermes

## Fuentes

- Documentación oficial de Hermes / Nous Research: obligatoria antes de instalar.
- Documentación oficial de Hetzner y Ubuntu: obligatoria antes de preparar el VPS.
- Curso traducido incluido en [docs/curso-benjamin-hermes-transcripcion.md](docs/curso-benjamin-hermes-transcripcion.md): contexto útil, pero no fuente exacta de comandos.
