# CAPTURA MOVIL V1

## Proposito

Guardar ideas, notas y situaciones capturadas desde el movil sin meter informacion privada en Git.

La captura movil es materia prima. No todo debe publicarse.

## Almacen privado

Ruta canonica en el VPS:

```text
/home/hermes/.hermes/data/ciudadanoinusual/capturas.jsonl
```

Este archivo no se versiona.

El repo solo contiene:

- instrucciones;
- script;
- pruebas sinteticas;
- exports curados si se aprueban manualmente.

## Script

```bash
python3 scripts/captura-movil.py add --text "idea en bruto"
python3 scripts/captura-movil.py list
python3 scripts/captura-movil.py show <id>
python3 scripts/captura-movil.py update-status <id> reviewed
python3 scripts/captura-movil.py export-curated --output tmp/capturas-curadas.jsonl
```

## Campos

Cada captura contiene:

- `id`
- `created_at` en horario Europe/Madrid
- `source`
- `input_type`: `text`, `voice` o `image_note`
- `original_text` inmutable
- `transcript`
- `tags`
- `privacy_flags`
- `suggested_format`
- `status`
- `derived_reference`

## Estados

- `inbox`: capturada, no revisada.
- `reviewed`: revisada y clasificada.
- `converted`: usada para una pieza.
- `discarded`: descartada.

## Reglas para Hermes

Cuando el usuario escriba desde Telegram algo tipo:

```text
Captura movil
...
```

Hermes debe:

1. detectar si hay datos sensibles;
2. guardar la nota con `scripts/captura-movil.py add`;
3. no modificar `original_text`;
4. devolver el `id`;
5. proponer una sola siguiente accion.

Si hay nombres reales, empresa, ubicacion exacta, matriculas, clientes, terceros o datos privados, marcarlos en `privacy_flags`.

## Verificacion minima

Una Captura Movil V1 funciona cuando:

- se puede agregar una captura;
- se puede listar;
- se puede recuperar por `id`;
- se puede cambiar estado;
- se puede exportar una version curada;
- el archivo privado no aparece en `git status`.

## Validacion anti-plantilla

`add` debe rechazar textos que incluyan instrucciones o placeholders del prompt en vez de una situacion real.

Ejemplo incorrecto:

```bash
python3 scripts/captura-movil.py add --text "[cuenta aquí una situación real de hoy]"
```

Resultado esperado:

```text
El texto parece incluir instrucciones o plantilla. Pasa solo la situación real.
```

El comando no debe crear ningun registro nuevo.

Tambien debe rechazarse si el texto contiene instrucciones como:

- `Antes de guardar:`
- `Devuélveme`
- `No lo conviertas`
- `Detecta riesgos`
- `Usa scripts/captura-movil.py`
- `No metas nada en Git`

Ejemplo correcto:

```bash
python3 scripts/captura-movil.py add --text "Hoy en la faena hizo mucho calor, paramos a comer algo sencillo y luego seguimos con otra tarea de campo." --tags "calle,trabajo" --privacy-flags "ubicacion" --suggested-format "guion"
```

Resultado esperado:

- se crea una captura con `status` `inbox`;
- `original_text` conserva solo la situacion real;
- no se guarda ninguna instruccion del prompt;
- el archivo privado sigue fuera de Git.
