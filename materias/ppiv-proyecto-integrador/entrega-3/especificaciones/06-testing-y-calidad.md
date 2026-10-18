# 06 · Pruebas y calidad

## Estrategia

| Nivel | Herramienta | Qué cubre | Meta |
|---|---|---|---|
| Unitarias | Vitest | Reglas de vigencia, cálculo de visibilidad, validaciones zod, cifrado del token, sanitización | ≥ 60 % de cobertura de la lógica del backend (meta de la Etapa 2) |
| API | Supertest + PostgreSQL de prueba | Contratos de `04-api.md`, permisos por rol, errores 4xx, idempotencia de la sincronización | Cada endpoint con caso feliz y caso de permiso |
| Extremo a extremo | Cypress (viewports 390 y 1440) | Escenarios E2E de abajo | Todos en verde antes del hito |
| Accesibilidad | axe en Cypress + Lighthouse CI | WCAG 2.2 AA | 0 violaciones graves; Accesibilidad ≥ 90 |
| Rendimiento | Lighthouse CI | Inicio y Novedades en móvil | Rendimiento ≥ 80; contenido principal < 2,5 s |
| Seguridad | Pruebas de API + revisión | Acceso sin sesión, escalada de roles, subida de archivos no permitidos, límites de frecuencia | Sin hallazgos altos |

Las integraciones externas se prueban con **dobles**: `FakeInstagramClient`, `InMemoryStorage`, `FakeMailer`. La prueba de concepto con la API real de Instagram es manual y se documenta.

## Datos de prueba

La semilla (`prisma/seed.ts`) crea: un usuario por rol, un ciclo público 2026-2.º, un ciclo anterior archivado, avisos (uno vigente, uno vencido, uno urgente), tres publicaciones sociales detectadas (una de efeméride "no prioritaria"), documentos archivados de 2024 y 2025, y los enlaces de interés reales.

## Escenarios E2E

| ID | Escenario | Requerimiento |
|---|---|---|
| E2E-01 | Un visitante recorre las seis páginas públicas en móvil y escritorio sin errores | RNF04 |
| E2E-02 | Login correcto, login incorrecto con mensaje genérico, bloqueo tras 5 intentos | RNF06 |
| E2E-03 | El Editor modera: aprueba una publicación de Instagram con sección y vigencia y la ve en el sitio | RF04 |
| E2E-04 | El Editor descarta una publicación y la recupera desde "Descartadas" | RF04 |
| E2E-05 | Falla de Instagram: el Resumen muestra el error y la carga manual funciona | RNF03 |
| E2E-06 | Bedelía crea un aviso con adjunto y vigencia; aparece en Estudiantes; al vencer desaparece pero queda en el panel | RF03 |
| E2E-07 | Bedelía pausa y reanuda un aviso | RF03 |
| E2E-08 | Bedelía carga una grilla de horarios por comisión y la publica; un llamado a examen se crea, edita y publica | RF06 |
| E2E-09 | El Administrador cambia el ciclo público con confirmación; el sitio muestra solo el nuevo ciclo | RF06 |
| E2E-10 | Archivo: búsqueda por año, ver detalle y restaurar un documento | RF03 |
| E2E-11 | Un usuario BEDELIA no ve ni accede a Usuarios ni a Publicaciones de redes | RF05 |
| E2E-12 | El Administrador crea un usuario con rol y lo desactiva; el usuario desactivado no puede entrar | RF05 |
| E2E-13 | Todas las pantallas se operan con teclado; los diálogos atrapan y devuelven el foco | RNF07 |
| E2E-14 | (Should) Contacto: exige consentimiento, guarda el mensaje aunque falle el correo | RF08 |
| E2E-15 | Subir un archivo de tipo no permitido o excedido muestra un error claro | RNF06 |

## Pruebas de la regla de vigencia (unitarias, obligatorias)

Casos de borde: `visibleFrom` y `visibleUntil` nulos; `now` justo en el límite; contenido `PAUSED`; ciclo que deja de ser público; dos ciclos con `publicCurrent` (debe ser imposible: restricción en servicio y prueba); zona horaria (medianoche en Buenos Aires).

## Criterios de salida para cada hito

| Hito | Criterio |
|---|---|
| Demostración intermedia | Sitio público con datos semilla; login; moderación de punta a punta con dobles |
| Versión funcional (semana 13) | Todos los Must con E2E en verde; 0 errores bloqueantes; Lighthouse en umbral; prueba de concepto de Instagram documentada |
| Cierre | Manual de usuario y documentación técnica; respaldo restaurado en una prueba; editores completan las 3 tareas típicas sin asistencia |
