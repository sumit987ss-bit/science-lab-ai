# POCKET Science Lab — Cloudflare migration

The Cloudflare Pages/PWA application is being built in parallel with the original Streamlit app. The original app remains untouched and must remain available until the migrated version passes feature-parity and live deployment tests.

## Current migration progress

- Mobile-first PWA shell, custom science flask icon, English/Punjabi UI, manifest and offline service worker.
- All 100 class-wise experiment catalogue records are present (25 per subject; five per class).
- Cloudflare Pages AI Mentor endpoint reads `GEMINI_API_KEY` only from a server-side secret.
- Detailed Electricity simulations now include:
  - Class 6: bulb-terminal/wire comparison and open/closed circuit.
  - Class 7: circuit-symbol gallery and selected-symbol explanation; crane-style electromagnet; fuse intact/blown comparison with a current-condition selector (no switch checkbox).
  - Class 8: liquid conductivity, electrolysis solution comparison, electroplating, electromagnet and cell circuit.
  - Class 9: series/parallel comparison with a main series switch and independent parallel-branch switches; qualitative Ohm's law.
  - Class 10: Ohm's law circuit, calculated current and observation table.
- Automated GitHub validation passed for JavaScript syntax, manifest JSON and the 100-record catalogue.

## Still required before calling this fully migrated

- Port and verify the individual Physics, Chemistry and Biology simulations against the original Streamlit app.
- Complete parity checks for every Electricity experiment, including all diagrams, controls, bilingual observations, quizzes and navigation.
- Test all 100 experiments on a real Android phone, including narrow screens and offline reload.
- Create the Cloudflare Pages project in the owner's Cloudflare account and deploy the testing branch.
- Add the Pages Function secret `GEMINI_API_KEY` and live-test the AI Mentor in English and Punjabi.
- Verify PWA installation, custom icon, cache refresh, accessibility and error states.
- Only after acceptance should the draft PR be reviewed/merged and the production app switched. Do not delete or retire the Streamlit backup before then.

## Cloudflare Pages testing settings

- Root directory: `cloudflare-app`
- Build command: leave empty (static app)
- Build output directory: `. ` (enter a single dot: `.`)
- Testing branch: `cloudflare-migration`
- Pages Function secret: `GEMINI_API_KEY`

The migration is in progress, not yet a production deployment.
