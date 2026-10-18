# 10 · Entregables de la Etapa 3 según la consigna de la cátedra

Fuente: `consigna/Etapa 3 - Desarrollo completo.pdf` (texto en `consigna/Etapa 3 - Desarrollo completo.txt`). La aplicación debe guardar coherencia con los requerimientos, diagramas, prototipos y documentación de las etapas anteriores, ejecutarse correctamente, tener la base de datos operativa y permitir las operaciones principales de manera estable.

## Qué pide la consigna y cómo se cumple

| Punto de la consigna | Qué se espera | Cómo se cumple en este proyecto |
|---|---|---|
| 2. Manual Técnico | Introducción, arquitectura, estructura del proyecto, base de datos (DER, tablas y campos, relaciones), configuración e instalación (tecnologías, versiones, dependencias, configuración inicial, ejecución, crear o restaurar la base, credenciales de prueba), componentes principales, gestión de errores y validaciones, pruebas implementadas | Se escribe en el repo nuevo a partir de `03-arquitectura-y-estructura.md`, `02-decisiones-tecnicas.md`, `schema.prisma` y `04-api.md`. El DER se genera desde el esquema Prisma (por ejemplo con `prisma-erd-generator`) y se complementa con la descripción de tablas y campos |
| 3. Manual de Usuario | Introducción, requisitos mínimos, pantalla principal, flujos paso a paso, capturas con descripción, mensajes o alertas frecuentes | Flujos de los editores y de bedelía (moderar publicaciones, crear avisos, cargar horarios, archivar, configurar). Capturas de la aplicación real con la identidad visual del Figma vigente |
| 4. Base de datos y CRUD | Base funcional; Create, Read, Update y Delete desde la aplicación; evitar duplicados; campos obligatorios; confirmación antes de eliminar; mensajes claros | PostgreSQL + Prisma. Tabla de CRUD de abajo. Duplicados, obligatorios y mensajes: reglas 8 y 9 de `01-requerimientos.md` |
| 5. Pruebas unitarias | 2 o 3 representativas con qué se probó, esperado y obtenido; evidencias de ejecución | `06-testing-y-calidad.md`, sección "Pruebas que se documentan para la cátedra" |
| 6. Pruebas de integración | 1 o 2 con pasos, esperado, obtenido y evidencias | Ídem |
| 7. Alcance de las pruebas | No hace falta probar todo; importan la relevancia y la claridad | Se prueba lo crítico (vigencia, validaciones, cifrado, creación y eliminación) |
| 8. Entregables | Repositorio Git actualizado; proyecto comprimido (.zip o .rar); PDF con toda la documentación; Manual Técnico; Manual de Usuario; evidencia de pruebas; base de datos o scripts de creación; ejecutable o enlace a la aplicación desplegada | Lista de verificación de abajo |
| Sección de instalación | El PDF debe incluir instrucciones que permitan a cualquier docente descargar, configurar y ejecutar el proyecto usando solo la documentación | Historia US-35: se verifica en una máquina limpia |

## CRUD demostrable por entidad

| Entidad | Crear | Leer | Actualizar | Eliminar (manual, con confirmación) |
|---|---|---|---|---|
| Avisos académicos | Nuevo aviso | Lista y detalle (panel y Estudiantes) | Editar, pausar, reanudar | Solo vencidos o pausados |
| Publicaciones | Aprobar desde redes o cargar manual | Panel y Novedades | Editar, pausar, reactivar | Borradores, pausadas o vencidas |
| Documentos | Archivar nuevo documento | Archivo con búsqueda y detalle | Editar metadatos, restaurar | Solo archivados |
| Horarios y llamados | Cargar grilla, configurar llamado | Panel y Estudiantes | Actualizar archivo, editar llamado | No publicados o de ciclos anteriores |
| Usuarios | Administrar usuarios y roles | Lista | Cambiar rol, desactivar | No se eliminan: se desactivan, para conservar la auditoría |
| Enlaces de interés | Nuevo enlace | Estudiantes | Editar, ocultar | Enlaces ocultos |

Cada eliminación abre el diálogo de confirmación único (ADR-11), registra en `AuditLog` y respeta las reglas de elegibilidad de `01-requerimientos.md`.

## Lista de verificación de la entrega final

- [ ] Repositorio Git con la versión final y su historial.
- [ ] Proyecto completo comprimido (.zip) generado desde el repositorio, sin secretos ni `node_modules`.
- [ ] PDF único con: Manual Técnico, Manual de Usuario, evidencias de pruebas unitarias y de integración, capturas del CRUD, sección de instalación y puesta en marcha.
- [ ] Scripts de creación de la base: migraciones de Prisma y `seed.ts` (semilla de demostración).
- [ ] Credenciales de prueba por rol (ADMIN, BEDELIA, EDITOR), solo para el entorno de demostración.
- [ ] Enlace a la aplicación desplegada (sitio y panel) y a la API.
- [ ] Presentación grabada con demostración en vivo (la consigna general de la cátedra la pide como defensa).
- [ ] Verificación de instalación en una máquina limpia siguiendo solo el PDF.

## Evidencias que el agente debe ir guardando

En `docs/evidencias/`: salida de Vitest (unitarias), salida de Supertest (integración), capturas de Cypress o de la aplicación para cada flujo del manual de usuario, captura de Lighthouse y de axe, y registro de la prueba de concepto de Instagram. Con nombre y fecha, porque no se pueden reconstruir al final.

## Entrega de avance del aula virtual (confirmar si es aparte)

La orientación de actividades del aula (archivo en `material/`) describe una etapa de desarrollo iterativo con productos propios: al menos **dos módulos funcionales** (con este plan, **Avisos académicos** y **Publicaciones de redes**, fases 1 y 2); control de versiones con **ramas por funcionalidad** y commits significativos; pruebas funcionales iniciales con registro de errores; **portfolio grupal** en el Campus Virtual (capturas, explicaciones, enlaces, decisiones, dificultades, tareas completadas y pendientes); **horas trabajadas por integrante**; y un **video de avance con cámara encendida**. El agente debe mantener en el repo nuevo `docs/avance.md` (tareas completadas y pendientes, dificultades y soluciones) para alimentar ese portfolio. Las horas por integrante las registra el equipo humano en su propia planilla.

## Historias de usuario en el formato de la cátedra

La cátedra pide el formato "Como [tipo de usuario], quiero [acción] para [objetivo]", entre 8 y 12 historias, con prioridad alta, media o baja. Las 35 historias técnicas de `07-backlog-y-plan.md` (US-01 a US-35) se resumen así para el documento:

| N.° | Historia | Prioridad |
|---|---|---|
| H1 | Como editor, quiero ver las publicaciones de Instagram detectadas para decidir cuáles mostrar en el sitio | Alta |
| H2 | Como editor, quiero aprobar una publicación con sección y vigencia para que aparezca en el sitio solo el tiempo que corresponde | Alta |
| H3 | Como editor, quiero descartar una publicación para que contenido interno menor no llegue a la web | Alta |
| H4 | Como personal de bedelía, quiero publicar avisos con adjunto y fecha de vencimiento para que los alumnos vean solo información vigente | Alta |
| H5 | Como personal de bedelía, quiero cargar los horarios por comisión y los llamados a examen para que los alumnos consulten el ciclo en curso | Alta |
| H6 | Como administrador, quiero definir el ciclo público para que el sitio muestre un solo período académico | Alta |
| H7 | Como alumno, quiero ver horarios, mesas y avisos vigentes y acceder a SIU y al aula virtual para resolver mi cursada desde un solo lugar | Alta |
| H8 | Como aspirante, quiero conocer la carrera, el plan de estudios y los pasos de ingreso para decidir si me inscribo | Alta |
| H9 | Como administrador, quiero crear usuarios con roles para que cada persona acceda solo a lo que le corresponde | Media |
| H10 | Como personal autorizado, quiero archivar, restaurar y eliminar documentos antiguos con confirmación para mantener ordenado el repositorio sin perder información por error | Media |
| H11 | Como visitante, quiero enviar una consulta al instituto para resolver dudas sin depender de una sola persona | Media |
| H12 | Como editor, quiero gestionar el plantel docente y una galería para mostrar la vida del instituto | Baja |

## Sobre la defensa

La consigna general de la cátedra exige una defensa grabada con problema detectado, solución propuesta, arquitectura, tecnologías, demostración en vivo, resultados y reflexión crítica. El paquete deja material para cada punto: `00-vision-y-alcance.md` (problema y solución), `03-arquitectura-y-estructura.md` (arquitectura), `02-decisiones-tecnicas.md` (tecnologías y decisiones).
