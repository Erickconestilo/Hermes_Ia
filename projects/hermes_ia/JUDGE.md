# JUDGE

## Proposito

Definir un juez minimo de calidad para decidir si una salida de `Hermes_Ia` merece guardarse como valida o debe mejorarse antes.

El objetivo no es crear burocracia. El objetivo es evitar guardar research flojo, contenido poco util o cambios Builder que no reduzcan friccion real.

## Criterios para Research

Una salida de `Hermes Research` debe tener:

- tema concreto
- tesis corta
- evidencia o fuentes verificables
- lectura practica
- riesgos o limites
- conclusion accionable

Debe evitar:

- resumen generico
- afirmaciones sin fuente cuando el tema requiere evidencia
- entusiasmo sin tradeoffs
- conclusion que no ayude a decidir nada

## Criterios para Content

Una salida de `Hermes Content` debe tener:

- hooks claros
- angulo reconocible para `CiudadanoInusual`
- estructura breve y usable
- cierre con utilidad real
- conexion clara con un briefing, idea o experiencia previa

Debe evitar:

- frases bonitas sin contenido
- hooks demasiado genericos
- copiar tono de terceros sin adaptacion
- piezas que no puedan evolucionar a post, guion o publicacion

## Criterios para Builder

Una salida de `Hermes Builder` debe tener:

- archivo concreto afectado
- cambio pequeno o claramente acotado
- verificacion reproducible
- reduccion real de friccion
- ausencia de cambios sensibles no aprobados

Debe evitar:

- cambios cosmeticos sin valor operativo
- nuevas plantillas sin uso inmediato
- tocar configuracion, secretos o servicios
- ampliar alcance hacia Docker, cron, Telegram, MCPs o proyectos externos sin autorizacion

## Escala simple 1-10

- 1-3: salida floja, generica o inutil
- 4-5: tiene algo aprovechable, pero no debe guardarse como valida
- 6-7: aceptable como borrador, pero necesita mejora
- 8: valida y guardable
- 9: muy buena, reutilizable y accionable
- 10: excelente, clara, verificable y con alto retorno

## Regla de calidad

Si una salida baja de 8/10, debe mejorarse antes de guardarse como valida.

Una salida puede guardarse cuando cumple dos condiciones:

- aporta valor real al uso oficial correspondiente
- deja claro como se verifica o reutiliza
