# Plipo — website

Landing page, Privacy Policy and Terms of Service for the Plipo plant care app
(Flutter source in `../flutter_plant_id`). Plain HTML and CSS, no build step; the colours,
fonts and painted icons are the app's Herbarium design.

- `index.html` — landing page
- `privacy.html` — Privacy Policy (linked from the app: Settings → Privacy Policy, paywall)
- `terms.html` — Terms of Service
- `assets/` — icons and illustrations copied from the app

Pushing to `main` deploys to GitHub Pages via `.github/workflows/pages.yml`:
<https://leemint9598.github.io/plant_care/>

When the app's data handling changes (a new SDK, a new kind of data sent to the server),
update `privacy.html` in the same change.
