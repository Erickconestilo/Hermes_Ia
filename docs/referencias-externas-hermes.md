# Referencias externas de Hermes

## Objetivo

Conservar materiales externos valiosos sobre Hermes sin confundirlos con la fuente operativa principal de este proyecto.

## Regla base

En este repositorio, la documentación local y los runbooks propios prevalecen sobre tutoriales, cursos, vídeos o narrativas externas.

Las referencias externas se usan para:

- visión estratégica
- ideas de fases futuras
- contraste de enfoques
- inspiración de casos de uso

No se usan como:

- autoridad final de comandos
- checklist literal de instalación
- sustituto de verificación oficial

## Referencia 1: Benjamin Cordero

Archivo relacionado:

- [curso-benjamin-hermes-transcripcion.md](/C:/Users/guill/Documents/Hermes_Ia/docs/curso-benjamin-hermes-transcripcion.md)

### Qué aporta

- visión amplia de Hermes como plataforma de agentes
- marco conceptual sólido sobre memoria, skills, cron, subagentes y automatización 24/7
- mapa de crecimiento hacia contenido, marketing, CRM, briefs, backups y otros sistemas

### Riesgos si se sigue al pie de la letra

- mezcla demasiadas capas demasiado pronto
- combina instalación base con integraciones avanzadas
- puede empujar a construir más rápido de lo que conviene aprender
- tiene un tono comercial y evangelizador que no siempre coincide con una estrategia conservadora

### Cómo lo usamos aquí

- como norte de largo plazo
- como mapa de madurez futura
- como referencia para fases posteriores

### Qué no copiamos todavía

- Telegram
- WhatsApp
- MCPs
- Playwright
- cron jobs complejos
- despliegues automáticos extra
- dashboards expuestos
- automatizaciones de negocio de alta complejidad

## Referencia 2: Fatz

Estado actual:

- existe una narrativa revisada fuera del repo y sirve como referencia comparativa de uso práctico

### Qué aporta

- aterriza mejor la idea de Hermes en un VPS real
- muestra con claridad el patrón de agente persistente en servidor
- sirve para pensar Hermes como asistente práctico multiuso

### Riesgos si se sigue al pie de la letra

- comprime demasiadas decisiones en una sola sesión
- mezcla bootstrap, proveedor, dashboard, procesos persistentes y acceso remoto
- es más útil como demo guiada que como instalación mínima trazable

### Cómo lo usamos aquí

- como referencia práctica de operación
- como contraste frente a la estrategia conservadora del proyecto
- como fuente de ideas para fases posteriores

### Qué no copiamos todavía

- quick setup como ruta principal
- dashboard remoto
- PM2
- Tailscale
- goals agresivos
- demos complejas de app-building como criterio de éxito inicial

## Posición del proyecto

La estrategia vigente de este repositorio es:

- Hermes nativo
- usuario `hermes`
- Ubuntu LTS
- backend local al inicio
- sin Docker al inicio
- sin dashboard público
- sin API pública
- sin Telegram
- sin MCPs
- sin Playwright al inicio salvo necesidad real

## Síntesis

- Benjamin = visión y mapa futuro
- Fatz = práctica y operación de campo
- runbooks del repo = verdad operativa actual

## Criterio de adopción futura

Cuando una idea venga de Benjamin, Fatz u otra fuente externa, antes de adoptarla en este proyecto debe pasar por estas preguntas:

1. ¿Reduce complejidad o la aumenta?
2. ¿Aporta valor ahora o solo “suena potente”?
3. ¿Tiene rollback claro?
4. ¿Exige más superficie de fallo?
5. ¿Está alineada con la fase actual del proyecto?

Si la respuesta no es suficientemente clara, la idea se documenta como futura y no se implementa todavía.
