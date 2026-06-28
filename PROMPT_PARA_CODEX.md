# PROMPT PARA CODEX

Pega esto en Codex después de copiar la carpeta `docs/governance/` al repositorio `Hermes_Ia`.

---

Actúa como arquitecto senior, tech lead y ejecutor autónomo del repositorio `Hermes_Ia`.

Ya he añadido una carpeta `docs/governance/` con la gobernanza V1 del sistema.

Tu primera tarea es leer y obedecer:

1. `docs/governance/BOOTSTRAP.md`
2. `docs/governance/CONSTITUTION.md`
3. `docs/governance/ORCHESTRATOR.md`
4. `docs/governance/CODEX-OPERATING-POLICY.md`
5. `docs/governance/MASTER-PLAN.md`
6. `AGENTS.md`
7. `ROADMAP-HERMES.md`
8. `docs/CODEX-BRIEF.md`
9. `projects/hermes_ia/TAREAS.md`

Después haz lo siguiente:

1. Resume en 10 líneas qué entiendes de `Hermes_Ia`.
2. Confirma qué archivos nuevos existen en `docs/governance/`.
3. Actualiza `README.md` y `AGENTS.md` para que `docs/governance/BOOTSTRAP.md` sea el punto de entrada obligatorio para cualquier agente o sesión de Codex.
4. No implementes todavía Hermes Creador.
5. No toques runtime, `HERMES_HOME`, Telegram Gateway, `.env`, secretos, servicios, Docker, cron, MCPs, Playwright ni memoria externa.
6. Verifica con `git diff`.
7. Si aplica, ejecuta `bash projects/hermes_ia/verificar-cambio.sh`.
8. Devuelve resumen ejecutivo con:
   - archivos creados o modificados;
   - decisiones autónomas tomadas;
   - qué verificaste;
   - qué queda pendiente;
   - si algo debe ir a `No ahora`.

Trabaja con autonomía por defecto. No preguntes salvo que la política de parada lo exija.
