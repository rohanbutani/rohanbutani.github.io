const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
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

const sections = document.querySelectorAll('main section[id]');
if ('IntersectionObserver' in window && nav) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      nav.querySelectorAll('a').forEach(link => {
        const active = link.getAttribute('href') === `#${entry.target.id}`;
        link.classList.toggle('active', active);
        if (active) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }
  }, { rootMargin: '-15% 0px -60% 0px', threshold: 0 });
  sections.forEach(section => observer.observe(section));
}

const mapDescriptions = {
  bio: 'BioFMs / Reusable representations of sequence, structure, and cellular state.',
  protein: 'Protein design / Moving from predicting biology to proposing useful designs.',
  scientific: 'Scientific ML / Learned models informed by geometry, dynamics, and mechanism.',
  interpretability: 'Interpretability / What does a representation know, and where does it fail?',
  health: 'Health ML / Reliable prediction grounded in real clinical questions.',
  genomics: 'Genomics / Learning from biological variation across sequences and systems.',
  generative: 'Generative models / Diffusion, flow matching, and constrained sampling.'
};
let pinnedNode = null;
function highlightNode(id) {
  document.querySelectorAll('.map-node').forEach(node => node.classList.toggle('active', node.dataset.node === id));
  document.querySelectorAll('[data-edge]').forEach(edge => edge.classList.toggle('active', edge.dataset.edge === id));
  const description = document.querySelector('#map-description');
  if (description) description.textContent = mapDescriptions[id] || 'Explore the connections. Hover or select a node.';
}
document.querySelectorAll('.map-node').forEach(node => {
  node.setAttribute('aria-pressed', 'false');
  node.addEventListener('pointerenter', () => highlightNode(node.dataset.node));
  node.addEventListener('pointerleave', () => highlightNode(pinnedNode));
  node.addEventListener('focus', () => highlightNode(node.dataset.node));
  node.addEventListener('blur', () => highlightNode(pinnedNode));
  node.addEventListener('click', () => {
    pinnedNode = pinnedNode === node.dataset.node ? null : node.dataset.node;
    document.querySelectorAll('.map-node').forEach(item => item.setAttribute('aria-pressed', String(item.dataset.node === pinnedNode)));
    highlightNode(pinnedNode);
  });
});

const interests = ['protein representation learning', 'generative molecular design', 'scientific foundation models', 'mechanistic biological models', 'reliable AI for high-stakes domains', 'multi-agent adaptation and scaling'];
let interestIndex = 0;
let motionPaused = reducedMotion.matches;
const motionButton = document.querySelector('.motion-toggle');
function updateMotionControl() {
  document.body.classList.toggle('motion-paused', motionPaused);
  if (!motionButton) return;
  motionButton.disabled = reducedMotion.matches;
  motionButton.textContent = motionPaused ? '▶' : 'Ⅱ';
  motionButton.setAttribute('aria-pressed', String(motionPaused));
  motionButton.setAttribute('aria-label', reducedMotion.matches ? 'Animations disabled by your reduced-motion preference' : motionPaused ? 'Resume animations' : 'Pause animations');
}
motionButton?.addEventListener('click', () => { motionPaused = !motionPaused; updateMotionControl(); });
reducedMotion.addEventListener('change', () => { motionPaused = reducedMotion.matches; updateMotionControl(); });
updateMotionControl();
const rotatingInterest = document.querySelector('#rotating-interest');
if (rotatingInterest) window.setInterval(() => {
  if (motionPaused || reducedMotion.matches || document.hidden) return;
  interestIndex = (interestIndex + 1) % interests.length;
  rotatingInterest.textContent = interests[interestIndex];
}, 5500);

const filters = document.querySelectorAll('[data-filter]');
filters.forEach(button => button.addEventListener('click', () => {
  filters.forEach(filter => {
    const active = filter === button;
    filter.classList.toggle('active', active);
    filter.setAttribute('aria-pressed', String(active));
  });
  let visible = 0;
  document.querySelectorAll('[data-categories]').forEach(card => {
    const show = button.dataset.filter === 'all' || card.dataset.categories.split(' ').includes(button.dataset.filter);
    card.hidden = !show;
    if (show) visible++;
  });
  document.querySelector('#work-count').textContent = `${String(visible).padStart(2, '0')} selected project${visible === 1 ? '' : 's'}`;
}));

