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

| Nombre | Ubicacion | Proposito | Estado | Fecha detectada | Riesgos | Evidencia de uso | Condicion para formalizar | Condicion para archivar |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ciudadanoinusual-mobile-intake` | `/home/hermes/.hermes/skills/note-taking/ciudadanoinusual-mobile-intake/` | Captura Movil V1, Modo Calle y flujo Telegram para CiudadanoInusual | experimental activa | 2026-06-21 | guardar plantillas como captura real; conservar datos sensibles; cambiar flujo sin registro | prueba real desde Telegram; placeholder accidental corregido; validacion anti-plantillas en `scripts/captura-movil.py` | superar 3 capturas reales utiles sin errores graves y sin tocar Git/servicios/secretos sin permiso | archivar si genera errores repetidos, riesgo de privacidad, ruido operativo o no aporta utilidad real |

## Criterio de formalizacion

Una skill experimental puede pasar a skill oficial versionada solo si:

- se usa varias veces con utilidad real;
- no genera errores graves;
- no aumenta riesgo operativo;
- queda claro que mejora ejecucion y no solo documentacion;
- Erick aprueba formalizarla en el repo.
