# 07 - Fase futura Docker backend

## Estado

Fuera de alcance inicial.

## Motivo

Primero queremos una instalación nativa estable y entendible. Contenerizar demasiado pronto añade:

- capas de red
- volúmenes
- permisos adicionales
- rutas ambiguas
- fallos nuevos de arranque y persistencia

## Condición para reconsiderarlo

Solo evaluar `terminal.backend = docker` cuando:

- Hermes nativo funcione bien
- haya un backup probado
- haya troubleshooting básico resuelto
- exista una razón concreta para usar Docker
