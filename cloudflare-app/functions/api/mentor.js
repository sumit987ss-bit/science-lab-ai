export async function onRequestPost({ request, env }) {
  const headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Cache-Control": "no-store",
    "X-Content-Type-Options": "nosniff"
  };
  const reply = (status, body) => new Response(JSON.stringify(body), { status, headers });
  if (!env.GEMINI_API_KEY) return reply(503, { error: "The AI Mentor is not configured yet." });

  let body;
  try { body = await request.json(); } catch { return reply(400, { error: "Invalid request." }); }

  const question = typeof body.question === "string" ? body.question.trim() : "";
  const language = body.language === "pa" ? "pa" : "en";
  if (!question || question.length > 2000) {
    return reply(400, { error: "Enter a question of up to 2,000 characters." });
  }

  const punjabiRules = [
    "ਤੁਸੀਂ ਜਮਾਤ 6 ਤੋਂ 10 ਦੇ ਵਿਦਿਆਰਥੀਆਂ ਲਈ ਵਿਗਿਆਨ ਦੇ ਅਧਿਆਪਕ-ਸਹਾਇਕ ਹੋ।",
    "ਜਵਾਬ ਸਿਰਫ਼ ਸੌਖੀ, ਸਹੀ ਅਤੇ ਕੁਦਰਤੀ ਪੰਜਾਬੀ ਭਾਸ਼ਾ ਵਿੱਚ ਗੁਰਮੁਖੀ ਲਿਪੀ ਵਰਤ ਕੇ ਲਿਖੋ।",
    "ਸਵਾਲ ਅੰਗਰੇਜ਼ੀ ਵਿੱਚ ਹੋਵੇ ਜਾਂ ਪੰਜਾਬੀ ਵਿੱਚ, ਜਵਾਬ ਪੰਜਾਬੀ ਵਿੱਚ ਹੀ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।",
    "ਅੰਗਰੇਜ਼ੀ ਵਾਕ ਜਾਂ ਅੰਗਰੇਜ਼ੀ ਵਿੱਚ ਪੂਰਾ ਜਵਾਬ ਨਾ ਦਿਓ। ਵਿਗਿਆਨਕ ਸੰਕੇਤ ਅਤੇ ਲੋੜੀਂਦੇ ਤਕਨੀਕੀ ਸ਼ਬਦ ਹੀ ਅੰਗਰੇਜ਼ੀ ਵਿੱਚ ਬ੍ਰੈਕਟਾਂ ਅੰਦਰ ਦੇ ਸਕਦੇ ਹੋ।",
    "ਵਿਸ਼ੇ ਨੂੰ ਕਦਮ-ਦਰ-ਕਦਮ, ਉਮਰ ਅਨੁਕੂਲ ਅਤੇ ਸਹੀ ਢੰਗ ਨਾਲ ਸਮਝਾਓ।",
    "ਜਵਾਬ ਭੇਜਣ ਤੋਂ ਪਹਿਲਾਂ ਜਾਂਚੋ ਕਿ ਮੁੱਖ ਵਿਆਖਿਆ ਗੁਰਮੁਖੀ ਪੰਜਾਬੀ ਵਿੱਚ ਹੈ।"
  ].join(" ");

  const englishRules =
    "You are a helpful science learning mentor for Classes 6–10. Answer in clear, accurate, age-appropriate English and guide students step by step.";

  const strictPunjabiRules =
    "You are a science teacher for Classes 6–10. You MUST answer entirely in Punjabi language using Gurmukhi script. This applies even when the question is written in English. Do not write English sentences. Keep only scientific symbols and unavoidable technical terms in English, in brackets. Explain accurately in simple Punjabi.";


  const system = language === "pa" ? punjabiRules : englishRules;

  async function askGemini(userText, instruction = system) {
    const upstream = await fetch(
      "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=" + encodeURIComponent(env.GEMINI_API_KEY),
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          systemInstruction: { parts: [{ text: instruction }] },
          contents: [{ role: "user", parts: [{ text: userText }] }],
          generationConfig: { temperature: 0.3, maxOutputTokens: 1200 }
        })
      }
    );
    const data = await upstream.json();
    if (!upstream.ok) throw new Error(upstream.status === 429 ? "RATE_LIMIT" : "UPSTREAM");
    return (data.candidates?.[0]?.content?.parts || [])
      .map(part => part.text || "")
      .join("\n")
      .trim();
  }

  try {
    const prompt = language === "pa"
      ? "ਇਸ ਸਵਾਲ ਦਾ ਜਵਾਬ ਸਿਰਫ਼ ਪੰਜਾਬੀ ਗੁਰਮੁਖੀ ਲਿਪੀ ਵਿੱਚ ਦਿਓ: " + question
      : question;

    let answer = await askGemini(prompt);

    // If the model ignores the selected Punjabi setting, request a strict Punjabi rewrite.
    if (language === "pa" && !/[\u0A00-\u0A7F]/.test(answer)) {
      answer = await askGemini(
        "Answer the following science question fully in Punjabi using Gurmukhi script only. Do not answer in English. Question: " + question,
        strictPunjabiRules
      );
    }

    if (!answer) return reply(502, { error: "No answer was returned. Please try a shorter question." });
    if (language === "pa" && !/[\u0A00-\u0A7F]/.test(answer)) {
      return reply(502, { error: "Punjabi response could not be generated. Please try again." });
    }
    return reply(200, { answer, language });
  } catch (error) {
    if (error.message === "RATE_LIMIT") {
      return reply(429, { error: "The AI service is temporarily busy. Please try again shortly." });
    }
    return reply(502, { error: "Could not get a response from the AI service. Please try again shortly." });
  }
}
