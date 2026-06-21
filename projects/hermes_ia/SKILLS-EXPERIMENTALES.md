# SKILLS EXPERIMENTALES

## Proposito

Registrar skills creadas por Hermes dentro de `HERMES_HOME` como incubadora de flujos repetibles de bajo riesgo.

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

| Nombre | Ubicacion | Estado | Proposito | Condicion para formalizar |
| --- | --- | --- | --- | --- |
| `ciudadanoinusual-mobile-intake` | `HERMES_HOME` (`/home/hermes/.hermes/skills/note-taking/ciudadanoinusual-mobile-intake/`) | experimental activa | Captura Movil V1 y Modo Calle desde Telegram | superar 3 capturas reales sin errores graves |

## Criterio de formalizacion

Una skill experimental puede pasar a skill oficial versionada solo si:

- se usa varias veces con utilidad real;
- no genera errores graves;
- no aumenta riesgo operativo;
- queda claro que mejora ejecucion y no solo documentacion;
- Erick aprueba formalizarla en el repo.
