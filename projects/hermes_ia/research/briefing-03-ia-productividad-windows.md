# Briefing Hermes Research 03

## Tema

IA practica para productividad personal en Windows: copilotos dentro del flujo de trabajo, no automatizacion total.

## Tesis corta

La forma mas util de usar IA en Windows no es hablar con un chatbot sin mas, sino usar copilotos dentro del flujo de trabajo para resumir, redactar, buscar archivos, explicar pantallas y acelerar decisiones rutinarias. El valor aparece cuando la IA reduce friccion real en tareas pequenas y frecuentes; el riesgo aparece cuando se la trata como fuente de verdad o se le da acceso a datos sensibles sin control.

## Evidencia / fuentes

- Microsoft Support indica que Copilot en Windows suele venir instalado en nuevos equipos con Windows 11, se puede abrir desde la barra de tareas o el menu Inicio, y da acceso a historial, voz, captura de pantalla, busqueda de archivos y ayuda con configuraciones de Windows.
  - https://support.microsoft.com/en-us/topic/getting-started-with-copilot-on-windows-1159c61f-86c3-4755-bf83-7fbff7e0982d
- Microsoft 365 Copilot se posiciona como asistente conectado a Word, Excel, PowerPoint, Outlook, OneDrive y Teams. La promesa central es ahorrar tiempo en redaccion, resumen, analisis, busqueda y colaboracion dentro del flujo de trabajo.
  - https://www.microsoft.com/en-us/microsoft-365-copilot/enterprise
- Microsoft Learn describe que Power Automate Desktop permite automatizar procesos repetitivos de escritorio, con arrastrar y soltar o grabacion de flujos, y que sirve para tareas sobre apps modernas, legadas, Excel, carpetas y web.
  - https://learn.microsoft.com/en-us/power-automate/desktop-flows/introduction
  - https://learn.microsoft.com/en-us/power-automate/desktop-flows/automation-web
- Microsoft Support muestra usos concretos de Copilot en Word: reescritura, resumen y conversion de texto en tabla, disponibles en Windows.
  - https://support.microsoft.com/en-us/office/rewrite-text-with-copilot-in-word-923d9763-f896-4da7-8a3f-5b12c3bfc475
- Microsoft tambien enmarca Copilot como asistente y a los agentes como herramientas especializadas para tareas concretas; eso refuerza que el mejor uso practico es separar ayuda general de automatizacion especifica.
  - https://www.microsoft.com/en-us/microsoft-copilot/copilot-101/copilot-ai-agents
- El estudio "Generative AI at Work" observo un aumento medio de productividad del 15% en 5.172 agentes de soporte, con mayor beneficio en trabajadores menos experimentados. Es evidencia fuerte, pero limitada a un contexto concreto de soporte.
  - https://arxiv.org/abs/2304.11771
- El perfil de IA generativa del NIST AI Risk Management Framework refuerza que la adopcion debe medirse, limitarse y gobernarse, especialmente cuando hay datos sensibles o decisiones importantes.
  - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- En privacidad, Microsoft distingue entre Copilot consumer y Microsoft 365 Copilot; para Microsoft 365 Copilot senala que prompts, respuestas y datos de Graph no se usan para entrenar modelos base, mientras que en Copilot consumer las conversaciones se guardan por defecto y el usuario debe revisar bien la informacion antes de decidir.
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy
  - https://support.microsoft.com/en-us/topic/privacy-faq-for-microsoft-copilot-27b3a435-8dc9-4b55-9a4b-58eeb9647a7f

## Lectura practica

La lectura util para alguien que trabaja en Windows es esta:

1. Para tareas de pensamiento y redaccion:
   - resumir textos largos
   - reescribir correos o documentos
   - convertir notas sueltas en borradores utiles
2. Para tareas de contexto:
   - encontrar archivos
   - revisar capturas de pantalla
   - pedir ayuda sobre ajustes del sistema
3. Para tareas repetitivas:
   - mover datos entre apps
   - copiar y pegar informacion de formularios
   - ordenar documentos o extraer datos de web o Excel

La pauta practica es no mezclar todo en un solo uso. Copilot sirve para acelerar el trabajo intelectual; Power Automate sirve para eliminar pasos mecanicos. Juntos, cubren el grueso de la productividad personal real en Windows.

El punto importante es separar dos usos:

- Copilot para primer borrador, primera busqueda y ayuda contextual.
- Automatizacion ligera para tareas mecanicas que se repiten.

No conviene convertir una ayuda puntual en habito pagado o automatizacion permanente si no demuestra ahorro real en 2 o 3 usos.

## Primer piloto recomendado

Automatizar o asistir una sola tarea diaria en Windows:

- resumir un documento largo
- ordenar una carpeta de descargas
- convertir notas sueltas en borrador
- preparar una respuesta de correo
- extraer datos repetitivos de una web o Excel

Elegir solo una y medirla durante 2 semanas.

## Riesgos

- privacidad y exposicion de datos: no conviene pegar informacion sensible sin revisar que cuenta, que producto y que politica se esta usando
- alucinaciones o errores de reescritura: la IA puede sonar convincente y aun asi equivocarse
- falsa productividad: ganar velocidad escribiendo no compensa si luego toca rehacer por falta de precision
- dependencia del ecosistema Microsoft: muchas ventajas aparecen solo dentro de Windows/Microsoft 365
- automatizacion fragil: los flujos de escritorio pueden romperse si cambia una interfaz, una ventana o un selector
- permisos de archivos: la busqueda contextual depende de permisos; activarla sin pensar puede ampliar la superficie de exposicion
- expectativas infladas: la evidencia fuerte viene de casos concretos, no de una mejora universal para todo usuario y toda tarea

## Conclusion accionable

Si quieres usar IA de forma practica en Windows, empieza con tres usos concretos y medibles:

- resumen de correos o documentos
- busqueda de archivos
- ayuda contextual sobre pantallas o ajustes

Elige uno, no los tres a la vez. Prueba durante 2 semanas una unica tarea diaria y mide:

- tiempo ahorrado
- errores introducidos
- necesidad de correccion manual

Si no mejora claramente esos tres puntos, se descarta o se simplifica. Si si mejora, entonces tiene sentido integrarlo como habito auxiliar, con una norma fija: no confiar en la IA para datos sensibles o decisiones importantes sin verificacion.
