# OPERATIVA DIARIA

## Objetivo

Tener un flujo simple, repetible y rapido para trabajar con `Hermes_Ia` sin volver al bucle de leer, resumir y no ejecutar.

## Regla principal

Cada sesion debe terminar con uno de estos resultados:

- un archivo nuevo util
- un archivo existente mejorado
- una decision concreta registrada
- una verificacion real ejecutada

Si no pasa una de esas cuatro cosas, la sesion no aporto suficiente.

## Niveles de autonomia

Regla base: confianza supervisada.

Hermes puede expandirse en bajo riesgo si deja rastro. Hermes debe pedir permiso en alto riesgo.

### Verde

Permitir sin confirmacion previa si es reversible y no toca secretos:

- leer archivos
- buscar con `grep`, `find` o `rg`
- ejecutar `git status`
- ejecutar `git diff`
- crear o modificar Markdown
- crear scripts pequenos dentro del repo
- ejecutar scripts simples de verificacion si ya se mostro el contenido y no tocan sistema
- crear o usar skills experimentales dentro de `HERMES_HOME`
- usar skills experimentales desde Telegram
- guardar capturas privadas fuera de Git
- recuperar capturas
- convertir capturas en borradores
- aplicar `JUDGE.md`
- crear archivos temporales en `tmp/` o `HERMES_HOME`
- proponer mejoras operativas
- enviar imagenes o archivos por Telegram con scripts ya probados
- probar `/whoami`, `/status`, imagenes, archivos, voz y `/background` pequeno desde Telegram si la tarea es no destructiva
- registrar aprendizajes en bitacora o indice cuando corresponda

### Amarillo

Exige registro posterior, y confirmacion solo si el riesgo sube:

- `chmod +x`
- scripts nuevos
- cambios en varios archivos
- pequenos cambios de flujo Git
- automatizaciones internas del repo
- nueva skill experimental creada
- archivo nuevo en `HERMES_HOME` que afecte comportamiento
- cambio de flujo operativo
- error detectado y corregido
- automatizacion experimental no recurrente

Si la accion es clara, local, reversible y de bajo riesgo, se puede permitir con `Allow once`.

### Rojo

Bloquear o pedir confirmacion fuerte para:

- `sudo`
- `apt`
- `systemctl`
- firewall
- SSH
- `.env`
- claves, tokens o secretos
- Docker
- cron recurrente
- cambios de configuracion del gateway de Telegram
- MCPs
- Playwright
- memoria externa
- publicacion automatica en redes
- borrar datos
- `hermes doctor --fix`
- cambios fuera de `Hermes_Ia`
- tocar `TopoField` o `TopoTask`
- convertir una skill experimental en oficial versionada en Git

## Flujo recomendado

### 1. Preparar contexto local

Trabajar primero en local dentro de:

- `C:\Users\guill\Documents\Hermes_Ia`

Leer solo lo necesario:

- `README.md`
- `runbooks/01-estado-actual.md`
- `projects/hermes_ia/CONTEXTO.md`
- `projects/hermes_ia/TAREAS.md`
- `projects/hermes_ia/GLOSARIO.md`
- `projects/hermes_ia/USO-IMMEDIATO.md`

No releer todo si la tarea ya esta clara.

### 2. Elegir una sola accion

La accion debe cumplir estas reglas:

- tocar como maximo un archivo, o dos si estan fuertemente conectados
- producir un cambio visible en Git
- no ser solo resumen o reformulacion de fase
- no abrir nuevas capas de complejidad

Ejemplos buenos:

- crear una guia concreta
- aclarar una contradiccion real
- registrar una decision tecnica cerrada
- mejorar una tarea activa para que sea ejecutable
- usar `Hermes Creador minimo` para convertir una situacion real en pieza sin prompt largo

Ejemplos malos:

- volver a resumir el estado
- pedir otra vez la fase actual
- crear plantillas sin uso inmediato
- prometer integraciones futuras sin necesidad actual

### 3. Ejecutar el cambio en local

Secuencia normal:

1. editar archivo
2. revisar `git diff`
3. `git add`
4. `git commit`

Formato habitual de commit:

- `docs: ...` para cambios documentales
- descripcion en espanol

### 4. Sincronizar con el VPS

Cuando el cambio ya este bien en local:

1. `git push vps master`
2. entrar por SSH como `hermes`
3. ir a `/home/hermes/workspace/Hermes_Ia`
4. abrir `hermes`

La sincronizacion normal ya no debe hacerse con `scp` salvo incidente puntual.

Regla de flujo para artefactos versionados:

- si el resultado debe vivir en Git, Hermes debe devolver el contenido en chat
- el archivo versionado se crea o actualiza en local
- despues se distribuye con `git push origin master` y `git push vps master`
- evitar que Hermes cree archivos nuevos directamente en el VPS si luego deben entrar en el repo

### 5. Usar Hermes con una instruccion corta

Preferir prompts cortos y operativos.

Patron recomendado:

```text
Lee el contexto actual de Hermes_Ia y dime una sola mejora util, pequena y verificable que no sea meta ni setup.
```

Patron aun mejor si ya sabes el archivo:

```text
Archivo: projects/hermes_ia/TAREAS.md
Cambio: propon una mejora pequena y util
Verificacion: el resultado debe validarse con git diff
```

### 6. Crear contenido con Hermes Creador

Cuando el objetivo sea contenido para `CiudadanoInusual`, usar primero:

- `projects/hermes_ia/content/ciudadanoinusual/HERMES-CREADOR.md`

Comandos humanos minimos:

- `¿Qué toca hoy?`
- `Vídeo`
- `Historia`
- `He publicado`

Regla:

- `¿Qué toca hoy?` decide solo una prioridad editorial o formato creativo; no organiza tareas personales salvo peticion explicita.
- `Vídeo` crea guion corto vertical.
- `Historia` crea una story concreta, no decide formato general.
- Hermes pide contexto minimo.
- El usuario conserva la decision final.
- No hay publicacion automatica.
- Las publicaciones reales se registran solo en `content/ciudadanoinusual/publicaciones/INDICE-PUBLICACIONES.md`.

## Criterio de sesion util

Una sesion cuenta como buena si al final puedes responder si o si a estas preguntas:

1. Que archivo cambie?
2. Que mejoro de forma concreta?
3. Como lo verifico?
4. Que sigue despues?

## Cuando parar a Hermes

Hay que cortarlo y redirigirlo si hace una de estas cosas:

- vuelve a resumir fases ya cerradas
- propone otra plantilla sin uso inmediato
- repite decisiones ya documentadas
- habla de Docker, cron, cambios de Telegram, MCPs o memoria externa sin permiso
- convierte una tarea simple en una ceremonia

No hay que cortarlo automaticamente si:

- propone un script pequeno de verificacion
- el contenido ya se vio
- la accion es local, reversible y de bajo riesgo

## Anti-patrones de este proyecto

- demasiados prompts para una tarea obvia
- demasiada lectura para un cambio pequeno
- demasiadas fases discutidas sin diff ni commit
- mezclar la carpeta antigua `Hermes IA` con la correcta `Hermes_Ia`
- usar `root` cuando el trabajo normal es con `hermes`

## Cierre minimo recomendado

Antes de cerrar una sesion:

1. `git status`
2. comprobar si el arbol esta limpio o que queda pendiente
3. si hubo avance real, dejar commit
4. si aplica, hacer `git push vps master`

## Resultado esperado

`Hermes_Ia` debe sentirse como un sistema de trabajo cada vez mas claro y cada vez menos ceremonioso.
