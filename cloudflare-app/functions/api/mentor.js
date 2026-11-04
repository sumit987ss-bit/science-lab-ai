export async function onRequestPost({ request, env }) {
  const cors = {
    "Content-Type": "application/json; charset=utf-8",
    "Cache-Control": "no-store",
    "X-Content-Type-Options": "nosniff"
  };
  const reply = (status, body) => new Response(JSON.stringify(body), { status, headers: cors });
  if (!env.GEMINI_API_KEY) return reply(503, { error: "The AI Mentor is not configured yet." });
  let body;
  try { body = await request.json(); } catch { return reply(400, { error: "Invalid request." }); }
  const question = typeof body.question === "string" ? body.question.trim() : "";
  const language = body.language === "pa" ? "pa" : "en";
  if (!question || question.length > 2000) return reply(400, { error: "Enter a question of up to 2,000 characters." });
  const system = language === "pa"
    ? "ਤੁਸੀਂ ਜਮਾਤ 6 ਤੋਂ 10 ਦੇ ਵਿਦਿਆਰਥੀਆਂ ਲਈ ਵਿਗਿਆਨ ਅਧਿਆਪਕ-ਸਹਾਇਕ ਹੋ। ਸੌਖੀ, ਸਹੀ ਪੰਜਾਬੀ ਵਿੱਚ ਸਮਝਾਓ। ਕਦਮ-ਦਰ-ਕਦਮ ਸਿੱਖਣ ਵਿੱਚ ਮਦਦ ਕਰੋ।"
    : "You are a helpful science learning mentor for Classes 6–10. Explain accurately in clear, age-appropriate language and guide students step by step.";
  try {
    const upstream = await fetch("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=" + encodeURIComponent(env.GEMINI_API_KEY), {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ systemInstruction: { parts: [{ text: system }] }, contents: [{ role: "user", parts: [{ text: question }] }], generationConfig: { temperature: 0.45, maxOutputTokens: 1200 } })
    });
    const data = await upstream.json();
    if (!upstream.ok) return reply(upstream.status === 429 ? 429 : 502, { error: "The AI service is temporarily unavailable. Please try again shortly." });
    const answer = (data.candidates?.[0]?.content?.parts || []).map(part => part.text || "").join("\n").trim();
    if (!answer) return reply(502, { error: "No answer was returned. Please try a shorter question." });
    return reply(200, { answer });
  } catch {
    return reply(502, { error: "Could not reach the AI service. Check your connection and try again." });
  }
}