# 02 - Seguridad

## Objetivo

Resumir las reglas ejecutivas de seguridad del proyecto `Hermes_Ia` sin duplicar el detalle técnico ya documentado en otros runbooks.

## Principios vigentes

- no guardar secretos reales en archivos versionados
- no ejecutar cambios sensibles sin análisis previo
- no exponer servicios públicamente por defecto
- no operar Hermes como `root`
- mantener el sistema lo más simple posible en las fases iniciales

## Deteccion automatica de secretos (2026-07-21)

`scripts/verificar-secretos.sh` revisa lo que esta en stage antes de cada commit: claves OpenAI (`sk-...`), tokens de GitHub, tokens de bot de Telegram, claves privadas (`BEGIN ... PRIVATE KEY`), claves AWS, e IPs publicas que deberian ser `<HETZNER_VPS_IP>`. No requiere instalar `gitleaks` ni ninguna herramienta nueva: es un `grep` con patrones conocidos.

Ya esta instalado como hook (`.git/hooks/pre-commit`) y probado: bloqueo un commit real con un secreto de prueba antes de que entrara al historial.

**`.git/hooks/` no se versiona en Git.** Si clonas el repo de nuevo en otra maquina, hay que reinstalar el hook una vez:

```bash
cp scripts/verificar-secretos.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

Uso manual, sin esperar a un commit:

```bash
bash scripts/verificar-secretos.sh
```

Si el hook da un falso positivo y hace falta forzar el commit de todas formas: `git commit --no-verify`. Usarlo con cuidado, revisando antes a mano lo que se esta forzando.

## Secretos y archivos sensibles

No deben entrar en Git:

- `.env`
- secretos reales
- claves SSH
- tokens
- backups sensibles
- logs con datos privados

## Postura actual de exposición

No se exponen como servicios HTTP publicos:

- dashboard público
- API pública
- WebUI pública

Telegram si esta expuesto como canal externo de mensajeria: existen dos bots operativos, uno para `default` y otro para `auscultacion`, cada uno con su gateway y allowlist. No equivale a una API publica del VPS, pero si aumenta la superficie de entrada y debe tratarse como canal externo autorizado.

### Mitigacion parcial de exfiltracion

La mitigacion disponible esta desplegada en los scripts versionados y probada con fixtures sinteticos, no como una proteccion global del runtime de Hermes. `scripts/verificar-secretos.sh` bloquea patrones conocidos en archivos staged y redacta sus valores; los scripts de envio y captura aplican allowlists, validacion de rutas y salidas sin cuerpos privados.

Cubre: secretos reconocibles en commits, destinos no autorizados de los scripts protegidos, rutas sensibles y algunos escapes por symlink.

No cubre: cualquier comando arbitrario que Hermes pueda ejecutar desde terminal, todas las formas de ofuscacion o exfiltracion, ni un bloqueo semantico global de red. F-01 queda como mitigacion parcial aceptada; el cierre global no forma parte del alcance actual.

La postura por defecto sigue siendo privada y conservadora: Telegram esta permitido solo para los bots autorizados y no hay publicacion automatica.

### `hermes egress` / iron-proxy — alcance comprobado (2026-08-25)

La auditoría de solo lectura confirmó que `hermes egress` está desactivado en
ambos perfiles: no hay binario, configuración, CA ni proceso activo. La función
es un firewall de salida con inyección de credenciales para **sandboxes Docker**:
el sandbox recibe tokens opacos, las peticiones pasan por el proxy TLS local y
solo se reenvían a hosts permitidos.

No protege el proceso host de Hermes ni sus llamadas LLM realizadas directamente
desde el backend `local`. Tampoco cubre sockets que evitan el proxy, archivos de
credenciales montados en el sandbox ni exfiltración hacia un dominio que ya esté
permitido. Por tanto, no sustituye la mitigación parcial actual de F-01 y no
aplica al backend vigente; solo debe reevaluarse si se aprueba migrar a Docker.

Documentación oficial: [Egress proxy de Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/egress/iron-proxy).

## Regla de cambios sensibles

Antes de cualquier cambio sensible futuro, debe evaluarse siempre:

- objetivo
- riesgo
- alternativa más segura
- rollback
- verificación

## Usuario operativo

La instalación y operación habitual usan el usuario dedicado `hermes`, no
`root`. Las rutas base son `/home/hermes/.hermes` y
`/home/hermes/workspace`; los permisos y el acceso administrativo se verifican
antes de cambiar SSH, sudoers o servicios. El detalle histórico del alta queda
archivado; el estado vigente se consulta en `runbooks/01-estado-actual.md`.

La decisión vigente es operar Hermes con:

- usuario `hermes`

No con:

- `root`, salvo bootstrap, recuperación o administración puntual

## Rollback mínimo esperado

Si se propone un cambio sensible, debe quedar claro:

- qué archivo o servicio cambia
- cómo se vuelve al estado anterior
- cómo se comprueba que el rollback funcionó

## Referencia técnica relacionada

Para el detalle de la creación del usuario `hermes`, ownership y validación del entorno, ver:

- El detalle histórico del alta está en `docs/archive/02-usuario-hermes-seguridad.md`.

## Endurecimiento SSH (ejecutado y verificado el 2026-08-08)

Estado: cerrado. `PasswordAuthentication no` aplicado y verificado con una segunda sesion antes de cerrar la original. `PermitRootLogin` ya estaba en `prohibit-password` desde antes, sin cambios. Detalle completo en `learning/bitacora.md`. Los dos pasos no bloqueantes (`fail2ban`, `ufw`) siguen sin ejecutar, ver "Verificacion adicional recomendada" mas abajo.

Motivo: el repositorio es público y ha expuesto históricamente la IP del VPS en texto plano (ya corregido en `learning/bitacora.md`). Reducir superficie de ataque en el punto de entrada real.

Riesgo: alto si se ejecuta mal — puede dejar el VPS inaccesible por SSH. Ejecutar cada paso por separado y verificar antes de cerrar la sesión SSH activa. No cerrar la sesión actual hasta confirmar que una segunda conexión nueva funciona.

Rollback: mantener una sesión SSH abierta mientras se aplican los cambios; si algo falla, revertir `/etc/ssh/sshd_config` desde la copia hecha en el paso 1 y `systemctl restart ssh`.

Pasos, como usuario con `sudo` (no como `hermes`, no como `root` salvo bootstrap):

```bash
# 1. Copia de seguridad de la configuración actual
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak-$(date +%Y%m%d)

# 2. Verificar estado actual antes de cambiar nada
sudo sshd -T | grep -Ei "permitrootlogin|passwordauthentication|port"

# 3. Confirmar que existe login por clave para el usuario habitual
#    (no continuar si esto falla)
grep -c "ssh-" ~/.ssh/authorized_keys

# 4. Editar /etc/ssh/sshd_config y fijar:
#    PermitRootLogin prohibit-password
#    PasswordAuthentication no
#    (dejar el puerto 22 salvo que ya se use otro por decisión explícita)

# 5. Validar sintaxis antes de reiniciar
sudo sshd -t

# 6. Reiniciar el servicio
sudo systemctl restart ssh

# 7. VERIFICACION OBLIGATORIA: abrir una terminal nueva (sin cerrar la actual)
#    y confirmar que la conexión por clave sigue funcionando:
ssh hermes

# 8. Solo si el paso 7 funciona, cerrar la sesión SSH original
```

Si el alias `hermes` de `~/.ssh/config` no estuviera disponible, la forma larga equivalente es `ssh -i $HOME/.ssh/hermes_hetzner_ed25519 hermes@<HETZNER_VPS_IP>`.

Verificación adicional recomendada (no bloqueante para este runbook, evaluar por separado):

- `fail2ban` o equivalente para mitigar fuerza bruta contra el puerto SSH expuesto.
- `ufw` u otro firewall limitando el acceso al puerto SSH si el rango de IPs de origen es predecible.

Estos dos últimos puntos son cambios de sistema (instalación de paquetes, servicios) y caen en zona roja de `AGENTS.md`: requieren permiso explícito antes de ejecutarse, no solo documentarse.

Registrar en `learning/bitacora.md` la fecha de ejecución, el resultado del paso 7 y cualquier desviación.
