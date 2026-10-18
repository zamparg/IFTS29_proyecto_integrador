# Etapa 3 — Especificaciones para generar el MVP

Esta carpeta es el **paquete de especificaciones** del MVP del sitio institucional del IFTS N.° 2. **No contiene código de la aplicación**: está pensada para entregársela a un agente de IA en **otro repositorio y otra sesión** para que construya el proyecto, y para que el equipo de Talento Tech la use como guía y como evidencia de la etapa.

**Cómo usarla:** copiá esta carpeta al repositorio nuevo, pedile al agente que lea `AGENTS.md` y seguí el plan de `especificaciones/07-backlog-y-plan.md`.

## Contenido

| Archivo | Para qué sirve |
|---|---|
| [historias-de-usuario.md](historias-de-usuario.md) | 12 historias de usuario en el formato de la cátedra, priorizadas, con criterios y trazabilidad |
| [AGENTS.md](AGENTS.md) | Reglas no negociables, orden de lectura, convenciones y definición de terminado |
| [especificaciones/00-vision-y-alcance.md](especificaciones/00-vision-y-alcance.md) | Problema, objetivo, alcance del MVP (Debe / Debería / Podría) y criterios de éxito |
| [especificaciones/01-requerimientos.md](especificaciones/01-requerimientos.md) | RF y RNF con prioridad, origen, pantallas y criterios de aceptación |
| [especificaciones/02-decisiones-tecnicas.md](especificaciones/02-decisiones-tecnicas.md) | Decisiones técnicas (ADR) con motivo, alternativas y estado de validación |
| [especificaciones/03-arquitectura-y-estructura.md](especificaciones/03-arquitectura-y-estructura.md) | Arquitectura, estructura del monorepo, variables de entorno, CI/CD y despliegue |
| [especificaciones/04-api.md](especificaciones/04-api.md) | Contrato de la API REST, permisos por rol y errores |
| [especificaciones/05-ui-y-pantallas.md](especificaciones/05-ui-y-pantallas.md) | Pantallas del Figma, contenido, estados, componentes y nodos |
| [especificaciones/06-testing-y-calidad.md](especificaciones/06-testing-y-calidad.md) | Estrategia de pruebas, escenarios E2E, presupuestos de calidad |
| [especificaciones/07-backlog-y-plan.md](especificaciones/07-backlog-y-plan.md) | Historias de usuario, fases y orden de implementación |
| [especificaciones/08-contenido-y-datos-semilla.md](especificaciones/08-contenido-y-datos-semilla.md) | Datos reales del cliente y datos semilla |
| [especificaciones/09-preguntas-abiertas.md](especificaciones/09-preguntas-abiertas.md) | Supuestos y dudas que el equipo debe validar con el cliente |
| [especificaciones/10-entregables-etapa-3.md](especificaciones/10-entregables-etapa-3.md) | Qué exige la consigna de la cátedra (manuales, CRUD, pruebas, instalación) y cómo se cumple |
| [especificaciones/prisma/schema.prisma](especificaciones/prisma/schema.prisma) | Modelo de datos ejecutable (Prisma + PostgreSQL) |
| [especificaciones/design-tokens.json](especificaciones/design-tokens.json) | Colores y tipografía del Figma vigente |

## Relación con la consigna de la cátedra

La consigna "Etapa 3 - Desarrollo completo" pide una aplicación funcional integrada con las etapas anteriores, Manual Técnico, Manual de Usuario, base de datos con CRUD, 2 o 3 pruebas unitarias y 1 o 2 de integración documentadas (qué se probó, esperado, obtenido, evidencias) y un PDF con instrucciones de instalación y puesta en marcha. **Este paquete es la entrada para construir eso en otro repositorio; no lo reemplaza.** El mapeo punto por punto está en `especificaciones/10-entregables-etapa-3.md`.

## Origen de la información

- Requerimientos: reunión de relevamiento del 04/09/2026, minuta del 30/06 y consigna de la cátedra (`proyecto/context.md`).
- Decisiones: Etapa 2 entregada (stack y arquitectura), registro `proyecto/decisiones.md` (D-001 a D-010).
- Diseño: Figma vigente al 18/10/2026, que incorpora la devolución del cliente sobre la paleta. El cliente dará correcciones adicionales, por lo que este paquete es **la versión 1** y se versiona.

## Estado y límites conocidos

- La paleta, las pantallas y los textos del Figma son vigentes pero **provisorios**: faltan las correcciones del cliente.
- **Contacto, Galería y Plantel docente no están diseñados en Figma**; están en la especificación como prioridad "Debería" o "Podría".
- Hosting, base de datos y almacenamiento gratuitos están **pendientes de validación por DevOps** (Santiago Cuda); la especificación los trata con interfaces reemplazables.
- La integración con Instagram **requiere prueba de concepto** antes de depender de ella.
