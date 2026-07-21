# 02 - Seguridad

## Objetivo

Resumir las reglas ejecutivas de seguridad del proyecto `Hermes_Ia` sin duplicar el detalle técnico ya documentado en otros runbooks.

## Principios vigentes

- no guardar secretos reales en archivos versionados
- no ejecutar cambios sensibles sin análisis previo
- no exponer servicios públicamente por defecto
- no operar Hermes como `root`
- mantener el sistema lo más simple posible en las fases iniciales

## Secretos y archivos sensibles

No deben entrar en Git:

- `.env`
- secretos reales
- claves SSH
- tokens
- backups sensibles
- logs con datos privados

## Postura actual de exposición

Actualmente no se expone:

- dashboard público
- API pública
- Telegram
- Discord
- WebUI pública

La postura por defecto sigue siendo privada y conservadora.

## Regla de cambios sensibles

Antes de cualquier cambio sensible futuro, debe evaluarse siempre:

- objetivo
- riesgo
- alternativa más segura
- rollback
- verificación

## Usuario operativo

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

- [02-usuario-hermes-seguridad.md](02-usuario-hermes-seguridad.md)

## Endurecimiento SSH (pendiente de ejecutar y verificar)

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
ssh -i $HOME/.ssh/hermes_hetzner_ed25519 hermes@<HETZNER_VPS_IP>

# 8. Solo si el paso 7 funciona, cerrar la sesión SSH original
```

Verificación adicional recomendada (no bloqueante para este runbook, evaluar por separado):

- `fail2ban` o equivalente para mitigar fuerza bruta contra el puerto SSH expuesto.
- `ufw` u otro firewall limitando el acceso al puerto SSH si el rango de IPs de origen es predecible.

Estos dos últimos puntos son cambios de sistema (instalación de paquetes, servicios) y caen en zona roja de `AGENTS.md`: requieren permiso explícito antes de ejecutarse, no solo documentarse.

Registrar en `learning/bitacora.md` la fecha de ejecución, el resultado del paso 7 y cualquier desviación.
