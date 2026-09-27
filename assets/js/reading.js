/* 55388.com — Free Number Blueprint lead funnel (3 steps: details → preview → unlock) */
(function () {
  const { $, $$, esc, toast, submitForm } = window.N55_UI;
  const D = window.N55_DATA, N = window.N55, base = (document.body.dataset.root ?? "/");
  const form = $("#blueprint"); if (!form) return;
  const steps = $$(".step", form), bars = $$(".steps span", form);
  let calc = null;
  function go(i) { steps.forEach((s, j) => s.classList.toggle("active", j === i)); bars.forEach((b, j) => b.classList.toggle("on", j <= i)); form.scrollIntoView({ behavior: "smooth", block: "start" }); }
  const info = n => D.digits[n] || D.masters[n];

  function compute() {
    const name = form.fullname.value.trim(), [y, m, d] = form.dob.value.split("-").map(Number);
    const lp = N.lifePath(y, m, d).number, nm = N.nameNumbers(name), py = N.personalYear(m, d, new Date().getFullYear());
    const lucky = [...new Set([lp, nm.expression, nm.soulUrge, N.reduce(d), py].map(x => x > 9 ? x : x))].slice(0, 5);
    const angel = lp > 9 ? `${lp}${nm.expression}` : `${lp}${lp}${nm.expression}`;
    return { name, lp, ...nm, py, lucky, angel, bday: N.reduce(d) };
  }
  // Step 1 → 2 (free preview)
  $("[data-next]", form).addEventListener("click", () => {
    if (!form.fullname.value.trim() || !form.dob.value) { toast("Please add your name and birthday."); return; }
    calc = compute(); const L = D.lifePath[calc.lp];
    $("#preview").innerHTML = `<div class="result-card"><div class="small muted">${esc(calc.name.split(" ")[0])}, your Life Path is</div><div class="big">${calc.lp}</div><h3>${L[0]}</h3><p class="muted">${esc(L[1])}</p></div>
      <div class="grid g3"><div class="result-card"><div class="small muted">Destiny</div><div class="big">${calc.expression}</div></div><div class="result-card"><div class="small muted">Soul Urge</div><div class="big">${calc.soulUrge}</div></div><div class="result-card"><div class="small muted">Personal Year</div><div class="big">${calc.py}</div></div></div>
      <div class="result-card blur" aria-hidden="true"><h3>Your lucky numbers, personal angel number & 12-month forecast</h3><p>Career timing, love compatibility, money windows and the one pattern holding you back…</p></div>`;
    go(1);
  });
  $("[data-back]", form).addEventListener("click", () => go(0));
  // Step 2 → 3 (email unlock)
  form.addEventListener("submit", async e => {
    e.preventDefault();
    if (!form.email.value || !form.consent.checked) { toast("Add your email and tick the consent box to unlock."); return; }
    const btn = $("button[type=submit]", form); btn.disabled = true; btn.textContent = "Unlocking…";
    let ok = false;
    try { ok = (await submitForm(form, { "Life Path": calc.lp, "Destiny": calc.expression, "Soul Urge": calc.soulUrge, "Personality": calc.personality, "Personal Year": calc.py, "Angel number": calc.angel })).ok; } catch (err) {}
    renderFull(); go(2); btn.disabled = false; btn.textContent = "Unlock My Full Blueprint";
    window.gtag && gtag("event", "generate_lead", { form: "blueprint" });
    if (!ok) console.info("Lead not delivered (inbox activation pending?) — report still shown to user.");
  });
  function renderFull() {
    const c = calc, L = D.lifePath[c.lp], goal = form.goal.value, gi = info(c.py);
    const goalLine = { love: gi.love, career: gi.career, money: gi.money, purpose: gi.core }[goal] || gi.core;
    const link = D.featured.includes(c.angel) ? `${base}angel-numbers/${c.angel}/` : `${base}angel-numbers/lookup/?n=${c.angel}`;
    $("#full").innerHTML = `<h2>${esc(c.name.split(" ")[0])}'s Number Blueprint</h2>
      <div class="result-card"><h3>Life Path ${c.lp} — ${L[0]}</h3><p>${esc(L[1])} ${esc(info(c.lp).core)}</p><p><strong>Watch for:</strong> ${esc(L[2])}<br><strong>Thrives in:</strong> ${esc(L[3])}</p></div>
      <div class="result-card"><h3>Destiny ${c.expression} — ${esc(info(c.expression).name)}</h3><p>${esc(info(c.expression).short)}</p></div>
      <div class="result-card"><h3>Soul Urge ${c.soulUrge} — ${esc(info(c.soulUrge).name)}</h3><p>${esc(info(c.soulUrge).short)}</p></div>
      <div class="result-card"><h3>Personality ${c.personality} — ${esc(info(c.personality).name)}</h3><p>${esc(info(c.personality).short)}</p></div>
      <div class="result-card"><h3>Your ${new Date().getFullYear()} forecast: Personal Year ${c.py}</h3><p>${esc(gi.short)}</p><p><strong>For your ${esc(goal)} goal:</strong> ${esc(goalLine)}</p></div>
      <div class="result-card"><h3>Lucky numbers</h3><div class="balls">${c.lucky.map(n => `<span class="ball">${n}</span>`).join("")}</div><p>Personal angel number: <a href="${link}"><strong>${c.angel}</strong></a></p></div>
      <div class="grid g2" style="margin-top:18px">
        <div class="card"><h3>Go deeper with a live reader</h3><p class="muted small">A human advisor can interpret your full chart in context — love, timing, big decisions.</p><a class="btn btn-grad btn-block" data-aff="liveReading" href="#live">Connect With a Reader</a></div>
        <div class="card"><h3>Running a business?</h3><p class="muted small">Get a lucky-number audit of your brand name, phone number, address and launch date.</p><a class="btn btn-primary btn-block" href="${base}business-lucky-number-audit/">Request Business Audit</a></div></div>
      <p style="margin-top:14px"><button class="btn btn-ghost" onclick="window.print()">Print / save as PDF</button></p>`;
    const aff = (window.SITE_CONFIG.affiliate || {}).liveReading; if (aff) $$("[data-aff]", $("#full")).forEach(a => { a.href = aff; a.target = "_blank"; a.rel = "sponsored noopener"; });
  }
  // Prefill from in-article forms (?fullname=&dob=) and auto-advance
  const q = new URLSearchParams(location.search);
  if (q.get("fullname")) form.fullname.value = q.get("fullname");
  if (q.get("dob")) form.dob.value = q.get("dob");
  if (q.get("fullname") && q.get("dob")) $("[data-next]", form).click();
})();
