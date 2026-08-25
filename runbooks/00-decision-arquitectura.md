# 00 - Decisión de arquitectura

## Decisión

Punto de partida:

- `Hermes Agent` nativo en Ubuntu VPS de Hetzner
- usuario dedicado `hermes`
- backend local al principio
- máxima simplicidad inicial

## Prioridad operativa

La prioridad del arranque es `Hermes IA`.

Orden de prioridades:

1. instalar Hermes de forma comprensible y estable
2. validar acceso, PATH, versión y `hermes doctor`
3. configurar proveedor de modelo
4. hacer primeras pruebas simples
5. solo después evaluar servicios complementarios

## Lo que esta decisión incluye

- Hermes no corre en Docker al inicio.
- Docker no se usa como backend de terminal al inicio.
- Dashboard no expuesto públicamente.
- API no expuesta públicamente.
- Telegram Gateway basico configurado como experimento controlado de Fase 1.
- MCPs no instalados todavía.
- Playwright no instalado todavía salvo requisito oficial.

## Lo que esta decisión no prohíbe a futuro

Una vez que `Hermes IA` esté estable, el VPS puede evolucionar para alojar además:

- frontend y backend de proyectos propios
- `PostgreSQL` / `PostGIS`
- `Redis`
- `Docker`
- `Coolify` o `Dokploy`
- `Uptime Kuma`
- `Dozzle`
- `n8n`
- `GitHub Actions Runner`
- snapshots, backups y cron jobs

Pero esa evolución se documentará por fases. No se instalará “todo de golpe”.

Docker solo se reconsidera cuando Hermes nativo funcione bien, exista un backup
restaurado de verdad, el troubleshooting básico esté resuelto y haya una razón
operativa concreta. Evaluarlo no autoriza instalarlo.

## Justificación

- Menos capas implica menos puntos de fallo iniciales.
- Facilita aprender Linux, usuarios, permisos y estructura real del sistema.
- Reduce bugs de volúmenes, redes, reverse proxy y contenedores.
- Hace más fácil depurar una instalación base antes de añadir automatización.
- Mantiene abierta una ruta de crecimiento para más proyectos sin comprometer el arranque.

## Estrategia de crecimiento

Si el VPS elegido es suficientemente capaz, la evolución recomendada sería:

1. `Hermes IA` nativo
2. reverse proxy y dominios/subdominios
3. frontend/backend de proyectos auxiliares
4. base de datos y caché si hacen falta
5. observabilidad y automatización

La arquitectura futura debe evitar duplicidades innecesarias:

- elegir `Coolify` o `Dokploy`, no ambos
- elegir `Nginx` o `Traefik` como capa principal, salvo caso muy justificado
- no activar `n8n`, runner CI, frontend y varias bases de datos el mismo día sin pruebas intermedias

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
