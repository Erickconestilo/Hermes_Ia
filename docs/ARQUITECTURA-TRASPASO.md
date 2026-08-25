# Arquitectura de traspaso - Hermes_Ia

## Proposito del documento

Este documento prepara el traspaso de `Hermes_Ia` a otro arquitecto senior.

No es un resumen linea a linea del repositorio. Es una lectura arquitectonica del sistema: que intenta ser, que ya funciona, donde estan los limites, que piezas viven dentro del repo, que piezas viven fuera y que decisiones deberia respetar quien continue el proyecto.

La informacion se basa en la documentacion y scripts versionados del repo. Cuando algo depende del runtime real de Hermes en el VPS o de `HERMES_HOME`, se indica explicitamente.

## Vision general

`Hermes_Ia` es el arnes personal de IA de Erick/CiudadanoInusual.

No es una aplicacion tradicional con frontend, backend y base de datos versionada. Es una capa operativa apoyada en:

- Hermes Agent instalado de forma nativa en un VPS.
- Markdown como fuente de verdad documental.
- Git como mecanismo de sincronizacion local, GitHub y VPS.
- Telegram como interfaz movil.
- Scripts pequenos para tareas concretas.
- Skills experimentales en `HERMES_HOME` como incubadora.
- Un sistema editorial y operativo alrededor de `CiudadanoInusual`.

La vision correcta no es "chatbot con prompts". La vision es un sistema personal de trabajo con IA que combina investigacion, contenido, decisiones privadas, captura movil, revision de calidad y mejoras pequenas del propio sistema.

## Objetivo real

El objetivo de `Hermes_Ia` es ayudar a Erick a trabajar mejor con IA en cuatro frentes:

- Research: investigar temas con fuentes, tesis, riesgos y conclusion accionable.
- Content: convertir research, vida real, trabajo, estudio, fotos y notas en piezas para `CiudadanoInusual`.
- Builder: mejorar el propio sistema con documentacion, scripts y verificaciones utiles.
- Mobile Ops / Personal Ops: capturar y recuperar ideas, decisiones y notas privadas desde Telegram.

El proyecto tambien funciona como aprendizaje practico: Erick esta construyendo su propio entorno de trabajo con IA, no consumiendo una herramienta cerrada.

## Estado actual

Estado tecnico documentado:

- Repo local principal: workspace local del proyecto.
- VPS: `hermes-01`, Hetzner CX33 x86, Ubuntu 24.04.
- Usuario operativo: `hermes`.
- Hermes instalado de forma nativa en `/home/hermes/.hermes`.
- Workspace VPS: `/home/hermes/workspace/Hermes_Ia`.
- Backend actual: `local`.
- Proveedores y modelos por perfil: ver la fuente unica en [`docs/CODEX-BRIEF.md`](CODEX-BRIEF.md#estado-de-proveedores-y-modelos-fuente-unica).
- Telegram Gateway operativo como servicio de usuario `hermes-gateway.service`.
- `systemd linger` habilitado para mantener el gateway tras cerrar SSH.
- Sincronizacion por Git entre local, GitHub `origin` y VPS `vps`.

Estado de producto/operacion:

- Fase 0 documental cerrada.
- Fase 1 activa en modo controlado.
- Research base cerrado con 6 briefings.
- Banco inicial de Content 20/20 cerrado.
- Judge minimo definido y usado.
- Mobile Ops V1 cerrado con evidencia real.
- Personal Ops V1 activo en modo controlado.
- Primera publicacion externa asistida por Hermes registrada.
- La skill experimental `ciudadanoinusual-mobile-intake` aparece en el historial, pero una comprobacion real del 2026-08-21 la encontro ausente y no detectable; no es una capacidad operativa actual.

## Arquitectura general

La arquitectura actual es intencionalmente ligera.

```text
Usuario
  |
  |-- Portatil Windows / Codex / PowerShell
  |      |
  |      |-- repo Hermes_Ia versionado
  |      |-- edicion documental y commits
  |      |-- push a GitHub y VPS
  |
  |-- Movil / Telegram
         |
         |-- Hermes Gateway en VPS
                |
                |-- Hermes Agent runtime en /home/hermes/.hermes
                |-- skills experimentales en HERMES_HOME
                |-- scripts del repo en /home/hermes/workspace/Hermes_Ia/scripts
                |-- almacenamiento privado fuera de Git
```

El repo no contiene todo el comportamiento vivo. Contiene la politica, contratos, scripts y documentacion. Parte de la ejecucion real vive en:

- `/home/hermes/.hermes`
- `/home/hermes/.hermes/skills`
- `/home/hermes/.hermes/data`
- `/home/hermes/.hermes/cache`
- `/home/hermes/.hermes/image_cache`

Esta separacion es funcional, pero tambien es la principal deuda arquitectonica.

## Patrones usados

### Markdown como fuente de verdad

El proyecto usa Markdown para decisiones, runbooks, roadmap, contratos, operativa y contenido. Esto da baja friccion, trazabilidad y compatibilidad con Git.

Riesgo: demasiados Markdown pueden volverse una segunda forma de burocracia si no se conectan con pruebas reales.

### Confianza supervisada

La politica vigente no bloquea a Hermes por defecto. Permite expansion de bajo riesgo si deja rastro y exige permiso fuerte en acciones rojas.

Verde:

- lectura;
- Markdown;
- scripts pequenos;
- capturas privadas fuera de Git;
- recuperacion de capturas;
- borradores;
- `JUDGE.md`;
- skills experimentales dentro de `HERMES_HOME`.

Rojo:

- `.env`;
- secretos;
- SSH;
- firewall;
- servicios;
- cron recurrente;
- Docker;
- MCPs;
- Playwright;
- memoria externa;
- publicacion automatica;
- borrar datos;
- cambios en TopoField o TopoTask.

### Incubadora antes de versionado oficial

Las skills pueden nacer como experimentales en `HERMES_HOME`. Solo pasan al repo si se repiten con utilidad real, no generan errores graves y Erick aprueba formalizarlas.

Este patron es correcto para no capar a Hermes, pero exige trazabilidad fuerte.

### Cierre por evidencia

Un item no se considera cerrado por estar escrito. Debe tener:

1. prueba real o decision ejecutada;
2. resultado observable;
3. registro corto;
4. conclusion reutilizable.

Este es uno de los patrones mas sanos del sistema.

### Separacion futura de responsabilidades

La skill experimental `ciudadanoinusual-mobile-intake` se considera demasiado amplia. La decision arquitectonica tomada es separarla en:

- `ciudadanoinusual-captura-privada`;
- `ciudadanoinusual-conversion-ligera`.

Los contratos ya estan escritos. La implementacion oficial sigue pendiente.

## Componentes principales y responsabilidades

### Hermes runtime

Ubicacion: `/home/hermes/.hermes`.

Responsabilidad:

- ejecutar Hermes Agent;
- mantener configuracion local;
- operar Telegram Gateway;
- almacenar cache, datos privados y skills experimentales.

No esta versionado en este repo.

### Repo `Hermes_Ia`

Responsabilidad:

- fuente documental principal;
- contratos de flujo;
- scripts pequenos;
- runbooks tecnicos;
- roadmap;
- banco de contenido;
- criterios de calidad.

No debe contener secretos ni capturas privadas.

### Telegram Gateway

Responsabilidad:

- canal movil para usar Hermes desde Telegram;
- recibir texto, imagenes, voz y PDFs;
- permitir comandos como `/whoami`, `/status` y `/background`;
- mantener el servicio activo via `systemd`.

Estado validado:

- texto;
- imagen;
- voz;
- PDF;
- ruta accesible de archivos;
- botones de copia para ids de capturas en `ultimas 5 capturas`.

Limite conocido:

- `.asc` fue rechazado por tipo no permitido.

### Captura movil

Script versionado: `scripts/captura-movil.py`.

Responsabilidad:

- guardar capturas privadas como JSONL;
- listar capturas recientes;
- mostrar captura por id o prefijo;
- actualizar estado;
- exportar capturas curadas;
- rechazar textos que parezcan plantilla o instrucciones.

Almacen por defecto:

```text
/home/hermes/.hermes/data/ciudadanoinusual/capturas.jsonl
```

Este archivo de datos vive fuera de Git.

### Envio de imagenes a Telegram

Script versionado: `scripts/send-telegram-photo.py`.

Responsabilidad:

- leer `TELEGRAM_BOT_TOKEN` y `TELEGRAM_HOME_CHANNEL` desde `/home/hermes/.hermes/.env`;
- enviar una imagen local al chat autorizado;
- devolver resultado JSON simple.

Riesgo:

- depende de secretos en `.env`, aunque no los imprime.

### `JUDGE.md`

Responsabilidad:

- definir criterios minimos de calidad para Research, Content y Builder;
- exigir mejora si una salida baja de 8/10;
- evitar guardar outputs flojos como validos.

### Banco editorial

Ubicacion principal:

```text
projects/hermes_ia/content/ciudadanoinusual/
```

Responsabilidad:

- salidas base;
- modos;
- guiones;
- posts;
- carruseles;
- publicables;
- indices de publicacion.

El banco mezcla contenido final, borradores y mecanismos editoriales. Es util, pero necesita seguir separando "publicable", "publicado" y "experimento".

### Research

Ubicacion:

```text
projects/hermes_ia/research/
```

Responsabilidad:

- briefings con fuentes, riesgos y conclusion accionable.

El estado documentado indica 6 briefings.

### Skills experimentales

Indice versionado:

```text
projects/hermes_ia/SKILLS-EXPERIMENTALES.md
```

Skill activa en runtime:

```text
/home/hermes/.hermes/skills/note-taking/ciudadanoinusual-mobile-intake/
```

Responsabilidad:

- Captura Movil V1;
- Modo Calle;
- flujo Telegram para CiudadanoInusual.

Estado:

- candidata a formalizacion;
- sigue como skill puente un ciclo mas;
- no debe ganar mas alcance.

## Flujo del sistema

### Flujo local

1. Erick trabaja en el workspace local del proyecto.
2. Codex o Erick editan documentos/scripts.
3. Se revisa diff.
4. Se hace commit.
5. Se empuja a `origin` y `vps`.
6. En VPS, Hermes puede leer el workspace actualizado.

### Flujo movil de captura

1. Erick envia desde Telegram una situacion, nota, imagen o voz.
2. Hermes detecta si la intencion es capturar, inspeccionar, convertir o responder.
3. Si es captura privada, se guarda fuera de Git en JSONL.
4. Hermes devuelve id, estado, flags, formato sugerido y ruta de almacen.
5. Erick puede pedir recuperacion por id, ultima captura, numero reciente o referencia semantica.
6. Si corresponde, la captura pasa a borrador, Judge y registro.

### Flujo editorial

1. Research produce briefing.
2. Content transforma briefing o experiencia real en hooks, guion, post o carrusel.
3. Judge evalua si merece guardarse.
4. Publicables se separan en `publicables/`.
5. Publicacion externa se registra manualmente.

### Flujo Builder

1. Se detecta friccion real.
2. Se propone una mejora pequena.
3. Se edita doc o script.
4. Se verifica con comando reproducible.
5. Se commit/push si aplica.

## Tecnologias usadas

Tecnologias confirmadas por documentacion:

- Windows local con PowerShell.
- Git.
- GitHub como remoto `origin`.
- VPS Hetzner CX33 x86.
- Ubuntu 24.04.
- Usuario Linux `hermes`.
- Hermes Agent instalado nativo.
- OpenAI Codex como proveedor principal.
- El proveedor y modelo vigente por perfil se mantienen en la fuente unica `docs/CODEX-BRIEF.md`.
- OpenRouter como fallback.
- Telegram Bot / Gateway.
- `systemd --user` y linger para persistencia del gateway.
- Python 3 para scripts pequenos.
- Markdown como formato principal.
- JSONL para capturas privadas.

No activos por decision:

- Docker;
- cron recurrente;
- MCPs;
- Playwright;
- memoria externa;
- dashboard publico;
- API publica.

## Estructura de carpetas y modulos

### Raiz

- `README.md`: vision, estado general y reglas de alcance.
- `AGENTS.md`: politica operativa para agentes.
- `ROADMAP-HERMES.md`: fuente canonica de estado y decisiones.
- `.env.example`: ejemplo, no secretos.

### `docs/`

Contexto transversal:

- `CODEX-BRIEF.md`;
- backlog futuro;
- referencias externas;
- curso/transcripcion usada como inspiracion, no autoridad operativa.

### `runbooks/`

Runbooks tecnicos:

- decision de arquitectura;
- estado actual;
- VPS;
- seguridad;
- instalacion nativa;
- configuracion de modelo;
- backup/restore;
- Docker futuro;
- troubleshooting;
- Telegram Gateway.

### `scripts/`

Scripts operativos pequenos:

- `captura-movil.py`;
- `send-telegram-photo.py`.

### `learning/`

Bitacora de decisiones, aprendizajes e incidencias.

### `projects/hermes_ia/`

Proyecto piloto real:

- contexto;
- operativa diaria/semanal;
- tareas;
- usos oficiales;
- Judge;
- contratos de skills;
- Personal Ops;
- skills experimentales;
- research;
- content.

### `projects/hermes_ia/content/ciudadanoinusual/`

Banco editorial:

- salidas base;
- modos diarios;
- referencias visuales;
- publicaciones;
- publicables.

## Contexto y memoria

El sistema maneja contexto en tres niveles:

### Contexto versionado

Esta es la memoria estable del proyecto:

- `ROADMAP-HERMES.md`;
- `docs/CODEX-BRIEF.md`;
- `AGENTS.md`;
- `runbooks/`;
- `projects/hermes_ia/`.

Ventaja:

- auditable y sincronizable.

Limite:

- requiere disciplina para mantenerlo actualizado.

### Contexto runtime

Vive en `HERMES_HOME`:

- skills experimentales;
- cache de imagenes;
- documentos recibidos;
- capturas privadas;
- configuracion real;
- token de Telegram;
- posible memoria interna de Hermes.

Ventaja:

- permite operacion real desde movil.

Riesgo:

- no todo queda versionado; otro arquitecto debe revisar el VPS para ver la verdad runtime.

### Memoria conversacional

El chat aporta contexto temporal, pero no debe ser fuente canonica.

Decision correcta del proyecto:

- pasar decisiones importantes a Markdown o bitacora.

## Automatico vs manual

### Automatico o semiautomatico hoy

- Telegram Gateway como servicio persistente.
- Recepcion de mensajes, imagenes, voz y PDFs.
- Guardado de capturas privadas mediante script.
- Listado y recuperacion de capturas.
- Envio de imagenes a Telegram mediante script.
- `/background` pequeno para tareas no destructivas.
- Botones de copia para ids de capturas en Telegram, implementados en runtime.

### Manual hoy

- Publicacion en redes.
- Revision de privacidad.
- Aplicacion consciente de Judge salvo flujo puntual.
- Commit y push.
- Decision de oficializar skills.
- Activacion de nuevas capacidades.
- Gestion de secretos.

### Deliberadamente no automatico

- publicar contenido;
- tocar servicios;
- activar cron recurrente;
- instalar dependencias;
- cambiar backend;
- usar Docker;
- activar MCPs;
- usar Playwright;
- mover memoria externa.

## Deuda tecnica

### 1. Parte del comportamiento vive fuera del repo

La skill `ciudadanoinusual-mobile-intake` y el parche de botones de copia se documentaron como artefactos de `HERMES_HOME`; la presencia real debe verificarse antes de usarlos. La comprobacion del 2026-08-21 encontro la skill ausente.

Esto era aceptable para incubar, pero no debe quedarse indefinidamente asi.

### 2. Skill experimental demasiado amplia

La skill mezcla:

- captura privada;
- recuperacion;
- inspeccion de adjuntos;
- conversion;
- Modo Calle;
- parte de contenido.

Ya existe decision de separarla, pero falta implementacion.

### 3. Estado distribuido

La verdad del sistema esta repartida entre:

- Markdown versionado;
- runtime de Hermes;
- JSONL privado;
- cache de Telegram;
- historial de Telegram;
- Git remotos.

Esto es normal en fase inicial, pero dificulta handoff completo.

### 4. Falta una prueba automatizada minima

`scripts/captura-movil.py` tiene logica suficiente para merecer tests unitarios minimos, especialmente:

- anti-plantillas;
- add/list/show/update;
- busqueda por prefijo ambiguo;
- export curated.

Hoy se valida principalmente por uso real y comandos manuales.

### 5. No hay inventario tecnico runtime reproducible

El repo documenta el runtime, pero no hay script versionado que audite:

- version de Hermes;
- estado gateway;
- rutas clave;
- existencia de skills experimentales;
- disponibilidad de scripts;
- salud de capturas JSONL.

### 6. Riesgo de crecimiento documental

El proyecto tiene mucha documentacion. Es util porque el sistema aun se esta formando, pero puede volverse friccion si cada avance crea otro documento sin cerrar tareas.

## Decisiones abiertas

### Oficializacion de skills

La decision estrategica esta tomada: separar en dos skills. Falta decidir cuando implementar:

- `ciudadanoinusual-captura-privada`;
- `ciudadanoinusual-conversion-ligera`.

### Duracion de la skill puente

Historicamente se acordo mantener `ciudadanoinusual-mobile-intake` un ciclo mas. La comprobacion del 2026-08-21 la encontro ausente, por lo que ya no es un puente operativo vigente.

### Personal Ops V1

Esta activo, pero requiere mas usos reales para medir si reduce friccion de portatil.

### Publicacion y feedback

Hay una publicacion externa registrada. Falta rutina semanal de medicion y aprendizaje.

### Orquestacion multiagente

Perfiles/subagentes estan planificados, pero no activos. Falta definir cuando aportan valor real frente a Hermes unico con modos.

### Cron

Cron one-shot queda como futuro experimento seguro con permiso. Cron recurrente sigue rojo.

## Riesgos

### Riesgo operativo

Cambios directos en `HERMES_HOME` pueden resolver fricciones rapido, pero tambien pueden perderse o quedar sin trazabilidad si no se registran.

### Riesgo de privacidad

El sistema recibe imagenes, voz, PDFs y notas personales. Debe tratar por defecto como privado:

- caras;
- terceros;
- logos;
- ubicaciones;
- rutinas;
- documentos;
- datos laborales.

### Riesgo de sobreautomatizacion

El usuario quiere usar Hermes al maximo, pero no quiere que publique, toque secretos o tome decisiones sensibles automaticamente.

### Riesgo de deriva editorial

`CiudadanoInusual` no debe convertirse en canal de hipotecas/credito/vivienda. Esa linea quedo como investigacion personal, no eje de contenido.

### Riesgo de mezclar proyectos

`TopoField` y `TopoTask` estan fuera de alcance. No deben tocarse desde este repo sin nueva decision.

### Riesgo de dependencia de chat

Si las decisiones importantes se quedan en conversaciones, el sistema pierde trazabilidad. La regla correcta es registrar cierres en repo.

## Roadmap recomendado

### Paso 1: cerrar inventario runtime

Crear una verificacion versionada que diga:

- gateway activo;
- ruta de capturas existe;
- skill experimental existe;
- scripts funcionan;
- ultimo estado Git local/VPS.

No debe imprimir secretos.

### Paso 2: implementar skill oficial 1

Crear `ciudadanoinusual-captura-privada` como skill versionada minima.

Debe cubrir:

- guardar;
- listar recientes;
- recuperar ultima;
- recuperar por numero;
- recuperar por referencia corta;
- inspeccionar adjunto sin inventar.

### Paso 3: probar skill oficial 1 con captura real

No basta crearla. Debe superar uso real desde Telegram.

### Paso 4: implementar skill oficial 2

Crear `ciudadanoinusual-conversion-ligera`.

Debe tomar capturas ya guardadas y devolver borradores sin invadir captura privada.

### Paso 5: retirar o congelar skill puente

Cuando ambas skills oficiales funcionen, archivar `ciudadanoinusual-mobile-intake` o dejarla como compatibilidad temporal documentada.

### Paso 6: formalizar rutina semanal

Rutina recomendada:

- revisar capturas;
- elegir 1-3 piezas;
- aplicar Judge;
- registrar publicacion o descarte;
- medir que formatos se repiten mejor.

### Paso 7: evaluar orquestador

Solo despues de estabilizar skills:

- Research agent;
- Content agent;
- Builder agent;
- Judge agent;
- Personal Ops agent.

No antes.

## Preparacion para evolucionar a orquestador + agentes

El proyecto esta razonablemente preparado conceptualmente, pero no implementado como orquestador formal.

Fortalezas:

- roles ya definidos: Research, Content, Builder, Judge, Mobile Ops, Personal Ops;
- limites de autonomia claros;
- contratos de skills ya existen;
- separacion futura de captura/conversion ya decidida;
- Markdown funciona como memoria compartida;
- Telegram aporta interfaz operativa real;
- Judge introduce control de calidad.

Debilidades:

- no hay scheduler/orquestador versionado;
- no hay estado central formal salvo Markdown y JSONL privado;
- skills oficiales aun no existen en repo;
- los agentes no tienen contratos ejecutables separados;
- no hay tests ni harness de simulacion;
- parte del runtime vive fuera de Git.

Nivel de preparacion:

- Arquitectura conceptual: alta.
- Implementacion operativa basica: media.
- Preparacion para multiagente robusto: media-baja hasta formalizar skills y pruebas.

## Que mejoraria como arquitecto principal

### 1. Convertir contratos en implementacion minima

El siguiente salto no debe ser mas teoria. Debe ser implementar la skill oficial de captura privada.

### 2. Crear un `runtime-audit` sin secretos

Un script que audite salud del sistema permitiria evitar reconstruir estado desde chats.

### 3. Reducir documentos vivos a pocos canonicos

Mantener como canonicos:

- `ROADMAP-HERMES.md`;
- `docs/CODEX-BRIEF.md`;
- `AGENTS.md`;
- `runbooks/09-telegram-gateway.md`;
- `projects/hermes_ia/TAREAS.md`;
- contratos de skills.

El resto debe servir como evidencia o archivo, no como decision diaria.

### 4. Anadir tests a `captura-movil.py`

Es un script pequeno, pero toca datos privados. Merece pruebas.

### 5. Definir criterio de promocion de skill

Ya hay criterio general. Falta una checklist concreta de promocion:

- pruebas;
- rollback;
- ruta;
- owner;
- version;
- ejemplo de uso;
- criterio de retiro de skill vieja.

### 6. Separar banco editorial de mecanismo operativo

El contenido crecio rapido. Conviene mantener separados:

- raw ideas;
- borradores;
- publicables;
- publicados;
- resultados.

### 7. Mantener Telegram como interfaz, no como unica fuente de verdad

Telegram es excelente para captura. No debe convertirse en el unico lugar donde viven decisiones.

## Informacion no inferible desde el repo

No se puede inferir completamente desde Git:

- estado exacto actual de `/home/hermes/.hermes`;
- contenido real de `capturas.jsonl`;
- configuracion completa de Telegram BotFather;
- contenido de `.env`;
- version exacta actual de la skill experimental remota;
- si el parche de botones de copia sigue aplicado tras futuras actualizaciones de Hermes;
- metricas reales de publicaciones en redes;
- estado actual de costes o limites de proveedores;
- comportamiento exacto de modelos externos en fecha futura.

Un arquitecto que continue debe verificar estas piezas en VPS antes de tomar decisiones de runtime.

## Resumen ejecutivo

Si otro arquitecto senior tuviera que continuar este proyecto manana, necesita entender esto:

`Hermes_Ia` no es una app clasica. Es un sistema operativo personal de IA, apoyado en Hermes Agent, Markdown, Git, Telegram y scripts pequenos. Su objetivo es ayudar a Erick/CiudadanoInusual a investigar, crear contenido, capturar ideas desde movil, ordenar decisiones privadas y mejorar el propio sistema sin meter complejidad prematura.

La base tecnica esta operativa: Hermes corre nativo en un VPS Hetzner con usuario `hermes`, `openai-codex` como proveedor principal, OpenRouter como fallback y Telegram Gateway persistido con `systemd`. El repo local se sincroniza con GitHub y VPS.

El sistema ya demostro valor real: Research, Content, Builder, Mobile Ops y Personal Ops existen como usos operativos; Mobile Ops V1 esta cerrado con pruebas reales; Telegram recibe texto, imagenes, voz y PDFs; las capturas privadas se guardan fuera de Git; las recuperaciones humanas ya no dependen de memorizar ids largos.

La principal deuda es que la documentacion describia logica viva en `HERMES_HOME`, especialmente la skill experimental `ciudadanoinusual-mobile-intake`, sin verificar su presencia. La comprobacion real del 2026-08-21 la encontro ausente. La decision arquitectonica vigente sigue siendo no versionar una skill monolitica: una futura implementacion debe separar `ciudadanoinusual-captura-privada` y `ciudadanoinusual-conversion-ligera`.

El siguiente arquitecto no deberia abrir Docker, cron, MCPs, Playwright, memoria externa ni multiagentes todavia. El siguiente movimiento correcto es formalizar la skill oficial de captura privada, probarla desde Telegram con una captura real, despues implementar conversion ligera y retirar la skill puente cuando deje de ser necesaria.

La vision a preservar es simple: Hermes puede crecer, pero solo si deja rastro, reduce friccion real y respeta limites claros de privacidad, seguridad y control humano.
