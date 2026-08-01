export const languages = {
  pt: 'Português',
  en: 'English',
} as const;

export type Lang = keyof typeof languages;

export const defaultLang: Lang = 'pt';

export const routes = {
  pt: {
    home: '/',
    byla: '/projetos/byla/',
    explicasurf: '/projetos/explicasurf/',
  },
  en: {
    home: '/en/',
    byla: '/en/projects/byla/',
    explicasurf: '/en/projects/explicasurf/',
  },
} as const;

const ui = {
  pt: {
    metaTitle: 'Levi Davi Tude Silva — Desenvolvedor full-stack',
    metaDescription:
      'Desenvolvedor full-stack júnior em Salvador. Byla Financeiro em produção, ExplicaSurf Stella (IA + previsões oceânicas) e automações.',
    navHome: 'Início',
    navProjects: 'Projetos',
    navExperience: 'Experiência',
    navAbout: 'Sobre',
    navContact: 'Contato',
    langLabel: 'EN',
    brand: 'Levi Davi Tude Silva',
    heroGreeting: 'Olá — eu sou',
    heroName: 'Levi Davi Tude Silva',
    heroRole: 'Desenvolvedor full-stack júnior',
    heroLocation: 'Salvador, BA · remoto ou presencial/híbrido',
    heroLead:
      'Entrego produtos web de ponta a ponta: o Byla Financeiro em produção na academia, e o ExplicaSurf Stella — app live que usa IA para explicar o mar a surfistas (TCC nota 10). Stack principal React, Node, Python/Flask e Supabase.',
    heroCtaProjects: 'Ver projetos',
    heroCtaContact: 'Falar comigo',
    heroCtaCv: 'Baixar CV',
    heroPhotoAlt: 'Levi Davi Tude Silva — foto de corpo inteiro',
    heroStackHint: 'React · Node · Python/Flask · Supabase · n8n · IA aplicada',
    featuredLabel: 'Destaque',
    experienceTitle: 'Experiência',
    experienceLead: 'Trabalho com usuários reais, não só protótipo.',
    expCompany: 'Espaço Byla',
    expRole: 'Desenvolvedor full-stack',
    expDates: 'fev/2026 — presente',
    expBullet1: 'Byla Financeiro em produção: React/TypeScript, Node/Express, Supabase.',
    expBullet2: 'Migração gradual Google Sheets → PostgreSQL, com RBAC admin/secretaria.',
    expBullet3: 'Automações n8n (IA, sync, WhatsApp) e módulos operacionais.',
    projectsTitle: 'Projetos',
    projectsLead:
      'Dois cases em destaque — produto em produção (Byla) e TCC publicado com app live (ExplicaSurf Stella). A evolução comercial multi-praia fica em segundo plano, ainda em desenvolvimento.',
    bylaBadge: 'Produção',
    bylaTitle: 'Byla Financeiro',
    bylaBlurb:
      'Painel full-stack que organiza finanças e operação de uma academia cultural: alunos, pagamentos, caixa e papéis claros entre gestão e secretaria.',
    bylaOutcome: 'Em uso por admin e secretaria no dia a dia da operação.',
    explBadge: 'TCC · Nota 10 · Live',
    explTitle: 'ExplicaSurf Stella',
    explBlurb:
      'TCC nota 10 com app live: interpreta swell, vento e maré com IA generativa e explica condições para surfistas em Stella Maris — fundamentado em ocean literacy.',
    commercialBadge: 'Em desenvolvimento',
    commercialTitle: 'ExplicaSurf (produto multi-praia)',
    commercialBlurb:
      'Evolução do TCC em Next.js 16 + Supabase para várias praias. MVP avançado — ainda sem produção plena nem calibração total de todos os spots.',
    commercialNote: 'Projeto separado do Stella live; case completo depois.',
    readCase: 'Ver case',
    visitLive: 'Abrir site',
    readArticle: 'Ler artigo (PDF)',
    aboutTitle: 'Sobre',
    aboutBody:
      'Sou Levi Davi Tude Silva, de Salvador, e construo software que alguém usa de verdade. Graduado em Ciência da Computação (UNIJORGE). No Espaço Byla mantenho o painel financeiro da academia (React, Node, Supabase). No ExplicaSurf Stella propus e entreguei uma solução com Python/Flask + Gemini que traduz previsões oceânicas para surfistas — TCC nota 10, com artigo científico e protótipo no ar.',
    aboutAside:
      'Defesa do TCC ExplicaSurf (nota 10). Busco vaga full-stack, IA aplicada ou automações.',
    aboutLang: 'Inglês avançado (C1).',
    skillsTitle: 'Stack principal',
    contactTitle: 'Vamos conversar',
    contactLead: 'Aberto a vagas e projetos. Respondo por e-mail ou LinkedIn.',
    contactCta: 'Enviar e-mail',
    email: 'E-mail',
    linkedin: 'LinkedIn',
    github: 'GitHub',
    footerNote: 'Astro · GitHub Pages · Salvador, BA',
    demoNote: 'Demonstração com dados fictícios',
    stackByla: 'React · TypeScript · Node/Express · Supabase · n8n · Vercel · Render',
    stackExpl: 'React · Python/Flask · Gemini · Open-Meteo · WorldTides · Redis',
    stackCommercial: 'Next.js 16 · Supabase · Tailwind · OpenRouter/Gemini',
    bylaPageTitle: 'Byla Financeiro',
    bylaPageLead:
      'Sistema interno de gestão financeira e operacional do Espaço Byla — da planilha compartilhada ao painel em produção usado pela equipe.',
    bylaProblemTitle: 'Problema',
    bylaProblem:
      'A academia rodava alunos, modalidades, pagamentos e caixa em Google Sheets. Ficava difícil auditar, separar o que a secretaria podia ver do extrato da gestão, e evoluir regras sem quebrar o dia a dia.',
    bylaSolutionTitle: 'Como o painel resolve',
    bylaSolution1:
      'Interface React/TypeScript com módulos de visão geral, entradas, despesas, fluxo operacional e aluguel de salas — feitos para quem não é técnico.',
    bylaSolution2:
      'API Node/Express + Supabase/PostgreSQL com autenticação e RBAC: secretaria opera alunos/pagamentos; admin acessa o financeiro oficial (extrato, categorias, relatórios).',
    bylaSolution3:
      'Migração gradual Sheets → banco, com convivência controlada até a equipe consolidar o uso; automações n8n para sync, relatórios assistidos por IA e WhatsApp.',
    bylaBuildTitle: 'Como construí',
    bylaBuild1:
      'Entrega ponta a ponta: modelagem de domínio (alunos, modalidades, pagamentos, caixa), frontend, API REST, deploy em Vercel + Render e iteração com feedback da operação.',
    bylaBuild2:
      'Segurança prática: JWT, perfis distintos, RLS e cuidados com dados sensíveis (incluindo minimização de PII em fluxos com IA).',
    bylaBuild3:
      'Os prints abaixo usam dados fictícios de demonstração — o sistema real roda com a operação da academia.',
    bylaRepo: 'Código no GitHub',
    explPageTitle: 'ExplicaSurf Stella',
    explPageLead:
      'TCC em Ciência da Computação (UNIJORGE), nota 10: aplicação web live que interpreta previsões oceânicas e climáticas e as explica com IA para surfistas em Stella Maris.',
    explProblemTitle: 'Problema',
    explProblem:
      'Plataformas como Surfline e Surfguru entregam números técnicos (swell, período, vento, maré) que iniciantes — e muitos intermediários — não interpretam bem. Isso afeta desempenho e segurança. O trabalho parte de ocean literacy: compreender e aplicar princípios do oceano no dia a dia.',
    explSolutionTitle: 'A solução proposta',
    explSolution1:
      'O ExplicaSurf não só mostra dados: integra APIs oceânicas/meteorológicas e gera explicações em linguagem acessível, personalizadas por nível, stance (regular/goofy) e experiência.',
    explSolution2:
      'A IA (Gemini) segue estrutura de domínio — análise geral → impacto por nível → recomendação → segurança — com opção de ouvir a explicação (TTS) e gráficos hora a hora.',
    explSolution3:
      'Conhecimento local de Stella Maris (picos, fundos, comportamento de swell e maré) e heurísticas de surf (energia da onda, tendência de vento, calibração de maré) tornam a resposta útil na praia.',
    explBuildTitle: 'Como construí',
    explBuild1:
      'Frontend React (Vite) + backend Python/Flask em arquitetura cliente–servidor: o Flask concentra integração Open-Meteo e WorldTides, calibração local, prompt engineering e cache Redis.',
    explBuild2:
      'Desenvolvimento em etapas: APIs e padronização de dados → protótipo de fluxo → integração da IA → ajustes com testes técnicos (maré vs Marinha/Surfguru/WorldTides, energia, vento, rotas e latência).',
    explBuild3:
      'Protótipo publicado em explicasurfstella.com.br; documentado em artigo científico (formato SBC) e defesa na UNIJORGE com nota 10.',
    explEvalTitle: 'Avaliação com usuários e testes',
    explEval1:
      'Validação com o público-alvo (surfistas de Stella Maris): formulário enviado a quem se cadastrou na plataforma (out–nov), com escala Likert e perguntas abertas sobre clareza, utilidade e aderência — inclusive das explicações geradas por IA.',
    explEval2:
      '27 respostas autorizaram o uso na análise. O artigo discute a percepção positiva de adoção e o cumprimento dos objetivos específicos do trabalho.',
    explEval3:
      'Além dos testes de usuário, houve testes funcionais de API/integração e medição de tempo de resposta com cache (ordem de ~1–2 s nas medições documentadas).',
    explNextNote:
      'A evolução comercial multi-praia (Next.js + Supabase) é outro projeto, ainda em desenvolvimento — não confundir com este case Stella, que está live.',
    backHome: '← Voltar ao início',
  },
  en: {
    metaTitle: 'Levi Davi Tude Silva — Full-stack developer',
    metaDescription:
      'Junior full-stack developer in Salvador, Brazil. Byla Financeiro in production, ExplicaSurf Stella (AI + ocean forecasts), and automations.',
    navHome: 'Home',
    navProjects: 'Projects',
    navExperience: 'Experience',
    navAbout: 'About',
    navContact: 'Contact',
    langLabel: 'PT',
    brand: 'Levi Davi Tude Silva',
    heroGreeting: "Hi — I'm",
    heroName: 'Levi Davi Tude Silva',
    heroRole: 'Junior full-stack developer',
    heroLocation: 'Salvador, Brazil · remote or on-site/hybrid',
    heroLead:
      'I ship end-to-end web products: Byla Financeiro in production at an academy, and ExplicaSurf Stella — a live app that uses AI to explain the ocean to surfers (thesis graded 10/10). Core stack React, Node, Python/Flask, and Supabase.',
    heroCtaProjects: 'See projects',
    heroCtaContact: 'Get in touch',
    heroCtaCv: 'Download CV',
    heroPhotoAlt: 'Levi Davi Tude Silva — full-body photo',
    heroStackHint: 'React · Node · Python/Flask · Supabase · n8n · applied AI',
    featuredLabel: 'Featured',
    experienceTitle: 'Experience',
    experienceLead: 'I ship for real users, not only demos.',
    expCompany: 'Espaço Byla',
    expRole: 'Full-stack developer',
    expDates: 'Feb 2026 — present',
    expBullet1: 'Byla Financeiro in production: React/TypeScript, Node/Express, Supabase.',
    expBullet2: 'Gradual Google Sheets → PostgreSQL migration, with admin/front-desk RBAC.',
    expBullet3: 'n8n automations (AI, sync, WhatsApp) and operational modules.',
    projectsTitle: 'Projects',
    projectsLead:
      'Two featured cases — a production product (Byla) and a published thesis with a live app (ExplicaSurf Stella). The multi-spot commercial evolution stays secondary and is still in development.',
    bylaBadge: 'Production',
    bylaTitle: 'Byla Financeiro',
    bylaBlurb:
      'Full-stack dashboard for financial and operational management of a cultural academy: students, payments, cash flow, and clear roles for management vs front desk.',
    bylaOutcome: 'Used daily by admin and front-desk staff.',
    explBadge: 'Thesis · 10/10 · Live',
    explTitle: 'ExplicaSurf Stella',
    explBlurb:
      'Thesis graded 10/10 with a live app: interprets swell, wind, and tide with generative AI and explains conditions for surfers at Stella Maris — grounded in ocean literacy.',
    commercialBadge: 'In development',
    commercialTitle: 'ExplicaSurf (multi-spot product)',
    commercialBlurb:
      'Thesis evolution on Next.js 16 + Supabase for multiple beaches. Advanced MVP — not full production yet, and not every spot is fully calibrated.',
    commercialNote: 'Separate from the live Stella thesis app; fuller case later.',
    readCase: 'Read case',
    visitLive: 'Open live site',
    readArticle: 'Read paper (PDF)',
    aboutTitle: 'About',
    aboutBody:
      "I'm Levi Davi Tude Silva, from Salvador, and I build software people actually use. B.Sc. in Computer Science (UNIJORGE). At Espaço Byla I maintain the academy's finance panel (React, Node, Supabase). With ExplicaSurf Stella I proposed and shipped a Python/Flask + Gemini solution that translates ocean forecasts for surfers — thesis graded 10/10, with a scientific paper and a live prototype.",
    aboutAside:
      'ExplicaSurf thesis defense (graded 10/10). Open to full-stack, applied AI, or automation roles.',
    aboutLang: 'English: advanced (C1).',
    skillsTitle: 'Core stack',
    contactTitle: "Let's talk",
    contactLead: 'Open to roles and projects. Reach me by email or LinkedIn.',
    contactCta: 'Send email',
    email: 'Email',
    linkedin: 'LinkedIn',
    github: 'GitHub',
    footerNote: 'Astro · GitHub Pages · Salvador, Brazil',
    demoNote: 'Demo with fictional data',
    stackByla: 'React · TypeScript · Node/Express · Supabase · n8n · Vercel · Render',
    stackExpl: 'React · Python/Flask · Gemini · Open-Meteo · WorldTides · Redis',
    stackCommercial: 'Next.js 16 · Supabase · Tailwind · OpenRouter/Gemini',
    bylaPageTitle: 'Byla Financeiro',
    bylaPageLead:
      'Internal financial and operations system for Espaço Byla — from shared spreadsheets to a production dashboard used by the team.',
    bylaProblemTitle: 'Problem',
    bylaProblem:
      'The academy ran students, modalities, payments, and cash flow on Google Sheets. Hard to audit, hard to separate front-desk work from management bank data, and fragile when rules changed.',
    bylaSolutionTitle: 'How the panel helps',
    bylaSolution1:
      'React/TypeScript UI with overview, income, expenses, operational flow, and room booking — designed for non-technical staff.',
    bylaSolution2:
      'Node/Express API + Supabase/PostgreSQL with auth and RBAC: front desk handles students/payments; admin sees official finance (ledger, categories, reports).',
    bylaSolution3:
      'Gradual Sheets → database migration with controlled dual-run; n8n automations for sync, AI-assisted reports, and WhatsApp.',
    bylaBuildTitle: 'How I built it',
    bylaBuild1:
      'End-to-end delivery: domain modeling, frontend, REST API, Vercel + Render deploy, and iteration with ops feedback.',
    bylaBuild2:
      'Practical security: JWT, distinct roles, RLS, and care with sensitive data (including PII minimization in AI flows).',
    bylaBuild3:
      'Screenshots below use fictional demo data — the real system runs with the academy’s operations.',
    bylaRepo: 'Code on GitHub',
    explPageTitle: 'ExplicaSurf Stella',
    explPageLead:
      'Computer Science thesis (UNIJORGE), graded 10/10: a live web app that interprets ocean/weather forecasts and explains them with AI for surfers at Stella Maris.',
    explProblemTitle: 'Problem',
    explProblem:
      'Platforms like Surfline and Surfguru dump technical numbers (swell, period, wind, tide) that beginners — and many intermediates — struggle to read. That affects performance and safety. The work is grounded in ocean literacy: understanding and applying ocean concepts in daily practice.',
    explSolutionTitle: 'The proposed solution',
    explSolution1:
      'ExplicaSurf does more than display data: it integrates ocean/weather APIs and generates accessible explanations personalized by skill level, stance (regular/goofy), and experience.',
    explSolution2:
      'Gemini follows a domain structure — overview → impact by level → recommendation → safety — with optional TTS and hour-by-hour charts.',
    explSolution3:
      'Local Stella Maris knowledge (peaks, bottoms, swell/tide behavior) and surf heuristics (wave energy, wind trend, tide calibration) make the output useful on the beach.',
    explBuildTitle: 'How I built it',
    explBuild1:
      'React (Vite) frontend + Python/Flask backend in a client–server layout: Flask owns Open-Meteo and WorldTides integration, local calibration, prompt engineering, and Redis caching.',
    explBuild2:
      'Built in stages: APIs and data shaping → flow prototype → AI integration → technical tests (tide vs Navy/Surfguru/WorldTides, energy, wind, routes, and latency).',
    explBuild3:
      'Prototype published at explicasurfstella.com.br; documented in an SBC-format scientific paper and UNIJORGE defense graded 10/10.',
    explEvalTitle: 'User evaluation and tests',
    explEval1:
      'Validation with the target audience (Stella Maris surfers): a form sent to registered users (Oct–Nov) with Likert scales and open questions on clarity, usefulness, and fit — including AI explanations.',
    explEval2:
      '27 responses authorized use in the analysis. The paper discusses positive adoption perception and that the specific research objectives were met.',
    explEval3:
      'Besides user evaluation, there were functional API/integration tests and documented response times with caching (around ~1–2 s in the recorded measurements).',
    explNextNote:
      'The multi-spot commercial evolution (Next.js + Supabase) is a separate project still in development — not to be confused with this live Stella case.',
    backHome: '← Back home',
  },
} as const;

export type UiKey = keyof (typeof ui)['pt'];

export function t(lang: Lang, key: UiKey): string {
  return ui[lang][key] ?? ui[defaultLang][key];
}

export function otherLang(lang: Lang): Lang {
  return lang === 'pt' ? 'en' : 'pt';
}

export function pathFor(lang: Lang, page: keyof (typeof routes)['pt']): string {
  return routes[lang][page];
}
