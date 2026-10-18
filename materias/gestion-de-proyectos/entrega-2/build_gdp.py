"""Compila parte-2.md -> HTML -> PDF (máx. 10 págs.). Uso: python build_gdp.py"""
import html, os, re, subprocess, sys
import markdown
import cpm

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_HTML = os.path.join(HERE, "parte-2.html")
OUT_PDF = os.path.join(HERE, "GDP_Comisión E_Equipo 08_TPI - Parte 2.pdf")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

text = open(os.path.join(HERE, "parte-2.md"), encoding="utf8").read()
cnt = {"tabla": 0, "fig": 0}

def inline(s):
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", html.escape(s, quote=False))

def tabla(m):
    cnt["tabla"] += 1
    return f'<p class="cap"><strong>Tabla.</strong> <em>{inline(m.group(1))}</em></p>\n'

def fig(m):
    cnt["fig"] += 1
    note = re.sub(r"^Nota\.", "<em>Nota.</em>", html.escape(m.group(3), quote=False))
    return (f'<figure><p class="cap"><strong>Figura {cnt["fig"]}.</strong> <em>{inline(m.group(2))}</em></p>'
            f'<img src="diagramas/{m.group(1)}"><figcaption>{note}</figcaption></figure>')

cpm_md, end, _ = cpm.cpm_table()
pert_md, te, sd, p13, p14 = cpm.pert_numbers()
fmt = lambda x: f"{x:.2f}".replace(".", ",")
text = (text.replace("{{CPM}}", cpm_md).replace("{{PERT}}", pert_md).replace("{{END}}", f"{end:g}")
        .replace("{{TE}}", fmt(te)).replace("{{SD}}", fmt(sd))
        .replace("{{P13}}", f"{p13*100:.0f}").replace("{{P14}}", f"{p14*100:.0f}"))
text = re.sub(r"\{\{tabla\|(.+?)\}\}", tabla, text)
text = re.sub(r"\{\{fig\|([^|]+)\|([^|]+)\|(.+?)\}\}", fig, text, flags=re.S)

body = markdown.markdown(text, extensions=["tables", "sane_lists"])
body = body.replace("<h1>Anexo A.", '<h1 class="nueva-pagina">Anexo A.')

portada = """<header class="portada"><div class="marca">TALENTO TECH</div>
<h1 class="titulo">Gestión de proyectos · Trabajo integrador, Parte 2</h1>
<p class="sub">Modernización del sitio institucional del IFTS N.° 2</p>
<p class="aut">Comisión E · Equipo 08 · Santiago Cuda · Adrián Madroñal · Martín Juan · Nicolás Rolón · Gastón Zampar</p></header>"""
css = """
@page { size: A4; margin: 1.6cm 1.7cm; @bottom-right { content: counter(page); font: 8.5pt Arial, sans-serif; color:#4d5566; } }
html { font-family: Arial, Helvetica, sans-serif; font-size: 10.5pt; color: #1a1f2b; }
body { line-height: 1.32; margin: 0; }
h1 { font-size: 13pt; color: #24507f; margin: .9em 0 .35em; border-bottom: 1.5pt solid #24507f; padding-bottom: 2px; break-after: avoid; }
h2 { font-size: 10.5pt; color: #1c3f66; margin: .8em 0 .3em; break-after: avoid; }
p { margin: 0 0 .5em; } ul, ol { margin: 0 0 .5em 1.1em; padding-left: .6em; } li { margin-bottom: .15em; }
a { color: #24507f; }
.nueva-pagina { break-before: page; }
.portada { text-align: left; margin-bottom: .4em; border-left: 5px solid #24507f; padding-left: 10px; }
.portada .marca { font-weight: 700; letter-spacing: .12em; color: #24507f; font-size: 9pt; }
.portada .titulo { font-size: 16pt; border: 0; margin: .1em 0; padding: 0; color:#1a1f2b; }
.portada .sub { font-size: 10.5pt; margin: 0; } .portada .aut { font-size: 8.5pt; color: #4d5566; margin: .2em 0 0; }
.cap { margin: .7em 0 .25em; break-after: avoid; font-size: 9pt; }
table { border-collapse: collapse; width: 100%; font-size: 8.4pt; line-height: 1.25; margin: 0 0 .5em; }
th { text-align: left; background: #e2ebf5; border-top: 1pt solid #24507f; border-bottom: 1pt solid #24507f; padding: 2.5px 3.5px; }
td { padding: 2.5px 3.5px; vertical-align: top; border-bottom: .4pt solid #c9d3e0; } tr { break-inside: avoid; }
figure { margin: 0 0 .5em; break-inside: avoid; text-align: center; } figure img { max-width: 100%; max-height: 12cm; }
figcaption { text-align: left; font-size: 8pt; color: #4d5566; }
"""
open(OUT_HTML, "w", encoding="utf8").write(
    f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>GdP Parte 2</title><style>{css}</style></head><body>{portada}{body}</body></html>')
print(f"HTML ok: {cnt['tabla']} tablas, {cnt['fig']} figuras; CPM fin={end:g} sem; P13={p13:.2f} P14={p14:.2f}")
if "--no-pdf" in sys.argv: sys.exit(0)
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={OUT_PDF}",
                "file:///" + OUT_HTML.replace("\\", "/")], check=True, capture_output=True)
import pymupdf
print("PDF:", len(pymupdf.open(OUT_PDF)), "páginas")
