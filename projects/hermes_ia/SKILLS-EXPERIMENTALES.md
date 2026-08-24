# SKILLS EXPERIMENTALES

## Proposito

Registrar skills creadas por Hermes dentro de `HERMES_HOME` como incubadora de flujos repetibles de bajo riesgo.

La politica vigente es confianza supervisada: Hermes puede expandirse en bajo riesgo si deja rastro; debe pedir permiso en alto riesgo.

Una skill experimental no es todavia una skill oficial versionada en el repo.

## Politica

Permitido:

- crear o usar skills experimentales en `HERMES_HOME`;
- probar flujos repetibles de bajo riesgo;
- registrar que se creo, donde vive y para que sirve.

No permitido sin aprobacion:

- tocar secretos;
- modificar `.env`;
- cambiar servicios;
- activar cron recurrente;
- instalar paquetes;
- tocar Docker, MCPs, Playwright o memoria externa;
- publicar automaticamente en redes;
- hacer cambios destructivos;
- modificar el repo sin diff claro.

## Registro actual

| Nombre | Ubicacion | Estado | Proposito | Fecha detectada | Evidencia de uso | Riesgos | Permisos | Limites | Condicion para formalizar | Condicion para archivar |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ciudadanoinusual-mobile-intake` | ruta historica: `/home/hermes/.hermes/skills/note-taking/ciudadanoinusual-mobile-intake/` | ausente del runtime el 2026-08-21 | flujo historico de Captura Movil V1 y Modo Calle | 2026-06-21 | 3 capturas reales utiles; recuperacion privada; Judge aplicado; archivo e imagen recibidos por Telegram; foto + instruccion breve de guardado validada | documentacion puede prometer una capacidad no instalada | no aplica mientras este ausente | no restaurar ni ganar alcance sin aprobacion | decidir si se instala una skill oficial 1 y se prueba en real | archivar esta referencia si se sustituye el flujo o documentar reinstalacion verificada |
| `ciudadanoinusual-social-video` | `/home/hermes/.hermes/skills/media/ciudadanoinusual-social-video/` | experimental activa, Shorts V1 0.2.0 | analisis, A/B/C, revision y aprobacion asistida de videos para CiudadanoInusual desde Telegram | 2026-08-24 | skill habilitada en runtime; controlador desplegado; 12 pruebas VPS y flujo sintetico A/B/C aprobados | recortes sin justificacion, PII visual, carga de CPU y acumulacion de videos privados | analisis, derivados privados y entrega por Telegram | sin publicar, cron, Docker, MCP, servicios, paquetes ni envio del video completo a proveedores nuevos | completar 3 cortos y 1 video de 2-15 minutos con una ronda maxima de correccion | archivar si no reduce edicion manual o genera riesgo de privacidad |

## Criterio de formalizacion

Una skill experimental puede pasar a skill oficial versionada solo si:

- se usa varias veces con utilidad real;
- no genera errores graves;
- no aumenta riesgo operativo;
- queda claro que mejora ejecucion y no solo documentacion;
- Erick aprueba formalizarla en el repo.

## Estado actual de decision

La evidencia de uso es historica, no estado actual. La comprobacion real del 2026-08-21 encontro la ruta ausente, sin `SKILL.md`, y `hermes skills list` no devolvio la skill.

Decision vigente:

- no restaurar automaticamente la skill ausente;
- conservar los contratos de captura y conversion como diseno futuro;
- decidir en una sesion separada si se instala una skill oficial minima o si el flujo queda limitado a scripts y prompts manuales.
