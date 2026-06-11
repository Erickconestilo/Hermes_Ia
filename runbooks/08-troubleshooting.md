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
