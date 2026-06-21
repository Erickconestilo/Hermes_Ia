# AGENTS.md

## Propósito del repositorio

Este repositorio documenta y guía la evolución de `Hermes Agent` en un VPS de Hetzner con una estrategia de autonomía controlada: base nativa, seguridad suficiente y crecimiento por fases con pruebas pequeñas, aisladas y reversibles.

## Decisiones vigentes

- Instalar Hermes de forma nativa en Ubuntu.
- Usar un usuario dedicado `hermes`, no `root`, para operar Hermes.
- Guardar datos de Hermes en `/home/hermes/.hermes`.
- Usar `/home/hermes/workspace` como workspace principal.
- Tratar Hermes como agente operativo real, no como chatbot limitado.
- Usar `Research`, `Content` y `Builder` como usos oficiales iniciales.
- No exponer dashboard público.
- No exponer API pública.
- Telegram Gateway queda activado como experimento controlado de Fase 1 para acceso movil.
- No activar MCPs o Playwright en la fase inicial salvo exigencia oficial.
- No usar `--yolo`.
- No guardar secretos reales en archivos versionados.

## Reglas de trabajo

- Priorizar la verdad técnica sobre repetir el curso o confirmar sesgos.
- Tratar [docs/curso-benjamin-hermes-transcripcion.md](docs/curso-benjamin-hermes-transcripcion.md) como contexto conceptual, no como autoridad operativa.
- Verificar comandos sensibles con fuentes oficiales antes de proponerlos.
- Explicar siempre: objetivo, riesgo, alternativa, rollback y verificación.
- Advertir explícitamente antes de cambios que puedan afectar acceso SSH, firewall o usuario administrador.
- Si algo es riesgoso, no lo bloquees sin más: propón una prueba mínima, aislada y reversible.
- Si desde Telegram el usuario pide una imagen, no basta con describirla. Si Hermes genera, encuentra, recorta, edita u optimiza una imagen en el VPS, debe enviar el archivo final con `python3 scripts/send-telegram-photo.py <ruta-imagen> "<caption>"` y devolver tambien la ruta exacta.
- Si desde Telegram recibes una idea para `CiudadanoInusual`, usa Captura Movil V1 antes de convertirla en contenido: guarda la nota con `python3 scripts/captura-movil.py add`, devuelve el `id` y marca riesgos de privacidad.

## Autonomía operativa

- Verde: permitir con poca fricción lectura, búsqueda, `git status`, `git diff`, Markdown, scripts pequeños del repo y verificaciones simples.
- Amarillo: revisar antes de ejecutar scripts nuevos, `chmod +x`, cambios en varios archivos o automatizaciones internas pequeñas.
- Rojo: bloquear o pedir confirmación fuerte para `sudo`, paquetes, servicios, `.env`, secretos, Docker, cron, cambios de Telegram, MCPs, Playwright, `hermes doctor --fix` y cambios fuera de `Hermes_Ia`.

## Convenciones de documentación

- Usar placeholders, nunca secretos reales.
- Documentar por fases, distinguiendo entre operativo ahora, siguiente experimento seguro, futuro planificado y descartado por ahora.
- Registrar decisiones y dudas abiertas en los runbooks y en la bitácora.
- Mantener el camino de migración futura a `terminal.backend = docker` sin implementarlo todavía.
