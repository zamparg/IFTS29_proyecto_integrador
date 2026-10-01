# Entrega 1 — Propuesta de Contenido y Estructura

> Organiza los 5 puntos básicos de la primera entrega según lo exigido en `PROYECTO INTEGRADOR IFTS 2 2026.docx` (secciones "Relevamiento y Análisis" y "Gestión del Proyecto"). Usa como insumo `context.md`, `propuesta-para-cliente.md` y `agente-gestion-proyecto.md`.

---

## Punto 1 — Documento de Relevamiento y Análisis

Estructura exigida por la cátedra, con contenido ya disponible para completar cada sección:

### 1.1 Introducción
- Presentar al cliente (IFTS N°2), la modalidad del proyecto (Software Factory, PP4 de IFTS N°29) y el objetivo general: modernización del sitio institucional + integración editorial con redes sociales.

### 1.2 Alcance
**Incluido en esta primera etapa:**
- Sitio público institucional renovado (identidad visual, secciones estancas y dinámicas).
- Panel de administración para carga de contenido (novedades, horarios, galería, plantel docente).
- Mecanismo de selección de publicaciones de redes sociales para mostrar en el sitio.
- Accesos directos a SIU Guaraní, Aulas Virtuales, Mi Argentina.
- Formulario de contacto.

**Fuera de alcance (esta etapa):**
- Publicación automática *desde* el sitio *hacia* redes sociales (se definió que el flujo es: cargar en redes → seleccionar/etiquetar → aparece en sitio, no al revés).
- Simulador gastronómico (mencionado como idea a futuro por el cliente, sin definición).
- Gestión documental completa de trámites de bedelía/certificados (solo formulario de contacto en esta etapa).
- Dominio propio definitivo y CMS de terceros tipo WordPress (decisión ya tomada: desarrollo propio).

### 1.3 Objetivos
Tomar directamente los OKR/KR definidos en `propuesta-para-cliente.md` sección 3, y los objetivos generales/específicos de `PROYECTO INTEGRADOR IFTS 2 2026.docx`.

### 1.4 Glosario
| Término | Definición |
|---|---|
| Contenido estanco | Información institucional que cambia con poca frecuencia (plan de carrera, autoridades, perfil del egresado) |
| Contenido dinámico | Información que se actualiza regularmente y se archiva por vencimiento (horarios, novedades, mesas de examen) |
| Panel de administración / Backoffice | Interfaz privada donde el cliente carga y edita contenido sin tocar código |
| Selección editorial | Criterio humano para decidir qué contenido de redes sociales se refleja en el sitio |
| Software Factory | Modalidad de la cátedra donde cada equipo actúa como una empresa de desarrollo independiente |
| OKR | Objectives & Key Results, marco de definición de objetivos medibles |
| KPI | Key Performance Indicator, métrica de seguimiento continuo |

### 1.5 Actores involucrados
Tabla completa ya disponible en `agente-gestion-proyecto.md`, sección 3 ("Actores"). Incluir también: administradores de contenido (Matías, María), usuarios finales (público general, alumnos, egresados).

### 1.6 Requerimientos funcionales
Extraídos y numerados desde `context.md`, sección 3:
1. RF01 — El sistema debe permitir administrar contenido del sitio desde un panel sin necesidad de conocimientos técnicos.
2. RF02 — El sistema debe distinguir contenido estanco de contenido dinámico.
3. RF03 — El sistema debe permitir archivar automáticamente contenido dinámico vencido por fecha, sin eliminarlo.
4. RF04 — El sistema debe permitir vincular publicaciones de Instagram/Facebook al sitio mediante selección/etiquetado editorial.
5. RF05 — El sistema debe soportar múltiples usuarios administradores sin límite relevante.
6. RF06 — El sistema debe mostrar horarios y mesas de examen del cuatrimestre/año académico vigente únicamente.
7. RF07 — El sistema debe incluir accesos directos a SIU Guaraní, Aulas Virtuales y Mi Argentina.
8. RF08 — El sistema debe incluir un formulario de contacto dirigido a un correo institucional.
9. RF09 — El sistema debe permitir gestionar galería de imágenes/videos con descripción y categoría.
10. RF10 — El sistema debe permitir gestionar plantel docente y materias con su docente a cargo, de forma actualizable.

### 1.7 Requerimientos no funcionales
1. RNF01 — Usabilidad: la interfaz de administración debe ser utilizable por personal no técnico sin capacitación extensa.
2. RNF02 — Costo: la solución debe operar preferentemente sobre infraestructura gratuita o de costo mínimo.
3. RNF03 — Disponibilidad: el sitio público debe estar accesible en internet de forma estable.
4. RNF04 — Responsive: el sitio debe visualizarse correctamente en dispositivos móviles y de escritorio.
5. RNF05 — Rendimiento: tiempos de carga aceptables pese al volumen alto de imágenes/videos históricos.
6. RNF06 — Seguridad: acceso al panel de administración restringido por autenticación.

### 1.8 Restricciones
- Presupuesto casi nulo (fondos limitados a caja chica, no destinable a servicios pagos).
- Perfil no técnico de los usuarios administradores.
- Dependencia de materiales de marca (colores, tipografía, logo) que el cliente debe proveer vía Drive.
- Coexistencia con 2 equipos más trabajando en paralelo sobre el mismo cliente.
- Cronograma fijo de la cátedra (16 semanas, hitos en semana 2, 6 y 13).

### 1.9 Supuestos
- El cliente proveerá acceso a la carpeta de materiales de marca antes de la demo de Semana 6.
- Matías y María seguirán siendo los referentes operativos de contenido durante todo el proyecto.
- El volumen de imágenes actual (histórico desde 2021) puede ser filtrado/reducido en la migración inicial sin objeción del cliente.
- El dominio .edu.ar es una opción viable a mediano plazo; en el corto plazo se puede operar sobre un subdominio o dominio provisorio gratuito.

---

## Punto 2 — Plan de Proyecto

- **Objetivos**: ver `propuesta-para-cliente.md`, sección 3.
- **Alcance**: ver punto 1.2 de este documento.
- **Entregables**: los 8 listados en `agente-gestion-proyecto.md`, sección 3.
- **Cronograma**: cronograma marco de la cátedra (semana 2/6/13) + cronograma interno del equipo a definir en la herramienta de gestión elegida.
- **Recursos**: equipo de hasta 5 integrantes, herramientas de gestión (Trello/Jira/GitHub Projects/Notion/ClickUp — a definir en sesión técnica), entornos de desarrollo, Meet/Discord para comunicación con cliente y cátedra.
- **Riesgos y mitigación**: tabla completa disponible en `agente-gestion-proyecto.md`, sección 5.

---

## Punto 3 — Evidencia de gestión ágil (a preparar en la herramienta elegida)
- Backlog inicial derivado de los requerimientos funcionales (RF01–RF10) de este documento.
- Primer Sprint Planning con foco en: setup del proyecto, wireframes/prototipo de diseño, definición de arquitectura (para preparar la DEMO de semana 6).
- Tablero visible con asignación de tareas por integrante.

*(Nota: la elección de la herramienta específica y el detalle de sprints se define en la sesión técnica, no en este documento de gestión.)*

---

## Punto 4 — Comunicación con el cliente (resumen a enviar)
Usar `propuesta-para-cliente.md` como base del documento/mail a compartir con el IFTS N°2, ajustando tono si se envía formalmente (revisar Manual de Estilo del GCABA disponible en `referencias/Manual de Estilo del GCABA - Normas de redaccion de documentos oficiales.pdf` si la comunicación es escrita y formal).

## Punto 5 — Checklist de cierre de Entrega 1
- [ ] Documento de Relevamiento y Análisis completo (punto 1).
- [ ] Plan de Proyecto completo (punto 2).
- [ ] Backlog y evidencia ágil inicial cargada en la herramienta elegida (punto 3).
- [ ] Resumen/propuesta enviado o presentado al cliente (punto 4).
- [ ] Bitácora de reuniones actualizada (incluir minuta 30/06 y reunión de relevamiento 04/09/2026).
