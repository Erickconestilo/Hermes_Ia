# 09 - Telegram Gateway

## Objetivo

Registrar como quedo activado el acceso movil a Hermes mediante Telegram, sin guardar secretos ni datos personales en Git.

## Estado validado

- Telegram Gateway esta operativo en Fase 1 como experimento controlado.
- El bot responde desde el movil.
- El gateway corre como servicio de usuario `hermes-gateway.service`.
- `systemd linger` esta habilitado para que el servicio sobreviva al cierre de SSH.
- El backend de Hermes sigue siendo `local`.
- El proveedor principal sigue siendo `openai-codex`.
- No se activo Docker.
- No se activaron MCPs, Playwright, cron ni memoria externa.

## Seguridad aplicada

- El token de Telegram se guardo en `/home/hermes/.hermes/.env`.
- El token no se copio al chat ni se versiono en Git.
- Se configuro allowlist de Telegram para limitar el uso al usuario autorizado.
- No se documenta el token ni el ID numerico del usuario.
- Cambios futuros de Telegram siguen siendo accion sensible y requieren confirmacion.

## Comandos utiles

Entrar al VPS:

```bash
ssh -i $HOME/.ssh/hermes_hetzner_ed25519 hermes@<IP_O_ALIAS_DEL_VPS>
cd /home/hermes/workspace/Hermes_Ia
source /home/hermes/.profile
```

Ver estado del gateway:

```bash
hermes gateway status
```

Reiniciar el gateway:

```bash
hermes gateway restart
```

Enviar una imagen generada al chat de Telegram:

```bash
python3 scripts/send-telegram-photo.py /ruta/a/imagen.png "caption opcional"
```

Ver logs recientes:

```bash
journalctl --user -u hermes-gateway -n 80 --no-pager
```

Seguir logs en vivo:

```bash
journalctl --user -u hermes-gateway -f
```

## Verificaciones realizadas

### Prueba 1: respuesta basica desde Telegram

Entrada desde el movil:

```text
hola
```

Respuesta observada:

```text
Hola Erick, que necesitas
```

Resultado:

- Hermes respondio rapido desde Telegram.
- El canal movil quedo validado.

### Prueba 2: lectura de contexto actualizado

Entrada desde Telegram:

```text
Lee docs/CODEX-BRIEF.md y dime en 3 lineas que cambio hoy sobre Telegram.
```

Respuesta observada:

```text
El cambio principal es de alcance y madurez: Hermes_Ia ya no se describe solo como instalacion base, sino como un sistema operativo personal de IA en evolucion gradual.
Tambien se actualiza el estado real: backend local, auth principal openai-codex, Telegram gateway ya operativo desde movil y CiudadanoInusual como sistema editorial activo.
Ademas, el brief endurece la regla operativa: toda idea debe clasificarse, se prohiben varias activaciones prematuras (cron, Kanban, Docker, perfiles, MCPs), y se fija como siguiente experimento seguro el flujo movil para CiudadanoInusual.
```

Resultado:

- Hermes leyo la documentacion actualizada.
- Ya no repitio que Telegram estaba pendiente para fases futuras.

## Matriz de capacidades

| Capacidad | Prueba | Resultado | Evidencia | Pendiente |
| --- | --- | --- | --- | --- |
| Respuesta basica | enviar `hola` desde movil | probado | respuesta rapida observada | no |
| Servicio persistente | `hermes gateway status` | probado | `User gateway service is running` | no |
| Lectura de contexto | pedir resumen de `docs/CODEX-BRIEF.md` | probado | respuesta con estado actualizado | no |
| Envio de imagen generada | `scripts/send-telegram-photo.py` | probado | `ok: true` y `message_id` | no |
| Captura Movil V1 | guardar nota desde Telegram | no probado | script creado, falta prueba real | si |
| Analisis de imagen recibida | enviar foto desde movil y pedir revision | no probado | sin evidencia todavia | si |
| Nota de voz / STT | enviar audio desde movil | no probado | sin evidencia todavia | si |
| Escritura temporal segura | crear prueba en `tmp/` | no probado | pendiente | si |
| Accion sensible con confirmacion | pedir accion roja o amarilla | no probado | pendiente | si |

No marcar una capacidad como cerrada sin evidencia concreta.

## Incidencias resueltas

### Proceso manual confundido con gateway real

Durante la configuracion inicial, `hermes gateway status` mostro un proceso activo, pero `hermes gateway list` indicaba que el gateway real no estaba corriendo.

Resolucion:

- Se arranco temporalmente `hermes gateway run` en segundo plano para validar respuesta.
- Luego se instalo el servicio de usuario con `hermes gateway install`.
- Se detuvo el proceso manual.
- Se arranco el servicio `hermes-gateway.service`.

## Estado final

El servicio quedo activo con:

```text
User gateway service is running
Systemd linger is enabled
```

El bot respondio desde el movil despues de arrancar el servicio.

## Imagenes generadas

El proveedor de imagenes se habilita mediante `FAL_KEY` en `/home/hermes/.hermes/.env`.

Regla operativa:

- si Hermes genera una imagen desde Telegram, no basta con describirla;
- debe enviar el archivo con `python3 scripts/send-telegram-photo.py <ruta-imagen> "<caption>"`;
- tambien debe devolver la ruta exacta del archivo generado;
- no debe mostrar `FAL_KEY`, `TELEGRAM_BOT_TOKEN` ni IDs privados.

## Captura Movil V1

Ruta privada prevista:

```text
/home/hermes/.hermes/data/ciudadanoinusual/capturas.jsonl
```

Comando base:

```bash
python3 scripts/captura-movil.py add --text "nota en bruto" --tags "calle,contenido" --privacy-flags "ubicacion" --suggested-format "post"
```

Reglas:

- no guardar capturas privadas en Git;
- preservar `original_text`;
- marcar riesgos de privacidad;
- devolver el `id` de captura;
- convertir a contenido solo despues de revisar.

## Limites vigentes

Telegram queda operativo solo como canal movil autorizado.

Sigue fuera de alcance:

- cambiar backend
- instalar Docker
- activar cron
- activar MCPs
- activar Playwright
- activar memoria externa
- exponer dashboard o API publica
- guardar secretos en Git
