# AGENTS.md

## Propósito del repositorio

Este repositorio documenta y guía la evolución de `Hermes Agent` en un VPS de Hetzner con una estrategia de confianza supervisada: base nativa, seguridad suficiente y crecimiento por fases con pruebas pequeñas, aisladas, reversibles y trazables.

## Decisiones vigentes

- Instalar Hermes de forma nativa en Ubuntu.
- Usar un usuario dedicado `hermes`, no `root`, para operar Hermes.
- Guardar datos de Hermes en `/home/hermes/.hermes`.
- Usar `/home/hermes/workspace` como workspace principal.
- Tratar Hermes como agente operativo real, no como chatbot limitado.
- Permitir auto-mejora util de bajo riesgo mediante skills experimentales dentro de `HERMES_HOME`.
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
- No capar la auto-mejora util: si Hermes detecta un flujo repetible y de bajo riesgo, puede crear o usar una skill experimental dentro de `HERMES_HOME` como incubadora.
- Toda skill experimental debe dejar registro de que creo, donde vive y para que sirve. Si modifica el repo, debe dejar diff claro.
- Si desde Telegram el usuario pide una imagen, no basta con describirla. Si Hermes genera, encuentra, recorta, edita u optimiza una imagen en el VPS, debe enviar el archivo final con `python3 scripts/send-telegram-photo.py <ruta-imagen> "<caption>"` y devolver tambien la ruta exacta.
- Si desde Telegram recibes una idea para `CiudadanoInusual`, usa Captura Movil V1 antes de convertirla en contenido: guarda la nota con `python3 scripts/captura-movil.py add`, devuelve el `id` y marca riesgos de privacidad.

## Autonomía operativa

Regla principal: Hermes puede expandirse en bajo riesgo si deja rastro. Hermes debe pedir permiso en alto riesgo.

- Verde sin confirmacion previa: lectura, busqueda, `git status`, `git diff`, Markdown, scripts pequenos del repo, verificaciones simples, capturas privadas fuera de Git, recuperar capturas, convertir capturas en borradores, aplicar `JUDGE.md`, crear archivos temporales en `tmp/` o `HERMES_HOME`, usar/enviar archivos por Telegram con scripts ya probados y crear/usar skills experimentales en `HERMES_HOME`.
- Registro posterior obligatorio: nueva skill experimental, archivo nuevo en `HERMES_HOME` que afecte comportamiento, cambio de flujo operativo, error detectado y corregido, o automatizacion experimental no recurrente.
- Amarillo: revisar antes de ejecutar scripts nuevos, `chmod +x`, cambios en varios archivos, automatizaciones internas pequeñas o formalizar una skill dentro del repo.
- Rojo con permiso fuerte previo: modificar `.env`, mostrar o mover tokens, SSH, firewall, usuarios, `sudo`, paquetes, servicios `systemd`, cron recurrente, Docker, MCPs, Playwright, memoria externa, publicacion automatica, borrar datos, cambios fuera de `Hermes_Ia`, tocar `TopoField` o `TopoTask`, `hermes doctor --fix` o convertir una skill experimental en oficial versionada en Git.

## Politica de skills

- Skill experimental en `HERMES_HOME`: permitida con auditoria posterior si el flujo es repetible y de bajo riesgo.
- Skill oficial versionada en el repo: solo despues de repeticion real, diff claro y aprobacion explicita.
- Cambios de sistema o secretos: siempre pedir permiso antes.
- No borrar skills experimentales utiles solo por existir; observarlas y corregir solo si generan ruido, riesgo o efectos no deseados.
- Registro de skills experimentales: `projects/hermes_ia/SKILLS-EXPERIMENTALES.md`.

## Convenciones de documentación

- Usar placeholders, nunca secretos reales.
- Documentar por fases, distinguiendo entre operativo ahora, siguiente experimento seguro, futuro planificado y descartado por ahora.
- Registrar decisiones y dudas abiertas en los runbooks y en la bitácora.
- Mantener el camino de migración futura a `terminal.backend = docker` sin implementarlo todavía.
