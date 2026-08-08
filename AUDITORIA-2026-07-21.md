# AUDITORIA HERMES_IA - 2026-07-21

Auditoria externa del repositorio `Hermes_Ia` sobre proceso, documentacion, seguridad y encaje con el objetivo declarado: arnes personal de IA + asesor de marca para `CiudadanoInusual`.

Metodo: lectura completa del repo, historial Git (114 commits), scripts, gobernanza y contenido. Sin acceso al VPS.

---

## 1. Veredicto en una linea

El sistema esta bien pensado y bien documentado, pero **produce reglas mas rapido de lo que produce resultados**. La gobernanza esta en Fase 3 y la ejecucion en Fase 0.

---

## 2. Los numeros que importan

| Metrica | Valor | Lectura |
| --- | --- | --- |
| Commits totales | 114 | actividad real |
| Commits `docs:` | 108 de 114 (95%) | el repo casi solo documenta |
| Scripts ejecutables | 3 (~500 lineas) | el sistema es casi todo texto |
| Lineas de gobernanza + operativa | ~4.150 | 8 lineas de doc por cada linea de codigo |
| Piezas de contenido creadas | 20 content + 18 publicables | inventario alto |
| Publicaciones reales registradas | **1** (LinkedIn, 21-jun) | conversion ~2% |
| Dias sin commit | **23** (ultimo: 28-jun) | el flujo se paro |
| Evaluaciones JUDGE | 5 de 5 con nota 8/10 | juez sin discriminacion |

Estos siete numeros son el diagnostico completo. Todo lo demas es detalle.

---

## 3. Proceso

### Lo que funciona

- Ciclo `TAREAS.md` -> `QUEUE.md` -> archivo -> evidencia esta bien definido y se ha usado de verdad.
- Los cierres operativos (captura privada, conversion ligera, limites de Telegram) estan documentados con evidencia, no con promesas.
- El semaforo verde/amarillo/rojo de `AGENTS.md` es una buena abstraccion de autonomia. Es de lo mejor del repo.
- Mensajes de commit consistentes y en formato convencional.

### Lo que falla

**3.1 El embudo produce inventario, no salidas.**
20 piezas de content -> 18 publicables -> 1 publicada. El cuello de botella no es la creacion, es la publicacion. Y todo el sistema esta optimizado para el lado que no es el cuello de botella. `QUEUE.md` tiene ~15 items pendientes de *crear* y cero items de *publicar*.

**3.2 El proyecto se paro hace 3 semanas sin registro de por que.**
Ultimo commit 28-jun. Hoy 21-jul. No hay entrada en `learning/bitacora.md` explicando la pausa. Un sistema que se define como "memoria y continuidad" tiene un hueco de 23 dias sin trazar. Esto es exactamente el fallo que la gobernanza deberia prevenir.

**3.3 Hay 7 archivos modificados sin commitear y los 7 cambios son ruido.**
El diff completo es "falta/sobra salto de linea final" en 7 archivos. Causa: no hay `.gitattributes`, y el repo se edita desde Windows y desde Linux (VPS). Consecuencia real: `verificar-cambio.sh` avisa de cambios que no son cambios, y se pierde confianza en `git status`.

**3.4 Meta-trabajo compitiendo con trabajo.**
`PLAN-SEPARACION-SKILLS-CAPTURA.md` (157 lineas) + `SPEC-FORMALIZACION-CAPTURA-MOVIL.md` (241 lineas) + `CONTRATO-CAPTURA-PRIVADA.md` (232 lineas) + `CONTRATO-CONVERSION-LIGERA.md` (168 lineas) = 798 lineas para decidir como formalizar **un script de 200 lineas que ya funciona**. La propia Constitucion lo prohibe ("nucleo pequeno", "no se implementa algo solo porque sea tecnicamente interesante") y aun asi ocurrio.

**3.5 El JUDGE no juzga.**
5 evaluaciones, 5 notas de 8/10, 5 "valida". Un juez cuya distribucion de notas es una constante no aporta informacion. Falta: evaluar piezas que se descartan, y registrar al menos un suspenso. Si nada baja de 8, el umbral de 8 no filtra nada.

---

## 4. Documentacion

### Lo que funciona

- `CONSTITUTION.md` es solido. Los principios 10 (tiempo en pareja), 11 (salud) y 14 (publicar manualmente) son decisiones maduras y poco habituales; protegen contra el fallo tipico de estos sistemas, que es convertirse en una fabrica de culpa.
- `BOOTSTRAP.md` como punto de entrada unico, enlazado desde README y AGENTS: correcto.
- Los runbooks tienen estructura util (objetivo, riesgo, rollback, verificacion).
- `GLOSARIO.md` e `INDICE-OPERATIVO.md`: buena higiene, poco comunes en proyectos personales.

### Lo que falla

**4.1 Coste de arranque desproporcionado.**
`BOOTSTRAP.md` obliga a leer 9 archivos antes de tocar nada: ~1.400 lineas de lectura previa. Para un repo con 3 scripts. Cualquier agente (o tu mismo dentro de dos meses) paga ese peaje entero antes de hacer algo util. Contradice el principio 4 de la Constitucion ("si obliga a recordar demasiados pasos, esta mal disenado").

**4.2 Cinco documentos compiten por ser "las instrucciones del agente".**
`AGENTS.md`, `docs/governance/CODEX-OPERATING-POLICY.md`, `docs/governance/CODEX-MASTER-PROMPT.md`, `docs/CODEX-BRIEF.md` y `PROMPT_PARA_CODEX.md` (este ultimo suelto en la raiz). Se solapan. Cuando se solapan, divergen. Cuando divergen, el agente elige y tu no sabes cual eligio.

**4.3 Tres jerarquias de decision distintas y no identicas.**
El orden de lectura de `BOOTSTRAP`, la jerarquia de conflicto de `BOOTSTRAP`, y el semaforo de `AGENTS.md`. No dicen lo mismo (ej.: `BOOTSTRAP` pone la Constitucion por encima de todo; `AGENTS.md` define autonomia sin referirse a ella). Ambiguedad estructural.

**4.4 Fase 0 declarada "cerrada" pero es la unica fase con entregables completos.**
`MASTER-PLAN` marca Fase 0 (gobernanza) como cerrada y Fase 1 (Hermes Creador minimo) como activa. Pero Fase 1 no tiene ni una sola prueba real registrada: `TAREAS.md` lo lista como "siguiente tarea concreta" desde el 28-jun. La fase esta abierta desde hace 23 dias con cero evidencia.

**4.5 Sin criterio de retirada.**
No hay ningun documento que diga cuando se archiva o borra otro documento. El repo solo puede crecer. `EVOLUTION-POLICY.md` cubre como anadir, no como quitar.

---

## 5. Seguridad

Postura general: **razonable para un proyecto personal, con tres puntos concretos que arreglar**. La higiene basica es correcta.

### Correcto

- Ningun secreto real versionado, verificado sobre todo el historial (busqueda de patrones `sk-`, tokens de Telegram, claves privadas, `ghp_`).
- `.gitignore` bien construido: `.env*` con excepcion explicita para `.env.example`, mas `secrets/`, `logs/`, `tmp/`, `*.pem`, `*.key`, `id_rsa`, `id_ed25519`, `*.token`.
- `.env.example` usa placeholders. Nunca hubo un `.env` real en el historial.
- `captura-movil.py` aplica `chmod 0600` al almacen de capturas y lo guarda **fuera** del repo (`/home/hermes/.hermes/data/`). Decision correcta.
- Usuario dedicado `hermes`, no `root`. Sin API publica, sin dashboard publico. Telegram autorizado a un solo usuario.
- Token de Telegram en `/home/hermes/.hermes/.env`, no versionado.

### Hallazgo 1 - IP del VPS expuesta en repositorio publico (MEDIO)

`learning/bitacora.md:20` contenia `ssh -i $HOME/.ssh/hermes_hetzner_ed25519 root@<HETZNER_VPS_IP>` con la IP real en texto plano (ya corregido, ver Hallazgo 1 mas abajo).

El repo es publico (`github.com/Erickconestilo/Hermes_Ia`). Combinado con lo que el propio repo documenta —usuario `hermes`, usuario `root` habilitado para bootstrap, Ubuntu 24.04, sin mencion de cambio de puerto SSH ni de fail2ban— eso es un objetivo con nombre y apellidos. No es explotable por si solo (hace falta la clave), pero es informacion gratis y elimina el trabajo de reconocimiento del atacante.

Accion: sustituir la IP por `<HETZNER_VPS_IP>` en la bitacora, verificar el resto del repo, y confirmar en el VPS que `PermitRootLogin` esta en `prohibit-password` o `no`, que `PasswordAuthentication no` esta activo y que hay `fail2ban` o equivalente. Nota: reescribir el historial de Git no merece la pena aqui; la IP ya circulo. Lo que importa es endurecer el servidor.

### Hallazgo 2 - El token de Telegram puede acabar en un traceback (MEDIO)

`scripts/send-telegram-photo.py` construye la URL como `https://api.telegram.org/bot{token}/sendPhoto` y llama a `urlopen` **sin `try/except`**. Si Telegram responde 401/403/429, Python lanza `HTTPError` y el traceback imprime la URL completa —con el token dentro— en stderr. Ese stderr puede acabar en un log de systemd, en un chat de Telegram o en una captura de pantalla.

Accion: envolver la llamada en `try/except urllib.error.HTTPError/URLError` y emitir solo el codigo de estado, nunca la URL. Son 6 lineas.

### Hallazgo 3 - Backup y restauracion nunca probados (MEDIO-ALTO)

Existe `runbooks/06-backup-restore.md`, pero no hay ni una sola evidencia de restauracion ejecutada. El VPS contiene el estado de Hermes, `HERMES_HOME`, las skills experimentales, el gateway de Telegram y —lo mas importante— `capturas.jsonl`, que **no esta en Git por diseno**. Es el unico dato del sistema sin copia distribuida.

Un backup no probado es una suposicion, no un backup. Si el VPS desaparece hoy, se pierden las capturas privadas y las skills experimentales enteras.

Accion: ejecutar una restauracion real a una ruta temporal, cronometrarla y registrar el resultado. Es la tarea de mayor retorno del repo ahora mismo.

### Puntos menores

- Sin deteccion automatica de secretos. Todo depende de disciplina humana; un `pre-commit` con `gitleaks` cubre el fallo del dia malo.
- Sin procedimiento de rotacion/revocacion de tokens documentado. Si manana se filtra el token de Telegram, no hay runbook: hay improvisacion.
- `send-telegram-photo.py` lee el fichero completo en memoria (`file_path.read_bytes()`). Irrelevante con fotos, problematico si algun dia se reutiliza para video.
- `secrets/` y `logs/` existen como carpetas vacias sin `.gitkeep`: se documentan en el README pero no existen para quien clona.

---

## 6. Encaje con lo que quieres: asesor de marca

Aqui esta el hueco mas grande, y no es de seguridad ni de proceso.

**Tienes una fabrica de piezas. No tienes un asesor.**

Lo que si hay: modos (post, guion, carrusel, calle), checklists de privacidad muy buenos, prompts de edicion, referencias visuales, plan semanal, `HERMES-CREADOR.md` con cuatro comandos bien definidos.

Lo que no hay, y es lo que convierte una fabrica en un asesor:

1. **Definicion de audiencia.** La Constitucion define tu identidad (quien eres tu). No define a quien le hablas. Sin eso, "¿que toca hoy?" solo puede responder desde tu energia, nunca desde el interes de nadie.

2. **Datos de resultado.** `INDICE-PUBLICACIONES.md` tiene 1 fila y su seguimiento sigue diciendo "revisar impresiones" un mes despues. Hermes Creador no puede aprender: no tiene de que. Esto viola directamente el Principio 6 de tu Constitucion ("evidencia antes que intuicion"). Ahora mismo el sistema optimiza a ciegas.

3. **Estrategia de canal.** LinkedIn, Instagram, TikTok y YouTube Shorts aparecen tratados como equivalentes. No lo son: distinta audiencia, distinto formato, distinto ritmo, distinto tipo de exito. Publicar en cuatro canales sin estrategia diferenciada es la forma mas rapida de no crecer en ninguno.

4. **Cadencia comprometida.** `PLAN-PUBLICACION-SEMANAL.md` existe, pero la cadencia real observada es 1 publicacion en 6 semanas. El plan no se esta cumpliendo y nada en el sistema lo detecta.

5. **Un `APRENDIZAJES.md` de marca.** Que funciono, que no, que hipotesis quedan abiertas. Sin esto, cada pieza empieza de cero.

Nota adicional: `MODO-CALLE.md`, el formato ranking `/25` de comida en ruta, y el angulo "topografia real, no glamurosa" son lo mas diferenciado que tienes. Son formato propio, repetible y dificil de copiar. En el sistema actual estan al mismo nivel que todo lo demas.

---

## 7. Que haria yo: focalizar

Pediste focalizar. Esta es la propuesta, en orden.

### Congelar

Durante 30 dias, **cero commits de tipo `docs:` en `docs/governance/`**. La gobernanza esta terminada. Anadirle mas es evasion productiva.

Congelar tambien la formalizacion de skills de captura. Las 798 lineas de spec para un script que ya funciona son deuda, no activo. La skill experimental se queda donde esta.

### La unica metrica de los proximos 30 dias

**Publicaciones reales por semana.**

No piezas creadas. No documentos mejorados. No skills formalizadas. Publicaciones que existen fuera del repositorio.

Objetivo minimo viable: **2 por semana**. Tienes 18 piezas publicables en inventario. Da para 9 semanas sin crear nada nuevo.

### Seis acciones concretas, en orden

| # | Accion | Coste | Por que |
| --- | --- | --- | --- |
| 1 | Probar restauracion de backup y registrarla | 1h | Unico riesgo de perdida irreversible |
| 2 | Quitar la IP de `bitacora.md` + endurecer SSH en el VPS | 30 min | Repo publico |
| 3 | `try/except` en `send-telegram-photo.py` | 10 min | Fuga de token en traceback |
| 4 | Anadir `.gitattributes` con `* text=auto eol=lf` y normalizar | 10 min | Elimina el ruido de los 7 diffs falsos |
| 5 | Publicar 2 piezas del inventario y rellenar `INDICE-PUBLICACIONES` con datos reales | 2h | Arranca el bucle de evidencia |
| 6 | Crear `AUDIENCIA.md` y `APRENDIZAJES.md` en `content/ciudadanoinusual/` | 1h | Convierte la fabrica en asesor |

Nada mas hasta que esas seis esten hechas.

### Fusiones pendientes (cuando se descongele)

- `PROMPT_PARA_CODEX.md` + `docs/CODEX-BRIEF.md` + `CODEX-MASTER-PROMPT.md` -> uno solo.
- `CONTRATO-CAPTURA-PRIVADA.md` + `CONTRATO-CONVERSION-LIGERA.md` + `SPEC-FORMALIZACION-*` + `PLAN-SEPARACION-*` -> un `CAPTURA.md`.
- Objetivo: `BOOTSTRAP.md` debe poder llevarte a trabajar leyendo 3 archivos, no 9.

### Regla nueva propuesta para la Constitucion

> **Principio 16 - Ratio de ejecucion.**
> Por cada documento de proceso nuevo debe existir una ejecucion real registrada de ese proceso.
> Si un proceso lleva 14 dias documentado sin una sola ejecucion, el documento se archiva.

Es la unica regla que falta, y es la que habria evitado los ultimos 23 dias.

---

## 8. Resumen de riesgos

| Riesgo | Nivel | Accion |
| --- | --- | --- |
| Backup/restore nunca probado; `capturas.jsonl` sin copia | Medio-alto | Probar restauracion ya |
| IP del VPS en repo publico | Medio | Sanitizar + endurecer SSH |
| Token de Telegram en traceback de error | Medio | `try/except` |
| Sin deteccion automatica de secretos | Bajo-medio | `gitleaks` en pre-commit |
| Sin runbook de rotacion de tokens | Bajo-medio | Documentar |
| Ruido de fin de linea entre Windows y VPS | Bajo | `.gitattributes` |
| Deriva documental (95% de commits son docs) | **Alto para el objetivo** | Congelar gobernanza 30 dias |
| Sin datos de resultado de marca | **Alto para el objetivo** | `INDICE-PUBLICACIONES` real |

---

## 9. Lo que no hay que cambiar

Para que el resto se lea en su contexto: la Constitucion, el semaforo de autonomia, la disciplina de privacidad en las piezas y la higiene de secretos estan por encima de lo que se ve en proyectos personales de este tipo. El problema no es la calidad del sistema. Es que el sistema esta construyendose a si mismo en lugar de producir.

Esta auditoria no dice "esta mal hecho". Dice "esta demasiado bien hecho para lo poco que hace todavia".
