"""CPM + PERT de Talento Tech (fuente de los números del documento, Parte 2).
Semanas desde el lunes 24/08/2026 (semana 1). t=0 inicio S1; t=13 fin S13; t=16 fin S16."""
import math, datetime as dt

# id: (nombre, responsable, optimista, probable, pesimista, predecesoras)
ACT = {
 "A": ("Relevamiento (reuniones y requerimientos)", "Martín", 1.5, 2, 2.5, []),
 "B": ("Análisis, documento de requerimientos y backlog", "Martín", 1.5, 2, 3, ["A"]),
 "C": ("Prototipo en Figma y preparación de la DEMO", "Gastón", 2, 3, 4, ["A"]),
 "D": ("Modelado: diagramas UML y modelo de datos", "Nicolás", 2, 3, 4, ["A"]),
 "E": ("DEMO con el cliente (S6) y ajustes", "Martín", 0.5, 1, 2, ["C", "D"]),
 "F": ("Arquitectura, repositorio, CI/CD y hosting", "Santiago", 0.5, 1, 1.5, ["B", "D"]),
 "G": ("Backend: API, base de datos y autenticación", "Nicolás", 4, 5, 7, ["F"]),
 "H": ("Frontend del sitio público", "Gastón", 4, 5, 6, ["E", "F"]),
 "I": ("Panel de administración", "Gastón y Nicolás", 4, 6, 7, ["E", "F"]),
 "J": ("Integración con Instagram (PoC y módulo)", "Nicolás", 1.5, 2, 3, ["G"]),
 "K": ("QA pruebas de integración y aceptación", "Adrián", 1.5, 2, 3, ["G"]),
 "M": ("HITO: versión funcional (reunión 3, S13)", "Todos", 0, 0, 0, ["H", "I", "J", "K"]),
 "L": ("Capacitación a los editores", "Martín", 1.5, 2, 2.5, ["M"]),
 "N": ("Manual de usuario y documentación técnica", "Gastón y Adrián", 2, 3, 4, ["M"]),
 "O": ("Correcciones posteriores a la reunión 3", "Todos", 0.5, 1, 1.5, ["M"]),
 "P": ("Cierre, traspaso y mantenimiento inicial", "Santiago", 0.5, 1, 1.5, ["L", "O"]),
}
ORDER = list(ACT)

def cpm(use=lambda a: a[3]):
    es, ef = {}, {}
    for k in ORDER:
        n, r, o, m, p, pre = ACT[k]
        es[k] = max([ef[x] for x in pre], default=0)
        ef[k] = es[k] + use(ACT[k])
    end = max(ef.values())
    lf, ls = {}, {}
    for k in reversed(ORDER):
        succ = [s for s in ORDER if k in ACT[s][5]]
        lf[k] = min([ls[s] for s in succ], default=end)
        ls[k] = lf[k] - use(ACT[k])
    slack = {k: round(ls[k] - es[k], 2) for k in ORDER}
    return es, ef, ls, lf, slack, end

def te(a): return (a[2] + 4 * a[3] + a[4]) / 6
def var(a): return ((a[4] - a[2]) / 6) ** 2

def phi(z): return 0.5 * (1 + math.erf(z / math.sqrt(2)))

def week_date(t):
    return dt.date(2026, 8, 24) + dt.timedelta(days=round(t * 7))

def cpm_table():
    es, ef, ls, lf, sl, end = cpm()
    rows = ["| ID | Actividad | Resp. | Dur. (sem) | Pred. | ES | EF | LS | LF | Holgura | Crít. |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for k in ORDER:
        n, r, o, m, p, pre = ACT[k]
        rows.append(f"| {k} | {n} | {r} | {m:g} | {', '.join(pre) or '—'} | {es[k]:g} | {ef[k]:g} | {ls[k]:g} | {lf[k]:g} | {sl[k]:g} | {'**Sí**' if sl[k] == 0 else 'No'} |")
    return "\n".join(rows), end, sl

def pert_numbers():
    es, ef, ls, lf, sl, end = cpm()
    crit_to_hito = ["A", "D", "F", "G", "J"]  # K es paralela e idéntica en te
    rows = ["| Act. | Optimista | Probable | Pesimista | Esperada te | Varianza |", "|---|---|---|---|---|---|"]
    tot_t = tot_v = 0
    for k in crit_to_hito:
        a = ACT[k]
        rows.append(f"| {k} | {a[2]:g} | {a[3]:g} | {a[4]:g} | {te(a):.2f} | {var(a):.3f} |")
        tot_t += te(a); tot_v += var(a)
    sd = math.sqrt(tot_v)
    p13 = phi((13 - tot_t) / sd); p14 = phi((14 - tot_t) / sd)
    rows.append(f"| **Ruta crítica hasta el hito** | | | | **{tot_t:.2f}** | **{tot_v:.3f}** |")
    return "\n".join(rows), tot_t, sd, p13, p14

def gantt_mmd():
    es, ef, ls, lf, sl, end = cpm()
    L = ["gantt", "    dateFormat YYYY-MM-DD", "    axisFormat %d/%m", "    tickInterval 1week", "    title Cronograma Talento Tech - 16 semanas (24/08 al 11/12/2026)"]
    sec = {"Análisis y diseño": "ABCDE", "Base técnica": "F", "Desarrollo y pruebas": "GHIJK", "Entrega y cierre": "MLNOP"}
    for s, ids in sec.items():
        L.append(f"    section {s}")
        for k in ids:
            n, r, o, m, p, pre = ACT[k]
            a = week_date(es[k]); b = week_date(ef[k])
            tag = "crit, " if sl[k] == 0 else ""
            short = n.split(" (")[0].split(":")[0].replace(",", "")
            if k == "M":
                L.append(f"    Hito S13 versión funcional :milestone, crit, {k}, {week_date(13) - dt.timedelta(days=3)}, 0d")
            else:
                L.append(f"    {k} · {short} :{tag}{k.lower()}, {a}, {max((b - a).days, 3)}d")
    L.append(f"    section Hitos con el cliente")
    L.append(f"    Reunión 1 (relevamiento) :milestone, r1, 2026-09-04, 0d")
    L.append(f"    Reunión 2 (DEMO) :milestone, r2, 2026-10-06, 0d")
    return "\n".join(L)

def network_mmd():
    es, ef, ls, lf, sl, end = cpm()
    L = ["flowchart LR"]
    for k in ORDER:
        n = ACT[k][0].split(" (")[0].split(":")[0]
        L.append(f'    {k}["<b>{k}</b> · {n}<br/>{ACT[k][3]:g} sem · ES {es[k]:g} / EF {ef[k]:g}<br/>holgura {sl[k]:g}"]')
    for k in ORDER:
        for p in ACT[k][5]:
            L.append(f"    {p} --> {k}")
    L.append("    classDef crit fill:#f3dcdc,stroke:#7a3a32,stroke-width:2px,color:#1a1f2b")
    L.append("    classDef norm fill:#e2ebf5,stroke:#24507f,color:#1a1f2b")
    L.append("    class " + ",".join(k for k in ORDER if sl[k] == 0) + " crit")
    L.append("    class " + ",".join(k for k in ORDER if sl[k] != 0) + " norm")
    return "\n".join(L)

if __name__ == "__main__":
    t, end, sl = cpm_table(); print(t); print("fin", end)
    p, tt, sd, p13, p14 = pert_numbers(); print(p); print(tt, sd, p13, p14)
