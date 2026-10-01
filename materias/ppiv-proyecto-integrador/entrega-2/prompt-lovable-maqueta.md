# Prompt para Lovable — Maqueta IFTS N°2

> Copiar y pegar directamente en Lovable. Pensado para generar un prototipo navegable (sitio público + panel de administración) que se pueda mostrar al cliente en la demo de validación de diseño.

---

```
Quiero que armes la maqueta de un sitio institucional para un instituto terciario de educación pública, junto con un panel de administración simple. Es un prototipo visual/navegable para mostrarle al cliente y validar diseño — no hace falta backend real ni persistencia de datos; los datos pueden estar hardcodeados o en mock data.

## Contexto del cliente

El cliente es el IFTS N°2 DE 20, un instituto de formación técnica superior de gestión pública (Ministerio de Educación, Gobierno de la Ciudad de Buenos Aires) que dicta la Tecnicatura Superior en Emprendimientos Gastronómicos. Tiene 18 años de trayectoria. Frase ancla que define su identidad, citada textualmente por la rectora: "No formamos chefs. Formamos empresarios gastronómicos." Todo el diseño debe transmitir esa idea: no es una escuela de cocina, es una institución que forma emprendedores.

El sitio actual es un Google Site sin mantenimiento hace más de un año, visualmente anticuado ("parece un colegio secundario"), que mezcla información de hasta 5 años de antigüedad sin ningún orden, no tiene panel de gestión, no integra redes sociales y no tiene formulario de contacto. El objetivo de este proyecto es reemplazarlo por algo profesional, moderno y fácil de mantener por personal SIN perfil técnico (los administradores son docentes, no programadores).

## Identidad visual

- Paleta: usar como color de marca principal el azul #24507F (institucional, serio, confiable), combinado con un fondo cálido neutro (blancos/off-white, no gris frío) y un acento cálido secundario que evoque gastronomía sin caer en cliché (evitar rojo "restaurante" genérico; preferir un tono terracota u oliva apagado como acento puntual, usado con moderación).
- Tipografía: una serif con carácter para títulos (que transmita solidez institucional) combinada con una sans-serif limpia para el cuerpo de texto y la interfaz del panel.
- Estilo general: profesional y cálido a la vez, no corporativo frío ni "colegial". Debe verse como una institución que forma empresarios, con fotografía de calidad (usar placeholders de alta calidad relacionados a gastronomía/formación/eventos institucionales).
- Nada de diseño genérico de IA: evitar gradientes morado-a-azul, evitar Inter/Space Grotesk como única tipografía, evitar tarjetas todas iguales con el mismo radio y sombra.

## Sitio público — Secciones

Diseñar como dos tipos de contenido, tratados visualmente distinto:

**Contenido "estanco" (institucional, cambia poco):**
- Página de inicio, con foco fuerte en el perfil del egresado ("formamos empresarios gastronómicos") como pieza central del mensaje.
- Plan de carrera / plan de estudios (Tecnicatura Superior en Emprendimientos Gastronómicos, 3 años, título oficial).
- Perfil del egresado.
- Autoridades / organigrama institucional (rector, asesor pedagógico, referentes).
- Correlatividades de materias.

**Contenido "dinámico" (se actualiza seguido, se archiva por fecha sin borrarse):**
- Sección de Novedades / Cartelera de eventos: mostrar tarjetas de eventos institucionales (ej. "Mateada Patria" 25 de mayo, Jornada de Gastronomía en octubre, colación, Noche de los Museos), con imagen, fecha y descripción corta. Simular que estos eventos se nutren de publicaciones de Instagram seleccionadas editorialmente (mostrar 4-6 tarjetas de ejemplo).
- Galería de imágenes/videos, organizada por año/cuatrimestre, con las más recientes arriba.
- Horarios y mesas de examen del cuatrimestre en curso (en formato de tabla o tarjetas, NO como planilla Excel incrustada), mostrando solo información vigente.
- Plantel docente: listado de docentes con la materia que dictan, editable/actualizable.

**Accesos rápidos / enlaces de interés (footer o sidebar visible):**
- SIU Guaraní (inscripción y gestión académica de alumnos).
- Aulas Virtuales (Moodle).
- Mi Argentina (verificación de título digital para egresados).
- Redes sociales institucionales: Instagram y Facebook.
- Formulario de contacto simple (nombre, email, motivo de consulta, mensaje) dirigido a una casilla institucional — hoy el instituto no tiene esto y lo pidió explícitamente.

## Panel de administración

Pensado para uso diario de 2-3 docentes sin conocimientos técnicos (hoy administran redes sociales, no un CMS). Debe sentirse tan simple como usar Instagram, no como un ERP.

Secciones del panel:
1. **Novedades/Eventos**: crear, editar y archivar eventos (título, imagen, fecha, categoría — institucional / por cuatrimestre / por cátedra — y rango de fechas de vigencia). Los eventos vencidos se archivan automáticamente, NUNCA se eliminan (mostrar un toggle o filtro "ver archivados").
2. **Selección de redes sociales**: una vista simulada donde el administrador ve publicaciones recientes de Instagram (mockeadas) y puede marcar cuáles se publican también en el sitio, simulando un flujo de "seleccionar y publicar" en 1-2 clics.
3. **Galería**: subir imágenes/videos con descripción y categoría, agrupados automáticamente por período.
4. **Horarios y mesas de examen**: editor tipo tabla/formulario simple para cargar horarios del cuatrimestre en curso, sin necesidad de subir archivos Excel.
5. **Plantel docente**: gestión simple de docentes y la materia que dictan.
6. **Usuarios administradores**: pantalla simple para ver quién tiene acceso al panel (sin límite de cantidad de administradores).

El panel debe verse claramente distinto del sitio público (un layout tipo dashboard con sidebar de navegación), pero mantener la misma identidad visual y tipografía.

## Qué NO incluir en esta maqueta

- No implementar autenticación real ni base de datos real (usar datos de ejemplo/mock).
- No incluir publicación automática desde el sitio hacia las redes sociales (el flujo es al revés: se publica en redes y se selecciona qué mostrar en el sitio).
- No incluir un simulador gastronómico ni gestión de trámites de bedelía (fuera de alcance de esta etapa).
- No usar WordPress ni ningún CMS de terceros: es una maqueta de una plataforma propia.

## Resultado esperado

Un prototipo navegable con: página de inicio, al menos 2-3 páginas de contenido estanco, la sección de novedades/cartelera con tarjetas de eventos, y el panel de administración con al menos 3 de sus 6 secciones desarrolladas visualmente (priorizar Novedades/Eventos, Selección de redes sociales y Horarios). Todo con datos de ejemplo realistas relacionados a un instituto de gastronomía (nombres de materias, eventos, docentes ficticios pero verosímiles).
```
