# F-03 — Backup cifrado externo y restauración verificable

## Estado y alcance

**Estado de F-03 en esta fase: `DESIGNADO`; no `CLOSED`.** Este documento define una ejecución futura y sus pruebas de aceptación. Durante Fase A no se crea, cifra, transfiere, borra ni restaura ningún backup.

La evidencia actual sólo demuestra respaldos locales en el mismo VPS. El TAR del 2026-07-21 pasó `gzip -t` y el ZIP del 2026-08-08 pasó una prueba de integridad con la biblioteca estándar; ambos pertenecen a `hermes`, tienen modo `664` y residen en el mismo filesystem que Hermes. Hubo una restauración aislada histórica de archivos, pero no existe una copia externa cifrada ni una restauración completa, consistente y reproducible del conjunto actual. El TAR además fue creado con aviso de posible cambio durante la lectura, por lo que no se considera snapshot consistente.

## Objetivos de cierre

F-03 sólo podrá pasar a `CLOSED` cuando exista un backup actual y consistente, cifrado antes de abandonar el VPS, almacenado en un dominio de fallo independiente, con credenciales de mínimo privilegio, manifiesto y hashes, retención y borrado documentados, y una restauración completa ensayada en entorno aislado sin credenciales productivas ni tráfico externo.

## Inventario de datos

| Clase | ¿Respaldar? | Método consistente futuro | Sensibilidad | Retención inicial | Prioridad de restore | Exclusiones |
|---|---|---|---|---|---|---|
| Repositorio y documentación | Sí, junto con referencia Git | `git bundle` o copia de árbol tras congelar el commit | Media; puede contener contexto operativo | Indefinida mientras el repo sea fuente de verdad | Alta | `.git` alternativos, temporales y worktrees no usados |
| Configuración y secretos | Sí, cifrados | Copia de archivos seleccionados con permisos conservados; nunca imprimirlos | Muy alta | 3 generaciones cifradas; revisar legalidad y necesidad | Crítica | claves no usadas, caches de login caducadas y valores fuera del inventario |
| Estado y sesiones | Sí, con Hermes detenido o snapshot lógico soportado | Snapshot coordinado; para SQLite, checkpoint/backup consistente según herramienta | Muy alta | 7 diarios, 4 semanales, 3 mensuales | Alta | sesiones expiradas según política, dumps legibles sin cifrar |
| Capturas y datos privados | Sí, separados del repo | Copia estable de JSONL y adjuntos; validar JSON línea a línea | Muy alta | 7/4/3, sujeto a retención de privacidad | Alta | descartadas fuera de plazo y cuerpos no necesarios |
| Skills locales | Sí, sólo las habilitadas y referencias necesarias | Copia de árbol tras registrar versión/hash | Media | Igual que configuración | Media | caches, dependencias descargadas y skills no utilizadas |
| Workspace | Sí, filtrado | Snapshot consistente del árbol, excluyendo temporales | Alta; puede incluir PII y proyectos | 7/4/3 si contiene estado útil | Alta | `tmp/`, builds, node_modules, caches, secretos duplicados |
| Unidad/configuración del gateway | Sí, separada | Exportar unidad y drop-ins sin valores secretos; congelar hash | Alta | 4 generaciones | Crítica | logs de entorno, tokens y overrides obsoletos |
| Instalación Hermes Agent | No como copia primaria | Registrar versión, commit, `pyproject`/lock y procedimiento reproducible | Media | Manifiesto histórico | Media | venv completo, caches y artefactos binarios regenerables |
| Logs | Sólo ventana operativa mínima | Exportación filtrada y redactada, nunca el journal completo por defecto | Media-alta | 7–30 días según necesidad | Baja | tokens, cuerpos de mensajes, cabeceras y logs redundantes |
| Temporales y cachés | No | Ninguno; limpiar antes del snapshot | Variable | 0 | Ninguna | todo `tmp/`, caches de modelos, npm/pip/uv y archivos de prueba |

La fuente de verdad debe ser un manifiesto de inclusión/exclusión versionado sin valores secretos. El backup cifrado contiene datos privados; el repositorio Git sólo contiene el procedimiento y metadatos no sensibles.

## Arquitecturas candidatas

| Opción | Aislamiento | Complejidad/coste operativo | Recuperación | Riesgo | Dictamen |
|---|---|---|---|---|---|
| A. Repositorio restic cifrado en almacenamiento externo compatible | Alto si el proveedor y cuenta son independientes del VPS | Media; deduplicación, `check`, snapshots y política de retención | Buena; restore selectivo y completo | Custodia de contraseña y credenciales del backend | Principal |
| B. Copia cifrada a equipo local controlado | Alto frente al fallo del VPS, depende de la disponibilidad local | Media; operación manual y almacenamiento local | Buena si el equipo y disco están disponibles | Pérdida/robo del equipo o falta de disciplina | Alternativa |
| C. Borg cifrado en host externo por SSH | Alto si el host pertenece a otro dominio | Media-alta; requiere Borg compatible en origen/destino | Buena, con deduplicación y verificación | Dependencia de SSH, host y operación del receptor | Viable condicionada |

No se presupone proveedor ni precio. Restic documenta cifrado del repositorio, backends SFTP/S3 y verificación; Borg documenta cifrado autenticado, deduplicación y almacenamiento remoto por SSH. Estas propiedades no prueban que un proveedor concreto sea adecuado.

## Recomendación y decisiones del usuario

Recomiendo **A: restic con cifrado en cliente y destino externo independiente**, manteniendo una exportación manual cifrada adicional en el equipo local como defensa contra la pérdida del proveedor. La alternativa B es preferible si no se desea contratar almacenamiento todavía. No recomiendo usar snapshots del mismo proveedor como única copia externa.

| Decisión pendiente | Opciones a elegir | No asumir |
|---|---|---|
| Destino externo | almacenamiento compatible con restic, equipo local o host Borg independiente | proveedor, región o dominio de cuenta |
| Presupuesto | cero con operación manual local; presupuesto mensual para almacenamiento externo | precios o cuotas |
| RPO | 24 h recomendado para datos privados; 7 días sólo como mínimo experimental | que el backup actual cubra cambios recientes |
| RTO | 4 h recomendado para servicio básico; 24 h para restauración completa | que el VPS o proveedor estén disponibles |
| Retención | 7 diarios / 4 semanales / 3 mensuales como propuesta inicial | obligación legal universal |
| Custodia de clave | gestor de contraseñas y copia offline separada; dos custodios si procede | guardar la clave en `.env`, Git o junto al backup |

## Diseño de ejecución futura (Fase B)

### 1. Preflight

Registrar commit Hermes, versión, uso de disco, estado del gateway, árbol Git, propietario/permisos y espacio del destino. Confirmar que no existe un proceso de escritura incompatible. No continuar si falta la clave de recuperación, el destino no es independiente o el manifiesto incluye secretos fuera del alcance.

### 2. Copia consistente

Preferir un snapshot lógico coordinado y una ventana corta sin escrituras. Si la base de estado soporta backup online, usar su mecanismo oficial; si no, detener temporalmente el escritor autorizado durante la copia, con aprobación separada, y verificar después. No usar un `tar` vivo de `.hermes` como prueba de consistencia.

### 3. Cifrado antes de salir

Inicializar un repositorio cifrado en cliente. La clave nunca se pasa como argumento ni se guarda en el árbol, `.env`, unidad systemd, logs o destino externo. Las credenciales del backend deben ser de escritura limitada al repositorio, sin permisos de lectura de otros objetos ni administración de cuentas.

### 4. Transferencia y verificación

Subir sólo el repositorio cifrado. Generar manifiesto con rutas relativas, tamaño, modo, propietario abstracto, fecha, hash y versión; almacenar el manifiesto dentro del repositorio y una copia no sensible local. Ejecutar verificación de integridad del repositorio y comparar recuentos/hash sin revelar nombres privados.

### 5. Restauración aislada

Restaurar en un directorio temporal fuera de `<HERMES_HOME>` real, con propietario no productivo y permisos restrictivos. No restaurar `.env` activo ni credenciales productivas: sustituirlos por placeholders o archivos de prueba con permisos equivalentes. Validar que la base abre de forma coherente, que JSONL es válido línea a línea y que las rutas esperadas existen.

### 6. Validación funcional segura

Arrancar una instancia de prueba con configuración ficticia, sin Telegram, sin correo, sin herramientas externas y sin acceso a la red. Comprobar lectura de configuración, carga de skills necesarias, apertura del estado y ejecución de una operación inocua. No enviar mensajes, no ejecutar cron y no conectar proveedores.

### 7. Limpieza y rollback

Eliminar sólo el directorio temporal exacto después de capturar conteos y resultado. Conservar el backup anterior hasta completar dos restauraciones satisfactorias. Si falla la nueva copia, no reemplazar la generación anterior; si falla una restauración, aislar el snapshot y volver al último backup verificado. Cualquier borrado debe tener ruta canónica comprobada y no usar globs ambiguos.

## Comandos propuestos, no ejecutados

Los siguientes son una plantilla futura. Requieren aprobación específica, destino elegido y credenciales preparadas; no deben copiarse a producción sin adaptar placeholders. Los comandos que crearían, transferirían, borrarían, detendrían o manejarían secretos quedan deliberadamente sin ejecutar en Fase A.

```bash
# Preflight sin secretos
git -C <HERMES_WORKSPACE> rev-parse HEAD
df -P <HERMES_HOME> <BACKUP_TARGET>
systemctl --user show hermes-gateway.service -p ActiveState -p NRestarts

# Futuro restic: placeholders, no ejecutar todavía
restic -r <BACKUP_TARGET> init
restic -r <BACKUP_TARGET> backup <INVENTORY_ROOTS> --exclude-file <EXCLUDE_MANIFEST>
restic -r <BACKUP_TARGET> check
restic -r <BACKUP_TARGET> forget --keep-daily 7 --keep-weekly 4 --keep-monthly 3 --prune
restic -r <BACKUP_TARGET> restore <SNAPSHOT_ID> --target <ISOLATED_RESTORE_DIR>

# Validación aislada
sha256sum <ISOLATED_RESTORE_DIR>/manifest.txt
python3 <VALIDATE_RESTORED_STATE>
# Arranque del harness aislado definido para la prueba, nunca de la unidad productiva.
<ISOLATED_HARNESS_START> --config <ISOLATED_CONFIG> --no-network
```

La última línea es un marcador de diseño, no una instrucción operativa aprobada: el harness deberá definirse y revisarse antes de Fase B; nunca se debe heredar la unidad productiva automáticamente.

## Operación, observabilidad y recuperación

- Ejecutar manualmente al principio; cron recurrente queda fuera de Fase A y requiere decisión posterior.
- Registrar sólo éxito/fallo, snapshot abstracto, duración, bytes, recuentos y hash del manifiesto; no rutas privadas ni cuerpos.
- Alertar por ausencia de backup dentro del RPO, fallo de verificación, destino lleno, credencial revocada o restauración no probada.
- Probar una restauración completa trimestralmente y una restauración selectiva mensual mientras el sistema contenga datos privados.
- Rotar credenciales del backend sin rotar la clave de recuperación; rotar la clave sólo con dos copias verificadas.
- Mantener una generación anterior hasta que la nueva tenga `check` y restore satisfactorios.

## Riesgos y controles

| Riesgo | Control | Residual |
|---|---|---|
| Backup inconsistente por escrituras concurrentes | snapshot lógico/ventana coordinada y validación de base | medio |
| Robo del destino | cifrado cliente, mínimo privilegio y clave separada | medio |
| Pérdida de la clave | gestor + copia offline separada + prueba de recuperación | medio |
| Proveedor externo caído | copia local cifrada secundaria y restore probado | medio |
| Retención excesiva de PII | política 7/4/3, etiquetas de datos y borrado verificado | medio |
| Credencial con demasiado alcance | cuenta sólo para este repositorio, sin administración | bajo-medio |
| Restaurar secretos productivos por accidente | placeholders, entorno aislado y preflight que rechaza producción | bajo |
| Backup usado como sustituto de Git | manifiesto y autoridad de datos explícita | bajo |

## Criterios verificables de aceptación de F-03

1. Manifiesto de inclusión/exclusión revisado y sin datos reales en Git.
2. Backup actual y consistente posterior a la última migración relevante.
3. Cifrado autenticado comprobado antes de cualquier transferencia.
4. Destino en dominio de fallo independiente y credencial de mínimo privilegio.
5. Hashes/manifiesto y verificación de integridad reproducibles.
6. Retención y borrado documentados, con una generación anterior protegida.
7. Restauración completa y selectiva en entorno aislado, sin credenciales productivas.
8. Permisos, base de estado, configuración mínima y skills necesarias verificadas.
9. Arranque de prueba sin red, Telegram, correo ni acciones externas.
10. Evidencia resumida sin secretos ni PII y procedimiento de rollback probado.

Hasta cumplir los diez puntos, F-03 permanece `DESIGNADO` o `PARTIAL`; esta fase sólo entrega el diseño.

## Referencias

- `runbooks/06-backup-restore.md` — procedimiento histórico que aún requiere cifrado, destino externo y restore real.
- `AUDITORIA-INTEGRAL-2026-08-11.md` — evidencia original y límites de la auditoría.
- Documentación oficial consultada de restic y Borg para cifrado autenticado, verificación, retención y backends remotos.
