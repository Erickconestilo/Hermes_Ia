# F-03 - Backup cifrado externo y restauracion verificable

## Estado

**CERRADO - verificado el 2026-08-21.**

La copia se creo en el VPS, se cifro con GPG usando AES-256 antes de salir del servidor, se transfirio al destino externo aprobado y se valido con checksum coincidente en origen y destino. La restauracion se hizo dentro del VPS en un directorio temporal aislado con permisos restrictivos y se elimino al terminar.

## Evidencia de ejecucion

- Backup completo de datos y configuracion creado sin modificar los datos de produccion.
- Cifrado GPG simetrico AES-256 realizado en el VPS.
- La contrasena se introdujo interactivamente en la sesion del usuario; no se guardo en Git, `.env`, argumentos, logs ni en el documento.
- Copia cifrada transferida fuera del VPS antes de restaurar.
- Checksum SHA-256 del archivo cifrado coincidente antes y despues de la transferencia.
- Restauracion verificada en directorio temporal aislado dentro del VPS.
- Recuentos restaurados: 1.427 mensajes, 41 sesiones y 11 capturas.
- El directorio temporal de restauracion fue eliminado al cerrar la prueba.

## Alcance restaurado

La prueba incluyo el estado privado necesario para comprobar mensajes, sesiones, capturas, configuracion y datos operativos. Los secretos permanecieron dentro del archivo cifrado y no se imprimieron ni se versionaron. La restauracion no arranco gateways, no envio mensajes y no conecto proveedores externos.

## Limitaciones que siguen vigentes

- Esta evidencia cierra la existencia y restauracion de una copia externa cifrada; no crea por si sola una politica automatica de retencion.
- No hay cron recurrente de backups.
- La clave de recuperacion debe conservarse fuera del VPS en un gestor de contraseñas y una copia offline separada.
- Cada nueva generacion debe repetir checksum y restauracion antes de reemplazar la anterior.

## Procedimiento resumido de repeticion

1. Confirmar destino externo, espacio, clave de recuperacion y alcance.
2. Crear la copia en el VPS sin imprimir datos privados.
3. Cifrar antes de transferir.
4. Transferir y comparar SHA-256.
5. Restaurar solo en un directorio temporal con permisos `700`.
6. Validar recuentos y estructura sin mostrar cuerpos de mensajes ni secretos.
7. Eliminar el directorio temporal exacto y registrar resultado en `learning/bitacora.md`.

## Referencias

- `runbooks/06-backup-restore.md` - procedimiento operativo de backup y restauracion.
- `learning/bitacora.md` - registro de la ejecucion del 2026-08-21.
- `learning/MEMORIA.md` - indice corto del cierre de F-03.
