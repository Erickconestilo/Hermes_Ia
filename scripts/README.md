# Scripts

Directorio reservado para automatizaciones pequeñas y auditables.

Reglas:

- no guardar secretos
- preferir scripts cortos y comentados
- documentar antes de automatizar pasos sensibles
- `retencion-datos.py` revisa candidatos de retencion en capturas privadas; usar `--dry-run` antes de cualquier `--apply`.
- `verificar-secretos.sh` analiza solo archivos en stage y, si detecta algo, informa tipo, archivo y linea sin imprimir valores sensibles.
- `preparar-video-social.py <ruta-video>` conserva la entrada compatible de analisis: extrae una hoja de fotogramas y transcribe audio localmente.
- `video-social.py` gestiona el flujo privado reproducible de CiudadanoInusual Shorts V1. Sus subcomandos son internos para Hermes, no comandos que el usuario deba memorizar: `ingest`, `analyze`, `render`, `approve`, `status`, `discard` y `retention --dry-run`.
- Cada trabajo de video guarda fuera de Git el original con checksum, analisis, planes versionados, previews A/B/C y export aprobado. Nunca publica ni borra automaticamente.

Ejemplo minimo de plan que consume `render`:

```json
{
  "selected_moment": {
    "start": 0.0,
    "end": 8.2,
    "reason": "La escena contiene contexto, desarrollo y remate completo."
  },
  "variants": {
    "A": {"label": "minima", "start": 0.0, "end": 8.2, "zoom": 1.0, "framing": "fit", "subtitles": true, "overlays": []},
    "B": {"label": "dinamica", "start": 0.0, "end": 8.2, "zoom": 1.15, "framing": "crop-center", "subtitles": true, "overlays": [{"start": 0.0, "end": 2.0, "text": "Hook breve", "position": "top"}]},
    "C": {"label": "experimental", "start": 0.0, "end": 8.2, "zoom": 1.25, "framing": "fit", "subtitles": true, "freeze_end": 0.5, "overlays": [{"start": 6.0, "end": 8.7, "text": "Remate", "position": "center"}]}
  },
  "recommendation": "B",
  "hook": "Hook breve",
  "caption": "Caption propuesto.",
  "privacy": [],
  "publish": false
}
```

El momento siempre necesita una razon narrativa. El controlador rechaza recortes arbitrarios, salidas de mas de 60 segundos, zoom superior a `1.35`, mas de tres textos y cualquier plan que solicite publicar.
