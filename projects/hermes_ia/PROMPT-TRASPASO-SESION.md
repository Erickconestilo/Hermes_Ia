# Prompt de traspaso de sesión - Hermes_Ia

Pega esto al empezar una sesión nueva (Claude, Codex u otro asistente) sobre `Hermes_Ia` para continuar sin perder contexto.

Sustituye a cualquier prompt de traspaso anterior a esta fecha. Los estados que describía un traspaso viejo (Mobile Ops V1 sin cerrar, JUDGE-REGISTRO con 2 entradas, skill sin 3/3, Personal Ops V1 pendiente de decidir, comandos `Modo guion`/`Modo post`) ya no son ciertos: todo eso se cerró hace semanas o se rediseñó en esta sesión. Este documento se debe volver a generar cuando deje de ser fiel al estado real — no editarlo a mano poco a poco.

---

## Contexto operativo de Hermes_IA — última actualización 2026-07-21

Eres Claude en modo Cowork. Te doy el contexto completo para continuar sin perder nada.

### Quién soy

- Nombre: Erick
- Ubicación: Barcelona
- Perfil: topógrafo de auscultación (Metro L8, L9) + desarrollador independiente + creador de contenido
- Marca de contenido: CiudadanoInusual (TikTok, LinkedIn, Instagram)
- Preferencia de estilo: respuestas concisas y directas, sin relleno

### Qué es Hermes_IA

Sistema operativo personal de IA en evolución. No es un chatbot, es un agente autónomo supervisado que vive en un VPS Hetzner.

**Stack:**

- VPS Hetzner Ubuntu 24.04 (`hermes-01`, CX33 x86, Nuremberg), usuario operativo `hermes`
- Instalación nativa de Hermes Agent, backend `local`
- Proveedor principal: `openai-codex` / modelo `gpt-5.4`; fallback OpenRouter
- Sync por Git entre local, GitHub y VPS (remoto `vps` por SSH, remoto `origin` en GitHub, repo público)
- Telegram Gateway activo para uso móvil, con menú nativo `/` propio de Hermes Agent (no personalizado — ver sección de comandos)
- Acceso SSH local vía alias `ssh hermes` (definido en `~/.ssh/config`; si falla, forma larga con la clave `hermes_hetzner_ed25519`)

**Política de confianza:** confianza supervisada, semáforo verde/amarillo/rojo en `AGENTS.md`. Prohibido sin permiso explícito: tocar `.env`, secretos, SSH, firewall, usuarios, servicios, cron recurrente, Docker, MCPs, Playwright, memoria externa o publicación automática.

### Cómo arrancar una sesión (ya no son 9 archivos)

`docs/governance/BOOTSTRAP.md` se redujo a un núcleo de 4 lecturas obligatorias: `CONSTITUTION.md`, `AGENTS.md`, `docs/CODEX-BRIEF.md`, `projects/hermes_ia/TAREAS.md`. El resto (`ORCHESTRATOR.md`, `CODEX-OPERATING-POLICY.md`, `MASTER-PLAN.md`, `ROADMAP-HERMES.md`) es lectura condicional, solo si la tarea lo pide. Para arrancar Codex, usar `docs/governance/CODEX-KICKOFF.md` en vez de los prompts antiguos (`PROMPT_PARA_CODEX.md` y `CODEX-MASTER-PROMPT.md` ya no existen, quedaron consolidados ahí).

### Comandos vigentes de Hermes Creador

Ya no son `Modo guion`/`Modo post`/`Modo carrusel`/`Modo calle`/`¿Qué toca hoy?`/`He publicado`. Ver `projects/hermes_ia/content/ciudadanoinusual/COMANDOS.md`:

- **Nivel 0 (el caso normal):** mandar foto, nota de voz o texto suelto sin ninguna palabra clave. Hermes decide formato, revisa privacidad y da una versión usable. Esta es la solución real a la fricción de calle que se reportó y probó el 21-jul.
- **Nivel 1:** `guion`, `post`, `carrusel` — para forzar formato.
- **Nivel 2:** `hoy`, `publicado`.
- **Nivel 3:** `guarda` — nota privada.

Se intentó publicitar estos comandos en el menú nativo `/` de Telegram (`setMyCommands`) y se abandonó: ese menú es propiedad de Hermes Agent y se resetea solo en cada `gateway restart`/`update`, sobrescribiendo cualquier lista personalizada. Detalle completo en `runbooks/10-telegram-comandos-nativos.md`.

### Estado real auditado el 2026-07-21

**Cerrado con evidencia esta sesión:**

- Auditoría completa de proceso, documentación y seguridad (`AUDITORIA-2026-07-21.md`, no versionado en Git a propósito — es un entregable, no operativa del repo).
- Seguridad: IP del VPS sanitizada en `learning/bitacora.md`; `send-telegram-photo.py` ya no filtra el token en un traceback; `.gitattributes` añadido (fin del ruido de EOL Windows/Linux); runbooks de backup/restore y endurecimiento SSH escritos con comandos exactos, pendientes de ejecución real en el VPS.
- Capa de marca nueva: `AUDIENCIA.md` (audiencia primaria/secundaria/anti-audiencia, dos patrones de voz reproducibles: antítesis y anti-épica) y `APRENDIZAJES.md` (5 meta-aprendizajes del inventario, el principal: 12 de 18 piezas publicables están bloqueadas por trabajo visual, no editorial).
- `COMANDOS.md` reescrito y toda la terminología vieja unificada en 12 archivos del repo.
- `JUDGE-REGISTRO.md`: pasó de 5 evaluaciones (todas 8/10, sin discriminar nada) a 24, con distribución real de 5 a 9. Dos hallazgos: `guion-03` usa el nombre real de una compañera en el cuerpo del texto, no solo en notas — no publicable tal cual; `carrusel-03` se autodescalifica en su propio documento (usa una captura ajena de TikTok).
- Deuda documental reducida: `PROMPT_PARA_CODEX.md` + `CODEX-MASTER-PROMPT.md` → `CODEX-KICKOFF.md`. Cuatro documentos de captura móvil (798 líneas) → `CAPTURA.md` (209 líneas). `BOOTSTRAP.md` de 9 a 4 lecturas obligatorias.
- Principio 16 añadido a la Constitución: todo documento de proceso nuevo necesita una ejecución real registrada, o se archiva a los 14 días.

**Pendiente, requiere acción fuera de este chat (VPS o mundo real, no ejecutable desde una sesión de Cowork sin acceso SSH):**

- Endurecer SSH (`runbooks/02-seguridad.md`) y probar restauración de backup (`runbooks/06-backup-restore.md`) — ambos listos para copiar y pegar en el VPS.
- Publicar 2 piezas del inventario. Las 4 sin bloqueo de edición de imagen: `post-04-comida-en-ruta.md`, `guion-01-ir-al-trabajo-tambien-cansa.md`, `guion-02-viernes-faena-comida-en-ruta.md` (ojo: pide confirmar consentimiento de la compañera), `guion-06-faena-cerrada-partida-guardada.md`.
- Rellenar `publicaciones/INDICE-PUBLICACIONES.md` con datos reales de la única publicación existente (LinkedIn, 21-jun) — sigue diciendo "revisar impresiones" un mes después.
- El trabajo visual (tapar matrículas, recortar logos) que bloquea 12 de 18 piezas publicables — es edición de fotos, no documental.
- Probar `Hermes Creador` con el Nivel 0 en una situación real de calle (la prueba que motivó todo el trabajo de comandos de esta sesión).

### Riesgos que ya no aplican (para no repetirlos en la próxima auditoría)

- ~~95% de commits eran `docs:` sin evidencia de uso~~ → Principio 16 ahora lo vigila.
- ~~JUDGE sin discriminar~~ → resuelto, distribución real.
- ~~Documentos de instrucciones del agente duplicados~~ → consolidados.
- ~~Peaje de lectura de 9 archivos~~ → reducido a 4.

### Lo que sigue sin resolverse y probablemente reaparezca

- La tasa de conversión de publicable a publicado sigue siendo el problema real de fondo: mucho banco, poca publicación. Esto no lo arregla más documentación — lo arregla publicar.
- Nadie ha vuelto a evaluar si el Nivel 0 de `COMANDOS.md` de verdad reduce la fricción en la calle; es una hipótesis fundamentada, no un hecho probado todavía.

---

## Lo que necesito de ti en esta sesión

[Rellenar aquí el objetivo concreto de la sesión nueva. No repetir el diagnóstico de arriba — ya está hecho. Ir directo a la tarea.]
