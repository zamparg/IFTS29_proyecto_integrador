"""Compila etapa-2-documento.md -> etapa-2-documento.html -> PDF (Chrome headless).

Uso:  python build.py
Marcadores propios dentro del .md:
  {{tabla|Título}}                 pone "Tabla N" + título (APA) antes de la tabla que sigue
  {{fig|archivo|Título|Nota}}      figura numerada con imagen de diagramas/ y nota
  <!-- WIREFRAMES -->              inserta como figuras todos los PNG/JPG de wireframes/
Los números de Tabla/Figura se asignan en orden de aparición: si agregás o mové uno,
revisá las referencias cruzadas escritas a mano en el texto.
"""
import glob
import html
import os
import re
import subprocess
import sys

import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "etapa-2-documento.md")
OUT_HTML = os.path.join(HERE, "etapa-2-documento.html")
OUT_PDF = os.path.join(HERE, "Etapa 2 - Proyecto Integrador.pdf")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

text = open(SRC, encoding="utf8").read()
counters = {"tabla": 0, "fig": 0}


def inline_md(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s


def tabla(m):
    counters["tabla"] += 1
    return (f'<p class="cap"><strong>Tabla {counters["tabla"]}</strong></p>\n'
            f'<p class="cap-tit"><em>{inline_md(m.group(1))}</em></p>\n')


WIDE = ("02a", "02b", "03a", "03b", "06a", "06b", "07-", "08-", "09a", "09b", "wireframes/")


def figure_html(src, title, note):
    counters["fig"] += 1
    wide = ' class="ancho"' if any(w in src for w in WIDE) else ""
    note = html.escape(note, quote=False)
    note = re.sub(r"^Nota\.", "<em>Nota.</em>", note)
    note_html = f'<figcaption>{note}</figcaption>' if note else ""
    return (f'<figure{wide}><p class="cap"><strong>Figura {counters["fig"]}</strong></p>'
            f'<p class="cap-tit"><em>{inline_md(title)}</em></p>'
            f'<img src="{src}" alt="{html.escape(title)}">{note_html}</figure>')


def fig(m):
    return figure_html("diagramas/" + m.group(1), m.group(2), m.group(3))


text = re.sub(r"\{\{tabla\|(.+?)\}\}", tabla, text)
text = re.sub(r"\{\{fig\|([^|]+)\|([^|]+)\|(.+?)\}\}", fig, text, flags=re.S)


def wireframes(_):
    files = sorted(glob.glob(os.path.join(HERE, "wireframes", "*.png")) +
                   glob.glob(os.path.join(HERE, "wireframes", "*.jpg")))
    if not files:
        return ('<p class="pendiente"><em>[Pendiente: exportar de Figma las pantallas clave '
                '(inicio, novedades, horarios, galería, contacto, login y paneles) como PNG en '
                'la carpeta wireframes/ y volver a ejecutar build.py: se insertan solas.]</em></p>')
    out = []
    for f in files:
        name = os.path.splitext(os.path.basename(f))[0]
        name = re.sub(r"^\d+[-_ ]*", "", name).replace("-", " ").replace("_", " ").strip().capitalize()
        out.append(figure_html("wireframes/" + os.path.basename(f), "Wireframe: " + name, ""))
    return "\n".join(out)


text = text.replace("<!-- WIREFRAMES -->", wireframes(None))

# Numeración de encabezados (Referencias y Anexo sin número)
lines, h1, h2 = [], 0, 0
for ln in text.split("\n"):
    m1 = re.match(r"^# (.+)$", ln)
    m2 = re.match(r"^## (.+)$", ln)
    if m1:
        title = m1.group(1)
        if title.startswith(("Referencias", "Anexo")):
            ln = f"# {title}"
        else:
            h1 += 1
            h2 = 0
            ln = f"# {h1}. {title}"
    elif m2 and h1:
        h2 += 1
        ln = f"## {h1}.{h2}. {m2.group(1)}"
    lines.append(ln)
text = "\n".join(lines)

body = markdown.markdown(text, extensions=["tables", "sane_lists"])
# Secciones con diagramas anchos -> páginas apaisadas
parts = re.split(r"(?=<h[12][ >])", body)
body = "".join(f'<div class="apaisada">{p}</div>' if 'class="ancho"' in p else p for p in parts)
# Anexo en página nueva
body = body.replace("<h1>Anexo A.", '<h1 class="nueva-pagina">Anexo A.')
body = body.replace("<h1>Referencias", '<h1 class="nueva-pagina">Referencias')

portada = """
<section class="portada">
  <p class="inst">Instituto de Formación Técnica Superior N.° 29<br>Tecnicatura Superior en Desarrollo de Software</p>
  <h1 class="titulo">Modernización del sitio institucional del IFTS N.° 2</h1>
  <p class="subtitulo">Segunda etapa: Análisis y modelado del diseño</p>
  <p class="empresa">Talento Tech</p>
  <p class="autores">Santiago Cuda · Adrián Madroñal · Martín Juan · Nicolás Rolón · Gastón Zampar</p>
  <p class="meta">Prácticas Profesionalizantes IV<br>
  Docentes: Prof. Lic. Emir García Ontiveros · Prof. Lic. Kevin Del Bello<br>
  Octubre de 2026</p>
</section>
"""

css = """
@page { size: A4; margin: 2.54cm; @top-right { content: counter(page); font: 10pt 'Times New Roman', serif; } }
@page apaisada { size: A4 landscape; margin: 2cm 2.54cm; @top-right { content: counter(page); font: 10pt 'Times New Roman', serif; } }
.apaisada { page: apaisada; }
.apaisada figure img { max-height: 12.6cm; }
.apaisada h2 { break-before: page; }
.apaisada figure ~ figure { break-before: page; }
@page :first { @top-right { content: none; } }
html { font-family: 'Times New Roman', Times, serif; font-size: 12pt; color: #000; }
body { line-height: 1.45; margin: 0; }
h1 { font-size: 13pt; font-weight: 700; text-align: center; margin: 1.6em 0 .6em; break-after: avoid; }
h2 { font-size: 12pt; font-weight: 700; text-align: left; margin: 1.3em 0 .4em; break-after: avoid; }
h3 { font-size: 12pt; font-weight: 700; font-style: italic; }
p { margin: 0 0 .7em; text-align: left; }
ul, ol { margin: 0 0 .8em 1.2em; padding-left: .8em; }
li { margin-bottom: .25em; }
a { color: #0b3d91; }
.nueva-pagina { break-before: page; margin-top: 0; }
.portada { height: 22cm; display: flex; flex-direction: column; justify-content: center; text-align: center; break-after: page; }
.portada p { text-align: center; }
.portada .inst { font-size: 12pt; margin-bottom: 3cm; }
.portada .titulo { font-size: 18pt; margin: 0 0 .5em; }
.portada .subtitulo { font-size: 14pt; margin-bottom: 2.4cm; }
.portada .empresa { font-weight: 700; font-size: 14pt; color: #24507f; }
.portada .autores { margin-bottom: 2.4cm; }
.portada .meta { font-size: 11pt; }
.cap { margin: 1.1em 0 0; font-weight: 700; break-after: avoid; }
.cap-tit { margin: 0 0 .4em; break-after: avoid; }
table { border-collapse: collapse; width: 100%; font-size: 9pt; line-height: 1.3; margin: 0 0 .5em; }
th { text-align: left; background: #e2ebf5; border-top: 1.2pt solid #000; border-bottom: 1.2pt solid #000; padding: 4px 5px; }
td { padding: 4px 5px; vertical-align: top; border-bottom: .5pt solid #bbb; }
tr { break-inside: avoid; }
tbody tr:last-child td { border-bottom: 1.2pt solid #000; }
figure { margin: 0 0 1em; break-inside: avoid; text-align: center; }
figure img { max-width: 100%; max-height: 20.5cm; width: auto; height: auto; }
figcaption { text-align: left; font-size: 10pt; margin-top: .4em; }
.pendiente { background: #fff3cd; padding: 6px 8px; border: 1px dashed #b58900; font-size: 10pt; }
"""

doc = (f'<!doctype html><html lang="es"><head><meta charset="utf-8">'
       f'<title>Etapa 2 - Proyecto Integrador - Talento Tech</title><style>{css}</style></head>'
       f'<body>{portada}{body}</body></html>')
open(OUT_HTML, "w", encoding="utf8").write(doc)
print(f"HTML ok: {counters['tabla']} tablas, {counters['fig']} figuras")

if "--no-pdf" in sys.argv:
    sys.exit(0)
if not os.path.exists(CHROME):
    sys.exit("No encuentro Chrome; abrí el HTML y exportá a PDF desde el navegador.")
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                f"--print-to-pdf={OUT_PDF}", "file:///" + OUT_HTML.replace("\\", "/")],
               check=True, capture_output=True)
print("PDF ok:", OUT_PDF)
