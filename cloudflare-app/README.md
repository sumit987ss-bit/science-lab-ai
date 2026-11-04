# POCKET Science Lab — Cloudflare migration

This folder is the new Cloudflare Pages application. The original Streamlit app remains in the repository root and is not changed by this migration branch.

## Cloudflare Pages setup
- Connect this GitHub repository to Cloudflare Pages.
- Production branch: `cloudflare-migration` while testing.
- Root directory: `cloudflare-app`.
- Build command: leave empty (static app).
- Build output directory: `.`.
- Add a Pages Function secret named `GEMINI_API_KEY` before enabling the AI Mentor.

## App installation
The web manifest, service worker and science flask SVG icon provide an installable PWA. Android Chrome can offer **Install app** or **Add to Home screen** after the Pages URL is served over HTTPS.

## Migration status
This is the PWA shell and secure AI endpoint foundation. The existing class-wise experiment engines must be ported and verified in stages before the Streamlit deployment is retired. Keep the original Streamlit app available until feature parity is confirmed.
