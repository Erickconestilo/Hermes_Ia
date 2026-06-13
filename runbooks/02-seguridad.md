# 02 - Seguridad

## Objetivo

Resumir las reglas ejecutivas de seguridad del proyecto `Hermes_Ia` sin duplicar el detalle técnico ya documentado en otros runbooks.

## Principios vigentes

- no guardar secretos reales en archivos versionados
- no ejecutar cambios sensibles sin análisis previo
- no exponer servicios públicamente por defecto
- no operar Hermes como `root`
- mantener el sistema lo más simple posible en las fases iniciales

## Secretos y archivos sensibles

No deben entrar en Git:

- `.env`
- secretos reales
- claves SSH
- tokens
- backups sensibles
- logs con datos privados

## Postura actual de exposición

Actualmente no se expone:

- dashboard público
- API pública
- Telegram
- Discord
- WebUI pública

La postura por defecto sigue siendo privada y conservadora.

## Regla de cambios sensibles

Antes de cualquier cambio sensible futuro, debe evaluarse siempre:

- objetivo
- riesgo
- alternativa más segura
- rollback
- verificación

## Usuario operativo

La decisión vigente es operar Hermes con:

- usuario `hermes`

No con:

- `root`, salvo bootstrap, recuperación o administración puntual

## Rollback mínimo esperado

Si se propone un cambio sensible, debe quedar claro:

- qué archivo o servicio cambia
- cómo se vuelve al estado anterior
- cómo se comprueba que el rollback funcionó

## Referencia técnica relacionada

Para el detalle de la creación del usuario `hermes`, ownership y validación del entorno, ver:

- [02-usuario-hermes-seguridad.md](02-usuario-hermes-seguridad.md)
