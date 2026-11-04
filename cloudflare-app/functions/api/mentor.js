export async function onRequestPost({ request, env }) {
  const headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Cache-Control": "no-store",
    "X-Content-Type-Options": "nosniff"
  };
  const reply = (status, body) => new Response(JSON.stringify(body), { status, headers });

  if (!env.GEMINI_API_KEY) {
    return reply(503, { error: "AI_SETUP: The Gemini API key is not configured in Cloudflare Pages." });
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return reply(400, { error: "REQUEST: Invalid request body." });
  }

  const question = typeof body.question === "string" ? body.question.trim() : "";
  const language = body.language === "pa" ? "pa" : "en";
  if (!question || question.length > 2000) {
    return reply(400, { error: "REQUEST: Enter a question of up to 2,000 characters." });
  }

  const punjabiSystem = [
    "ਤੁਸੀਂ ਜਮਾਤ 6 ਤੋਂ 10 ਦੇ ਵਿਦਿਆਰਥੀਆਂ ਲਈ ਵਿਗਿਆਨ ਦੇ ਅਧਿਆਪਕ-ਸਹਾਇਕ ਹੋ।",
    "ਜਵਾਬ ਸੌਖੀ, ਕੁਦਰਤੀ ਅਤੇ ਸਹੀ ਪੰਜਾਬੀ ਵਿੱਚ ਗੁਰਮੁਖੀ ਲਿਪੀ ਵਰਤ ਕੇ ਦਿਓ।",
    "ਸਵਾਲ ਅੰਗਰੇਜ਼ੀ ਵਿੱਚ ਹੋਵੇ ਜਾਂ ਪੰਜਾਬੀ ਵਿੱਚ, ਜਵਾਬ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਵਿੱਚ ਹੀ ਹੋਵੇ।",
    "ਅੰਗਰੇਜ਼ੀ ਦੇ ਪੂਰੇ ਵਾਕ ਨਾ ਲਿਖੋ। ਵਿਗਿਆਨਕ ਚਿੰਨ੍ਹ ਅਤੇ ਲੋੜੀਂਦੇ ਤਕਨੀਕੀ ਸ਼ਬਦ ਬ੍ਰੈਕਟਾਂ ਵਿੱਚ ਦੇ ਸਕਦੇ ਹੋ।",
    "ਵਿਸ਼ੇ ਨੂੰ ਕਦਮ-ਦਰ-ਕਦਮ, ਜਮਾਤ 6 ਤੋਂ 10 ਦੇ ਪੱਧਰ ਅਨੁਸਾਰ ਸਮਝਾਓ।",
    "ਜਵਾਬ ਵਿੱਚ ਪਰਿਭਾਸ਼ਾ, ਸੌਖੀ ਵਿਆਖਿਆ ਅਤੇ ਇੱਕ ਛੋਟੀ ਉਦਾਹਰਨ ਸ਼ਾਮਲ ਕਰੋ ਜਦੋਂ ਉਚਿਤ ਹੋਵੇ।"
  ].join(" ");

  const englishSystem =
    "You are a helpful science learning mentor for Classes 6–10. Answer in clear, accurate, age-appropriate English. Explain step by step and give a short example when useful.";

  async function askGemini(userText, systemInstruction) {
    let upstream;
    try {
      upstream = await fetch(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=" + encodeURIComponent(env.GEMINI_API_KEY),
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            systemInstruction: { parts: [{ text: systemInstruction }] },
            contents: [{ role: "user", parts: [{ text: userText }] }],
            generationConfig: { temperature: 0.2, maxOutputTokens: 1800, thinkingConfig: { thinkingBudget: 0 } }
          })
        }
      );
    } catch {
      throw new Error("NETWORK: Cloudflare could not reach the Gemini service.");
    }

    let data = {};
    try { data = await upstream.json(); } catch { /* handled below */ }

    if (!upstream.ok) {
      const apiMessage = data?.error?.message || "";
      if (upstream.status === 400) throw new Error("GEMINI_REQUEST: " + apiMessage);
      if (upstream.status === 401 || upstream.status === 403) throw new Error("API_KEY_OR_PERMISSION: Check the Gemini API key and its permissions in Cloudflare Pages.");
      if (upstream.status === 404) throw new Error("MODEL_NOT_AVAILABLE: The configured Gemini model is unavailable for this key.");
      if (upstream.status === 429) throw new Error("RATE_LIMIT: Gemini is temporarily busy or the API quota has been reached.");
      throw new Error("GEMINI_HTTP_" + upstream.status + ": " + apiMessage);
    }

    const candidate = data?.candidates?.[0];
    const answer = (candidate?.content?.parts || [])
      .map(part => typeof part.text === "string" ? part.text : "")
      .join("\n")
      .trim();

    if (!answer) {
      const reason = candidate?.finishReason || data?.promptFeedback?.blockReason || "empty response";
      throw new Error("EMPTY_RESPONSE: " + reason);
    }
    return answer;
  }

  try {
    if (language === "en") {
      const answer = await askGemini(question, englishSystem);
      return reply(200, { answer, language });
    }

    const answer = await askGemini(
      "ਹੇਠਾਂ ਦਿੱਤੇ ਵਿਗਿਆਨਕ ਸਵਾਲ ਦਾ ਜਵਾਬ ਸਿਰਫ਼ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਵਿੱਚ ਦਿਓ। ਸਵਾਲ: " + question,
      punjabiSystem
    );

    // Ask for a second Punjabi-only version if the first response ignored the selected language.
    const gurmukhiCount = (answer.match(/[\u0A00-\u0A7F]/g) || []).length;
    const letterCount = (answer.match(/[\p{L}]/gu) || []).length;
    if (gurmukhiCount < 4 || gurmukhiCount < letterCount * 0.2) {
      const retry = await askGemini(
        "ਪਿਛਲਾ ਜਵਾਬ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਵਿੱਚ ਨਹੀਂ ਸੀ। ਹੁਣ ਇਸ ਸਵਾਲ ਦਾ ਪੂਰਾ ਅਤੇ ਸੌਖਾ ਜਵਾਬ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਲਿਪੀ ਵਿੱਚ ਹੀ ਲਿਖੋ। ਅੰਗਰੇਜ਼ੀ ਵਾਕ ਨਾ ਵਰਤੋ। ਸਵਾਲ: " + question,
        punjabiSystem + " ਜਵਾਬ ਦੀ ਮੁੱਖ ਭਾਸ਼ਾ ਲਾਜ਼ਮੀ ਤੌਰ ਤੇ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਹੋਵੇ।"
      );
      const retryGurmukhi = (retry.match(/[\u0A00-\u0A7F]/g) || []).length;
      if (retryGurmukhi < 4) {
        return reply(502, { error: "PUNJABI_OUTPUT: Gemini did not return a usable Gurmukhi Punjabi answer. Please try once more." });
      }
      return reply(200, { answer: retry, language });
    }

    return reply(200, { answer, language });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Unknown AI service error.";
    return reply(502, { error: message });
  }
}
