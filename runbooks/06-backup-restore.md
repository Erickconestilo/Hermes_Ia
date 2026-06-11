# 06 - Backup y restore

## Objetivo

Respaldar el estado mínimo de Hermes sin mezclar secretos en el repositorio.

## Alcance inicial

- `/home/hermes/.hermes`
- `/home/hermes/workspace`

## Reglas

- no guardar backups con secretos dentro del repositorio
- no versionar dumps con tokens o claves
- documentar nombre, fecha y origen del backup

## Restore

Pendiente de documentar cuando la instalación base exista y la estructura real haya sido validada.
