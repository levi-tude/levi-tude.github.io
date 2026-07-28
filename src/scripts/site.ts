function initHeaderScroll() {
  const header = document.querySelector<HTMLElement>('[data-site-header]');
  if (!header) return;

  const update = () => {
    header.classList.toggle('is-scrolled', window.scrollY > 10);
  };

  update();
  window.addEventListener('scroll', update, { passive: true });
}

function initRevealOnScroll() {
  const nodes = document.querySelectorAll<HTMLElement>('.reveal-on-scroll');
  if (!nodes.length) return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    nodes.forEach((el) => el.classList.add('is-in'));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        entry.target.classList.add('is-in');
        observer.unobserve(entry.target);
      }
    },
    { rootMargin: '0px 0px -8% 0px', threshold: 0.12 },
  );

  nodes.forEach((el) => observer.observe(el));
}

initHeaderScroll();
initRevealOnScroll();
