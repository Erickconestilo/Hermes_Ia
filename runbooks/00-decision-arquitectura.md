# 00 - Decisión de arquitectura

## Decisión

Punto de partida:

- `Hermes Agent` nativo en Ubuntu VPS de Hetzner
- usuario dedicado `hermes`
- backend local al principio
- máxima simplicidad inicial

## Lo que esta decisión incluye

- Hermes no corre en Docker al inicio.
- Docker no se usa como backend de terminal al inicio.
- Dashboard no expuesto públicamente.
- API no expuesta públicamente.
- Telegram no configurado todavía.
- MCPs no instalados todavía.
- Playwright no instalado todavía salvo requisito oficial.

## Justificación

- Menos capas implica menos puntos de fallo iniciales.
- Facilita aprender Linux, usuarios, permisos y estructura real del sistema.
- Reduce bugs de volúmenes, redes, reverse proxy y contenedores.
- Hace más fácil depurar una instalación base antes de añadir automatización.

## Riesgos asumidos

- Menor aislamiento que una arquitectura contenedorizada.
- Menor portabilidad inmediata.
- Evolución futura a Docker requerirá una migración controlada.

## Criterio de éxito

- Instalación estable
- comandos comprensibles
- estructura de archivos clara
- verificación con `hermes --version` y `hermes doctor`

## Dudas abiertas

- Método oficial exacto de instalación en Ubuntu vigente.
- Dependencias obligatorias reales.
- Requisitos de modelo/proveedor y autenticación compatibles.
