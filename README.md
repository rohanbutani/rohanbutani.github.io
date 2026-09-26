# Rohan Butani — Research website

A static personal research website focused on machine learning for scientific discovery, with a white and light-green visual system and text-led layouts. Built with HTML, CSS, and vanilla JavaScript; no package installation or production build is required.

## Local preview

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://localhost:8000`.

## Structure

- `index.html`: homepage, selected research, separate research and professional experience, independent projects, current learning, and contact.
- `styles.css`: responsive visual system and CV print styles.
- `app.js`: research filters, navigation, email copying, and CV printing.
- `work/*/index.html`: four research pages and the planned BioFM playground page.
- `projects/*/index.html`: Isotope, AlphaRx, and GlucaGone project profiles.
- `notes/*/index.html`: three initial research notebook entries with primary-source references.
- `cv.html`: printable HTML CV; use **Print / Save PDF** to export from your browser.
- `scripts/build_pages.py`: project and note content, plus their shared HTML template.

To update project or notebook content, edit `scripts/build_pages.py`, then run:

```sh
python3 scripts/build_pages.py
```

Commit the regenerated HTML pages along with the source. Homepage summaries and the CV are edited separately.

## GitHub Pages

The repository is ready to serve from the repository root through GitHub Pages. In repository **Settings → Pages**, configure deployment from the desired branch and its root directory. `.nojekyll` keeps the output as plain static files. Pushing changes to that configured branch will update the published site through GitHub Pages.

## Content conventions

The homepage and CV use the supplied biographical and research information. Numerical results are approximate; exploratory results and the design-stage BioFM project are labeled explicitly. Publication URLs, author lists, and precise workshop names were not invented. Add verified paper, code, and citation links when available.

Isotope is featured as a team-built GitHub Action and the winner of the Strategy Sponsor Track at HopHacks 2026. AlphaRx is a working research prototype; GlucaGone is intentionally described briefly.

The notebook entries are initial concept sketches and research questions, with links to primary literature. The “Now” section and CV are dated September 2026 and should be updated as the research direction and roles change.

## Accessibility and performance

Core content and navigation work without JavaScript. Interactions support keyboard focus, research-filter state, a mobile navigation toggle, and announcements for filter counts and clipboard results. The layout uses typography and lightweight HTML instead of decorative diagrams, image assets, or animated tickers. Smooth scrolling respects the operating system’s reduced-motion preference.

Fonts are loaded from Google Fonts with local serif, sans-serif, and monospace fallbacks. No analytics, cookies, or application dependencies are included.

## Validation

The original version was checked in headless Chrome for navigation, filters, clipboard copying, print styles, and responsive layouts. The light-theme revision was checked again: all 14 HTML pages passed local link/asset/anchor checks; research filters returned the expected counts; mobile navigation worked; no horizontal overflow was found at 320, 390, 680, 768, 1024, and 1440 pixels; and no JavaScript runtime errors were observed. Desktop and mobile screenshots were reviewed.
