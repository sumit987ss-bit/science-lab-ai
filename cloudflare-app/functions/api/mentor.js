const MODEL = "gemini-2.5-flash";

function json(status, data) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store, no-cache, must-revalidate",
      "X-Content-Type-Options": "nosniff"
    }
  });
}

// A lightweight diagnostic endpoint: it never returns or exposes the secret.
export async function onRequestGet({ env }) {
  return json(200, {
    ok: true,
    service: "POCKET Science Lab AI Mentor",
    configured: Boolean(env.GEMINI_API_KEY),
    model: env.GEMINI_MODEL || MODEL
  });
}

export async function onRequestPost({ request, env }) {
  if (!env.GEMINI_API_KEY) {
    return json(503, {
      error: "AI_SETUP: Cloudflare Pages secret GEMINI_API_KEY is missing. Add it under Settings > Variables and Secrets, then redeploy."
    });
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return json(400, { error: "REQUEST: The server received invalid JSON." });
  }

  const question = typeof body.question === "string" ? body.question.trim() : "";
  const language = body.language === "pa" ? "pa" : "en";
  if (!question || question.length > 2000) {
    return json(400, { error: "REQUEST: Enter a question containing 1–2,000 characters." });
  }

  const punjabiSystem = [
    "ਤੁਸੀਂ ਜਮਾਤ 6 ਤੋਂ 10 ਦੇ ਵਿਦਿਆਰਥੀਆਂ ਲਈ ਵਿਗਿਆਨ ਦੇ ਅਧਿਆਪਕ-ਸਹਾਇਕ ਹੋ।",
    "ਹਰ ਜਵਾਬ ਸੌਖੀ, ਕੁਦਰਤੀ ਅਤੇ ਸਹੀ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਵਿੱਚ ਦਿਓ।",
    "ਸਵਾਲ ਅੰਗਰੇਜ਼ੀ ਵਿੱਚ ਹੋਵੇ ਜਾਂ ਪੰਜਾਬੀ ਵਿੱਚ, ਜਵਾਬ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਵਿੱਚ ਹੀ ਹੋਵੇ।",
    "ਅੰਗਰੇਜ਼ੀ ਦੇ ਪੂਰੇ ਵਾਕ ਨਾ ਲਿਖੋ; ਵਿਗਿਆਨਕ ਚਿੰਨ੍ਹ ਅਤੇ ਲੋੜੀਂਦੇ ਤਕਨੀਕੀ ਸ਼ਬਦ ਵਰਤ ਸਕਦੇ ਹੋ।",
    "ਵਿਸ਼ੇ ਨੂੰ ਜਮਾਤ 6 ਤੋਂ 10 ਦੇ ਪੱਧਰ ਅਨੁਸਾਰ ਕਦਮ-ਦਰ-ਕਦਮ ਸਮਝਾਓ।",
    "ਜਿੱਥੇ ਉਚਿਤ ਹੋਵੇ, ਪਰਿਭਾਸ਼ਾ, ਸੌਖੀ ਵਿਆਖਿਆ ਅਤੇ ਇੱਕ ਉਦਾਹਰਨ ਦਿਓ।"
  ].join(" ");

  const systemInstruction = language === "pa"
    ? punjabiSystem
    : "You are a helpful science learning mentor for Classes 6–10. Answer in clear, accurate, age-appropriate English. Explain step by step and give a short example when useful.";

  async function callGemini(text, instruction) {
    const model = env.GEMINI_MODEL || MODEL;
    const endpoint = "https://generativelanguage.googleapis.com/v1beta/models/" +
      encodeURIComponent(model) + ":generateContent?key=" + encodeURIComponent(env.GEMINI_API_KEY);
    let upstream;
    try {
      upstream = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        signal: AbortSignal.timeout(25000),
        body: JSON.stringify({
          systemInstruction: { parts: [{ text: instruction }] },
          contents: [{ role: "user", parts: [{ text }] }],
          generationConfig: {
            temperature: 0.25,
            maxOutputTokens: 1800,
            responseMimeType: "text/plain"
          }
        })
      });
    } catch (error) {
      if (error && error.name === "TimeoutError") {
        throw new Error("GEMINI_TIMEOUT: Gemini did not respond within 25 seconds. Please retry.");
      }
      throw new Error("NETWORK: Cloudflare could not connect to Gemini. Check the Pages deployment and try again.");
    }

    let data = {};
    try { data = await upstream.json(); } catch { /* handled as an upstream error */ }

    if (!upstream.ok) {
      const detail = data?.error?.message || "No error details were returned.";
      if (upstream.status === 400) throw new Error("GEMINI_REQUEST: " + detail);
      if (upstream.status === 401 || upstream.status === 403) {
        throw new Error("API_KEY_OR_PERMISSION: Gemini rejected the key. Check that GEMINI_API_KEY is a valid Google AI Studio key and that its API access is enabled.");
      }
      if (upstream.status === 404) {
        throw new Error("MODEL_NOT_AVAILABLE: " + model + " is unavailable for this key. Check the GEMINI_MODEL setting.");
      }
      if (upstream.status === 429) {
        throw new Error("RATE_LIMIT: Gemini quota or request limit reached. Wait briefly and retry.");
      }
      throw new Error("GEMINI_HTTP_" + upstream.status + ": " + detail);
    }

    const candidate = data?.candidates?.[0];
    const answer = (candidate?.content?.parts || [])
      .map(part => typeof part.text === "string" ? part.text : "")
      .join("\n")
      .trim();

    if (!answer) {
      const reason = candidate?.finishReason || data?.promptFeedback?.blockReason || "Gemini returned an empty answer.";
      throw new Error("EMPTY_RESPONSE: " + reason);
    }
    return answer;
  }

  try {
    const userPrompt = language === "pa"
      ? "ਇਸ ਸਵਾਲ ਦਾ ਜਵਾਬ ਸਿਰਫ਼ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਵਿੱਚ ਦਿਓ: " + question
      : question;

    let answer = await callGemini(userPrompt, systemInstruction);

    // Retry only when Gemini returned no Gurmukhi at all; mixed technical terms are acceptable.
    if (language === "pa" && !/[\u0A00-\u0A7F]/.test(answer)) {
      answer = await callGemini(
        "ਪਿਛਲਾ ਜਵਾਬ ਪੰਜਾਬੀ ਵਿੱਚ ਨਹੀਂ ਸੀ। ਹੁਣ ਇਸ ਸਵਾਲ ਦਾ ਸੌਖਾ ਅਤੇ ਪੂਰਾ ਜਵਾਬ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਵਿੱਚ ਹੀ ਦਿਓ: " + question,
        punjabiSystem + " ਜਵਾਬ ਵਿੱਚ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਲਿਪੀ ਲਾਜ਼ਮੀ ਵਰਤੋ।"
      );
      if (!/[\u0A00-\u0A7F]/.test(answer)) {
        throw new Error("PUNJABI_OUTPUT: Gemini did not produce Gurmukhi text. Please retry.");
      }
    }

    return json(200, { answer, language, model: env.GEMINI_MODEL || MODEL });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Unknown AI service error.";
    return json(502, { error: message });
  }
}
