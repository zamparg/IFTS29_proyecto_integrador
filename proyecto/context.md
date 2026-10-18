# Context.md — Cliente: IFTS N°2 DE 20 (Tecnicatura Superior en Emprendimientos Gastronómicos)

> Documento de contexto consolidado. Fuentes: sitio web actual del cliente (scraping), transcripción de la reunión de relevamiento (04/09/2026), notas propias, minuta de reunión 30/06 y documento "PROYECTO INTEGRADOR IFTS 2 2026" (cátedra).

---

## 1. Quién es el cliente

- **Institución**: Instituto de Formación Técnica Superior N° 2 DE 20 (IFTS N°2), gestión pública, dependiente del **Ministerio de Educación del Gobierno de la Ciudad de Buenos Aires (GCABA)**.
- **Carrera que dicta**: Tecnicatura Superior en Emprendimientos Gastronómicos.
  - Duración: 3 años / 2758 horas cátedra.
  - Título: Técnico/a Superior en Emprendimientos Gastronómicos, oficial y de alcance nacional.
  - Requisito de ingreso: secundario completo.
  - Cursada presencial, lunes a viernes de 18:00 a 22:00 hs.
  - Sede: Cañada de Gómez 3850, Villa Lugano, CABA.
  - Antigüedad: 18 años formando "emprendedores gastronómicos".
- **Perfil del egresado (frase ancla del cliente, citada textualmente en la reunión)**:
  > "Nosotros no formamos chefs. Formamos empresarios/microempresarios gastronómicos."
  - Esta idea fue señalada explícitamente por la rectora como **lo que sí o sí debe destacarse** en el proyecto.

### Relación entre instituciones (importante para no confundir roles)
- El **IFTS N°2** es el **cliente** (dueño del sitio, quien recibe la solución).
- Nosotros somos alumnos del **IFTS N°29** (Tecnicatura Superior en Desarrollo de Software), cursando Prácticas Profesionalizantes IV.
- La cátedra armó **3 grupos de desarrollo** que trabajan en paralelo como si fueran "software factories" independientes compitiendo/ofertando sobre el mismo proyecto (modalidad tipo licitación interna).
- Referentes del lado del cliente:
  - **Cecilia** — Rectora del IFTS N°2.
  - **Gabriel (Hector S. en la transcripción)** — Asesor pedagógico del IFTS N°2.
  - **Matías Peláez** y **María del Carmen Canobi** — Docentes de gastronomía, **administradores/editores de contenido reales**: son quienes manejan hoy Instagram y Facebook institucional y serán quienes carguen datos en la futura plataforma.
  - **Mónica** — Asesora que gestiona la carpeta Drive con materiales de marca (mencionada varias veces, sin acceso directo confirmado en la reunión; se gestionó el acceso a cierre de la llamada).
- Referentes del lado de la cátedra/facultad: Emir García Ontiveros y Kevin Del Bello (docentes responsables Desarrollo de Software).
- **Javier N. (Javier Navarro)** pertenece a **otro de los 3 grupos de desarrollo** de IFTS 29 (competidor/par, no es del cliente ni de Talento Tech). En la reunión de relevamiento del 04/09/2026 inició la grabación y consultó al instituto por costos. Nuestro canal único con el cliente es el Product Owner, **Martín Juan** (Etapa 1 y Gestión de Proyectos Parte 1).

---

## 2. Estado actual del sitio (diagnóstico técnico y de contenido)

Sitio actual: **Google Sites** → https://sites.google.com/bue.edu.ar/ifts-2-de-20/

### Estructura relevada (scraping)
Menú de navegación actual:
- Página principal
- Docentes
- Alumnos
- Ingreso 2025
- Información Académica
- Tutoría
- ¿Dónde estamos?
- Galería de imágenes
- Redes sociales

### Problemas identificados
1. **Visual/UX anticuado**: estética "institucional escolar", sin banner/hero, tipografía básica, sin jerarquía visual moderna. En palabras del interlocutor del cliente: *"hace un año que está ahí inmóvil"*; en palabras del equipo: *"parece un colegio secundario"*.
2. **Contenido desactualizado y sin curaduría temporal**: la sección Alumnos mezcla horarios y mesas de examen de **2021, 2022, 2023, 2024, 2025 y 2026** todos visibles a la vez, sin archivado. El cliente confirmó en la reunión que **lo antiguo se puede borrar directamente**; solo debe quedar visible lo del año académico en curso (y a futuro, próximas fechas, ej. exámenes de febrero 2027).
3. **Datos en formatos poco gestionables**: horarios y mesas de examen están como **archivos Excel/PDF incrustados**, no como datos estructurados editables desde una interfaz.
4. **Sin gestión centralizada de redes sociales**: Instagram y Facebook se administran aparte; hoy Instagram replica a Facebook, pero nada de esto se refleja en el sitio. No hay automatización ni selección editorial de qué mostrar en la web.
5. **Sin formulario de contacto**: las consultas de alumnos (mesas de examen, certificados, etc.) hoy recaen informalmente sobre una sola persona.
6. **Sin gestión de administradores**: nadie está manejando el Google Site actualmente ("se abandonó por falta de tiempo/personal"); no hay un panel de administración, cualquier cambio requiere edición manual del Site.
7. **Dominio**: sitio bajo `sites.google.com`, no tiene dominio propio.

### Datos de contacto (vigentes, tomados del sitio)
- Teléfono: 4638-5656
- Correo institucional: dfts_ifts2_de20@bue.edu.ar
- Oficina de Alumnos / Bedelía: bedelia.ifts2@gmail.com
- Jefatura de Trabajos Prácticos: ayudantiaiftsn2@gmail.com
- Dirección: Cañada de Gómez 3850, Villa Lugano, CABA

### Redes sociales activas
- Instagram: https://www.instagram.com/ifts_2_ok/ (la más activa, usada como fuente primaria de contenido)
- Facebook: https://www.facebook.com/iftsn2/ (replica automáticamente lo que se sube en Instagram)
- Mención de un LinkedIn y un TikTok pasados, sin gestión activa confirmada.

### Enlaces externos que el cliente pidió vincular desde la web (documento "Páginas a vincular")
- **Aulas virtuales (Moodle)**: https://aulasvirtuales.bue.edu.ar/
- **SIU Guaraní – acceso Alumnos**: para inscripción a la Tecnicatura y consulta de historia académica.
- **SIU Guaraní – Gestión Académica** (acceso Profesores/Secretaría): https://guarani-gestionagencia.bue.edu.ar/
- **Mi Argentina**: para que los egresados verifiquen su Título Digital emitido por GCABA (sistema SITED).
- Redes sociales institucionales (IG/Facebook, ver arriba).

---

## 3. Qué pidió el cliente (síntesis de la reunión de relevamiento, 04/09/2026)

### Pedido explícito, no es un desarrollo de software desde cero de un sistema nuevo
> "La idea no era un desarrollo de software, sino que ustedes puedan trabajar con nuestra página oficial y modernizarla."

Objetivo central: **modernizar/renovar el sitio institucional** y que pueda **nuclear las redes sociales**, de forma que una sola publicación pueda impactar en todos los canales sin cargar contenido por separado en cada lugar.

### Requerimientos funcionales relevados
1. **Modernización visual completa** del sitio (identidad más profesional, acorde a "formar empresarios", no "colegio secundario").
2. **Integración selectiva con redes sociales**:
   - No todo lo que se publica en Instagram/Facebook debe aparecer en la web.
   - El **criterio de selección es editorial y humano**: el cliente decide qué es relevante institucionalmente (ej. "Mateada Patria" del 25 de mayo, cierre de cuatrimestre, colación, Jornada de Gastronomía en octubre, Noche de los Museos, eventos de Práctica Profesional II) vs. contenido interno menor (ej. "Día de la Secretaria") que no amerita estar en el sitio.
   - Mecanismo propuesto y validado en la reunión: **etiquetado por hashtag** en la publicación de Instagram + selección manual de qué se vincula al sitio, con posibilidad de fijar **rango de fechas** de vigencia (mostrar/ocultar, nunca borrar automáticamente — el cliente fue explícito en que el borrado automático es "un riesgo grave").
3. **Panel de administración (backoffice)**:
   - Multi-administrador (Matías Peláez y María del Carmen Canobi cargan contenido; puede haber más).
   - Gestión de: plantel docente, docentes a cargo de cada materia, planes de estudio, novedades/eventos, galería de imágenes y videos (con descripción y categoría).
   - Formato dinámico (tablas/tarjetas) en lugar de Excel incrustado para horarios y mesas de examen.
   - Posibilidad de reordenar secciones del panel.
4. **Sección de Novedades / Cartelera de eventos**:
   - Debe permitir clasificar eventos (institucionales, cuatrimestrales, por cátedra).
   - Mostrar contenido reciente arriba, archivar automáticamente lo vencido por antigüedad/fecha (sin eliminar datos).
   - Alimentada parcialmente desde redes sociales (selección editorial).
5. **Distinción entre información "estanca" y "dinámica"**:
   - **Estanca** (cambia poco, casi institucional/regulatoria): plan de carrera, perfil del egresado, correlatividades, autoridades/organigrama (con posibilidad de actualizar cuando cambian personas).
   - **Dinámica** (dada de baja o archivada con el tiempo): horarios del cuatrimestre en curso, mesas de examen vigentes, novedades, eventos, galería.
6. **Alcance de "solo año en curso"**: horarios y mesas de examen deben mostrar únicamente el cuatrimestre/año académico vigente; lo anterior se puede eliminar sin problema (ya validado por el cliente).
7. **Enlaces de interés / accesos directos** para alumnos y graduados:
   - SIU Guaraní (inscripción y gestión académica)
   - Aulas virtuales (Moodle)
   - Mi Argentina (verificación de título digital)
8. **Formulario de contacto**, dirigido a un correo/bedelía, para consultas frecuentes (fechas de examen, certificados, etc.) — hoy no existe.
9. **Multiplicidad de administradores**: el cliente aclaró que no hay límite relevante en la cantidad de personas con acceso de administración ("podemos tener la cantidad de administradores que sea necesario, eso no es limitante" — respuesta del equipo, validada por el cliente).
10. **Usuarios finales de la plataforma**: público general y futuros interesados en la tecicatura (no es una intranet solo para alumnos ya inscriptos). Quien carga contenido: Matías y María (equipo de comunicación/redes del IFTS N°2).

### Restricciones y datos duros a tener en cuenta
- **Presupuesto acotado**: el instituto no puede afrontar costos relevantes. Fondos disponibles (caja chica) se destinan a materia prima para prácticas de los alumnos, no a servicios digitales. Se evaluarán primero opciones **gratuitas** (hosting, dominio) y recién si no alcanzan, costos mínimos (ej. dominio .com.ar ronda $8.500 ARS/año, mencionado en la reunión). Como institución educativa pueden aspirar a dominio **.edu.ar**, potencialmente gratuito pero requiere documentación de respaldo (a gestionar con la supervisión del GCABA).
- **Volumen de imágenes/videos**: alto (hay historial extenso en Instagram desde ~2021). Puede exceder límites de planes gratuitos de hosting/almacenamiento; a evaluar con el cliente cuántas fotos por álbum/slide son razonables.
- **Sin backup automático de borrado**: cualquier mecanismo de "vencimiento" de contenido debe ocultar/archivar, nunca eliminar datos de forma irreversible.
- **Capacidad digital limitada del cliente**: perfil de usuarios administradores no técnico (docentes, no personal de sistemas), la plataforma debe ser **simple e intuitiva**.
- **Decisión cerrada: desarrollo a medida; la cátedra dijo NO a WordPress/CMS genérico** (ver `proyecto/decisiones.md`, D-001), porque el objetivo pedagógico de la carrera es que el equipo desarrolle su propia plataforma (Software Factory), no integrar un CMS de terceros.

### Materiales que el cliente se comprometió a compartir (pendientes de confirmación de acceso completo)
- Carpeta Drive institucional con: plan de estudios, flyer de la tecnicatura (identidad visual: colores/tipografía provistos por la Agencia de Habilidades), materiales de marca.
- Reglamento de los IFTS.
- Documentación para trámite de dominio .edu.ar (a confirmar si la tiene el instituto o hay que gestionarla vía supervisión).

### Ideas "a futuro" mencionadas, fuera de alcance de esta primera etapa
- Simulador gastronómico (en conversación con el "centro de simulación" del GCABA, en etapa muy inicial).
- Vinculación con áreas de Bedelía/Jefatura de Trabajos Prácticos vía formularios específicos.

---

## 4. Cronograma marco del proyecto (fijado por la cátedra)

| Hito | Semana | Contenido |
|---|---|---|
| Reunión 1 con cliente | Semana 2 | Relevamiento inicial de necesidades y toma de requerimientos (**ya realizada**, 04/09/2026) |
| Reunión 2 con cliente | Semana 6 | Presentación de diseño, prototipos y alcance definitivo (DEMO) |
| Reunión 3 con cliente | Semana 13 | Presentación de versión funcional del sistema |

Duración total de la práctica: 16 clases de 9 hs semanales (2° cuatrimestre 2026). Equipos de hasta 5 integrantes, funcionando como "empresa de desarrollo de software" independiente, con libertad de stack tecnológico (a justificar documentalmente).

---

## 5. Prototipo en Figma (MVP) — versión vigente, 18/10/2026
**Por qué cambió:** en una reunión reciente con el cliente (segunda reunión; fecha `[completar]`) no les gustó la paleta verde y quedaron en darnos correcciones adicionales. El equipo rediseñó todo el Figma. La Etapa 2 ya se entregó con la versión verde y **no se reentrega**: el trabajo avanza hacia la Etapa 3.

**Tokens (Color styles, leídos con `get_variable_defs`):** primary `#8D775F` · base `#F6F6F3` · accent `#6F5142` · accent-2 `#E0DFD5` · accent-3 `#291711` · font `#6E7271` · success-text `#556B3F` / back `#E8EDE4` · warning-text `#B77A3A` / back `#F7E9D6` · danger-text `#7A3A32` / back `#F3DCDC`. Tipografía Inter. Fotografías reales de cocina e instituto en hero y tarjetas. Pie oscuro (accent-3).

**Sitio público (escritorio, 6):** 01 Inicio, 02 Institucional (sede, formación integral, instalaciones de práctica, cuerpo docente y bedelía, enlaces a plan de estudios e ingreso), 03 La carrera, 04 Estudiantes (horarios y exámenes con selector de ciclo, "Vida en la cocina", accesos SIU/Aula virtual/Tutoría), 05 Ingreso, 06 Novedades (filtros año y categoría). Barra superior institucional como componente.

**Panel "Panel de Gestión Académica" (escritorio, 7):**
- **13 Login:** correo institucional @bue.edu.ar, contraseña, "recordar sesión", "¿olvidaste tu clave?"; acceso restringido a personal directivo y administrativo.
- **07 Resumen (Panel de control):** estado de "Instagram API: Sincronizada (clic para sincronizar)"; tarjetas Redes sociales (3 posts por moderar), Avisos activos / Cartelera (4; 1 próximo a vencer en 7 días), Período vigente (2.º cuatrimestre; turno extraordinario de mesas en diciembre), Ingreso (inscripción ciclo 2027); lista de publicaciones de redes por moderar (ej. "Jornada gastronómica en sede Lugano", "Feliz Día del Trabajador Gastronómico"); cartelera institucional activa con adjuntos (cronograma_mesas.pdf) y etiquetas En línea / Urgente.
- **08 Publicaciones:** publicaciones de Instagram con filtros de origen y estado; modal para moderar (elegir si se muestra, sección y vigencia), confirmar publicación o descartar.
- **09 Avisos académicos:** cartelera oficial con destinatario (toda la comunidad…), estado, categoría (Mesas de examen, Urgente / Documentación), vigencia ("Vigente hasta…"), adjunto PDF; acciones Pausar y Editar; modal "Publicar nuevo aviso"; los avisos activos se sincronizan de inmediato con la pantalla de estudiantes.
- **10 Horarios:** cargar nueva grilla por comisión (A y B, Comisión Única, Prácticas Finales) subiendo archivo; configurar/editar llamado a examen; cambiar ciclo lectivo público; confirmaciones.
- **11 Archivo:** repositorio documental histórico: tabla con documento, categoría, ciclo lectivo, fecha de archivo, peso y acciones Ver detalle / Restaurar; búsqueda por título, código de resolución o año; filtros de tipo y ciclo; "Archivar nuevo documento".
- **12 Configuración:** período académico (año lectivo, cuatrimestre visible, inscripciones a mesas SIU habilitadas), datos institucionales (dirección, correo de bedelía, teléfono), administradores del sistema por rol (Rectoría/Dirección: acceso total; Bedelía Académica: horarios y cartelera) y modal "Administrar usuarios y roles".
- ~25 modales de edición y confirmación asociados.

**Móvil:** 7 pantallas (inicio, institucional, carrera, estudiantes, ingreso, novedades, login). El panel no tiene versión móvil en esta versión.

**Cambios de alcance que implica el Figma (a reflejar en las specs de Etapa 3):**
- Los horarios y las mesas se **cargan como archivos/grilla adjunta** por comisión y llamado, no solo como tablas estructuradas; las mesas de examen se gestionan como "llamados".
- Aparece un **repositorio documental** (archivo) con restauración, y **avisos académicos** con destinatario, adjuntos, pausa y vencimiento.
- La **configuración global** define el período visible en el sitio público.
- Roles concretos: Rectoría/Dirección (superadmin) y Bedelía Académica. No se ven todavía: formulario de Contacto, Galería ni Plantel docente.
- La integración con Instagram se muestra con estado de sincronización y botón de sincronizar; sigue "sujeta a validación técnica".
- Datos de ejemplo del Figma a reemplazar: correo `ifts2@bue.edu.ar` y teléfono `(011) 4601-2345` no coinciden con los datos reales del cliente (dfts_ifts2_de20@bue.edu.ar, 4638-5656).

## 5b. Consigna de la Etapa 3 de PPIV (Desarrollo completo)
- Aplicación funcional coherente con requerimientos, diagramas y prototipos; base de datos operativa; **CRUD completo con confirmación antes de eliminar**, sin duplicados y con campos obligatorios validados.
- Documentación: **Manual Técnico** (arquitectura, estructura, DER, instalación, componentes, errores, pruebas) y **Manual de Usuario** (flujos, capturas, mensajes), más sección de instalación que permita a un docente ejecutar el proyecto.
- Pruebas: 2 o 3 unitarias y 1 o 2 de integración, documentadas (qué se probó, esperado, obtenido, evidencias).
- Entrega: repositorio Git, .zip, PDF único, scripts de base, ejecutable o enlace desplegado. La defensa final se graba (consigna general).
- Texto completo: `materias/ppiv-proyecto-integrador/consigna/Etapa 3 - Desarrollo completo.txt`. Plan de trabajo: `materias/ppiv-proyecto-integrador/entrega-3/`.

## 5c. Orientación de actividades de PPIV (aula virtual, copiada el 18/10/2026)
Archivo: `materias/ppiv-proyecto-integrador/material/Orientacion_de_Actividades_Proyecto_Integrador.pdf`. Etapas del aula: empresa → análisis y relevamiento → **modelado, casos de uso e historias de usuario** → metodología y stack → estructura base (repo inicial, conexión a base, primer módulo) → **desarrollo iterativo** → ITIL 4 → coloquio final.
- **Historias de usuario:** formato "Como [tipo de usuario], quiero [acción] para [objetivo]"; mínimo 5, recomendado 8 a 12; priorizadas en alta, media y baja.
- **Desarrollo iterativo (lo que el aula llama segunda entrega del proyecto):** al menos **dos módulos funcionales**; control de versiones con ramas por funcionalidad y commits significativos; pruebas funcionales iniciales con registro de errores; **portfolio grupal en el Campus Virtual** (capturas, explicaciones técnicas, enlaces al repo, decisiones, dificultades, tareas completadas y pendientes, **horas trabajadas por integrante** para el presupuesto final); **video de avance** con cámara encendida donde cada integrante explica su trabajo.
- **ITIL 4:** actividades de análisis (cuatro dimensiones, cadena de valor, incidentes y problemas, mejora continua); productos: informes breves, casos, mapas conceptuales, presentaciones. Material en `materias/ppiv-proyecto-integrador/material/`.
- **Decisión del equipo (18/10/2026):** la "segunda entrega" de avance que menciona el aula no aplica; se va directamente a la Etapa 3. ITIL 4 sin definir.

## 6. Estado de entregas y recursos
- **Recursos del equipo** (de la Tabla 13 del PDF de Etapa 2): Drive `https://drive.google.com/drive/folders/1UNzvDp6loFH1cEmlk3ogOX_Ol3Lwo_UN`, repo `https://github.com/zamparg/IFTS29_proyecto_integrador`, Trello "ifts-n2-sprint-board-scrum", Lucidchart y Canva (links en el PDF), sitio `https://talento-tech-group.vercel.app`.
- **Requerimientos vigentes:** RF01–RF10 y RNF01–RNF08 (RNF07 accesibilidad y RNF08 datos personales agregados en Etapa 2).
- **Datos económicos fijados:** esfuerzo 680 h (de 720 disponibles), USD 30/h → USD 20.400; infraestructura $0; dominio contingente ≈ $8.500 ARS/año; licencia MIT propuesta.
- **Feedback de la cátedra a GdP Parte 1 (84/100):** falta el origen de los requerimientos (Negocio / Sistemas) y reformular la justificación de Scrumban (ver D-003).

## 7. Fuentes de este documento
- Transcripción de reunión de relevamiento — Meet 04/09/2026 (`proyecto/Meeting Transcription.pdf`).
- Notas propias tomadas durante la reunión (`proyecto/notes.md`).
- Minuta de reunión 30/06 (`cliente/ifts2/Minuta reunión 30_06.docx`).
- Documento de cátedra "PROYECTO INTEGRADOR IFTS 2 2026" (`cliente/ifts2/PROYECTO INTEGRADOR IFTS 2 2026.docx`).
- Documento "Páginas a vincular con la WEB del IFTS N°2" (carpeta de contexto del cliente).
- Presentación institucional y ficha de la Tecnicatura (PDFs de la carpeta de contexto del cliente).
- Scraping del sitio actual: https://sites.google.com/bue.edu.ar/ifts-2-de-20/
