# Scripts

Directorio reservado para automatizaciones pequeñas y auditables.

Reglas:

- no guardar secretos
- preferir scripts cortos y comentados
- documentar antes de automatizar pasos sensibles
- `retencion-datos.py` revisa candidatos de retencion en capturas privadas; usar `--dry-run` antes de cualquier `--apply`.
- `verificar-secretos.sh` analiza solo archivos en stage y, si detecta algo, informa tipo, archivo y linea sin imprimir valores sensibles.
