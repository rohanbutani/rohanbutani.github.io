# Rohan Butani — Research website

A static personal research website focused on machine learning for scientific discovery. Built with HTML, CSS, and vanilla JavaScript; no package installation or production build is required.

## Local preview

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://localhost:8000`.

## Structure

- `index.html`: homepage, research directions, experience, current learning, and contact.
- `styles.css`: responsive visual system and CV print styles.
- `app.js`: interactive research map, project filters, navigation, motion controls, and email copying.
- `work/*/index.html`: five complete, directly addressable project pages.
- `notes/*/index.html`: three initial research notebook entries with primary-source references.
- `cv.html`: printable HTML CV; use **Print / Save PDF** to export from your browser.
- `scripts/build_pages.py`: project and note content, plus their shared HTML template.

To update project or notebook content, edit `scripts/build_pages.py`, then run:

```sh
python3 scripts/build_pages.py
```

Commit the regenerated HTML pages along with the source. Homepage summaries and the CV are edited separately.

## GitHub Pages

The repository is ready to serve from the repository root through GitHub Pages. In repository **Settings → Pages**, configure deployment from the desired branch and its root directory. `.nojekyll` keeps the output as plain static files. No deployment has been performed by this implementation.

## Content conventions

The homepage and CV use the supplied biographical and research information. Numerical results are approximate; exploratory results and the design-stage BioFM project are labeled explicitly. Publication URLs, author lists, and precise workshop names were not invented. Add verified paper, code, and citation links when available.

The notebook entries are initial concept sketches and research questions, with links to primary literature. The “Now” section and CV are dated September 2026 and should be updated as the research direction and roles change.

## Accessibility and performance

Core content and navigation work without JavaScript. Interactions support keyboard focus, project-filter and node-selection state, a mobile navigation toggle, and announcements for filter counts and clipboard results. Motion can be paused and respects the operating system’s reduced-motion preference. The hero uses lightweight SVG rather than a 3D library.

Fonts are loaded from Google Fonts with local serif, sans-serif, and monospace fallbacks. No analytics, cookies, or application dependencies are included.

## Validation

Checked in headless Chrome at desktop and mobile widths: local page links, all five project filters, map selection, mobile menu behavior, JavaScript runtime errors, and horizontal overflow from 320px through 1440px. Also reviewed desktop and mobile screenshots.
