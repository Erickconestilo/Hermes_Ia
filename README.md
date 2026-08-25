# Hermes IA

Repositorio de documentacion y operacion para evolucionar `Hermes Agent` en un VPS de Hetzner como arnes personal de IA de Erick/CiudadanoInusual.

## Punto de entrada obligatorio

Antes de operar sobre este repositorio, cualquier agente, modelo, herramienta o sesion de Codex debe empezar por:

- [docs/governance/BOOTSTRAP.md](docs/governance/BOOTSTRAP.md)

Ese archivo define el orden de lectura, la jerarquia de decision, los limites de autonomia y las condiciones de parada.

La gobernanza completa vive en:

- [docs/governance/](docs/governance/)

## Estrategia vigente

La estrategia actual sigue siendo simple y controlada:

- instalacion nativa en Ubuntu
- usuario dedicado `hermes`
- sin Docker al inicio
- sin dashboard publico
- sin API publica
- Telegram Gateway operativo como canal movil controlado
- sin MCPs ni Playwright en la fase inicial salvo requisito oficial
- gobernanza V1 activa como capa de continuidad para agentes

## Objetivo

Construir un sistema de trabajo con IA estable, entendible y facil de auditar antes de anadir complejidad operativa.

## Prioridad actual

La prioridad inmediata del proyecto es `Hermes IA`.

Eso significa:

- mantener la instalacion nativa estable y verificable
- usar Hermes para Research, Content, Builder, Mobile Ops y Personal Ops
- producir contenido y aprendizaje real para `CiudadanoInusual`
- formalizar capacidades solo cuando hayan demostrado utilidad real
- evaluar servicios complementarios solo cuando haya caso de uso claro

## Capacidad futura de la infraestructura

Tomamos en cuenta que un VPS de Hetzner tambien puede servir mas adelante como base para:

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

- no desplegar varias capas complejas el mismo dia
- priorizar primero `Hermes IA`
- anadir el resto por fases y con documentacion

## Principios

- Simplicidad primero: un sistema simple que funciona antes que un sistema flexible pero fragil.
- Seguridad minima sensata: sin exponer servicios innecesarios y sin guardar secretos en archivos versionados.
- Documentacion antes de automatizacion: cada decision importante debe quedar escrita.
- Evolucion por fases: primero instalacion nativa; Docker backend queda para una fase posterior.
- Verificacion oficial: los comandos de instalacion deben contrastarse con documentacion oficial antes de ejecutarse.
- Gobernanza antes de expansion: nuevas capacidades deben respetar `docs/governance/BOOTSTRAP.md`.

## Estructura

- [docs/governance/BOOTSTRAP.md](docs/governance/BOOTSTRAP.md)
- [AGENTS.md](AGENTS.md)
- [.env.example](.env.example)
- [runbooks/](runbooks/)
- [learning/bitacora.md](learning/bitacora.md)
- [learning/MEMORIA.md](learning/MEMORIA.md): indice corto de cambios importantes, referencia rapida opcional (no es lectura obligatoria)
- [scripts/](scripts/)
- `logs/`
- `secrets/`

## Roadmap y proyecto piloto

La hoja de ruta principal del proyecto esta en:

- [ROADMAP-HERMES.md](ROADMAP-HERMES.md)

El proyecto piloto inicial para construir el sistema de trabajo con Hermes es:

- [projects/hermes_ia/CONTEXTO.md](projects/hermes_ia/CONTEXTO.md)
- [projects/hermes_ia/OPERATIVA-DIARIA.md](projects/hermes_ia/OPERATIVA-DIARIA.md)

El estado tecnico resumido de la instalacion actual esta en:

- [runbooks/01-estado-actual.md](runbooks/01-estado-actual.md)

Regla vigente de alcance:

- `Hermes_Ia` es el unico proyecto piloto inicial.
- Todavia no se escala este sistema a `TopoField` ni `TopoTask`.
- No se activan Docker, Playwright, cron recurrente, MCPs ni memoria externa.
- Telegram Gateway ya esta operativo, pero cambios adicionales de Telegram siguen siendo sensibles.

## Estado actual

Fase 0 documental: cerrada.

Fase 1: activa en modo controlado.

Estado validado dentro de esta fase:

- proveedor elegido: `Hetzner`
- servidor creado: `hermes-01`
- plan: `CX33`
- arquitectura: `x86`
- ubicacion: `Nuremberg`
- imagen: `Ubuntu 24.04`
- acceso SSH validado
- usuario `hermes` creado
- Hermes instalado y operativo
- proveedor principal `openai-codex` con `gpt-5.6-terra`, observado en el runtime el 2026-08-21
- OpenRouter configurado como fallback
- sincronizacion local, GitHub y VPS por Git ya operativa
- Telegram Gateway operativo desde movil
- Captura Movil V1 cerrada con evidencia real
- Personal Ops V1 activo en modo controlado
- primera publicacion externa asistida por Hermes registrada

La siguiente prioridad no es abrir integraciones pesadas. Es consolidar gobernanza, Hermes Creador y la formalizacion gradual de skills ya probadas.

## Verificacion local

La suite completa se ejecuta desde la raiz del repositorio con un unico comando:

```text
python -m unittest discover -s tests -t .
```

La linea base actual pasa con 51 pruebas. Se omiten 6 pruebas de `test_f01_approvals.py` porque requieren `HERMES_AGENT_SOURCE` apuntando a un checkout instalado de Hermes Agent, que no forma parte de este repositorio. En Windows pueden omitirse ademas 4 pruebas que necesitan crear enlaces simbolicos y el proceso no tiene ese privilegio; ambas omisiones son esperadas y quedan visibles en la salida de unittest.

## Fuentes

- Documentacion oficial de Hermes / Nous Research: obligatoria antes de instalar.
- Documentacion oficial de Hetzner y Ubuntu: obligatoria antes de preparar el VPS.
- Curso traducido incluido en [docs/curso-benjamin-hermes-transcripcion.md](docs/curso-benjamin-hermes-transcripcion.md): contexto util, pero no fuente exacta de comandos.
