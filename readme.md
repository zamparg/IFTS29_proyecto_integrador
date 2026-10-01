# Proyecto Integrador — Talento Tech × IFTS N°2

Repositorio de trabajo del equipo **Talento Tech** (IFTS N°29, Tecnicatura Superior en Desarrollo de Software, 2° cuatrimestre 2026). Un único proyecto —modernizar el sitio institucional del **IFTS N°2 DE 20** (Tec. Sup. en Emprendimientos Gastronómicos)— alimenta los trabajos prácticos de varias materias. El contexto del proyecto vive una sola vez en `proyecto/`; cada materia tiene su carpeta con consigna y entregas.

**Equipo:** Santiago Cuda (DevOps) · Adrián Madroñal (QA) · Martín Juan (Product Owner) · Nicolás Rolón (Backend) · Gastón Zampar (Frontend).
**Sitio de presentación del equipo:** talento-tech-group.vercel.app

## Enlaces

- **Figma (MVP visual y panel de administración):** https://www.figma.com/design/aRnoXCbNpkCFkHPH0En5B5/IFTS-N%25C2%25B0-2-%25E2%2580%2594-MVP-visual-y-panel-de-administraci%25C3%25B3n?node-id=0-1&p=f — insumo para wireframes/prototipo de la Etapa 2 de PPIV y la DEMO de semana 6.

## Estructura

```
.
├── readme.md                  Este archivo (índice + estado). CLAUDE.md lo importa.
├── agents/                    Agentes/personas de IA reutilizables
│   └── agente-gestion-proyecto.md   Asesor de gestión (OKR, KPI, SMART, riesgos, WBS)
├── proyecto/                  FUENTE DE VERDAD compartida por todas las materias
│   ├── context.md             Cliente, estado del sitio, requerimientos, restricciones, cronograma  ← leer primero
│   ├── propuesta-para-cliente.md   Resumen ejecutivo orientado al cliente
│   ├── notes.md               Notas crudas de la reunión de relevamiento
│   ├── Meeting Transcription.pdf   Transcripción reunión 04/09/2026
│   └── catedra/               Consigna general de la cátedra + minuta 30/06
├── cliente/ifts2/             Material del cliente: logos, flyer, plan de carrera, links a vincular
├── referencias/               Normativa y estilo: Ley de Pasantías, Práctica Profesionalizante (Ministerio), Manual de Estilo GCABA
└── materias/
    ├── ppiv-proyecto-integrador/     Práctica Profesionalizante IV
    │   ├── consigna/          Etapa 2 (PDF + resumen del docente)
    │   ├── entrega-1/         Etapa 1 (PDF), sitio HTML interactivo, estructura de contenido
    │   ├── entrega-2/         prompt-lovable-maqueta.md (prototipo)
    │   └── material/          ITIL 4, Modelado de Sistemas, Vicente y Ayala cap. 7
    ├── gestion-de-proyectos/
    │   ├── consigna/          Propuesta de TP integrador + rúbrica
    │   ├── entrega-1/         Parte 1 (docx + pdf de trabajo, y PDF "Comisión E Equipo 08")
    │   └── entrega-2/         (vacía) Parte 2
    └── emprendedurismo/
        ├── consigna/          1° TP integrador (Unidades 1 a 3)
        ├── entrega-1/         trabajo-practico-integrador.md
        ├── entrega-2/         (vacía)
        └── material/          Lecturas y clases (Unidades 1–3, Running Lean, etc.)
```

Convención: `materias/<materia>/{consigna, entrega-N, material}`. Todo lo compartido entre materias va en `proyecto/`, **nunca se duplica** dentro de una materia: se enlaza.

## Estado de las entregas

| Materia | Entrega 1 | Entrega 2 |
|---|---|---|
| **PPIV – Proyecto integrador** | ✅ Hecha (Etapa 1: empresa Talento Tech, misión/visión, roles, relevamiento) | ⏳ Etapa 2 — *Análisis y Modelado del Diseño*: diagramas UML (casos de uso, clases, secuencia, actividades, estados, componentes, despliegue, ER), wireframes/prototipo en Figma, roles + CV/LinkedIn, viabilidad, propuesta (resumen ejecutivo, objetivos SMART, recursos, impacto). Formato APA, PDF + Canva/presentación, links públicos en Drive. Demo al cliente (semana 6). Hay un prompt de Lovable ya armado para la maqueta. |
| **Gestión de Proyectos** | ✅ Hecha (Parte 1: visión, cultura organizacional, fases, metodología, stakeholders y requerimientos) | ⏳ Parte 2: (6) planificación y seguimiento, (7) estructura y cronograma con Gantt + CPM/PERT, (8) riesgos y mitigación, (9) sostenibilidad y licenciamiento, (10) presupuesto, costos y punto de equilibrio. Máx. 10 páginas, PDF `GDP_Comisión X_Equipo ZZZ_TPI - Parte y.pdf`. |
| **Emprendedurismo** | ✅ Hecha (1° TP: perfil emprendedor, desarrollo profesional, oportunidad, FODA) | ❓ Consigna de la 2ª entrega **no está en el repo** (el material cubre Unidades 1–3). Agregarla en `materias/emprendedurismo/consigna/`. |

## Hitos del proyecto con el cliente (fijados por la cátedra)

| Semana | Hito | Estado |
|---|---|---|
| 2 | Reunión 1: relevamiento (04/09/2026) | ✅ |
| 6 | Reunión 2: DEMO de diseño/prototipos y alcance definitivo | ⏳ |
| 13 | Reunión 3: versión funcional | ⏳ |

## Resumen del proyecto (detalle en `proyecto/context.md`)

- **Cliente:** IFTS N°2 (GCABA). Ancla de identidad: *"No formamos chefs. Formamos empresarios gastronómicos."*
- **Problema:** sitio en Google Sites abandonado, con contenido de 2021–2026 mezclado, sin panel, sin contacto, sin integración con redes.
- **Solución propuesta:** sitio público + panel de administración propio; contenido *estanco* vs *dinámico* (archivar, nunca borrar); selección editorial de posts de Instagram/Facebook (hashtag + rango de fechas); accesos a SIU Guaraní, Aulas Virtuales y Mi Argentina; formulario de contacto.
- **Restricciones:** presupuesto casi nulo (hosting/dominio gratuitos; .edu.ar a evaluar), administradores no técnicos (Matías Peláez, María del Carmen Canobi), 3 equipos compitiendo por el mismo cliente, desarrollo propio (sin CMS de terceros).
- **Marca:** azul institucional `#24507F`, tipografías Fraunces + Inter (usadas en el HTML de la Entrega 1).

## Para agentes de IA

1. Antes de cualquier tarea, leer `proyecto/context.md`. Para trabajo de materia, leer además la `consigna/` correspondiente y la entrega 1 de esa materia (mantener coherencia de nombres, roles, objetivos y datos).
2. No inventar datos del cliente ni del equipo: salen de `proyecto/` y de las entregas hechas. Si falta algo, marcarlo como `[completar]`.
3. Entregas nuevas van en `materias/<materia>/entrega-N/`; si hay información nueva del cliente, actualizar `proyecto/context.md` (no la materia).
4. Respetar el formato exigido por cada consigna (APA en PPIV; máx. 10 págs. y nombre de archivo en GdP; conciso y fundamentado en Emprendedurismo).
5. Para gestión (OKR/KPI/SMART/riesgos) usar `agents/agente-gestion-proyecto.md`. Para comunicación escrita formal con el cliente, `referencias/Manual de Estilo del GCABA...pdf`.
6. Español rioplatense, tono profesional y directo.
7. Las consignas de `consigna/` tienen un `.txt` al lado del PDF (extraído con `pdftotext -layout`): leer ese. Para otros PDF/DOCX, extraer el texto en vez de asumir su contenido.

## Pendientes de orden

- Borrar las carpetas vacías heredadas: `context/` y `docs/` (quedaron sin archivos tras la reorganización).
- Confirmar cuál de los dos PDF de GdP Parte 1 es el entregado (`GDP_Comisión E_Equipo 08_TPI - Parte 1.pdf` vs `GDP_ComisionX_TalentoTech_TPI-Parte1.pdf`) y descartar el otro.
