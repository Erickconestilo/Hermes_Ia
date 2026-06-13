# 04 - Configuración del modelo

## Objetivo

Configurar el proveedor de modelo más adecuado para una primera prueba estable.

## Criterios

- simplicidad operativa
- documentación oficial clara
- bajo riesgo de bloqueo por credenciales o límites
- sin guardar secretos en archivos versionados

## Placeholders relevantes

- `<OPENAI_API_KEY>`
- `<OPENROUTER_API_KEY>`

## Dudas a resolver

- Qué proveedores soporta oficialmente Hermes hoy.
- Qué flujo es más estable para una primera instalación: API key, OAuth u otro método oficial.
- Qué implicaciones de coste, rate limits y privacidad tiene cada opción.

## Decisión ejecutada

- Proveedor elegido para la primera etapa: `OpenRouter`
- Motivo:
  - permite probar gratis primero
  - evita meter varias claves de varios proveedores
  - encaja con la prioridad actual de simplicidad

## Configuración aplicada

- Modelo principal:
  - `nex-agi/nex-n2-pro:free`
- Fallback:
  - `nvidia/nemotron-3-ultra-550b-a55b:free`
- Backend terminal actual:
  - `local`

## Archivos tocados

- `/home/hermes/.hermes/config.yaml`
- `/home/hermes/.hermes/.env`

## Incidencia encontrada

- La clave de OpenRouter se escribió inicialmente comentada en `.env`:

```env
# OPENROUTER_API_KEY=...
```

- Mientras la línea estuvo comentada, `hermes doctor` reportó correctamente que no había credenciales disponibles para `openrouter`.

## Corrección aplicada

- Se activó la variable quitando el `#`.
- Se dejó la clave sin comillas ni espacios extra:

```env
OPENROUTER_API_KEY=<OPENROUTER_API_KEY>
```

## Resultado alcanzado

- `hermes doctor` pasó a validar `OpenRouter API`.
- Hermes respondió con el modelo principal configurado a través de OpenRouter.

## Nota operativa

- Si una key aparece en chat, capturas o historial compartido, debe asumirse expuesta y conviene rotarla.
