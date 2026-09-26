# Rohan Butani — Research website

A static personal research website focused on machine learning for scientific discovery, with a white and light-green visual system and text-led layouts. Built with HTML, CSS, and vanilla JavaScript; no package installation or production build is required.

## Local preview

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://localhost:8000`.

## Structure

- `index.html`: homepage, separate research and professional experience, projects and contact, with the notebook and learning sections stored but hidden.
- `styles.css`: responsive visual system and resume link styles.
- `app.js`: navigation and email copying.
- `work/*/index.html`: the Georgia Tech UCLR and Wharton NFL studies, the two LLM project pages. Published study URLs are preserved.
- `projects/*/index.html`: Isotope, AlphaRx, and GlucaGone project profiles.
- `notes/*/index.html`: three initial notebook entries with primary-source references, currently hidden from homepage navigation and marked noindex.
- `Rohan_Butani_Research_Resume.pdf`: the supplied résumé. Resume links open it in a new tab using the browser’s PDF viewer, which provides preview, printing, and download controls.
- `cv.html`: compatibility redirect from the old CV address to the résumé PDF.
- `scripts/build_pages.py`: project and note content, plus their shared HTML template.

To update project or notebook content, edit `scripts/build_pages.py`, then run:

```sh
python3 scripts/build_pages.py
```

Commit the regenerated HTML pages along with the source. Homepage summaries are edited separately. To update the résumé, replace `Rohan_Butani_Research_Resume.pdf` with the new PDF using the same filename.

## GitHub Pages

The repository is ready to serve from the repository root through GitHub Pages. In repository **Settings → Pages**, configure deployment from the desired branch and its root directory. `.nojekyll` keeps the output as plain static files. Pushing changes to that configured branch will update the published site through GitHub Pages.

## Content conventions

The homepage uses the supplied biographical and research information; the Resume links display the supplied PDF unchanged. Numerical results are approximate; exploratory results are labeled explicitly. Publication URLs, author lists, and precise workshop names were not invented. Add verified paper, code, and citation links when available.

Isotope is featured as a team-built GitHub Action and the winner of the Strategy Sponsor Track at HopHacks 2026. AlphaRx is a working research prototype; GlucaGone is intentionally described briefly.

The notebook entries are initial concept sketches and research questions, with links to primary literature. The homepage notebook section has a `hidden` attribute and no navigation link until posts are ready. To reveal it, remove that attribute, restore the Notes navigation link, and remove the notebook noindex setting in `scripts/build_pages.py`. The résumé PDF should be replaced as roles change. The “Now” section is stored in the homepage with `hidden` and has no navigation link.

## Accessibility and performance

Core content and navigation work without JavaScript. Interactions support keyboard focus, a mobile navigation toggle and announcements for clipboard results. The layout uses typography and lightweight HTML instead of decorative diagrams, image assets, or animated tickers. Smooth scrolling respects the operating system’s reduced-motion preference.

Fonts are loaded from Google Fonts with local serif, sans-serif, and monospace fallbacks. No analytics, cookies, or application dependencies are included.

## Validation

The original version was checked in headless Chrome for navigation, filters, clipboard copying, print styles, and responsive layouts. The light-theme revision was checked again: all 14 HTML pages passed local link/asset/anchor checks; research filters returned the expected counts; mobile navigation worked; no horizontal overflow was found at 320, 390, 680, 768, 1024, and 1440 pixels; and no JavaScript runtime errors were observed. Desktop and mobile screenshots were reviewed.

The homepage has no keyword badges or standalone education/toolkit section. AlphaRx and GlucaGone share a desktop row, following the two language-model projects. The résumé PDF retains education and technical details. Research experience includes UCLR at Georgia Tech and NFL injury prediction at Wharton; the two LLM studies are listed under Projects.

Experience dates and role titles follow the supplied September 2026 résumé. UC San Diego is dated June 2025–January 2026. The DSAI research assistant role with Prof. Soufiane Hayou starts September 2026; the current expected graduation date is May 2028. Seattle University and CORE Institute retain their previously supplied dates because they are absent from that résumé.

BioFM is retained only as a draft in `scripts/build_pages.py` (`draft: True`). Its public page and homepage/resume entries are removed. To publish it later, complete the content, remove the draft flag, regenerate the pages, and add a homepage entry.
