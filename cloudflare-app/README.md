# POCKET Science Lab — Cloudflare migration

This is a parallel migration of the Streamlit science laboratory into a static Cloudflare Pages PWA. The original Streamlit app on `main` is preserved as the live backup.

## Implemented in this migration branch

- Mobile-first POCKET Science Lab interface with a custom SVG flask icon, web app manifest and offline service worker.
- English and Punjabi UI, bilingual experiment catalogue titles/aims/notes, translated experiment choices and translated knowledge checks.
- 100 class-wise experiment catalogue records: 25 each for Electricity, Physics, Chemistry and Biology; five per subject per class for Classes 6–10.
- Interactive renderer with subject-specific SVG diagrams for Electricity, Physics, Chemistry and Biology.
- Subject-specific situation choices and variable labels; qualitative dropdown-only controls are used where appropriate, while quantitative Physics and Class 10 Electricity experiments retain model sliders.
- Electricity-specific work includes circuit symbols, electromagnet crane, fuse condition selector, liquid conductivity, electrolysis, electroplating, cell circuit, series/parallel switching and Class 10 Ohm's law calculation table.
- Offline bilingual science-mentor fallback covering 20 curriculum topics. The live Gemini endpoint remains optional and reads `GEMINI_API_KEY` server-side only.
- Security headers and automated GitHub checks for JavaScript syntax, manifest JSON, experiment counts, PWA icon/offline assets and subject-engine helpers.

## Verification status

GitHub Actions passed the validation workflow on the current migration branch. These checks confirm syntax and static asset/catalogue structure; they do not replace interactive browser testing or prove full one-to-one parity with every Streamlit experiment.

## Still required before production migration

1. Complete a side-by-side parity review of every one of the 100 experiments against the original Streamlit app. Some web diagrams and observations are simplified visual models and are not yet guaranteed to reproduce every original interactive detail.
2. Test navigation, control changes, quizzes, English/Punjabi text, responsive layout and accessibility in real browsers and on Android.
3. Add GitHub repository Actions secrets `CLOUDFLARE_API_TOKEN` (Cloudflare Pages Edit permission) and `CLOUDFLARE_ACCOUNT_ID`, then run **Actions → Deploy POCKET Science Lab preview to Cloudflare Pages → Run workflow**. The workflow creates the Pages project if needed and deploys the `cloudflare-migration` preview branch.
4. Add the Pages Function secret `GEMINI_API_KEY` if live AI responses are desired. The offline mentor fallback works without it.
5. Test install prompt, homescreen name/icon, offline launch, cache refresh and live Mentor responses on the deployed URL.
6. Only after acceptance should the draft PR be merged and production switched. Keep Streamlit available until then.

## Cloudflare Pages setup

- Connect GitHub repository: `sumit987ss-bit/science-lab-ai`
- Production/test branch initially: `cloudflare-migration`
- Root directory: `cloudflare-app`
- Build command: none
- Build output directory: `.`
- Optional Pages Function secret (set in Cloudflare Pages dashboard, not GitHub Actions): `GEMINI_API_KEY`
- GitHub Actions repository secrets needed for deployment: `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`

A manual preview-deployment workflow is prepared at `.github/workflows/deploy-cloudflare-preview.yml`. It has not been run because Cloudflare account authorization secrets are not available in this repository session. This migration is not yet production-complete.
