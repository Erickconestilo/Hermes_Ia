# AGENTS.md

## Propósito del repositorio

Este repositorio documenta y guía el despliegue de `Hermes Agent` en un VPS de Hetzner con una estrategia inicial nativa y conservadora.

## Decisiones vigentes

- Instalar Hermes de forma nativa en Ubuntu.
- Usar un usuario dedicado `hermes`, no `root`, para operar Hermes.
- Guardar datos de Hermes en `/home/hermes/.hermes`.
- Usar `/home/hermes/workspace` como workspace principal.
- No exponer dashboard público.
- No exponer API pública.
- No activar Telegram, MCPs o Playwright en la fase inicial salvo exigencia oficial.
- No usar `--yolo`.
- No guardar secretos reales en archivos versionados.

## Reglas de trabajo

- Priorizar la verdad técnica sobre repetir el curso o confirmar sesgos.
- Tratar [docs/curso-benjamin-hermes-transcripcion.md](/C:/Users/guill/Documents/Hermes_Ia/docs/curso-benjamin-hermes-transcripcion.md) como contexto conceptual, no como autoridad operativa.
- Verificar comandos sensibles con fuentes oficiales antes de proponerlos.
- Explicar siempre: objetivo, riesgo, alternativa, rollback y verificación.
- Advertir explícitamente antes de cambios que puedan afectar acceso SSH, firewall o usuario administrador.

## Convenciones de documentación

- Usar placeholders, nunca secretos reales.
- Documentar por fases y con pasos pequeños.
- Registrar decisiones y dudas abiertas en los runbooks y en la bitácora.
- Mantener el camino de migración futura a `terminal.backend = docker` sin implementarlo todavía.
