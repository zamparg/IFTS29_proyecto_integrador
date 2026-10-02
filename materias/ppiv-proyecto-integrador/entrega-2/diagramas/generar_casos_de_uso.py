"""Genera 01-casos-de-uso.svg (UML estándar: actores, frontera, include/extend, generalización).

Uso: python generar_casos_de_uso.py
Para el PNG: chrome --headless --screenshot=01-casos-de-uso.png --window-size=1200,1400 01-casos-de-uso.svg
"""
from xml.sax.saxutils import escape

W, H = 1200, 1400
BLUE, INK, SOFT, FILL, ACCENT = "#24507f", "#1a1f2b", "#4d5566", "#e2ebf5", "#f7e5d8"
CX, RX, RY = 600, 152, 24

out = []
def add(s): out.append(s)

def actor(x, y, label, secondary=False):
    c = BLUE
    add(f'<circle cx="{x}" cy="{y}" r="12" fill="white" stroke="{c}" stroke-width="2"/>')
    add(f'<line x1="{x}" y1="{y+12}" x2="{x}" y2="{y+48}" stroke="{c}" stroke-width="2"/>')
    add(f'<line x1="{x-22}" y1="{y+24}" x2="{x+22}" y2="{y+24}" stroke="{c}" stroke-width="2"/>')
    add(f'<line x1="{x}" y1="{y+48}" x2="{x-18}" y2="{y+78}" stroke="{c}" stroke-width="2"/>')
    add(f'<line x1="{x}" y1="{y+48}" x2="{x+18}" y2="{y+78}" stroke="{c}" stroke-width="2"/>')
    for i, line in enumerate(label.split("|")):
        add(f'<text x="{x}" y="{y+98+i*16}" text-anchor="middle" font-size="13" font-weight="700" fill="{INK}">{escape(line)}</text>')
    if secondary:
        add(f'<text x="{x}" y="{y+98+len(label.split("|"))*16}" text-anchor="middle" font-size="11" fill="{SOFT}">«actor secundario»</text>')

def uc(y, label, fill=FILL):
    lines = label.split("|")
    add(f'<ellipse cx="{CX}" cy="{y}" rx="{RX}" ry="{RY}" fill="{fill}" stroke="{BLUE}" stroke-width="1.6"/>')
    for i, line in enumerate(lines):
        dy = y + 5 + (i - (len(lines) - 1) / 2) * 15
        add(f'<text x="{CX}" y="{dy}" text-anchor="middle" font-size="13.5" fill="{INK}">{escape(line)}</text>')

def line(x1, y1, x2, y2, dashed=False, arrow=False, hollow=False):
    extra = ' stroke-dasharray="6 4"' if dashed else ""
    marker = ' marker-end="url(#open)"' if arrow else (' marker-end="url(#hollow)"' if hollow else "")
    add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{SOFT}" stroke-width="1.3"{extra}{marker}/>')

# --- datos -------------------------------------------------------------
public = ["Ver novedades y eventos", "Consultar plan de estudios", "Ver plantel docente",
          "Consultar horarios y|mesas de examen vigentes", "Ver galería de imágenes y videos",
          "Acceder a enlaces de interés|(SIU, Aulas Virtuales, Mi Argentina)", "Enviar consulta de contacto"]
panel = ["Iniciar sesión", "Gestionar novedades y eventos", "Archivar y reactivar contenido",
         "Seleccionar publicaciones de redes", "Importar publicaciones de Instagram",
         "Gestionar plantel y plan de estudios", "Gestionar horarios y mesas de examen",
         "Gestionar galería", "Gestionar enlaces y secciones institucionales",
         "Revisar mensajes de contacto", "Gestionar usuarios y permisos"]
py = [136 + i * 64 for i in range(len(public))]
ay = [660 + i * 66 for i in range(len(panel))]

add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Arial, Helvetica, sans-serif">')
add('<defs>'
    f'<marker id="open" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10" fill="none" stroke="{SOFT}" stroke-width="1.4"/></marker>'
    f'<marker id="hollow" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" orient="auto"><path d="M1,1 L11,6 L1,11 Z" fill="white" stroke="{SOFT}" stroke-width="1.4"/></marker>'
    '</defs>')
add(f'<rect width="{W}" height="{H}" fill="white"/>')

# frontera del sistema
add(f'<rect x="300" y="40" width="600" height="{H-80}" rx="6" fill="none" stroke="{BLUE}" stroke-width="2"/>')
add(f'<text x="{CX}" y="70" text-anchor="middle" font-size="17" font-weight="700" fill="{BLUE}">Plataforma web IFTS N°2</text>')
add(f'<text x="{CX}" y="90" text-anchor="middle" font-size="12" fill="{SOFT}">Sitio público</text>')
sep = 576
add(f'<line x1="300" y1="{sep}" x2="900" y2="{sep}" stroke="{BLUE}" stroke-width="1" stroke-dasharray="3 5"/>')
add(f'<text x="{CX}" y="{sep+24}" text-anchor="middle" font-size="12" fill="{SOFT}">Panel de administración</text>')
add(f'<text x="{CX}" y="{sep+40}" text-anchor="middle" font-size="11" font-style="italic" fill="{SOFT}">Todos los casos del panel requieren «Iniciar sesión»</text>')

# actores
VX, EX, MX = 130, 1070, 130
vis_y, ed_y, adm_y, meta_y = 270, 850, 1210, 840
actor(VX, vis_y, "Visitante|(público, alumno,|aspirante, egresado)")
actor(MX, meta_y, "API de Instagram|y Facebook (Meta)", secondary=True)
actor(EX, ed_y, "Editor|(docente de comunicación)")
actor(EX, adm_y, "Administrador")

# casos de uso
for y, l in zip(py, public): uc(y, l)
for y, l in zip(ay, panel): uc(y, l, ACCENT if l == "Iniciar sesión" else FILL)

# asociaciones visitante
for y in py:
    line(VX + 26, vis_y + 24, CX - RX + 6, y)
# editor -> casos (todos menos archivar, importar, usuarios)
for i, y in enumerate(ay):
    if i in (2, 4, 10): continue
    line(EX - 26, ed_y + 24, CX + RX - 6, y)
# admin -> usuarios
line(EX - 26, adm_y + 24, CX + RX - 6, ay[10])
# generalización Admin -> Editor
line(EX, adm_y - 2, EX, ed_y + 128, hollow=True)
# Meta -> importar
line(MX + 26, meta_y + 24, CX - RX + 4, ay[4])

# include / extend
def rel(y_from, y_to, text, dx):
    line(CX + dx, y_from - RY, CX + dx, y_to + RY, dashed=True, arrow=True)
    add(f'<text x="{CX+dx+8}" y="{(y_from+y_to)/2+4}" font-size="11" font-style="italic" fill="{SOFT}">{text}</text>')
rel(ay[3], ay[4], "«include»", 0) if False else None
# seleccionar (3) include importar (4): flecha hacia abajo
line(CX, ay[3] + RY, CX, ay[4] - RY - 2, dashed=True, arrow=True)
add(f'<text x="{CX+10}" y="{(ay[3]+ay[4])/2+4}" font-size="11" font-style="italic" fill="{SOFT}">«include»</text>')
# archivar (2) extend gestionar novedades (1): flecha hacia arriba
line(CX, ay[2] - RY, CX, ay[1] + RY + 2, dashed=True, arrow=True)
add(f'<text x="{CX+10}" y="{(ay[1]+ay[2])/2+4}" font-size="11" font-style="italic" fill="{SOFT}">«extend»</text>')

add('</svg>')
open("01-casos-de-uso.svg", "w", encoding="utf8").write("\n".join(out))
print("ok")
