# POCKET Science Lab — Render migration

This branch prepares the existing POCKET Science Lab PWA for deployment on Render. It preserves the current mobile-first interface, experiment catalogue, interactive subject engines, English/Punjabi interface, offline mentor fallback, app icon, and installable PWA.

## Hosting architecture

- Render Node.js Web Service serves the static PWA files from this directory.
- The same service exposes `GET /api/mentor` for a safe readiness check and `POST /api/mentor` for Gemini AI answers.
- The Gemini key is read only from the server-side `GEMINI_API_KEY` environment variable. It is never sent to the browser.
- The default model is `gemini-2.5-flash`; it can be changed with `GEMINI_MODEL`.
- The service binds to `0.0.0.0` and Render's assigned `PORT`.

## Render deployment

A Blueprint is provided at the repository root in `render.yaml`.

- Service name: `pocket-science-lab`
- Runtime: Node.js
- Root directory: `cloudflare-app`
- Build command: `npm install`
- Start command: `npm start`
- Initial plan: Free (for preview/testing only)
- Health check: `/api/mentor`

Connect the GitHub repository `sumit987ss-bit/science-lab-ai` to Render and create the service from the Blueprint. Render will ask for the secret value of `GEMINI_API_KEY`; enter the Google AI Studio Gemini API key directly in Render's environment settings. Do not put the key in GitHub or in frontend code.

## Important free-plan limitation

Render's free web services spin down after 15 minutes without inbound traffic and can take about a minute to wake up. Free instances are intended for testing and hobby projects, not production-critical availability. No paid plan is selected or required for the initial preview.

## Verification still required

The repository changes prepare the app for Render, but they do not prove a live deployment or a working Gemini response. After Render creates the service, verify:

1. The homepage loads and the app can be installed on Android.
2. The readiness endpoint reports `configured: true`.
3. A simple English science question receives an AI answer.
4. A Punjabi question receives a Gurmukhi answer.
5. The experiment catalogue and interactive controls work on mobile.

Keep the existing Streamlit and Cloudflare deployments available as backups until the Render deployment passes these checks.
