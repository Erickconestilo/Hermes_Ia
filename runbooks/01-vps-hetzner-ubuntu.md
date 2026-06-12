# 01 - VPS Hetzner Ubuntu

## Objetivo

Preparar un VPS simple y estable sobre Ubuntu LTS, minimizando decisiones irreversibles al principio.

## Principios

- Elegir Ubuntu LTS, no una versión experimental.
- Evitar automatizaciones opacas en la fase inicial.
- Mantener un usuario administrador separado del usuario `hermes`.
- No tocar firewall o SSH sin plan claro de rollback.
- No usar una App preinstalada de Hermes si el objetivo es instalación nativa.

## Verificaciones que haremos antes de actuar

- Tipo exacto de servidor contratado
- versión de Ubuntu elegida
- IP pública del VPS
- método de acceso inicial entregado por Hetzner

## Pendiente de validación oficial

Completar comandos exactos después de revisar:

- documentación oficial de Hetzner Cloud
- documentación oficial de Ubuntu Server

## Notas oficiales ya validadas

- Hetzner permite crear un servidor desde `Servers > Add server`.
- Hetzner permite elegir `OS Images` o `Apps`; para este proyecto conviene `OS Images`.
- Hetzner indica que la clave SSH se selecciona al crear el servidor y que luego no puede añadirse desde la consola.
- Hetzner permite activar Backups diarios del disco del servidor.
- Ubuntu 26.04 LTS es la LTS más reciente a fecha `2026-06-11`, pero Ubuntu 24.04 LTS sigue en soporte estándar hasta junio de 2029.

## Recomendación inicial

Para minimizar sorpresas, empezar con:

- imagen Ubuntu 24.04 LTS
- servidor limpio, sin App de Hermes
- IPv4 pública activa
- clave SSH añadida en el alta si ya la tienes
- backups opcionales según presupuesto

La elección de Ubuntu 24.04 LTS es una inferencia de estabilidad, no un mandato de Hetzner ni de Hermes: 26.04 LTS es más nueva, pero también más joven.

## Decisión ejecutada

Configuración finalmente elegida:

- proveedor: `Hetzner Cloud`
- proyecto: `hermes-ia`
- tipo: `Cost-Optimized`
- plan: `CX33`
- arquitectura: `x86`
- ubicación: `Nuremberg`
- imagen: `Ubuntu 24.04`
- red pública: `IPv4 + IPv6`
- clave SSH del proyecto: dedicada a Hermes
- nombre del servidor: `hermes-01`

## Motivo de la decisión

Se eligió `CX33` porque equilibra:

- capacidad suficiente para `Hermes IA`
- margen razonable para proyectos auxiliares y laboratorio
- mejor calidad operativa percibida que opciones más baratas
- posibilidad de crecer después con DNS, snapshots, volúmenes, redes y otros servicios de Hetzner

## Cosas que deliberadamente no se activaron en el alta

- firewall inicial
- volúmenes extra
- cloud-config
- placement groups
- despliegue de servicios adicionales

## Siguiente paso

Fase 2:

- entrar por SSH con acceso inicial seguro
- actualizar el sistema
- crear el usuario `hermes`
- dejar la base lista antes de instalar Hermes
