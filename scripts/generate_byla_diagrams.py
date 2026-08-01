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
    # Grade 3 colunas alinhadas; altura do card = padding + conteudo
    col_w = 460
    gap = 50
    left = 48
    cols = [left, left + col_w + gap, left + 2 * (col_w + gap)]
    pad = 28
    line_h = 38
    title_block = 52

    def card_h(n):
        return pad + title_block + n * line_h + pad

    def draw_card(d, x, y, w, h, fill, outline, title, lines):
        box(d, (x, y, x + w, y + h), fill, outline)
        put(d, (x + pad, y + pad), title, font(24, True))
        yy = y + pad + title_block
        for line in lines:
            put(d, (x + pad, yy), line, font(18), "#243642")
            yy += line_h

    row1_y = 120
    h1 = card_h(4)
    auth_band_h = 48
    row2_y = row1_y + h1 + 28 + auth_band_h + 28
    h2 = card_h(4)
    footer_y = row2_y + h2 + 36
    footer_h = 190
    W = cols[2] + col_w + 48
    H = footer_y + footer_h + 40

    img = Image.new("RGB", (W, H), "#f7fafb")
    d = ImageDraw.Draw(img)

    put(d, (48, 28), "Arquitetura - Byla Financeiro", font(34, True))
    put(
        d,
        (48, 74),
        f"Diagrama conceitual de portf{o}lio - sem URLs ou tokens",
        font(20),
        "#5a717c",
    )

    lx = W - 560
    box(d, (lx, 34, lx + 30, 56), "#e6f5f3", "#0f7f7a", 2, 4)
    put(d, (lx + 40, 36), "Sistema atual", font(16), "#243642")
    box(d, (lx + 180, 34, lx + 210, 56), "#fff7ed", "#b45309", 2, 4)
    put(d, (lx + 220, 36), "Legado", font(16), "#243642")
    box(d, (lx + 310, 34, lx + 340, 56), "#f0f7f8", "#0c3b47", 2, 4)
    put(d, (lx + 350, 36), f"Automa{c}{ot}es", font(16), "#243642")

    draw_card(
        d,
        cols[0],
        row1_y,
        col_w,
        h1,
        "#e6f5f3",
        "#0f7f7a",
        "Frontend",
        [
            "React + TypeScript (Vite)",
            "UI operacional e financeira",
            "Hospedagem: Vercel",
            f"Pap{e}is: Admin / Secretaria",
        ],
    )
    draw_card(
        d,
        cols[1],
        row1_y,
        col_w,
        h1,
        "#e6f5f3",
        "#0f7f7a",
        "Backend",
        [
            "Node.js + Express",
            f"Regras de neg{o}cio e APIs",
            "JWT + RBAC (requireRoles)",
            "Hospedagem: Render",
        ],
    )
    draw_card(
        d,
        cols[2],
        row1_y,
        col_w,
        h1,
        "#e6f5f3",
        "#0f7f7a",
        "Armazenamento",
        [
            "Supabase + PostgreSQL",
            f"Fonte prim{a}ria de dados",
            f"Auth / perfil / dom{i}nio",
            "RLS e views oficiais",
        ],
    )

    mid_y = row1_y + h1 // 2
    arrow_h(d, cols[0] + col_w + 4, mid_y, cols[1] - 4)
    put(d, (cols[0] + col_w + 8, mid_y - 26), f"API de neg{o}cio", font(13), "#5a717c")
    arrow_h(d, cols[1] + col_w + 4, mid_y, cols[2] - 4)
    put(d, (cols[1] + col_w + 10, mid_y - 26), f"Persist{e}ncia", font(13), "#5a717c")

    auth_y = row1_y + h1 + 28
    box(
        d,
        (cols[0], auth_y, cols[2] + col_w, auth_y + auth_band_h),
        "#ffffff",
        "#d7e3e7",
        2,
        10,
    )
    put(
        d,
        (cols[0] + 18, auth_y + 14),
        f"Auth / perfil: frontend -> Supabase (JWT)   |   Opera{c}{ot}es: frontend -> backend -> banco",
        font(16),
        "#0369a1",
    )

    draw_card(
        d,
        cols[0],
        row2_y,
        col_w,
        h2,
        "#f0f7f8",
        "#0c3b47",
        f"Automa{c}{ot}es n8n",
        [
            f"Jobs peri{o}dicos",
            f"Sync e relat{o}rios com IA",
            "WhatsApp (aluguel de salas)",
            "Fora do app interativo",
        ],
    )
    draw_card(
        d,
        cols[1],
        row2_y,
        col_w,
        h2,
        "#fff7ed",
        "#b45309",
        "Google Sheets (legado)",
        [
            f"Migra{c}{at}o gradual",
            "Leitura/escrita controlada",
            "Somente via backend",
            "Sem UI direta no painel",
        ],
    )
    draw_card(
        d,
        cols[2],
        row2_y,
        col_w,
        h2,
        "#e6f5f3",
        "#0f7f7a",
        f"Dom{i}nio (resumo)",
        [
            "Alunos / modalidades",
            "Pagamentos / caixa",
            "Financeiro oficial (admin)",
            "Sem valores ou PII neste desenho",
        ],
    )

    mid2 = row2_y + h2 // 2
    arrow_h(d, cols[0] + col_w + 4, mid2, cols[1] - 4, "#0c3b47")
    put(d, (cols[0] + col_w + 12, mid2 - 26), "Jobs / sync", font(13), "#0c3b47")
    bridge_x = cols[1] + col_w // 2
    arrow_up(d, bridge_x, row2_y, auth_y + auth_band_h)
    put(d, (bridge_x + 14, row2_y - 22), "Ponte legado", font(13), "#b45309")
    arrow_h(d, cols[1] + col_w + 4, mid2, cols[2] - 4)
    put(d, (cols[1] + col_w + 16, mid2 - 26), f"Dom{i}nio", font(13), "#5a717c")

    box(d, (48, footer_y, W - 48, footer_y + footer_h), "#ffffff", "#d7e3e7", 2)
    put(d, (72, footer_y + 22), "Acesso por perfil (camada de aplicativo)", font(22, True))
    put(
        d,
        (72, footer_y + 64),
        "Secretaria - fluxo de caixa operacional, aluguel de salas e perfil",
        font(18),
        "#243642",
    )
    put(
        d,
        (72, footer_y + 96),
        f"Admin - financeiro oficial, valida{c}{at}o, calend{a}rio, relat{o}rios e vis{at}o geral (+ rotas da secretaria)",
        font(18),
        "#243642",
    )
    put(
        d,
        (72, footer_y + 132),
        f"Seguran{c}a: segrega{c}{at}o na UI/rotas; dados sens{i}veis restritos ao admin",
        font(16),
        "#5a717c",
    )
    put(
        d,
        (72, footer_y + 158),
        f"Produ{c}{at}o: Vercel (frontend) + Render (backend) - migra{c}{at}o Sheets ainda progressiva",
        font(16),
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
        f"Migra{c}{at}o progressiva: ainda n{at}o est{a} 100% conclu{i}da.",
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
