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
      'Desenvolvedor full-stack júnior em Salvador. Produto em produção (Byla Financeiro), IA aplicada (ExplicaSurf) e automações.',
    navHome: 'Início',
    navProjects: 'Projetos',
    navAbout: 'Sobre',
    navContact: 'Contato',
    langLabel: 'EN',
    brand: 'Levi Tude',
    heroRole: 'Desenvolvedor full-stack júnior',
    heroLocation: 'Salvador, BA · remoto ou presencial/híbrido',
    heroLead:
      'Construo produtos web de ponta a ponta — do painel usado no dia a dia ao app que explica o mar com IA.',
    heroCtaProjects: 'Ver projetos',
    heroCtaContact: 'Falar comigo',
    heroPhotoSoon: 'Foto em breve',
    projectsTitle: 'Projetos',
    projectsLead: 'Três histórias distintas — experiência em produção, TCC publicado e produto em evolução.',
    bylaBadge: 'Produção',
    bylaTitle: 'Byla Financeiro',
    bylaBlurb:
      'Painel full-stack para gestão financeira e operacional de uma academia cultural. Em uso por admin e secretaria.',
    explBadge: 'TCC · Live',
    explTitle: 'ExplicaSurf Stella',
    explBlurb:
      'App que traduz swell, vento e maré em explicações acessíveis para surfistas em Stella Maris.',
    commercialBadge: 'Em evolução',
    commercialTitle: 'ExplicaSurf (produto)',
    commercialBlurb:
      'Reescrita multi-praia em Next.js 16 + Supabase. MVP avançado — ainda sem produção plena.',
    readCase: 'Ver case',
    visitLive: 'Abrir site',
    aboutTitle: 'Sobre',
    aboutBody:
      'Graduado em Ciência da Computação (UNIJORGE). No Espaço Byla entrego software com usuários reais; no ExplicaSurf apliquei IA a um domínio que conheço de perto. Busco vaga full-stack, IA aplicada ou automações.',
    skillsTitle: 'Stack',
    contactTitle: 'Contato',
    contactLead: 'Disponível para conversar sobre vagas e projetos.',
    email: 'E-mail',
    linkedin: 'LinkedIn',
    github: 'GitHub',
    footerNote: 'Feito com Astro · hospedado no GitHub Pages',
    demoNote: 'Demonstração com dados fictícios',
    stackByla: 'React · TypeScript · Node/Express · Supabase · n8n · Vercel · Render',
    stackExpl: 'React · Flask · Gemini · Open-Meteo · WorldTides',
    stackCommercial: 'Next.js 16 · Supabase · Tailwind · OpenRouter/Gemini',
    bylaPageTitle: 'Byla Financeiro',
    bylaPageLead:
      'Sistema interno de gestão financeira e operacional para o Espaço Byla — da planilha ao painel em produção.',
    bylaProblemTitle: 'Problema',
    bylaProblem:
      'A operação rodava em Google Sheets: difícil de auditar, sem papéis claros entre secretaria e gestão, e frágil para crescer.',
    bylaSolutionTitle: 'O que entreguei',
    bylaSolution1:
      'Painel React/TypeScript + API Node/Express + Supabase/PostgreSQL, com autenticação e RBAC (admin vs secretaria).',
    bylaSolution2:
      'Migração gradual Sheets → banco, mantendo convivência controlada até a equipe consolidar o uso do sistema.',
    bylaSolution3:
      'Automações n8n (relatórios com IA, sync, WhatsApp) e módulos operacionais como aluguel de salas.',
    bylaHonestTitle: 'Limites honestos',
    bylaHonest:
      'Não é SaaS multi-tenant vendido. A migração de planilhas é progressiva — não 100% concluída. Prints abaixo usam dados fictícios de demonstração.',
    bylaRepo: 'Código no GitHub',
    explPageTitle: 'ExplicaSurf Stella',
    explPageLead:
      'TCC em Ciência da Computação (UNIJORGE): app live que explica previsões oceânicas para surfistas.',
    explProblemTitle: 'Problema',
    explProblem:
      'Plataformas de forecast entregam números técnicos (swell, período, vento, maré) que iniciantes e muitos intermediários não interpretam bem.',
    explSolutionTitle: 'O que construí',
    explSolution1:
      'Frontend React + backend Flask, integrando Open-Meteo e WorldTides com calibração local de Stella Maris.',
    explSolution2:
      'Explicações geradas com Gemini, personalizadas por nível, stance e experiência — com opção de ouvir (TTS).',
    explSolution3: 'Artigo em formato SBC e protótipo publicado em explicasurfstella.com.br.',
    explHonestTitle: 'Separação importante',
    explHonest:
      'Este case é o TCC (uma praia, live). O produto comercial multi-praia é outro projeto, ainda em desenvolvimento.',
    backHome: '← Voltar ao início',
  },
  en: {
    metaTitle: 'Levi Davi Tude Silva — Full-stack developer',
    metaDescription:
      'Junior full-stack developer in Salvador, Brazil. Production product (Byla Financeiro), applied AI (ExplicaSurf), and automations.',
    navHome: 'Home',
    navProjects: 'Projects',
    navAbout: 'About',
    navContact: 'Contact',
    langLabel: 'PT',
    brand: 'Levi Tude',
    heroRole: 'Junior full-stack developer',
    heroLocation: 'Salvador, Brazil · remote or on-site/hybrid',
    heroLead:
      'I ship end-to-end web products — from dashboards used every day to an app that explains the ocean with AI.',
    heroCtaProjects: 'See projects',
    heroCtaContact: 'Get in touch',
    heroPhotoSoon: 'Photo coming soon',
    projectsTitle: 'Projects',
    projectsLead: 'Three distinct stories — production experience, published thesis app, and a product in progress.',
    bylaBadge: 'Production',
    bylaTitle: 'Byla Financeiro',
    bylaBlurb:
      'Full-stack dashboard for financial and operational management of a cultural academy. Used by admin and front desk.',
    explBadge: 'Thesis · Live',
    explTitle: 'ExplicaSurf Stella',
    explBlurb:
      'App that turns swell, wind, and tide into accessible explanations for surfers at Stella Maris.',
    commercialBadge: 'In progress',
    commercialTitle: 'ExplicaSurf (product)',
    commercialBlurb:
      'Multi-spot rewrite on Next.js 16 + Supabase. Advanced MVP — not full production yet.',
    readCase: 'Read case',
    visitLive: 'Open live site',
    aboutTitle: 'About',
    aboutBody:
      'B.Sc. in Computer Science (UNIJORGE). At Espaço Byla I ship software for real users; with ExplicaSurf I applied AI to a domain I know firsthand. Open to full-stack, applied AI, or automation roles.',
    skillsTitle: 'Stack',
    contactTitle: 'Contact',
    contactLead: 'Happy to talk about roles and projects.',
    email: 'Email',
    linkedin: 'LinkedIn',
    github: 'GitHub',
    footerNote: 'Built with Astro · hosted on GitHub Pages',
    demoNote: 'Demo with fictional data',
    stackByla: 'React · TypeScript · Node/Express · Supabase · n8n · Vercel · Render',
    stackExpl: 'React · Flask · Gemini · Open-Meteo · WorldTides',
    stackCommercial: 'Next.js 16 · Supabase · Tailwind · OpenRouter/Gemini',
    bylaPageTitle: 'Byla Financeiro',
    bylaPageLead:
      'Internal financial and operations system for Espaço Byla — from spreadsheets to a production dashboard.',
    bylaProblemTitle: 'Problem',
    bylaProblem:
      'Operations ran on Google Sheets: hard to audit, unclear roles between front desk and management, fragile to grow.',
    bylaSolutionTitle: 'What I shipped',
    bylaSolution1:
      'React/TypeScript UI + Node/Express API + Supabase/PostgreSQL with auth and RBAC (admin vs front desk).',
    bylaSolution2:
      'Gradual Sheets → database migration with controlled dual-run until the team adopted the panel.',
    bylaSolution3:
      'n8n automations (AI-assisted reports, sync, WhatsApp) and operational modules like room booking.',
    bylaHonestTitle: 'Honest limits',
    bylaHonest:
      'Not a sold multi-tenant SaaS. Spreadsheet migration is progressive — not 100% done. Screenshots below use fictional demo data.',
    bylaRepo: 'Code on GitHub',
    explPageTitle: 'ExplicaSurf Stella',
    explPageLead:
      'Computer Science thesis (UNIJORGE): a live app that explains ocean forecasts for surfers.',
    explProblemTitle: 'Problem',
    explProblem:
      'Forecast platforms dump technical numbers (swell, period, wind, tide) that beginners and many intermediates struggle to interpret.',
    explSolutionTitle: 'What I built',
    explSolution1:
      'React frontend + Flask backend, integrating Open-Meteo and WorldTides with local Stella Maris calibration.',
    explSolution2:
      'Gemini-generated explanations personalized by level, stance, and experience — with optional TTS.',
    explSolution3: 'SBC-format paper and a published prototype at explicasurfstella.com.br.',
    explHonestTitle: 'Important separation',
    explHonest:
      'This case is the thesis app (one beach, live). The commercial multi-spot product is a separate project still in development.',
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
