# 6. Planificación y seguimiento

**Herramientas utilizadas y justificación.** Cada herramienta cubre una necesidad de flujo, iteración o control del proyecto, y todas funcionan en plan gratuito.

| Necesidad | Herramienta | Evidencia | Por qué |
|---|---|---|---|
| Flujo de tareas (Kanban) y backlog | Trello, tablero *ifts-n2-sprint-board-scrum* | [Tablero](https://trello.com/invite/b/6ab060ef5c1a94256279aa09/ATTI8f6929fe873ca1ea489347a631df47bfD3DB9833/ifts-n2-sprint-board-scrum) | Visualiza el flujo y el trabajo en curso; curva de aprendizaje mínima |
| Código y control de versiones | GitHub (repositorio con revisión cruzada) | [Repositorio](https://github.com/zamparg/IFTS29_proyecto_integrador) | Historial de decisiones y cambios verificable |
| Diseño y validación con el cliente | Figma | [Prototipo](https://www.figma.com/design/aRnoXCbNpkCFkHPH0En5B5/IFTS-N%25C2%25B0-2-%25E2%2580%2594-MVP-visual-y-panel-de-administraci%25C3%25B3n?node-id=0-1&p=f) | Permitió que el cliente rechazara la paleta antes de programar |
| Diagramas y documentación | Lucidchart, Google Drive | [Diagramas](https://lucid.app/lucidchart/a1dba306-c42d-45a0-a6f8-8c9b250ab91b/edit?invitationId=inv_e3ec5e19-c06e-4fbd-8fa3-2f5d9c389cd5), [Drive](https://drive.google.com/drive/folders/1UNzvDp6loFH1cEmlk3ogOX_Ol3Lwo_UN?usp=drive_link) | Trabajo compartido y enlaces públicos para la cátedra |
| Cronograma | Gantt y red CPM (secciones 7.2 y 7.3) | Figuras 1 y 2 | Muestra dependencias y camino crítico |

**Metodología: Scrumban (justificación corregida).** La Parte 1 descartaba Scrum argumentando el tamaño del equipo; la cátedra observó que ese no es un criterio válido. Scrumban se elige por tres necesidades del proyecto: **(1) iteración**, porque hay hitos fijos con el cliente (semanas 2, 6 y 13) que exigen incrementos revisables cada dos semanas; **(2) flujo**, porque las prioridades cambian según las devoluciones del cliente (por ejemplo, el rediseño de la paleta tras su rechazo) y un tablero continuo absorbe ese cambio sin replanificar un sprint completo; y **(3) control**, porque el límite de trabajo en curso (WIP) y la revisión cruzada de cada tarea detectan cuellos de botella temprano. Se mantienen del marco Scrum la planificación y la retrospectiva por sprint, y de Kanban el tablero con límite de WIP.

**Sprints** (2 semanas): S1 relevamiento (sem. 1-2) · S2 análisis y modelado (3-4) · S3 diseño y DEMO (5-6) · S4 base técnica y backend (7-8) · S5 desarrollo del panel y del sitio (9-10, en curso al 18/10) · S6 integración y QA (11-12) · S7 versión funcional y capacitación (13-14) · S8 cierre y traspaso (15-16).

**Plan de seguimiento y control.**

| Indicador | Meta | Umbral de alerta | Acción |
|---|---|---|---|
| Tareas completadas por sprint / planificadas | ≥ 80 % | < 60 % | Retrospectiva y recorte de alcance del sprint siguiente |
| Trabajo en curso por persona (WIP) | ≤ 2 tarjetas | > 3 | Terminar antes de empezar |
| Desvío del cronograma (semanas de atraso de la ruta crítica) | 0 | ≥ 1 | Aplicar el plan de contingencia de la sección 8 |
| Errores bloqueantes abiertos | 0 al hito | > 0 a dos semanas del hito | Congelar funciones nuevas |
| Respuesta del cliente a una validación | ≤ 5 días | > 10 días | Escalar a Martín Juan (canal único) y avanzar con datos de prueba |

**Registro de reuniones.** Las reuniones internas se resumen en actas en la carpeta de Drive del equipo `[completar enlace a las actas]`.

| Fecha | Reunión | Resultado |
|---|---|---|
| 30/06/2026 | IFTS N.° 2 e IFTS N.° 29 (cátedra) | Roles cliente y oferentes, cronograma de tres reuniones |
| 04/09/2026 | Relevamiento con el cliente (S2) | Requerimientos, restricciones de costo, criterio editorial de redes |
| Semana del 28/09/2026 `[confirmar fecha]` | DEMO de diseño con el cliente (S6) y devolución | Prototipo presentado; el cliente rechazó la paleta verde y dará correcciones adicionales |

**Registro de decisiones relevantes.**

| N.° | Decisión | Motivo |
|---|---|---|
| D-001 | Desarrollo a medida; la cátedra descartó WordPress | El alcance de la materia exige el ciclo completo de ingeniería de software |
| D-002 | Martín Juan, único canal con el cliente | Evitar respuestas contradictorias con tres equipos en paralelo |
| D-004 | El contenido vencido se archiva, nunca se borra | Pedido explícito del cliente ("un riesgo grave") |
| D-005 | Redes sociales: selección editorial del instituto | Criterio institucional humano, no réplica automática |
| D-006 | Infraestructura gratuita en la etapa inicial | El instituto no puede asumir costos |
| D-007 | Paleta tierra en lugar de la verde | Rechazo del cliente tras la DEMO |
| D-010 | La Etapa 3 se entrega como especificaciones para generar el MVP | Separar diseño técnico de implementación |

# 7. Estructura del proyecto y cronograma

## 7.1. Estructura de desglose del trabajo (WBS)

| Fase | Paquetes de trabajo | Responsable | Horas |
|---|---|---|---|
| 1. Análisis y requerimientos | Relevamiento, documento de requerimientos, backlog (A, B) | Martín Juan | 70 |
| 2. Diseño del sistema | Prototipo, diagramas UML, modelo de datos, DEMO (C, D, E) | Gastón Zampar, Nicolás Rolón | 110 |
| 3. Desarrollo | Arquitectura y CI/CD (F), API y base (G), sitio (H), panel (I), Instagram (J) | Nicolás Rolón, Gastón Zampar, Santiago Cuda | 280 |
| 4. Pruebas y calidad | QA de integración y aceptación (K) | Adrián Madroñal | 90 |
| 5. Capacitación | Capacitación a editores (L) | Martín Juan | 40 |
| 6. Manual y soporte | Manual de usuario y documentación técnica (N) | Gastón Zampar, Adrián Madroñal | 60 |
| 7. Mantenimiento | Correcciones, cierre y traspaso (O, P) | Santiago Cuda | 30 |
| | **Total** (de 720 h disponibles: 5 personas × 9 h × 16 semanas) | | **680** |

## 7.2. Diagrama de Gantt

El cronograma tiene 16 semanas, del 24/08 al 11/12/2026, con los tres hitos de la cátedra. En rojo, las actividades críticas; la línea vertical marca la fecha de elaboración de este documento (semana 9).

{{fig|gantt.svg|Diagrama de Gantt del proyecto|Nota. Las semanas 1 a 6 (análisis, diseño y DEMO) corresponden a trabajo ya realizado; las duraciones de las actividades A a E son las efectivamente transcurridas.}}

## 7.3. Método de la ruta crítica (CPM)

Con las duraciones probables y las dependencias de la Figura 2, el proyecto dura **{{END}} semanas**, que es exactamente el cuatrimestre: **no hay margen global**. La ruta crítica es **A → D → F → G → (J y K) → hito de la semana 13 → (L → P y N)**. Las actividades B, C, E, H, I y O tienen holgura de 1 o 2 semanas y funcionan como amortiguador.

{{fig|red-cpm.svg|Red de actividades con ruta crítica|Nota. Cada nodo muestra duración, inicio más temprano (ES), fin más temprano (EF) y holgura. Rojo: actividades críticas.}}

{{tabla|Cálculo CPM: tiempos más tempranos y más tardíos, en semanas desde el 24/08}}

{{CPM}}

## 7.4. Estimación PERT de la ruta crítica

Para la parte de la ruta crítica anterior al hito de la semana 13 se usaron estimaciones de tres puntos: **te = (O + 4M + P) / 6** y varianza **((P − O) / 6)²**.

{{tabla|Estimaciones PERT de las actividades críticas hasta el hito de la semana 13}}

{{PERT}}

**Lectura.** La duración esperada hasta el hito es de **{{TE}} semanas** con desvío estándar de **{{SD}}**. La probabilidad de llegar a la versión funcional dentro de la semana 13 es de **{{P13}} %**, y de llegar dentro de la semana 14, de **{{P14}} %**. Es decir, **el hito de la semana 13 es ajustado**: la incertidumbre se concentra en el backend (G, varianza 0,25) y en el modelado de datos (D). Por eso el plan de riesgos prioriza recortar alcance antes que extender plazos (sección 8) y acordar con el cliente que la reunión 3 puede mostrar un MVP con los módulos esenciales.

# 8. Informe de riesgos y mitigación

Escala: probabilidad (P) e impacto (I) de 1 (bajo) a 3 (alto); exposición = P × I. Orden por exposición.

{{tabla|Registro de riesgos, evaluación y planes de mitigación y contingencia}}

| N.° | Riesgo | Tipo | P | I | Exp. | Mitigación (preventiva) | Contingencia (si ocurre) | Resp. |
|---|---|---|---|---|---|---|---|---|
| R1 | Retraso en la ruta crítica (backend) y no llegar al hito de la semana 13 (probabilidad calculada en 7.4) | Técnico | 3 | 3 | 9 | Contrato de API definido primero; trabajo en paralelo de frontend y panel con datos simulados; WIP limitado | Recortar a un MVP: novedades, horarios, archivo y login; el resto va a la semana 14 | Nicolás |
| R2 | La integración con la API de Instagram no resulta viable o el token vence | Técnico | 2 | 3 | 6 | Prueba de concepto temprana; módulo aislado detrás de una interfaz | Carga manual asistida desde el panel; el sitio no depende de la API | Nicolás |
| R3 | El cliente cambia o rechaza el diseño y obliga a rehacer (ya ocurrió con la paleta) | Cliente | 3 | 2 | 6 | Tokens de diseño centralizados; validar en Figma antes de programar | Cambio de tokens, sin rediseño de estructura | Gastón |
| R4 | Baja disponibilidad del cliente para validar y entregar contenidos | Cliente | 3 | 2 | 6 | Canal único; pedidos anticipados con fecha | Avanzar con datos de prueba; validar solo en reuniones 2 y 3 | Martín |
| R5 | Crecimiento de alcance (el Figma sumó avisos, archivo documental y configuración) | Alcance | 3 | 2 | 6 | Backlog priorizado (MoSCoW); todo pedido nuevo pasa por Martín | Posponer lo "Could" a la siguiente cohorte | Martín |
| R6 | Dedicación parcial, ausencias o sobrecarga del equipo | Humano | 2 | 3 | 6 | Revisión cruzada y conocimiento compartido entre pares; buffers de holgura | Reasignar tareas según holgura; reducir WIP | Martín |
| R7 | Infraestructura gratuita: suspensión por inactividad, límites de base de datos o de almacenamiento | Económico | 2 | 2 | 4 | Elegir planes sin vencimiento; compresión de imágenes; respaldos periódicos | Migrar a otro proveedor; costo mínimo aprobado con el cliente | Santiago |
| R8 | Datos personales y fotos de estudiantes sin consentimiento (Ley 25.326) | Legal | 2 | 3 | 6 | Aviso de uso de datos; publicar solo con consentimiento; mínimo de datos | Retiro inmediato del contenido | Adrián |
| R9 | Pérdida de datos o acceso indebido al panel | Técnico | 1 | 3 | 3 | Hash de contraseñas, roles, respaldos, secretos en variables de entorno | Restaurar el último respaldo; rotar credenciales | Santiago |
| R10 | Tres equipos con el mismo cliente generan pedidos contradictorios | Organizacional | 2 | 2 | 4 | Acuerdos por escrito; no asumir exclusividad | Priorizar lo confirmado por escrito | Martín |
| R11 | Trámite del dominio .edu.ar demorado | Externo | 2 | 1 | 2 | Iniciar documentación temprano | Subdominio provisorio gratuito | Santiago |
| R12 | Baja adopción del panel por parte de los docentes | Humano | 2 | 3 | 6 | Panel simple, capacitación con casos prácticos, manual | Sesión de refuerzo y acompañamiento en las primeras semanas | Martín |

**Mapa de calor.** Exposición alta (6 a 9): R1, R2, R3, R4, R5, R6, R8, R12. Media (3 a 4): R7, R9, R10. Baja (1 a 2): R11. Los riesgos R1, R3 y R5 son los que la propia ejecución ya puso a prueba y se revisan en cada retrospectiva.

# 9. Sostenibilidad del proyecto

**Estrategia de sostenimiento.** El proyecto es académico y no se cobra; la sostenibilidad se resuelve en tres capas:

1. **Costo operativo cero para el cliente:** hosting, base de datos, CDN y correo en planes gratuitos, y un dominio .edu.ar o un subdominio provisorio. El instituto solo asume, eventualmente, un dominio .com.ar de unos $8.500 ARS por año.
2. **Mantenimiento por continuidad académica:** la cátedra y el cliente acordaron que una cohorte siguiente puede retomar el proyecto para mejoras (minuta del 30/06). El traspaso incluye documentación técnica, manual de usuario y repositorio, y el equipo de Talento Tech cierra el proyecto con la fase de mantenimiento inicial (actividad P).
3. **Reutilización como servicio:** la estructura modular permite adaptar la plataforma a otras instituciones con costos de adaptación y soporte; esa línea es la que sostiene económicamente a la empresa (sección 10.3).

**Modelo de licenciamiento.**

| Modelo | A favor | En contra | Evaluación |
|---|---|---|---|
| **MIT (propuesto)** | Máxima reutilización; el instituto y futuras cohortes pueden modificar y mejorar el código; sin costo de licencias | No obliga a quien lo reutilice a compartir sus mejoras | **Elegido** |
| GPL v3 | Obliga a mantener abiertas las derivaciones | Desalienta su adopción en entornos que quieran integrarlo con software cerrado | Alternativa válida |
| Propietario | Control comercial | Contradice el carácter público del cliente, genera dependencia y costo | Descartado |
| Freemium / SaaS | Ingreso recurrente | Requiere operar infraestructura y soporte con pago, lo que el instituto no puede sostener hoy | Posible a futuro para otras instituciones |

Se adopta **MIT para el código**, con cesión de uso al IFTS N.° 2; los contenidos, textos, fotografías y la marca pertenecen al instituto y no se licencian.

**Prácticas sostenibles y control de calidad.**

| Dimensión | Práctica |
|---|---|
| Económica | Infraestructura gratuita; documentación de traspaso para que el mantenimiento no dependa del equipo original |
| Ambiental | Sin servidores propios dedicados; imágenes comprimidas y servidas por CDN; páginas livianas |
| Social | Accesibilidad WCAG 2.2 AA; protección de datos personales (Ley 25.326); panel pensado para personal no técnico |
| Calidad | Revisión cruzada de cada tarea; pruebas automatizadas (meta: 60 % de cobertura del backend); integración continua; definición de "terminado" con QA; retrospectiva por sprint |

# 10. Presupuesto estimado y análisis de costos

## 10.1. Costos del proyecto actual

Los costos de mano de obra se calculan con 680 horas a un valor referencial de **USD 30 por hora**. Es un proyecto sin cobro: el valor sirve para dimensionar el servicio y evaluar su factibilidad.

{{tabla|Presupuesto por fase, costos directos e indirectos}}

| Concepto | Tipo | Cálculo | Monto |
|---|---|---|---|
| 1. Análisis y requerimientos | Directo, variable | 70 h × USD 30 | USD 2.100 |
| 2. Diseño del sistema | Directo, variable | 110 h × USD 30 | USD 3.300 |
| 3. Desarrollo e implementación | Directo, variable | 280 h × USD 30 | USD 8.400 |
| 4. Pruebas y control de calidad | Directo, variable | 90 h × USD 30 | USD 2.700 |
| 5. Capacitación | Directo, variable | 40 h × USD 30 | USD 1.200 |
| 6. Manual y soporte | Directo, variable | 60 h × USD 30 | USD 1.800 |
| 7. Mantenimiento inicial | Directo, variable | 30 h × USD 30 | USD 900 |
| **Subtotal mano de obra** | | 680 h × USD 30 | **USD 20.400** |
| Hosting, base de datos, CDN y correo | Directo, fijo | Planes gratuitos | USD 0 |
| Licencias de software (Trello, GitHub, Figma, Lucidchart) | Indirecto, fijo | Planes gratuitos | USD 0 |
| Dominio .com.ar (contingente) | Directo, fijo anual | Valor mencionado en la reunión | $8.500 ARS |
| Equipamiento, conexión y energía | Indirecto | Aportados por los integrantes | No imputado |
| Reserva de contingencia (10 % de mano de obra, sobre R1 y R5) | Indirecto | 10 % × USD 20.400 | USD 2.040 |
| **Total estimado** | | | **USD 22.440** + dominio |

## 10.2. Costos de mantenimiento posterior

Supuesto del equipo: 4 horas mensuales de soporte y correcciones (48 h por año), es decir **USD 1.440 por año** a valor referencial, más hosting USD 0 mientras alcance el plan gratuito. Si fuera necesario pasar a un plan pago, el costo se cotizará y se acordará con el instituto antes de aplicarlo (riesgo R7).

## 10.3. Factibilidad económica y punto de equilibrio

**Factibilidad.** Para el instituto el proyecto es factible porque su costo en dinero es cero; para el equipo es factible porque las 680 horas planificadas entran en las 720 disponibles. No lo es como negocio de un único cliente: el costo de USD 22.440 supera cualquier presupuesto institucional del cliente, y por eso se sostiene como práctica profesional y como base reutilizable.

**Punto de equilibrio de la empresa con proyectos similares.** Fórmula: **PE = costos fijos anuales / (precio − costo variable por proyecto)**. Se supone que Talento Tech tiene costos fijos de USD 4.200 por año (herramientas pagas, administración y difusión), supuesto a validar.

| Escenario | Precio | Costo variable | Margen por proyecto | Punto de equilibrio |
|---|---|---|---|---|
| Proyecto nuevo desde cero (como el actual) | USD 26.000 (costo más 25 %) | USD 20.700 (mano de obra e infraestructura) | USD 5.300 | 4.200 / 5.300 = 0,8, o sea **1 proyecto por año** |
| Proyecto similar reutilizando la plataforma (120 h de adaptación) | USD 6.000 | USD 3.700 (120 h × USD 30 más USD 100 de infraestructura) | USD 2.300 | 4.200 / 2.300 = 1,8, o sea **2 proyectos por año** |

**Conclusión.** El modelo reutilizable es el que hace accesible el servicio para instituciones con presupuesto reducido (USD 6.000 contra USD 26.000) y alcanza el equilibrio con dos adaptaciones por año. Un solo proyecto desde cero cubre los costos fijos, pero solo con un cliente que pueda pagar el precio completo, que no es el caso del IFTS N.° 2.

# Anexo A. Corrección de la Parte 1: origen de los requerimientos

La cátedra pidió consignar el origen de cada requerimiento. **Negocio:** surge de los objetivos o restricciones del instituto. **Sistema:** surge de condiciones técnicas, normativas o de calidad del producto. Fuentes: reunión de relevamiento (R04/09), notas del equipo (N) y normativa (L: Ley 25.326; W: WCAG 2.2).

{{tabla|Origen y fuente de los requerimientos relevados}}

| ID | Requerimiento | Tipo | Origen | Fuente |
|---|---|---|---|---|
| RF01 | Administrar contenido desde un panel sin conocimientos técnicos | Funcional | Negocio | R04/09 |
| RF02 | Distinguir contenido estanco de dinámico | Funcional | Negocio | R04/09 |
| RF03 | Archivar contenido vencido sin eliminarlo | Funcional | Negocio | R04/09 |
| RF04 | Vincular publicaciones de Instagram y Facebook por selección editorial | Funcional | Negocio | R04/09 |
| RF05 | Soportar múltiples administradores | Funcional | Negocio | R04/09 |
| RF06 | Mostrar solo horarios y mesas del período vigente | Funcional | Negocio | R04/09 |
| RF07 | Accesos a SIU Guaraní, Aulas Virtuales y Mi Argentina | Funcional | Negocio | Documento "Páginas a vincular" |
| RF08 | Formulario de contacto a correo institucional | Funcional | Negocio | R04/09 |
| RF09 | Gestionar galería con descripción y categoría | Funcional | Negocio | R04/09 |
| RF10 | Gestionar plantel docente y materias | Funcional | Negocio | R04/09 |
| RNF01 | Usabilidad para personal no técnico | No funcional | Negocio | R04/09 |
| RNF02 | Infraestructura gratuita o de costo mínimo | No funcional | Negocio | R04/09 |
| RNF03 | Disponibilidad estable | No funcional | Sistema | N |
| RNF04 | Diseño responsive | No funcional | Sistema | N |
| RNF05 | Rendimiento con alto volumen de imágenes | No funcional | Sistema | R04/09 |
| RNF06 | Acceso al panel con autenticación | No funcional | Sistema | N |
| RNF07 | Accesibilidad WCAG 2.2 AA | No funcional | Sistema | W |
| RNF08 | Protección de datos personales | No funcional | Sistema | L |
