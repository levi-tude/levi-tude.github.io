# -*- coding: utf-8 -*-
"""Gera diagramas PNG do Byla Financeiro para o portfólio."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(r"C:\Users\55719\levi-tude.github.io\public\images\byla")


def font(size: int, bold: bool = False):
    paths = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            continue
    return ImageFont.load_default()


def box(draw, xy, fill, outline, width=3, radius=16):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def txt(draw, xy, s, fnt, fill="#0a1620"):
    draw.text(xy, s, font=fnt, fill=fill)


def arrow_right(draw, x, y, color="#0f7f7a"):
    draw.rectangle([x, y - 3, x + 28, y + 3], fill=color)
    draw.polygon([(x + 28, y - 10), (x + 48, y), (x + 28, y + 10)], fill=color)


def save(img, name):
    path = OUT / name
    img.save(path, "PNG", optimize=True)
    print("saved", path.name, path.stat().st_size)


def make_arquitetura():
    w, h = 1600, 980
    img = Image.new("RGB", (w, h), "#f7fafb")
    d = ImageDraw.Draw(img)
    txt(d, (48, 36), "Arquitetura — Byla Financeiro", font(34, True))
    txt(
        d,
        (48, 84),
        "Diagrama conceitual de portfólio · sem dados reais, URLs ou tokens",
        font(20),
        "#5a717c",
    )

    lx = 900
    box(d, (lx, 40, lx + 40, 62), "#e6f5f3", "#0f7f7a", 2, 4)
    txt(d, (lx + 50, 42), "Sistema atual", font(16), "#243642")
    box(d, (lx + 200, 40, lx + 240, 62), "#fff7ed", "#b45309", 2, 4)
    txt(d, (lx + 250, 42), "Legado", font(16), "#243642")
    box(d, (lx + 340, 40, lx + 380, 62), "#f0f7f8", "#0c3b47", 2, 4)
    txt(d, (lx + 390, 42), "Automações", font(16), "#243642")

    tops = [
        (
            48,
            140,
            480,
            340,
            "#e6f5f3",
            "#0f7f7a",
            "Frontend",
            [
                "React + TypeScript (Vite)",
                "UI operacional e financeira",
                "Hospedagem: Vercel",
                "Papéis: Admin · Secretaria",
            ],
        ),
        (
            560,
            140,
            992,
            340,
            "#e6f5f3",
            "#0f7f7a",
            "Backend",
            [
                "Node.js + Express",
                "Regras de negócio e APIs",
                "JWT + RBAC (requireRoles)",
                "Hospedagem: Render",
            ],
        ),
        (
            1072,
            140,
            1552,
            340,
            "#e6f5f3",
            "#0f7f7a",
            "Armazenamento",
            [
                "Supabase + PostgreSQL",
                "Fonte primária de dados",
                "Auth · perfil · domínio",
                "RLS e views oficiais",
            ],
        ),
    ]
    for x1, y1, x2, y2, fill, stroke, title, lines in tops:
        box(d, (x1, y1, x2, y2), fill, stroke)
        txt(d, (x1 + 24, y1 + 24), title, font(24, True))
        yy = y1 + 78
        for line in lines:
            txt(d, (x1 + 24, yy), line, font(18), "#243642")
            yy += 36

    arrow_right(d, 492, 240)
    txt(d, (500, 205), "API de negócio", font(14), "#5a717c")
    arrow_right(d, 1004, 240)
    txt(d, (1012, 205), "Persistência", font(14), "#5a717c")
    txt(d, (480, 360), "Auth / perfil: frontend → Supabase (JWT)", font(18), "#0369a1")

    bots = [
        (
            48,
            420,
            480,
            620,
            "#f0f7f8",
            "#0c3b47",
            "Automações n8n",
            [
                "Jobs periódicos",
                "Sync e relatórios com IA",
                "WhatsApp (aluguel de salas)",
                "Fora do app interativo",
            ],
        ),
        (
            560,
            420,
            992,
            620,
            "#fff7ed",
            "#b45309",
            "Google Sheets (legado)",
            [
                "Migração gradual",
                "Leitura/escrita controlada",
                "Somente via backend",
                "Sem UI direta no painel",
            ],
        ),
        (
            1072,
            420,
            1552,
            620,
            "#e6f5f3",
            "#0f7f7a",
            "Domínio (resumo)",
            [
                "Alunos · modalidades",
                "Pagamentos · caixa",
                "Financeiro oficial (admin)",
                "Sem valores ou PII neste desenho",
            ],
        ),
    ]
    for x1, y1, x2, y2, fill, stroke, title, lines in bots:
        box(d, (x1, y1, x2, y2), fill, stroke)
        txt(d, (x1 + 24, y1 + 24), title, font(22, True))
        yy = y1 + 78
        for line in lines:
            txt(d, (x1 + 24, yy), line, font(18), "#243642")
            yy += 34

    arrow_right(d, 492, 520)
    txt(d, (498, 485), "Jobs / sync", font(14), "#0c3b47")
    # Ponte legado: Sheets sobe para o backend (conceito)
    d.rectangle([760, 340, 766, 420], fill="#b45309")
    d.polygon([(750, 340), (763, 318), (776, 340)], fill="#b45309")
    txt(d, (780, 350), "Ponte legado", font(14), "#b45309")
    arrow_right(d, 1004, 520)
    txt(d, (1010, 485), "Domínio", font(14), "#5a717c")

    box(d, (48, 660, 1552, 920), "#ffffff", "#d7e3e7", 2)
    txt(d, (72, 690), "Acesso por perfil (camada de aplicativo)", font(24, True))
    txt(
        d,
        (72, 740),
        "Secretaria — fluxo de caixa operacional, aluguel de salas e perfil",
        font(20),
        "#243642",
    )
    txt(
        d,
        (72, 780),
        "Admin — financeiro oficial, validação, calendário, relatórios e visão geral (+ rotas da secretaria)",
        font(20),
        "#243642",
    )
    txt(
        d,
        (72, 830),
        "Segurança: segregação de acesso na UI/rotas; dados sensíveis restritos ao admin",
        font(18),
        "#5a717c",
    )
    txt(
        d,
        (72, 870),
        "Produção: Vercel (frontend) + Render (backend) · migração Sheets ainda progressiva",
        font(18),
        "#5a717c",
    )
    save(img, "byla-arquitetura.png")


def make_migracao():
    w, h = 1600, 900
    img = Image.new("RGB", (w, h), "#f7fafb")
    d = ImageDraw.Draw(img)
    txt(d, (48, 36), "Migração gradual: Sheets → Supabase", font(34, True))
    txt(
        d,
        (48, 84),
        "Sem valores, nomes reais ou IDs — apenas o desenho do fluxo",
        font(20),
        "#5a717c",
    )

    steps = [
        (
            48,
            150,
            400,
            400,
            "#fff7ed",
            "#b45309",
            "1. Legado",
            ["Google Sheets", "Alunos e pagamentos", "Caixa operacional", "Fonte anterior"],
        ),
        (
            432,
            150,
            784,
            400,
            "#e6f5f3",
            "#0f7f7a",
            "2. Backend",
            ["Parsers e regras", "de domínio", "Sync controlado", "Node/Express"],
        ),
        (
            816,
            150,
            1168,
            400,
            "#e6f5f3",
            "#0f7f7a",
            "3. Fonte primária",
            ["Supabase/PostgreSQL", "Auth · RLS · tabelas", "Fonte do painel", "Dados oficiais"],
        ),
        (
            1200,
            150,
            1552,
            400,
            "#f0f7f8",
            "#0c3b47",
            "4. Interface",
            ["Painel React", "Usado pela equipe", "Admin e secretaria", "Em produção"],
        ),
    ]
    for x1, y1, x2, y2, fill, stroke, title, lines in steps:
        box(d, (x1, y1, x2, y2), fill, stroke)
        txt(d, (x1 + 22, y1 + 28), title, font(24, True))
        yy = y1 + 90
        for line in lines:
            txt(d, (x1 + 22, yy), line, font(18), "#243642")
            yy += 36

    for x in (408, 792, 1176):
        arrow_right(d, x, 270)

    box(d, (48, 450, 1552, 840), "#ffffff", "#d7e3e7", 2)
    txt(d, (72, 490), "Como a migração acontece na prática", font(24, True))
    bullets = [
        "Reaproveitamento de parsers e regras já usadas na planilha (alunos, modalidades, pagamentos, caixa).",
        "Convivência controlada entre planilha e sistema até a equipe consolidar o uso do painel.",
        "Migração progressiva: não é “big bang” e ainda não está 100% concluída.",
        "Segurança: a secretaria não vê o extrato oficial; o admin acessa o financeiro completo.",
    ]
    yy = 550
    for b in bullets:
        txt(d, (72, yy), "•  " + b, font(20), "#243642")
        yy += 55
    save(img, "byla-migracao.png")


def make_rbac():
    w, h = 1600, 980
    img = Image.new("RGB", (w, h), "#f7fafb")
    d = ImageDraw.Draw(img)
    txt(d, (48, 36), "RBAC por perfil — navegação do aplicativo", font(34, True))
    txt(
        d,
        (48, 84),
        "Menus e rotas por papel · sem tokens, URLs internas ou políticas de banco",
        font(20),
        "#5a717c",
    )

    box(d, (48, 140, 760, 880), "#ffffff", "#d7e3e7", 2)
    d.rounded_rectangle([48, 140, 760, 230], radius=16, fill="#0f7f7a")
    d.rectangle([48, 200, 760, 230], fill="#0f7f7a")
    txt(d, (72, 168), "Secretaria", font(28, True), "#ffffff")
    txt(d, (72, 205), "Fluxo operacional do dia a dia", font(18), "#e6f5f3")

    txt(d, (72, 260), "PODE", font(16, True), "#5a717c")
    for i, label in enumerate(
        [
            "Fluxo de caixa operacional (alunos/pagamentos)",
            "Aluguel de salas",
            "Perfil",
        ]
    ):
        y = 300 + i * 70
        box(d, (72, y, 736, y + 52), "#e6f5f3", "#0f7f7a", 2, 10)
        txt(d, (92, y + 14), label, font(18), "#0a1620")

    txt(d, (72, 530), "NÃO PODE", font(16, True), "#5a717c")
    for i, label in enumerate(
        [
            "Extrato e transações oficiais",
            "Entradas/despesas do financeiro bancário",
            "Relatórios financeiros administrativos",
        ]
    ):
        y = 570 + i * 70
        box(d, (72, y, 736, y + 52), "#f7fafb", "#d7e3e7", 2, 10)
        txt(d, (92, y + 14), label, font(18), "#5a717c")

    box(d, (840, 140, 1552, 880), "#ffffff", "#d7e3e7", 2)
    d.rounded_rectangle([840, 140, 1552, 230], radius=16, fill="#0c3b47")
    d.rectangle([840, 200, 1552, 230], fill="#0c3b47")
    txt(d, (864, 168), "Admin", font(28, True), "#ffffff")
    txt(d, (864, 205), "Gestão completa + rotas da secretaria", font(18), "#e6f5f3")

    txt(d, (864, 260), "INCLUI SECRETARIA", font(16, True), "#5a717c")
    box(d, (864, 300, 1180, 352), "#f7fafb", "#5a717c", 2, 10)
    txt(d, (884, 314), "Fluxo de caixa", font(18))
    box(d, (1200, 300, 1528, 352), "#f7fafb", "#5a717c", 2, 10)
    txt(d, (1220, 314), "Aluguel / Perfil", font(18))

    txt(d, (864, 380), "FINANCEIRO OFICIAL", font(16, True), "#5a717c")
    for x1, y, x2, lab in [
        (864, 420, 1180, "Visão geral"),
        (1200, 420, 1528, "Transações"),
        (864, 480, 1180, "Entradas"),
        (1200, 480, 1528, "Despesas"),
        (864, 540, 1528, "Controle de caixa"),
    ]:
        box(d, (x1, y, x2, y + 48), "#f0f7f8", "#0c3b47", 2, 10)
        txt(d, (x1 + 20, y + 12), lab, font(18))

    txt(d, (864, 610), "VALIDAÇÃO E RELATÓRIOS", font(16, True), "#5a717c")
    for x1, y, x2, lab in [
        (864, 650, 1180, "Validação de pagamentos"),
        (1200, 650, 1528, "Calendário financeiro"),
        (864, 710, 1180, "Relatórios com IA"),
        (1200, 710, 1528, "Performance / atividade"),
    ]:
        box(d, (x1, y, x2, y + 48), "#f0f7f8", "#0c3b47", 2, 10)
        txt(d, (x1 + 16, y + 12), lab, font(17))

    txt(d, (864, 800), "Diferença de perfil na UI e nas rotas;", font(18), "#5a717c")
    txt(d, (864, 835), "conteúdo financeiro oficial restrito ao admin.", font(18), "#5a717c")
    save(img, "byla-rbac.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    make_arquitetura()
    make_migracao()
    make_rbac()
    print("done")
