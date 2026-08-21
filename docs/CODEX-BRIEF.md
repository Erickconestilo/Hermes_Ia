# CODEX BRIEF

## Objetivo
Foto comprimida y operativa de `Hermes_Ia` para futuras sesiones de Codex.

## Memoria rapida compartida

`learning/MEMORIA.md` es el indice corto (una linea, 40-150 caracteres) de cambios importantes, leible por Claude, Codex y Hermes por igual. Revisar ahi antes de asumir el estado del repo desde cero. Detalle completo siempre en `learning/bitacora.md`.

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
- Captura Movil V1: operativa; almacenamiento privado fuera de Git.
- Personal Ops V1: activo en modo controlado desde Telegram para decisiones, prioridades y notas privadas.
- Skills experimentales: permitidas en `HERMES_HOME` como incubadora de bajo riesgo.
- Fase 0 documental: cerrada.
- Fase 1: activa en modo controlado.
- `CiudadanoInusual`: sistema editorial activo.

## Norte estrategico
`Hermes_Ia` es el arnes personal de IA de Erick/CiudadanoInusual.

Debe ayudar a investigar con fuentes, convertir vida real en contenido, mejorar el sistema con scripts/docs utiles y capturar ideas desde movil.

Tambien cubre Personal Ops en modo controlado: decisiones, dudas recurrentes, ideas no publicables, resumen semanal manual y priorizacion de sesiones de portatil.

Inspiraciones: Benjamin Cordero, Fatz y Gentleman Programming. Regla: adaptar, no copiar stacks completos.

## Clasificacion obligatoria
Toda idea nueva cae en una categoria: operativo ahora, siguiente experimento seguro, futuro planificado o descartado por ahora. Si no cae claramente en una, no se ejecuta.

## Seguridad vigente

La fuente única de permisos, acciones rojas y confianza supervisada es `AGENTS.md`. Esta foto rápida no duplica el semáforo: antes de ejecutar, comprobar allí el nivel de riesgo.

Estado relevante: Telegram sigue como canal móvil autorizado; las capturas privadas, el envío de imágenes y las pruebas no destructivas siguen permitidos dentro de esos límites.

## Skills

- Experimental en `HERMES_HOME`: permitida con auditoria posterior.
- Oficial versionada en repo: solo tras repeticion real y aprobacion.
- `ciudadanoinusual-mobile-intake`: ausente del runtime y no detectable por Hermes el 2026-08-21; no depender de ella hasta una decision explicita.
- Indice: `projects/hermes_ia/SKILLS-EXPERIMENTALES.md`.

## Root vs Docker

- `root`: solo bootstrap, recuperacion o administracion puntual.
- `hermes`: operacion diaria.
- Docker: futuro sandbox para Builder fuerte, no cambio inmediato.

## Usos oficiales
Hermes Research investiga IA, tecnologia, FP, vivienda, topografia y oportunidades con fuentes, riesgos y conclusion accionable.

Hermes Content transforma ideas, fotos, vivencias y research en contenido para `CiudadanoInusual`. Comandos activos: `guion`, `post`, `carrusel`, `hoy`, `publicado`, `guarda`, y Nivel 0 sin comando (ver `projects/hermes_ia/content/ciudadanoinusual/COMANDOS.md`).

Hermes Builder mejora `Hermes_Ia` con docs, scripts y verificaciones. No toca `TopoField` ni `TopoTask` en esta fase.

## Inventario editorial

- Research: 6 briefings.
- Content base: 20 salidas.
- Guiones publicables: 6.
- Posts visuales: 6.
- Carruseles: 6.
- Publicaciones registradas: 1.

## Siguiente experimento seguro

Validar capacidades reales de Mobile Ops V1:

1. probar `/whoami` y `/status` desde Telegram;
2. probar envio de archivo, recepcion de imagen y nota de voz;
3. probar `/background` con tarea pequena no destructiva;
4. capturar idea desde Telegram y guardarla fuera de Git;
5. convertirla en nota, borrador o pieza solo si aporta;
6. aplicar `JUDGE.md` cuando haya salida concreta;
7. registrar aprendizaje.

## Futuro planificado

- Formalizar skills solo tras repeticion real.
- Perfiles/subagentes cuando haya usos estables.
- Cron one-shot solo con permiso explicito y prueba manual previa.
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
