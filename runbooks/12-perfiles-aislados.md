# 12 - Perfiles aislados

## Objetivo

Mantener separados los contextos, credenciales, datos, skills y gateways de
`default` (CiudadanoInusual) y `auscultacion` (operacion de campo).

Un perfil no hereda automaticamente la configuracion de otro. La presencia de
una credencial en `hermes auth list` no demuestra que este disponible dentro de
otro perfil.

## Estructura

El perfil base vive en `/home/hermes/.hermes/`. Cada perfil aislado vive en:

```text
/home/hermes/.hermes/profiles/<perfil>/
```

Rutas relevantes:

```text
/home/hermes/.hermes/.env                         # default
/home/hermes/.hermes/profiles/<perfil>/.env       # perfil aislado
/home/hermes/.config/systemd/user/hermes-gateway.service
/home/hermes/.config/systemd/user/hermes-gateway-<perfil>.service
```

Los archivos `.env` deben tener permisos `600`. Nunca se copia su contenido al
repositorio, al chat ni entre perfiles sin una decision explicita.

## Crear un perfil

Crear un perfil sin skills iniciales:

```bash
hermes profile create <perfil> --no-skills \
  --description "Descripcion breve del uso del perfil"
```

No combinar `--no-skills` con `--clone-from`, `--clone` o `--clone-all`.
Despues de crearlo, configurar el perfil de forma explicita:

```bash
hermes -p <perfil> setup
hermes -p <perfil> setup model
hermes -p <perfil> setup gateway
chmod 600 /home/hermes/.hermes/profiles/<perfil>/.env
```

Si el perfil necesita skills, se incorporan despues de revisar su alcance. Una
skill experimental vive en `HERMES_HOME` y no se convierte en oficial ni se
versiona sin repeticion real y aprobacion.

## Uso sistematico del perfil

Para no enviar una consulta al perfil equivocado, usar siempre `-p` en la CLI:

```bash
hermes -p default chat
hermes -p auscultacion chat
hermes -p default profile show
hermes -p auscultacion gateway status
```

Los wrappers (`hermes` y `auscultacion`) son comodidades, no sustituyen la
comprobacion del perfil activo cuando una accion pueda guardar datos o cambiar
configuracion.

## Instalar y persistir el gateway

Ejecutar la instalacion desde el perfil correcto:

```bash
hermes -p <perfil> gateway install
hermes -p <perfil> gateway start
hermes -p <perfil> gateway status
```

En el VPS se usa un servicio de usuario con `systemd` y `linger` habilitado.
Los nombres esperados son:

```text
hermes-gateway.service
hermes-gateway-auscultacion.service
```

No se debe asumir que instalar o reiniciar un gateway afecta al otro.

## Orden de configuracion y reinicio

La regla operativa es configurar primero y reiniciar despues:

1. Confirmar el perfil objetivo.
2. Cambiar solo la configuracion autorizada de ese perfil.
3. Revisar proveedor, modelo y base URL sin mostrar secretos.
4. Reiniciar el servicio correspondiente.
5. Comprobar estado y logs del mismo servicio.
6. Probar desde el canal asociado al perfil.

Comandos de reinicio y comprobacion:

```bash
hermes -p default gateway restart
hermes -p default gateway status
systemctl --user is-active hermes-gateway.service
journalctl --user -u hermes-gateway.service -n 80 --no-pager
```

```bash
hermes -p auscultacion gateway restart
hermes -p auscultacion gateway status
systemctl --user is-active hermes-gateway-auscultacion.service
journalctl --user -u hermes-gateway-auscultacion.service -n 80 --no-pager
```

Si se modificaron ambos perfiles, repetir el ciclo por separado, primero
`default` y despues `auscultacion`. Un estado activo solo confirma el proceso;
la respuesta del bot debe probarse en el canal correcto.

## Verificacion por perfil

### `default`

- `hermes profile show default` identifica el perfil base.
- Existe `/home/hermes/.hermes/.env` y su modo es `600`.
- `hermes-gateway.service` esta `active (running)`.
- El proveedor y modelo coinciden con la tabla canonica de
  `docs/CODEX-BRIEF.md`.
- Telegram responde sin publicar ni ejecutar acciones externas automaticamente.

### `auscultacion`

- `hermes profile show auscultacion` identifica la ruta aislada.
- Existe `/home/hermes/.hermes/profiles/auscultacion/.env` y su modo es `600`.
- `hermes-gateway-auscultacion.service` esta `active (running)`.
- El proveedor y modelo coinciden con la tabla canonica de
  `docs/CODEX-BRIEF.md`.
- El perfil mantiene separado su contexto tecnico y no mezcla CiudadanoInusual.

Comprobacion de permisos sin leer secretos:

```bash
stat -c '%a %n' \
  /home/hermes/.hermes/.env \
  /home/hermes/.hermes/profiles/auscultacion/.env
```

## Limites

- No cambiar `.env`, SSH, `systemd`, paquetes, cron, Docker, MCPs, Playwright o
  memoria externa sin la autorizacion correspondiente.
- No usar el gateway de un perfil para validar otro.
- No registrar tokens, claves, IDs privados, coordenadas ni datos de obra en Git.
- Un backup restaurado demuestra que los archivos existen; no demuestra que un
  servicio este activado. La activacion se verifica aparte y no forma parte de
  una restauracion de prueba.
