/* 55388.com — interactive tools */
(function () {
  const { $, $$, esc, toast } = window.N55_UI;
  const D = window.N55_DATA, N = window.N55, base = (document.body.dataset.root ?? "/");
  const parseDob = v => { const [y, m, d] = (v || "").split("-").map(Number); return y ? { y, m, d } : null; };
  const info = n => D.digits[n] || D.masters[n];
  const LP = D.lifePath;
  const card = (label, num, title, text, link) => `<div class="result-card"><div class="small muted">${label}</div><div class="big">${num}</div><h3>${esc(title)}</h3><p class="muted">${esc(text)}</p>${link ? `<a href="${link}">Read the full meaning →</a>` : ""}</div>`;
  const cta = () => `<div class="card" style="margin-top:14px"><strong>Want the full picture?</strong> <span class="muted">Get your complete Number Blueprint — Life Path, Destiny, Soul Urge, lucky numbers and your year ahead.</span><div style="margin-top:10px;display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-primary" href="${base}reading/">Get My Free Blueprint</a><button class="btn btn-ghost" data-copy>Copy result</button></div></div>`;
  function wireCopy(out) { const b = $("[data-copy]", out); b && b.addEventListener("click", () => { navigator.clipboard && navigator.clipboard.writeText(out.innerText.replace(/Copy result|Get My Free Blueprint/g, "").trim() + "\n— via 55388.com"); toast("Copied!"); }); }

  const handlers = {
    "life-path-calculator"(f, out) {
      const b = parseDob(f.dob.value); if (!b) return;
      const lp = N.lifePath(b.y, b.m, b.d), l = LP[lp.number];
      out.innerHTML = card("Your Life Path number", lp.number, `${l[0]}`, `${l[1]} Watch for: ${l[2]} Great fits: ${l[3]}`, `${base}numerology/life-path/${lp.number}/`) + `<p class="small muted">Calculation: ${esc(lp.steps)}</p>` + cta();
    },
    "name-numerology-calculator"(f, out) {
      const r = N.nameNumbers(f.fullname.value); if (!r.letters) return toast("Please type a name using letters A–Z.");
      out.innerHTML = `<div class="grid g3">${card("Destiny / Expression", r.expression, info(r.expression).name, info(r.expression).short)}${card("Soul Urge", r.soulUrge, info(r.soulUrge).name, info(r.soulUrge).short)}${card("Personality", r.personality, info(r.personality).name, info(r.personality).short)}</div>` + cta();
    },
    "personal-year-calculator"(f, out) {
      const b = parseDob(f.dob.value); if (!b) return; const now = new Date();
      const py = N.personalYear(b.m, b.d, now.getFullYear()), pm = N.reduce(py + now.getMonth() + 1, false), pd = N.reduce(pm + now.getDate(), false);
      out.innerHTML = `<div class="grid g3">${card("Personal Year " + now.getFullYear(), py, info(py).name, info(py).short)}${card("Personal Month", pm, info(pm).name, info(pm).short)}${card("Personal Day", pd, info(pd).name, info(pd).short)}</div>` + cta();
    },
    "compatibility-calculator"(f, out) {
      const a = parseDob(f.dob1.value), b = parseDob(f.dob2.value); if (!a || !b) return;
      const A = N.lifePath(a.y, a.m, a.d).number, B = N.lifePath(b.y, b.m, b.d).number, s = N.compatibility(A, B);
      out.innerHTML = `<div class="result-card"><div class="small muted">Life Path ${A} + Life Path ${B}</div><div class="big">${s}%</div><div class="meter"><i style="width:${s}%"></i></div>
        <p><strong>${LP[A][0]}</strong> meets <strong>${LP[B][0]}</strong>. ${s >= 85 ? "Natural allies — you speak the same language." : s >= 70 ? "A strong, complementary match with shared rhythm." : s >= 58 ? "Workable — different styles that can balance each other with effort." : "Opposites in approach: exciting, but requires conscious communication."}</p>
        <p class="muted small">You bring: ${esc(LP[A][1])}<br>They bring: ${esc(LP[B][1])}</p></div>` + cta();
    },
    "angel-number-finder"(f, out) {
      const b = parseDob(f.dob.value); if (!b) return;
      const lp = N.lifePath(b.y, b.m, b.d).number, ex = N.nameNumbers(f.fullname.value).expression;
      const n = lp > 9 ? String(lp) + String(ex) : String(lp).repeat(2) + String(ex);
      const featured = D.featured.includes(n), link = featured ? `${base}angel-numbers/${n}/` : `${base}angel-numbers/lookup/?n=${n}`;
      out.innerHTML = card(`${esc(f.fullname.value)}, your personal angel number is`, n, `Life Path ${lp} × Destiny ${ex}`, `${info(lp).short} ${info(ex).short}`, link) + cta();
    },
    "chinese-lucky-number-checker"(f, out) {
      const r = N.chinese(f.n.value); if (!r) return toast("Type a number with digits.");
      out.innerHTML = `<div class="result-card"><div class="small muted">Chinese luck score for ${r.number}</div><div class="big">${r.score}/100</div><div class="meter"><i style="width:${r.score}%"></i></div><h3>${r.verdict}</h3></div>
      <div class="digit-row">${r.digits.map(x => `<div><div class="d">${x.d}</div><div>${x.hanzi} · ${x.pinyin}</div><div class="small muted">${esc(x.sounds)}</div></div>`).join("")}</div>
      ${r.combos.length ? `<h3 style="margin-top:16px">Combinations found</h3><ul>${r.combos.map(c => `<li><strong>${c.n}</strong> — ${esc(c.meaning)}</li>`).join("")}</ul>` : ""}
      <div class="card" style="margin-top:14px"><strong>Choosing a business phone number, address or launch date?</strong> <span class="muted">Get a professional lucky-number audit for your brand.</span><div style="margin-top:10px"><a class="btn btn-primary" href="${base}business-lucky-number-audit/?number=${r.number}">Request a Business Audit</a> <button class="btn btn-ghost" data-copy>Copy result</button></div></div>`;
    },
    "lottery-number-generator"(f, out) {
      const g = D.lotteries.find(x => x[0] === f.game.value), lines = +f.lines.value, lucky = parseInt(f.lucky.value, 10);
      let html = `<h3>${esc(g[1])}</h3>`;
      for (let i = 0; i < lines; i++) {
        let main;
        if (g[3] === 0) main = Array.from({ length: g[2] }, () => N.randInt(0, 9));
        else { main = N.pick(g[2], g[3]); if (lucky >= 1 && lucky <= g[3] && !main.includes(lucky) && i === 0) { main[N.randInt(0, main.length - 1)] = lucky; main.sort((a, b) => a - b); } }
        const bonus = g[4] ? N.pick(g[4], g[5]) : [];
        html += `<div class="balls">${main.map(n => `<span class="ball">${n}</span>`).join("")}${bonus.map(n => `<span class="ball bonus" title="${esc(g[6])}">${n}</span>`).join("")}</div>`;
      }
      out.innerHTML = html + `<p class="small muted">Random quick picks for entertainment. Not affiliated with any lottery. Confirm rules with the official operator. Play responsibly.</p><button class="btn btn-ghost" data-copy>Copy numbers</button>`;
    },
    "random-number-generator"(f, out) {
      let min = Math.ceil(+f.min.value), max = Math.floor(+f.max.value), count = Math.min(500, Math.max(1, +f.count.value || 1)), unique = f.unique.value === "1";
      if (min > max) [min, max] = [max, min];
      if (unique && count > max - min + 1) return toast("Range too small for that many unique numbers.");
      const set = new Set(), arr = [];
      while (arr.length < count) { const v = N.randInt(min, max); if (unique) { if (set.has(v)) continue; set.add(v); } arr.push(v); }
      out.innerHTML = count === 1 ? `<div class="result-card center"><div class="big">${arr[0]}</div></div>` : `<div class="balls">${arr.map(n => `<span class="ball">${n}</span>`).join("")}</div>`;
      out.innerHTML += `<button class="btn btn-ghost" data-copy>Copy</button>`;
    },
    "number-to-words"(f, out) {
      const t = N.toWords(f.n.value, { cheque: f.mode.value === "cheque", currency: f.cur.value, case: f.case.value, uk: f.style.value === "uk" });
      if (!t) return toast("Please enter a valid number.");
      out.innerHTML = `<div class="result-card"><p style="font-size:1.25rem;margin:0">${esc(t)}</p></div><button class="btn btn-ghost" data-copy>Copy</button>`;
    }
  };

  $$("[data-tool]").forEach(tool => {
    const slug = tool.dataset.tool, out = $(".out", tool) || tool, form = $("form[data-calc]", tool);
    if (slug === "lookup") return renderLookup(tool);
    if (!form || !handlers[slug]) return;
    form.addEventListener("submit", e => { e.preventDefault(); handlers[slug](form.elements, out); wireCopy(out); window.gtag && gtag("event", "tool_use", { tool: slug }); out.scrollIntoView({ behavior: "smooth", block: "nearest" }); });
    const d = $("[data-dice]", tool), c = $("[data-coin]", tool);
    d && d.addEventListener("click", () => { const a = N.randInt(1, 6), b = N.randInt(1, 6); out.innerHTML = `<div class="result-card center"><div class="big">⚀ ${a} + ${b} = ${a + b}</div></div>`; });
    c && c.addEventListener("click", () => { out.innerHTML = `<div class="result-card center"><div class="big">${N.randInt(0, 1) ? "Heads" : "Tails"}</div></div>`; });
    // auto-run when prefilled via query string
    const q = new URLSearchParams(location.search); if (q.get("n") && form.elements.n) { form.elements.n.value = q.get("n"); handlers[slug](form.elements, out); wireCopy(out); }
  });

  function renderLookup(el) {
    const n = (new URLSearchParams(location.search).get("n") || "").replace(/\D/g, "").slice(0, 12);
    const input = $("#lk-q"); if (input) input.value = n;
    if (!n) { el.innerHTML = `<p class="muted">Type any number above to see its meaning.</p>`; return; }
    const a = N.analyze(n), ch = N.chinese(n), dom = D.digits[a.dominant];
    document.title = `${n} Angel Number Meaning | 55388`; $("#lk-title").textContent = `${n} Angel Number Meaning`;
    el.innerHTML = `<div class="keyfacts"><div><b>Root number</b><span>${a.root} · ${esc(a.rootInfo.name)}</span></div><div><b>Pattern</b><span>${esc(a.pattern.label)}</span></div><div><b>Core energy</b><span>${a.dominant} · ${esc(dom.name)}</span></div><div><b>Chinese luck</b><span>${ch.score}/100</span></div></div>
      <h2>What does ${n} mean?</h2><p>${esc(dom.core)}</p><p><strong>Pattern:</strong> ${esc(a.pattern.text)}</p><p><strong>Numerology:</strong> ${n.split("").join(" + ")} = ${a.sum}${a.sum !== a.root ? " → " + a.root : ""}. ${esc(a.rootInfo.core)}</p>
      ${a.layers && a.uniq.length > 1 ? `<h3>Reading ${n} in layers</h3><ul><li><strong>Cause (${a.layers.cause}):</strong> ${esc(D.digits[a.layers.cause].short)}</li><li><strong>Core (${a.layers.core}):</strong> ${[...new Set(a.layers.core)].map(x => esc(D.digits[x].name)).join(" · ")}</li><li><strong>Outcome (${a.layers.outcome}):</strong> ${esc(D.digits[a.layers.outcome].short)}</li></ul>` : ""}
      <h2>Love</h2><p>${esc(dom.love)}</p><h2>Career</h2><p>${esc(dom.career)}</p><h2>Money</h2><p>${esc(dom.money)}</p>
      <h2>Chinese luck: ${ch.score}/100 — ${ch.verdict}</h2><p>${ch.digits.map(x => `${x.d} ${x.hanzi} (${x.pinyin})`).join(" · ")}</p>
      <h2>What to do</h2><p>${esc(dom.action)}</p>
      <p><button class="btn btn-ghost" data-share="Angel number ${n} meaning">Share ↗</button></p>`;
    $$("[data-share]", el).forEach(b => b.addEventListener("click", async () => { try { await navigator.share({ title: document.title, url: location.href }); } catch (e) { navigator.clipboard && navigator.clipboard.writeText(location.href); toast("Link copied!"); } }));
  }
})();
