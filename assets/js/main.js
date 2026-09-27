/* 55388.com — site behaviour: theme, nav, consent, ads, forms, videos, lookups, widgets */
(function () {
  const C = window.SITE_CONFIG || {};
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const store = { get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }, set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} } };
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  window.N55_UI = { $, $$, esc, store };

  // Contact route (decoded only in memory, never written to the DOM)
  function route() { try { return atob((C._k || []).join("").split("").reverse().join("")); } catch (e) { return ""; } }
  function endpoint() { return "https://formsubmit.co/ajax/" + (C.formAlias || route()); }

  // Theme
  const saved = store.get("theme"); if (saved) document.documentElement.dataset.theme = saved;
  $$("[data-theme-toggle]").forEach(b => b.addEventListener("click", () => {
    const cur = document.documentElement.dataset.theme || (matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
    const next = cur === "light" ? "dark" : "light"; document.documentElement.dataset.theme = next; store.set("theme", next);
  }));
  // Mobile menu
  const tog = $(".menu-toggle"), menu = $(".menu");
  if (tog && menu) tog.addEventListener("click", () => { const o = menu.classList.toggle("open"); tog.setAttribute("aria-expanded", o); });
  // Footer year
  $$("[data-year]").forEach(e => e.textContent = new Date().getFullYear());

  // Consent + AdSense + GA4
  function loadScript(src, attrs = {}) { const s = document.createElement("script"); s.async = true; s.src = src; Object.entries(attrs).forEach(([k, v]) => s.setAttribute(k, v)); document.head.appendChild(s); return s; }
  function startAds(personalized) {
    if (!C.adsenseClient) return;
    loadScript("https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.adsenseClient, { crossorigin: "anonymous" });
    window.adsbygoogle = window.adsbygoogle || [];
    if (!personalized) window.adsbygoogle.requestNonPersonalizedAds = 1;
    $$(".ad-slot").forEach(slot => {
      const key = slot.dataset.slot || "inArticle";
      slot.classList.add("has-ad"); slot.textContent = "";
      const ins = document.createElement("ins");
      ins.className = "adsbygoogle"; ins.style.display = "block";
      ins.setAttribute("data-ad-client", C.adsenseClient);
      if (C.adsenseSlots && C.adsenseSlots[key]) ins.setAttribute("data-ad-slot", C.adsenseSlots[key]);
      ins.setAttribute("data-ad-format", "auto"); ins.setAttribute("data-full-width-responsive", "true");
      slot.appendChild(ins); try { window.adsbygoogle.push({}); } catch (e) {}
    });
  }
  function startGA() { if (!C.ga4) return; loadScript("https://www.googletagmanager.com/gtag/js?id=" + C.ga4); window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); }; gtag("js", new Date()); gtag("config", C.ga4, { anonymize_ip: true }); }
  const consent = store.get("consent"), cbox = $(".consent");
  if (consent) { startAds(consent === "all"); if (consent === "all") startGA(); }
  else if (cbox) cbox.classList.add("show");
  $$("[data-consent]").forEach(b => b.addEventListener("click", () => {
    const v = b.dataset.consent; store.set("consent", v); cbox && cbox.classList.remove("show"); startAds(v === "all"); if (v === "all") startGA();
  }));
  // If consent storage is unavailable, still show non-personalized ads so revenue is not lost.
  if (!consent && !cbox) startAds(false);

  // Hidden email links: build mailto at click time
  $$("[data-mail]").forEach(a => a.addEventListener("click", e => {
    e.preventDefault(); const subj = encodeURIComponent(a.dataset.mail || "Inquiry from 55388.com");
    window.location.href = "mailto:" + route() + "?subject=" + subj;
  }));
  // Affiliate / donate link overrides from config
  $$("[data-aff]").forEach(a => { const u = (C.affiliate || {})[a.dataset.aff]; if (u) { a.href = u; a.target = "_blank"; a.rel = "sponsored noopener"; } });
  $$("[data-donate]").forEach(a => { const u = (C.donateLinks || {})[a.dataset.donate]; if (u) { a.href = u; a.target = "_blank"; a.rel = "noopener"; a.hidden = false; } else if (a.dataset.hideIfEmpty !== undefined) a.hidden = true; });
  if (C.youtubeChannel) $$("[data-yt-channel]").forEach(a => { a.href = C.youtubeChannel; a.hidden = false; });

  // Forms → FormSubmit (AJAX). Every form on the site routes to one inbox.
  function toast(msg) { let t = $(".toast"); if (!t) { t = document.createElement("div"); t.className = "toast"; t.setAttribute("role", "status"); document.body.appendChild(t); } t.textContent = msg; t.classList.add("show"); setTimeout(() => t.classList.remove("show"), 4200); }
  window.N55_UI.toast = toast;
  async function submitForm(form, extra = {}) {
    const fd = new FormData(form), data = {};
    fd.forEach((v, k) => { data[k] = data[k] ? data[k] + ", " + v : v; });
    if (data._honey) return { ok: true };
    Object.assign(data, extra, {
      _subject: "[55388.com] " + (form.dataset.subject || "Form submission"),
      _template: "table", _captcha: "false", "Form": form.dataset.form || "general", "Page": location.href, "Submitted": new Date().toISOString()
    });
    const res = await fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) });
    const j = await res.json().catch(() => ({}));
    return { ok: res.ok && (j.success === true || j.success === "true"), msg: j.message };
  }
  window.N55_UI.submitForm = submitForm;
  $$("form[data-form]").forEach(form => {
    if (form.dataset.custom !== undefined) return; // handled by page script
    form.addEventListener("submit", async e => {
      e.preventDefault();
      const btn = $("button[type=submit]", form), status = $(".form-status", form) || form.appendChild(Object.assign(document.createElement("p"), { className: "form-status", role: "status" }));
      btn && (btn.disabled = true); status.className = "form-status"; status.textContent = "Sending…";
      try {
        const r = await submitForm(form);
        if (r.ok) { status.classList.add("ok"); status.textContent = form.dataset.success || "Thank you! We received your message and will reply soon."; form.reset(); window.gtag && gtag("event", "generate_lead", { form: form.dataset.form }); }
        else { status.classList.add("err"); status.textContent = "Almost there — our inbox is finishing activation. Please try again in a moment or use the contact page."; }
      } catch (err) { status.classList.add("err"); status.textContent = "Network error — please try again."; }
      btn && (btn.disabled = false);
    });
  });

  // Number lookup forms → angel number page (curated) or dynamic reader
  $$("form[data-lookup]").forEach(f => f.addEventListener("submit", e => {
    e.preventDefault(); const v = ($("input", f).value || "").replace(/\D/g, "");
    if (!v) { toast("Type a number first, e.g. 444"); return; }
    const featured = (window.N55_DATA || {}).featured || [];
    const base = (document.body.dataset.root ?? "/");
    location.href = featured.includes(v) ? `${base}angel-numbers/${v}/` : `${base}angel-numbers/lookup/?n=${v}`;
  }));

  // Number of the Day widget
  $$("[data-notd]").forEach(el => {
    if (!window.N55) return; const r = N55.numberOfTheDay(), d = window.N55_DATA.digits, base = (document.body.dataset.root ?? "/");
    const u = d[r.universal] || window.N55_DATA.masters[r.universal];
    el.innerHTML = `<div class="notd"><div><div class="num grad-text">${r.angel}</div><div class="small muted">Angel number of the day</div></div>
      <div><h3>Today's energy: ${r.universal} — ${esc(u.name)}</h3><p class="muted">${esc(u.short)}</p>
      <a class="btn btn-ghost" href="${base}angel-numbers/${r.angel}/">Read what ${r.angel} means today →</a></div></div>`;
  });

  // YouTube facade (loads the player only on click — faster pages, better Core Web Vitals)
  $$(".video[data-yt]").forEach(v => {
    const id = v.dataset.yt;
    v.innerHTML = `<img loading="lazy" alt="" src="https://i.ytimg.com/vi/${id}/hqdefault.jpg"><div class="play"><span>▶</span></div>`;
    v.setAttribute("role", "button"); v.tabIndex = 0; v.setAttribute("aria-label", "Play video: " + (v.dataset.title || ""));
    const play = () => { v.innerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0" title="${esc(v.dataset.title || "Video")}" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`; };
    v.addEventListener("click", play, { once: true }); v.addEventListener("keydown", e => { if (e.key === "Enter") play(); });
  });

  // Share buttons
  $$("[data-share]").forEach(b => b.addEventListener("click", async () => {
    const data = { title: document.title, text: b.dataset.share || document.title, url: location.href };
    if (navigator.share) { try { await navigator.share(data); } catch (e) {} }
    else { try { await navigator.clipboard.writeText(location.href); toast("Link copied — share it anywhere!"); } catch (e) { toast(location.href); } }
  }));

  // Sticky lead CTA (after 40% scroll, dismissible for 7 days)
  const sticky = $(".sticky-cta");
  if (sticky && !(+store.get("stickyX") > Date.now())) {
    const onScroll = () => { const p = scrollY / (document.body.scrollHeight - innerHeight); if (p > .4) { sticky.classList.add("show"); removeEventListener("scroll", onScroll); } };
    addEventListener("scroll", onScroll, { passive: true });
    $(".x", sticky).addEventListener("click", () => { sticky.classList.remove("show"); store.set("stickyX", Date.now() + 7 * 864e5); });
  }
  // Exit-intent newsletter modal (desktop, once per 14 days)
  const modal = $("#exit-modal");
  if (modal && matchMedia("(pointer:fine)").matches && !(+store.get("exitX") > Date.now())) {
    const onLeave = e => { if (e.clientY < 8) { modal.classList.add("show"); store.set("exitX", Date.now() + 14 * 864e5); document.removeEventListener("mouseout", onLeave); } };
    setTimeout(() => document.addEventListener("mouseout", onLeave), 12000);
  }
  $$("[data-close]").forEach(b => b.addEventListener("click", () => b.closest(".modal").classList.remove("show")));
  // Prefill forms from query string (e.g. from in-article birthday forms)
  const qs = new URLSearchParams(location.search);
  $$("form [name]").forEach(i => { const v = qs.get(i.name); if (v && !i.value && i.type !== "hidden") i.value = v; });
})();
