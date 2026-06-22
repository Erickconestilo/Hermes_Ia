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
| `ciudadanoinusual-mobile-intake` | `/home/hermes/.hermes/skills/note-taking/ciudadanoinusual-mobile-intake/` | skill puente activa por un ciclo mas | Captura Movil V1, Modo Calle y flujo Telegram para CiudadanoInusual | 2026-06-21 | 3 capturas reales utiles; recuperacion privada; Judge aplicado; archivo e imagen recibidos por Telegram; foto + instruccion breve de guardado validada | conservar datos sensibles; cambiar flujo sin registro; seguir mezclando captura con redaccion si la intencion es ambigua; retrasar demasiado el versionado oficial | capturas privadas fuera de Git, recuperacion, borradores y registro posterior | no tocar Git, servicios, `.env`, secretos, cron recurrente ni sistema sin permiso; no ganar alcance nuevo | implementar la skill oficial 1 y mantener el flujo movil estable mientras actua como puente | archivar cuando la skill oficial 1 y la skill oficial 2 pasen prueba minima o si vuelve a meter plantillas en `original_text`, inventa, toca Git sin permiso, modifica sistema o empeora el flujo |

## Criterio de formalizacion

Una skill experimental puede pasar a skill oficial versionada solo si:

- se usa varias veces con utilidad real;
- no genera errores graves;
- no aumenta riesgo operativo;
- queda claro que mejora ejecucion y no solo documentacion;
- Erick aprueba formalizarla en el repo.

## Estado actual de decision

`ciudadanoinusual-mobile-intake` ya no esta solo en incubacion temprana.

Con `3/3` capturas reales utiles y uso real desde Telegram, pasa a candidata a formalizacion.

Todavia no debe considerarse oficial porque le falta una mejora minima:

- aceptar mejor texto libre;
- aceptar foto + contexto breve;
- aceptar nota de voz + intencion explicita de guardado;
- y, si la intencion no esta clara, preguntar una sola vez antes de desviarse a analisis o contenido.

Estado tras la ultima prueba real:

- foto + instruccion breve de guardado ya funciona;
- la skill prioriza captura sobre analisis visual cuando la intencion es clara;
- el siguiente umbral ya no es de uso basico, sino de decision de versionado oficial o permanencia en `HERMES_HOME`.

Decision aprobada:

- no oficializar una sola skill monolitica;
- preparar separacion futura en:
  - skill de captura/recuperacion privada;
  - skill de conversion ligera a contenido.
- mantener la skill actual un ciclo mas solo como puente operativo;
- no darle mas alcance nuevo;
- retirarla cuando las dos skills oficiales minimas ya esten probadas.
