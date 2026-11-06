import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const MODEL = process.env.GEMINI_MODEL || "gemini-2.5-flash";
const PORT = Number(process.env.PORT || 10000);
const MIME = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".webmanifest": "application/manifest+json; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".ico": "image/x-icon"
};

function sendJson(res, status, data) {
  res.writeHead(status, {
    "Content-Type": "application/json; charset=utf-8",
    "Cache-Control": "no-store, no-cache, must-revalidate",
    "X-Content-Type-Options": "nosniff"
  });
  res.end(JSON.stringify(data));
}

async function readJson(req) {
  let raw = "";
  for await (const chunk of req) {
    raw += chunk;
    if (raw.length > 12000) throw new Error("REQUEST: Request body is too large.");
  }
  try {
    return JSON.parse(raw || "{}");
  } catch {
    throw new Error("REQUEST: The server received invalid JSON.");
  }
}

const punjabiSystem = [
  "ਤੁਸੀਂ ਜਮਾਤ 6 ਤੋਂ 10 ਦੇ ਵਿਦਿਆਰਥੀਆਂ ਲਈ ਵਿਗਿਆਨ ਦੇ ਅਧਿਆਪਕ-ਸਹਾਇਕ ਹੋ।",
  "ਹਰ ਜਵਾਬ ਸੌਖੀ, ਕੁਦਰਤੀ ਅਤੇ ਸਹੀ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਵਿੱਚ ਦਿਓ।",
  "ਸਵਾਲ ਅੰਗਰੇਜ਼ੀ ਵਿੱਚ ਹੋਵੇ ਜਾਂ ਪੰਜਾਬੀ ਵਿੱਚ, ਜਵਾਬ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਵਿੱਚ ਹੀ ਹੋਵੇ।",
  "ਅੰਗਰੇਜ਼ੀ ਦੇ ਪੂਰੇ ਵਾਕ ਨਾ ਲਿਖੋ; ਵਿਗਿਆਨਕ ਚਿੰਨ੍ਹ ਅਤੇ ਲੋੜੀਂਦੇ ਤਕਨੀਕੀ ਸ਼ਬਦ ਵਰਤ ਸਕਦੇ ਹੋ।",
  "ਵਿਸ਼ੇ ਨੂੰ ਜਮਾਤ 6 ਤੋਂ 10 ਦੇ ਪੱਧਰ ਅਨੁਸਾਰ ਕਦਮ-ਦਰ-ਕਦਮ ਸਮਝਾਓ।",
  "ਜਿੱਥੇ ਉਚਿਤ ਹੋਵੇ, ਪਰਿਭਾਸ਼ਾ, ਸੌਖੀ ਵਿਆਖਿਆ ਅਤੇ ਇੱਕ ਉਦਾਹਰਨ ਦਿਓ।"
].join(" ");

async function callGemini(question, language, instructionOverride) {
  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) throw new Error("AI_SETUP: Add GEMINI_API_KEY to the Render service environment.");
  const instruction = instructionOverride || (language === "pa"
    ? punjabiSystem
    : "You are a helpful science learning mentor for Classes 6–10. Answer in clear, accurate, age-appropriate English. Explain step by step and give a short example when useful.");
  const endpoint = "https://generativelanguage.googleapis.com/v1beta/models/" +
    encodeURIComponent(MODEL) + ":generateContent?key=" + encodeURIComponent(apiKey);

  let response;
  try {
    response = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      signal: AbortSignal.timeout(25000),
      body: JSON.stringify({
        systemInstruction: { parts: [{ text: instruction }] },
        contents: [{ role: "user", parts: [{ text: question }] }],
        generationConfig: {
          temperature: 0.25,
          maxOutputTokens: 1800,
          responseMimeType: "text/plain"
        }
      })
    });
  } catch (error) {
    if (error?.name === "TimeoutError") throw new Error("GEMINI_TIMEOUT: Gemini did not respond within 25 seconds. Please retry.");
    throw new Error("NETWORK: The server could not connect to Gemini. Please retry.");
  }

  let data = {};
  try { data = await response.json(); } catch {}
  if (!response.ok) {
    const detail = data?.error?.message || "No error details were returned.";
    if (response.status === 400) throw new Error("GEMINI_REQUEST: " + detail);
    if (response.status === 401 || response.status === 403) {
      throw new Error("API_KEY_OR_PERMISSION: Gemini rejected the key. Check the Google AI Studio key and Gemini API access.");
    }
    if (response.status === 404) throw new Error("MODEL_NOT_AVAILABLE: " + MODEL + " is unavailable for this key. Check GEMINI_MODEL.");
    if (response.status === 429) throw new Error("RATE_LIMIT: Gemini quota or request limit reached. Wait briefly and retry.");
    throw new Error("GEMINI_HTTP_" + response.status + ": " + detail);
  }

  const candidate = data?.candidates?.[0];
  const answer = (candidate?.content?.parts || [])
    .map(part => typeof part.text === "string" ? part.text : "")
    .join("\n").trim();
  if (!answer) {
    const reason = candidate?.finishReason || data?.promptFeedback?.blockReason || "Gemini returned an empty answer.";
    throw new Error("EMPTY_RESPONSE: " + reason);
  }
  return answer;
}

async function mentorPost(req, res) {
  let body;
  try { body = await readJson(req); }
  catch (error) { return sendJson(res, 400, { error: error.message }); }

  const question = typeof body.question === "string" ? body.question.trim() : "";
  const language = body.language === "pa" ? "pa" : "en";
  if (!question || question.length > 2000) {
    return sendJson(res, 400, { error: "REQUEST: Enter a question containing 1–2,000 characters." });
  }

  try {
    const prompt = language === "pa"
      ? "ਇਸ ਸਵਾਲ ਦਾ ਜਵਾਬ ਸਿਰਫ਼ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਵਿੱਚ ਦਿਓ: " + question
      : question;
    let answer = await callGemini(prompt, language);

    if (language === "pa" && !/[\u0A00-\u0A7F]/.test(answer)) {
      answer = await callGemini(
        "ਪਿਛਲਾ ਜਵਾਬ ਪੰਜਾਬੀ ਵਿੱਚ ਨਹੀਂ ਸੀ। ਹੁਣ ਇਸ ਸਵਾਲ ਦਾ ਸੌਖਾ ਅਤੇ ਪੂਰਾ ਜਵਾਬ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਵਿੱਚ ਹੀ ਦਿਓ: " + question,
        "pa",
        punjabiSystem + " ਜਵਾਬ ਵਿੱਚ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਲਿਪੀ ਲਾਜ਼ਮੀ ਵਰਤੋ।"
      );
      if (!/[\u0A00-\u0A7F]/.test(answer)) {
        throw new Error("PUNJABI_OUTPUT: Gemini did not produce Gurmukhi text. Please retry.");
      }
    }
    return sendJson(res, 200, { answer, language, model: MODEL });
  } catch (error) {
    return sendJson(res, 502, { error: error instanceof Error ? error.message : "Unknown AI service error." });
  }
}

function serveStatic(req, res, pathname) {
  let decoded;
  try { decoded = decodeURIComponent(pathname); }
  catch { res.writeHead(400); return res.end("Bad request"); }
  const relative = decoded === "/" ? "index.html" : decoded.replace(/^\/+/, "");
  const filePath = path.resolve(ROOT, relative);
  if (filePath !== ROOT && !filePath.startsWith(ROOT + path.sep)) {
    res.writeHead(403); return res.end("Forbidden");
  }
  fs.stat(filePath, (error, stat) => {
    if (error || !stat.isFile()) {
      res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
      return res.end("Not found");
    }
    const ext = path.extname(filePath).toLowerCase();
    const cache = [".html", ".webmanifest", ".js"].includes(ext)
      ? "no-cache"
      : "public, max-age=3600";
    res.writeHead(200, {
      "Content-Type": MIME[ext] || "application/octet-stream",
      "Cache-Control": cache,
      "X-Content-Type-Options": "nosniff",
      "Referrer-Policy": "strict-origin-when-cross-origin"
    });
    if (req.method === "HEAD") return res.end();
    fs.createReadStream(filePath).pipe(res);
  });
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url || "/", "http://localhost");
  if (url.pathname === "/api/mentor" && req.method === "GET") {
    return sendJson(res, 200, {
      ok: true,
      service: "POCKET Science Lab AI Mentor",
      configured: Boolean(process.env.GEMINI_API_KEY),
      model: MODEL
    });
  }
  if (url.pathname === "/api/mentor" && req.method === "POST") return mentorPost(req, res);
  if (url.pathname.startsWith("/api/")) return sendJson(res, 404, { error: "API route not found." });
  if (req.method !== "GET" && req.method !== "HEAD") {
    res.writeHead(405, { Allow: "GET, HEAD" }); return res.end("Method not allowed");
  }
  serveStatic(req, res, url.pathname);
});

server.listen(PORT, "0.0.0.0", () => {
  console.log("POCKET Science Lab listening on 0.0.0.0:" + PORT);
});
