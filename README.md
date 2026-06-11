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

## Principios

- Simplicidad primero: un sistema simple que funciona antes que un sistema flexible pero frágil.
- Seguridad mínima sensata: sin exponer servicios innecesarios y sin guardar secretos en archivos versionados.
- Documentación antes de automatización: cada decisión importante debe quedar escrita.
- Evolución por fases: primero instalación nativa; Docker backend queda para una fase posterior.
- Verificación oficial: los comandos de instalación deben contrastarse con documentación oficial antes de ejecutarse.

## Estructura

- [AGENTS.md](/C:/Users/guill/Documents/Hermes_Ia/AGENTS.md)
- [.env.example](/C:/Users/guill/Documents/Hermes_Ia/.env.example)
- [runbooks/](/C:/Users/guill/Documents/Hermes_Ia/runbooks)
- [learning/bitacora.md](/C:/Users/guill/Documents/Hermes_Ia/learning/bitacora.md)
- [scripts/](/C:/Users/guill/Documents/Hermes_Ia/scripts)
- `logs/`
- `secrets/`

## Estado actual

Fase 0 en curso: documentación base del proyecto.

## Fuentes

- Documentación oficial de Hermes / Nous Research: obligatoria antes de instalar.
- Documentación oficial de Hetzner y Ubuntu: obligatoria antes de preparar el VPS.
- Curso traducido incluido en [docs/curso-benjamin-hermes-transcripcion.md](/C:/Users/guill/Documents/Hermes_Ia/docs/curso-benjamin-hermes-transcripcion.md): contexto útil, pero no fuente exacta de comandos.
