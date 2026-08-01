# -*- coding: utf-8 -*-
"""Gera diagramas PNG do Byla Financeiro para o portfolio.

Regras:
- Acentos so via escapes Unicode
- Sem middle-dot, emdash, seta Unicode, aspas curvas ou bullet
- Padding generoso para o texto nao cortar na borda do card
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(r"C:\Users\55719\levi-tude.github.io\public\images\byla")

a = "\u00e1"
e = "\u00e9"
i = "\u00ed"
o = "\u00f3"
u = "\u00fa"
c = "\u00e7"
at = "\u00e3"  # a til
ot = "\u00f5"  # o til
At = "\u00c3"  # A til


def font(size: int, bold: bool = False):
    path = r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf"
    return ImageFont.truetype(path, size)


def box(draw, xy, fill, outline, width=3, radius=18):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def put(draw, xy, s, fnt, fill="#0a1620"):
    draw.text(xy, s, font=fnt, fill=fill)


def arrow_h(draw, x0, y, x1, color="#0f7f7a"):
    draw.line([(x0, y), (x1 - 14, y)], fill=color, width=4)
    draw.polygon([(x1 - 16, y - 9), (x1, y), (x1 - 16, y + 9)], fill=color)


def arrow_up(draw, x, y0, y1, color="#b45309"):
    draw.line([(x, y0), (x, y1 + 14)], fill=color, width=4)
    draw.polygon([(x - 9, y1 + 16), (x, y1), (x + 9, y1 + 16)], fill=color)


def save(img, name):
    path = OUT / name
    img.save(path, "PNG", optimize=True)
    print("saved", path.name, path.stat().st_size)


def card(draw, x, y, w, h, fill, outline, title, lines):
    box(draw, (x, y, x + w, y + h), fill, outline)
    put(draw, (x + 24, y + 24), title, font(24, True))
    yy = y + 78
    for line in lines:
        put(draw, (x + 24, yy), line, font(18), "#243642")
        yy += 36


def make_arquitetura():
    img = Image.new("RGB", (1600, 1040), "#f7fafb")
    d = ImageDraw.Draw(img)

    put(d, (48, 28), "Arquitetura - Byla Financeiro", font(34, True))
    put(
        d,
        (48, 74),
        f"Diagrama conceitual de portf{o}lio - sem dados reais, URLs ou tokens",
        font(20),
        "#5a717c",
    )

    box(d, (980, 34, 1010, 56), "#e6f5f3", "#0f7f7a", 2, 4)
    put(d, (1020, 36), "Sistema atual", font(16), "#243642")
    box(d, (1180, 34, 1210, 56), "#fff7ed", "#b45309", 2, 4)
    put(d, (1220, 36), "Legado", font(16), "#243642")
    box(d, (1320, 34, 1350, 56), "#f0f7f8", "#0c3b47", 2, 4)
    put(d, (1360, 36), f"Automa{c}{ot}es", font(16), "#243642")

    card(
        d, 48, 120, 450, 280, "#e6f5f3", "#0f7f7a", "Frontend",
        [
            "React + TypeScript (Vite)",
            "UI operacional e financeira",
            "Hospedagem: Vercel",
            f"Pap{e}is: Admin / Secretaria",
        ],
    )
    card(
        d, 575, 120, 450, 280, "#e6f5f3", "#0f7f7a", "Backend",
        [
            "Node.js + Express",
            f"Regras de neg{o}cio e APIs",
            "JWT + RBAC (requireRoles)",
            "Hospedagem: Render",
        ],
    )
    card(
        d, 1102, 120, 450, 280, "#e6f5f3", "#0f7f7a", "Armazenamento",
        [
            "Supabase + PostgreSQL",
            f"Fonte prim{a}ria de dados",
            f"Auth / perfil / dom{i}nio",
            "RLS e views oficiais",
        ],
    )
    arrow_h(d, 498, 250, 575)
    put(d, (505, 218), f"API de neg{o}cio", font(14), "#5a717c")
    arrow_h(d, 1025, 250, 1102)
    put(d, (1035, 218), f"Persist{e}ncia", font(14), "#5a717c")
    put(d, (48, 420), "Auth / perfil: frontend -> Supabase (JWT)", font(18), "#0369a1")

    card(
        d, 48, 460, 450, 280, "#f0f7f8", "#0c3b47", f"Automa{c}{ot}es n8n",
        [
            f"Jobs peri{o}dicos",
            f"Sync e relat{o}rios com IA",
            "WhatsApp (aluguel de salas)",
            "Fora do app interativo",
        ],
    )
    card(
        d, 575, 460, 450, 280, "#fff7ed", "#b45309", "Google Sheets (legado)",
        [
            f"Migra{c}{at}o gradual",
            "Leitura/escrita controlada",
            "Somente via backend",
            "Sem UI direta no painel",
        ],
    )
    card(
        d, 1102, 460, 450, 280, "#e6f5f3", "#0f7f7a", f"Dom{i}nio (resumo)",
        [
            "Alunos / modalidades",
            "Pagamentos / caixa",
            "Financeiro oficial (admin)",
            "Sem valores ou PII neste desenho",
        ],
    )
    arrow_h(d, 498, 590, 575)
    put(d, (515, 558), "Jobs / sync", font(14), "#0c3b47")
    arrow_up(d, 800, 460, 400)
    put(d, (812, 415), "Ponte legado", font(14), "#b45309")
    arrow_h(d, 1025, 590, 1102)
    put(d, (1050, 558), f"Dom{i}nio", font(14), "#5a717c")

    box(d, (48, 770, 1552, 1000), "#ffffff", "#d7e3e7", 2)
    put(d, (72, 800), "Acesso por perfil (camada de aplicativo)", font(24, True))
    put(
        d,
        (72, 850),
        "Secretaria - fluxo de caixa operacional, aluguel de salas e perfil",
        font(20),
        "#243642",
    )
    put(
        d,
        (72, 890),
        f"Admin - financeiro oficial, valida{c}{at}o, calend{a}rio, relat{o}rios e vis{at}o geral (+ rotas da secretaria)",
        font(20),
        "#243642",
    )
    put(
        d,
        (72, 935),
        f"Seguran{c}a: segrega{c}{at}o de acesso na UI/rotas; dados sens{i}veis restritos ao admin",
        font(18),
        "#5a717c",
    )
    put(
        d,
        (72, 968),
        f"Produ{c}{at}o: Vercel (frontend) + Render (backend) - migra{c}{at}o Sheets ainda progressiva",
        font(18),
        "#5a717c",
    )
    save(img, "byla-arquitetura.png")


def make_migracao():
    img = Image.new("RGB", (1600, 940), "#f7fafb")
    d = ImageDraw.Draw(img)
    put(d, (48, 28), f"Migra{c}{at}o gradual: Sheets -> Supabase", font(34, True))
    put(
        d,
        (48, 74),
        "Sem valores, nomes reais ou IDs - apenas o desenho do fluxo",
        font(20),
        "#5a717c",
    )

    steps = [
        (48, "#fff7ed", "#b45309", "1. Legado", ["Google Sheets", "Alunos e pagamentos", "Caixa operacional", "Fonte anterior"]),
        (432, "#e6f5f3", "#0f7f7a", "2. Backend", ["Parsers e regras", f"de dom{i}nio", "Sync controlado", "Node/Express"]),
        (816, "#e6f5f3", "#0f7f7a", f"3. Fonte prim{a}ria", ["Supabase/PostgreSQL", "Auth / RLS / tabelas", "Fonte do painel", "Dados oficiais"]),
        (1200, "#f0f7f8", "#0c3b47", "4. Interface", ["Painel React", "Usado pela equipe", "Admin e secretaria", f"Em produ{c}{at}o"]),
    ]
    for x, fill, stroke, title, lines in steps:
        card(d, x, 130, 352, 290, fill, stroke, title, lines)

    for x0, x1 in ((400, 432), (784, 816), (1168, 1200)):
        arrow_h(d, x0, 265, x1)

    box(d, (48, 460, 1552, 900), "#ffffff", "#d7e3e7", 2)
    put(d, (72, 500), f"Como a migra{c}{at}o acontece na pr{a}tica", font(24, True))
    bullets = [
        f"Reaproveitamento de parsers e regras j{a} usadas na planilha (alunos, modalidades, pagamentos, caixa).",
        f"Conviv{e}ncia controlada entre planilha e sistema at{e} a equipe consolidar o uso do painel.",
        f"Migra{c}{at}o progressiva: n{at}o {e} big bang e ainda n{at}o est{a} 100% conclu{i}da.",
        f"Seguran{c}a: a secretaria n{at}o v{e} o extrato oficial; o admin acessa o financeiro completo.",
    ]
    yy = 560
    for b in bullets:
        put(d, (72, yy), "-  " + b, font(20), "#243642")
        yy += 58
    save(img, "byla-migracao.png")


def make_rbac():
    img = Image.new("RGB", (1600, 1020), "#f7fafb")
    d = ImageDraw.Draw(img)
    put(d, (48, 28), f"RBAC por perfil - navega{c}{at}o do aplicativo", font(34, True))
    put(
        d,
        (48, 74),
        f"Menus e rotas por papel - sem tokens, URLs internas ou pol{i}ticas de banco",
        font(20),
        "#5a717c",
    )

    box(d, (48, 120, 760, 960), "#ffffff", "#d7e3e7", 2)
    d.rounded_rectangle([48, 120, 760, 210], radius=18, fill="#0f7f7a")
    d.rectangle([48, 180, 760, 210], fill="#0f7f7a")
    put(d, (72, 145), "Secretaria", font(28, True), "#ffffff")
    put(d, (72, 182), "Fluxo operacional do dia a dia", font(18), "#e6f5f3")

    put(d, (72, 240), "PODE", font(16, True), "#5a717c")
    for idx, label in enumerate(
        [
            "Fluxo de caixa operacional (alunos/pagamentos)",
            "Aluguel de salas",
            "Perfil",
        ]
    ):
        y = 280 + idx * 72
        box(d, (72, y, 736, y + 54), "#e6f5f3", "#0f7f7a", 2, 10)
        put(d, (92, y + 15), label, font(18), "#0a1620")

    put(d, (72, 520), f"N{At}O PODE", font(16, True), "#5a717c")
    for idx, label in enumerate(
        [
            f"Extrato e transa{c}{ot}es oficiais",
            f"Entradas/despesas do financeiro banc{a}rio",
            f"Relat{o}rios financeiros administrativos",
        ]
    ):
        y = 560 + idx * 72
        box(d, (72, y, 736, y + 54), "#f7fafb", "#d7e3e7", 2, 10)
        put(d, (92, y + 15), label, font(18), "#5a717c")

    box(d, (840, 120, 1552, 960), "#ffffff", "#d7e3e7", 2)
    d.rounded_rectangle([840, 120, 1552, 210], radius=18, fill="#0c3b47")
    d.rectangle([840, 180, 1552, 210], fill="#0c3b47")
    put(d, (864, 145), "Admin", font(28, True), "#ffffff")
    put(d, (864, 182), f"Gest{at}o completa + rotas da secretaria", font(18), "#e6f5f3")

    put(d, (864, 240), "INCLUI SECRETARIA", font(16, True), "#5a717c")
    box(d, (864, 280, 1180, 334), "#f7fafb", "#5a717c", 2, 10)
    put(d, (884, 296), "Fluxo de caixa", font(18))
    box(d, (1200, 280, 1528, 334), "#f7fafb", "#5a717c", 2, 10)
    put(d, (1220, 296), "Aluguel / Perfil", font(18))

    put(d, (864, 360), "FINANCEIRO OFICIAL", font(16, True), "#5a717c")
    for x1, y, x2, lab in [
        (864, 400, 1180, f"Vis{at}o geral"),
        (1200, 400, 1528, f"Transa{c}{ot}es"),
        (864, 462, 1180, "Entradas"),
        (1200, 462, 1528, "Despesas"),
        (864, 524, 1528, "Controle de caixa"),
    ]:
        box(d, (x1, y, x2, y + 48), "#f0f7f8", "#0c3b47", 2, 10)
        put(d, (x1 + 20, y + 12), lab, font(18))

    put(d, (864, 600), "VALIDACAO E RELATORIOS", font(16, True), "#5a717c")
    # titulo com acentos corretos
    d.rectangle([864, 590, 1528, 630], fill="#ffffff")
    put(d, (864, 600), "VALIDA" + "\u00c7\u00c3O E RELAT\u00d3RIOS", font(16, True), "#5a717c")

    for x1, y, x2, lab in [
        (864, 640, 1180, f"Valida{c}{at}o de pagamentos"),
        (1200, 640, 1528, f"Calend{a}rio financeiro"),
        (864, 702, 1180, f"Relat{o}rios com IA"),
        (1200, 702, 1528, "Performance / atividade"),
    ]:
        box(d, (x1, y, x2, y + 48), "#f0f7f8", "#0c3b47", 2, 10)
        put(d, (x1 + 16, y + 12), lab, font(17))

    put(d, (864, 790), f"Diferen{c}a de perfil na UI e nas rotas;", font(18), "#5a717c")
    put(d, (864, 828), f"conte{u}do financeiro oficial restrito ao admin.", font(18), "#5a717c")
    save(img, "byla-rbac.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    make_arquitetura()
    make_migracao()
    make_rbac()
    print("done")
