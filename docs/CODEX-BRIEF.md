# CODEX BRIEF

## Objetivo
Foto comprimida y operativa de `Hermes_Ia` para futuras sesiones de Codex.

## Estado actual real

- Repo local: `C:\Users\guill\Documents\Hermes_Ia`
- VPS: `hermes-01`, Hetzner CX33 x86, Ubuntu 24.04.
- Instalacion Hermes: nativa.
- Usuario operativo: `hermes`.
- Backend actual: `local`.
- Auth principal: `openai-codex`.
- Modelo principal: `gpt-5.4`.
- Fallback: OpenRouter.
- Sync local, GitHub y VPS: Git operativo.
- Telegram Gateway: operativo desde movil mediante bot autorizado.
- Imagenes generadas: envio a Telegram con `scripts/send-telegram-photo.py`.
- Captura Movil V1: en construccion; almacenamiento privado fuera de Git.
- Skills experimentales: permitidas en `HERMES_HOME` como incubadora de bajo riesgo.
- Fase 0 documental: cerrada.
- Fase 1: activa en modo controlado.
- `CiudadanoInusual`: sistema editorial activo.

## Norte estrategico
`Hermes_Ia` es el arnes personal de IA de Erick/CiudadanoInusual.

Debe ayudar a investigar con fuentes, convertir vida real en contenido, mejorar el sistema con scripts/docs utiles y capturar ideas desde movil.

Inspiraciones: Benjamin Cordero, Fatz y Gentleman Programming. Regla: adaptar, no copiar stacks completos.

## Clasificacion obligatoria
Toda idea nueva cae en una categoria: operativo ahora, siguiente experimento seguro, futuro planificado o descartado por ahora. Si no cae claramente en una, no se ejecuta.

## Seguridad vigente

- No guardar secretos reales en Git.
- No operar Hermes como `root` salvo bootstrap o recuperacion.
- No cambiar SSH, firewall, usuarios ni `.env` sin confirmacion fuerte.
- No instalar componentes nuevos sin objetivo, riesgo, rollback y verificacion.
- Si algo es riesgoso, proponer prueba minima, aislada y reversible.
- No capar auto-mejora util: exigir trazabilidad y limites rojos.

## Permitido ahora

- Markdown, Git, scripts pequenos del repo y verificaciones locales.
- Research, Content y Builder dentro de `Hermes_Ia`.
- Telegram como canal movil autorizado.
- Captura privada de ideas con `scripts/captura-movil.py`.
- Envio de imagenes generadas al bot con `scripts/send-telegram-photo.py`.
- Skills experimentales en `HERMES_HOME` si son de bajo riesgo y dejan registro.
- Disenar criterios de perfiles o cron sin activarlos.

## No activar todavia

- Docker.
- Cambio de `terminal.backend`.
- Cron recurrente.
- Kanban.
- Perfiles reales o subagentes permanentes.
- Playwright.
- Discord.
- MCPs nuevos.
- Memoria externa tipo Engram.
- `hermes doctor --fix`.
- Cambios en `.env`.
- Cambios en `TopoField` o `TopoTask`.

## Skills

- Experimental en `HERMES_HOME`: permitida con auditoria posterior.
- Oficial versionada en repo: solo tras repeticion real y aprobacion.
- `ciudadanoinusual-mobile-intake`: experimental activa para Captura Movil V1 y Modo Calle.

## Root vs Docker

- `root`: solo bootstrap, recuperacion o administracion puntual.
- `hermes`: operacion diaria.
- Docker: futuro sandbox para Builder fuerte, no cambio inmediato.

## Usos oficiales
Hermes Research investiga IA, tecnologia, FP, vivienda, topografia y oportunidades con fuentes, riesgos y conclusion accionable.

Hermes Content transforma ideas, fotos, vivencias y research en contenido para `CiudadanoInusual`. Formatos activos: Modo guion, Modo post, Modo carrusel y Modo calle.

Hermes Builder mejora `Hermes_Ia` con docs, scripts y verificaciones. No toca `TopoField` ni `TopoTask` en esta fase.

## Inventario editorial

- Research: 6 briefings.
- Content base: 20 salidas.
- Guiones publicables: 6.
- Posts visuales: 6.
- Carruseles: 6.
- Publicaciones registradas: 1.

## Siguiente experimento seguro

Validar Mobile Ops V1:

1. capturar idea desde Telegram;
2. guardarla fuera de Git con `scripts/captura-movil.py`;
3. revisar privacidad;
4. convertirla en post, guion, carrusel o nota privada;
5. aplicar `JUDGE.md`;
6. publicar manualmente o dejar lista;
7. registrar aprendizaje.

## Futuro planificado

- Formalizar skills solo tras repeticion real.
- Perfiles/subagentes cuando haya usos estables.
- Cron solo con prueba manual previa y no recurrente.
- Docker backend como sandbox futuro.
- Memoria externa solo si la memoria actual falla con evidencia.

## Descartado por ahora

- Instalar Docker ya.
- Activar cron recurrente ya.
- Abrir dashboard o API publica.
- Mover backend a Docker.
- Expandir el sistema a otros proyectos.

## Regla para Codex

Priorizar cambios que produzcan archivo util, mejora real, decision registrada o verificacion reproducible.

Evitar resumen repetido, prompts interminables y meta-documentacion sin salida operativa.
