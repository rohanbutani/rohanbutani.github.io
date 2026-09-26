const header = document.querySelector('.site-header');
const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('.main-nav');

function closeMenu() {
  if (!menu || !nav) return;
  menu.setAttribute('aria-expanded', 'false');
  nav.classList.remove('open');
  menu.querySelector('span').textContent = '+';
}

menu?.addEventListener('click', () => {
  const open = menu.getAttribute('aria-expanded') !== 'true';
  menu.setAttribute('aria-expanded', String(open));
  nav.classList.toggle('open', open);
  menu.querySelector('span').textContent = open ? '−' : '+';
});
nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menu?.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    menu.focus();
  }
});
document.addEventListener('click', event => {
  if (header && !header.contains(event.target)) closeMenu();
});
window.addEventListener('scroll', () => header?.classList.toggle('scrolled', window.scrollY > 12), { passive: true });
header?.classList.toggle('scrolled', window.scrollY > 12);

const sections = document.querySelectorAll('main section[id]:not([hidden])');
if ('IntersectionObserver' in window && nav) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      nav.querySelectorAll('a').forEach(link => {
        const sectionId = entry.target.id;
        const active = link.getAttribute('href') === `#${sectionId}`;
        link.classList.toggle('active', active);
        if (active) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }
  }, { rootMargin: '-15% 0px -60% 0px', threshold: 0 });
  sections.forEach(section => observer.observe(section));
}

document.querySelector('.copy-email')?.addEventListener('click', async () => {
  const status = document.querySelector('.copy-feedback');
  try {
    await navigator.clipboard.writeText('rbutani1@jh.edu');
    status.textContent = 'Email address copied.';
  } catch {
    status.textContent = 'Select and copy: rbutani1@jh.edu';
  }
});
