# Retencion de datos privados

## Alcance actual

Esta politica cubre las capturas privadas de CiudadanoInusual almacenadas fuera de Git en `capturas.jsonl` y los trabajos privados de video de `CiudadanoInusual Shorts V1`. No borra ni modifica sesiones, logs, adjuntos ajenos al flujo, backups ni datos de otros sistemas.

## Regla de minimizacion

- No guardar secretos, documentos laborales reales ni datos sensibles en una captura.
- Marcar riesgos con `privacy_flags` antes de convertir una captura en contenido.
- No publicar ni exportar por defecto. Cualquier salida externa requiere una revision humana separada.

## Retencion por estado

| Estado | Plazo | Accion al vencer |
| --- | ---: | --- |
| `discarded` | 30 dias | candidato a borrado |
| `inbox` | 90 dias | candidato a borrado o revision manual |
| `reviewed` | 90 dias | candidato a borrado o revision manual |
| `converted` | 180 dias | candidato a borrado tras comprobar que el derivado util existe |

El vencimiento nunca borra datos por si solo. Primero se ejecuta una revision con `--dry-run`; el borrado solo puede ocurrir con `--apply` y una confirmacion explicita de la persona operadora.

## Procedimiento

1. Ejecutar la revision sobre una copia o sobre el almacen privado, sin `--apply`.
2. Revisar los identificadores candidatos, no los cuerpos de texto.
3. Confirmar que no se necesita recuperar ninguna captura ni conservarla por un motivo concreto.
4. Hacer backup cifrado actualizado antes de usar `--apply` sobre datos reales.
5. Ejecutar `--apply` solo con aprobacion explicita y registrar el resultado sin contenido privado.

## Limites y seguimiento

- El script no toca datos existentes en modo `--dry-run`.
- Backups: conservar segun la politica F-03; su purga se decide por separado.
- Sesiones, logs y adjuntos requieren una politica posterior basada en su formato y valor operativo. Esta politica no afirma cubrirlos.
- La primera aplicacion real requiere una sesion independiente y autorizacion para borrar datos.

## Trabajos de video

`scripts/video-social.py retention --dry-run` solo lista identificadores, estados y antiguedad. No tiene modo de borrado.

| Estado | Plazo para aparecer como candidato |
| --- | ---: |
| `discarded` o `failed` | 7 dias |
| `rendered` sin aprobar | 30 dias |
| `exported` | 90 dias |

El original, las previews y el export permanecen intactos aunque el trabajo aparezca como candidato. Cualquier limpieza posterior exige backup y aprobacion explicita.
