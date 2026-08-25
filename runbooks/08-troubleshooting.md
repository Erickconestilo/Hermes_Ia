# 08 - Troubleshooting

## Método

Ante cualquier problema, registrar siempre:

- síntoma
- comando ejecutado
- salida exacta
- contexto del usuario (`root` o `hermes`)
- cambio previo que pudo causarlo

## Fallos probables a vigilar

- PATH incorrecto
- binario no encontrado
- permisos de `HOME`
- instalación hecha como `root` por error
- proveedor de modelo mal configurado
- archivos de configuración en rutas inesperadas

## Regla

No aplicar cambios acumulativos a ciegas. Hacer una corrección por vez y verificar.

## Caso resuelto: falso fallo de autenticacion con Google AI Studio

### Sintoma

Telegram devolvia `Provider authentication failed` de forma persistente al
probar un modelo de Google. El mensaje apuntaba a credenciales, pero no
identificaba correctamente la causa.

### Causas encadenadas

Se confirmaron tres problemas distintos:

1. **Base URL incorrecta.** Hermes ofrece por defecto la API nativa de Google
   en `/v1beta`. Para un cliente compatible OpenAI, la base correcta era
   `/v1beta/openai`:
   `https://generativelanguage.googleapis.com/v1beta/openai`.
2. **Perfiles aislados.** Cada perfil tiene su propio `.env`:
   `/home/hermes/.hermes/profiles/<perfil>/.env`. La `GOOGLE_API_KEY` estaba
   solo en el `.env` principal, por lo que el pool de credenciales de
   `auscultacion` estaba vacio. `hermes auth list` podia mostrar una
   credencial global aunque el perfil no la tuviera disponible.
3. **Saturacion del modelo.** `gemini-3.7-flash` devolvia `503 high demand`.
   `gemini-3.6-flash` respondia. `gemini-2.5-flash` estaba retirado y devolvia
   `404`.

El indicador `Tier check: paid` de Hermes tambien resulto incorrecto frente a
la consola de Google, que confirmaba nivel gratuito. El limite gratuito de
250 peticiones por dia se consume rapidamente cuando Hermes hace varias
llamadas internas por mensaje.

### Leccion operativa

Diagnosticar primero con `curl` directo al endpoint y despues tocar la
configuracion. Los errores de Hermes no siempre distinguen una credencial
ausente, un `503` de capacidad o una URL incompatible: varias causas pueden
aparecer como fallo de autenticacion.

### Diagnostico seguro

Ejecutar dentro del perfil que se quiere probar y no imprimir la clave ni su
contenido:

```bash
set -a; source $(hermes config env-path); set +a
curl -s "<base_url>/chat/completions" \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"<modelo>","messages":[{"role":"user","content":"test"}]}'
```

La variable `KEY` debe existir solo en la sesion de shell y apuntar a la
credencial del perfil correcto. Sustituir `<base_url>` y `<modelo>` por valores
no sensibles y adecuados al proveedor. No pegar la salida completa en un chat
si contiene metadatos de cuenta o proveedor.

### Orden despues de corregir

Configurar primero el perfil, revisar proveedor/modelo/base URL sin secretos,
reiniciar despues el gateway correcto y verificar su estado:

- `hermes-gateway.service` para `default`.
- `hermes-gateway-auscultacion.service` para `auscultacion`.

No asumir que una credencial visible en `hermes auth list` esta disponible para
otro perfil.
