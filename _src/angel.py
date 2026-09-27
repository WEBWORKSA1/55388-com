"""Angel-number page composer: turns digit data into rich, unique static pages."""
from data import DIGITS, MASTERS, INTROS, FEATURED, CHINESE
from layout import page, ad, breadcrumbs, faq_schema, faq_html, birthday_inline, newsletter_band, e, depth_prefix

MASTER = (11, 22, 33)

def dsum(s): return sum(int(c) for c in s)
def reduce(n, keep=True):
    while n > 9 and not (keep and n in MASTER):
        n = dsum(str(n))
    return n

def root_info(n): return DIGITS[str(n)] if n <= 9 else MASTERS[n]

def pattern(s):
    if len(s) > 1 and len(set(s)) == 1:
        return "Repeating number", f"Every digit is {s[0]}, so the energy of {s[0]} is amplified {len(s)}× — the clearest, loudest form of the message."
    if len(s) > 2 and s == s[::-1]:
        return "Mirror / palindrome", "It reads the same forwards and backwards — a sign of reflection: what you send out comes back to you."
    if len(s) % 2 == 0 and len(s) >= 4 and s[:len(s)//2] == s[len(s)//2:]:
        return "Double sequence", f"The pair {s[:len(s)//2]} repeats — a nudge to notice a cycle that is replaying in your life."
    if len(s) > 2 and all(int(s[i]) == int(s[i-1]) + 1 for i in range(1, len(s))):
        return "Ascending sequence", "The digits climb step by step — progress, momentum and a clear next step."
    if len(s) > 2 and all(int(s[i]) == int(s[i-1]) - 1 for i in range(1, len(s))):
        return "Descending sequence", "The digits count down — release, simplification and letting go of excess."
    if len(s) == 4 and s[0] == s[1] and s[2] == s[3]:
        return "Paired digits", f"Two pairs ({s[0]}{s[0]} and {s[2]}{s[2]}) — two areas of life asking to be balanced."
    if len(s) == 2 and s[0] == s[1]:
        return "Master / double digit", f"Double {s[0]} — the energy of {s[0]} in a concentrated, partnered form."
    return "Mixed sequence", "A mixed sequence is read in layers: first digits = the cause, middle digits = the core message, last digits = the likely outcome."

def chinese_score(s):
    ds = CHINESE["digits"]
    score = sum(ds[c]["score"] for c in s) / len(s)
    combos = [c for c in CHINESE["combos"] if c["n"] in s]
    score += sum(c["bonus"] for c in combos)
    if s.endswith("8"): score += 5
    if s.endswith("4"): score -= 5
    return max(1, min(100, round(score))), combos

TWIN = {
  "0": "a reunion or a fresh start with a soul connection — the circle is closing and reopening.",
  "1": "the start of a twin-flame journey or a new phase in it; lead with self-love first.",
  "2": "harmony and reunion — balance between giving and receiving is the key.",
  "3": "communication is the bridge; say what's unsaid and growth follows.",
  "4": "building something stable together; patience through the 'separation' phase pays off.",
  "5": "change in the connection — a shift, a move, or a breakthrough in how you relate.",
  "6": "healing and unconditional love; nurture the bond without losing yourself.",
  "7": "a spiritual awakening within the connection; trust intuition over appearances.",
  "8": "karmic balance — the energy you invest in the relationship comes back multiplied.",
  "9": "completion of a cycle — either union at a higher level or a graceful release.",
}

def related(s):
    out = []
    d = s[0]
    for cand in [d * 3, d * 4, d * 2, str((int(s) - 1)) if s.isdigit() else "", str(int(s) + 1)]:
        if cand and cand != s and cand in FEATURED and cand not in out:
            out.append(cand)
    for cand in ["111", "444", "555", "777", "888", "1111", "1212", "55388"]:
        if cand != s and cand not in out and len(out) < 10:
            out.append(cand)
    return out[:10]

def angel_page(s):
    path = f"angel-numbers/{s}/"
    r = depth_prefix(path)
    total = dsum(s); root = reduce(total)
    ri = root_info(root)
    plabel, ptext = pattern(s)
    counts = {c: s.count(c) for c in dict.fromkeys(s)}
    dom = sorted(counts.items(), key=lambda kv: (-kv[1], -int(kv[0])))[0][0]
    D = DIGITS[dom]
    score, combos = chinese_score(s)
    intro = INTROS.get(s) or (
        f"Seeing {s} again and again? In numerology, {s} is driven by the energy of {dom} — {D['name'].lower()} — "
        f"and reduces to the root number {root} ({ri['name']}). Together they point to {', '.join(D['kw'][:3])}.")
    reduction = " + ".join(s) + f" = {total}" + (f" → {root}" if total != root else "")
    digits_rows = "".join(
        f"<tr><td><strong>{c}</strong> ×{n}</td><td>{DIGITS[c]['name']}</td><td>{', '.join(DIGITS[c]['kw'])}</td></tr>" for c, n in counts.items())
    layers = ""
    if len(s) >= 3 and len(set(s)) > 1:
        layers = f"""<h3>Reading {s} in layers</h3><ul>
<li><strong>Cause ({s[0]}):</strong> {DIGITS[s[0]]['short']}</li>
<li><strong>Core message ({s[1:-1]}):</strong> {' '.join(DIGITS[c]['name'] for c in dict.fromkeys(s[1:-1]))} — the heart of what this number wants you to notice.</li>
<li><strong>Outcome ({s[-1]}):</strong> {DIGITS[s[-1]]['short']}</li></ul>"""
    combo_txt = "".join(f"<li><strong>{c['n']}</strong> — {e(c['meaning'])}</li>" for c in combos)
    ch_digits = " · ".join(f"{c} {CHINESE['digits'][c]['hanzi']} ({CHINESE['digits'][c]['pinyin']})" for c in dict.fromkeys(s))
    lucky = "yes — it is considered very fortunate" if score >= 70 else ("mostly neutral to positive" if score >= 50 else "traditionally not — several digits carry unlucky sound-alikes")
    qas = [
        (f"What does {s} mean spiritually?", f"{s} carries the amplified energy of {dom} ({D['name']}) and reduces to {root} ({ri['name']}). Spiritually it points to {', '.join(D['kw'])}. {D['action']}"),
        (f"What does {s} mean in love?", D["love"]),
        (f"Is {s} a twin flame number?", f"Many readers link {s} to {TWIN[dom]}"),
        (f"What does {s} mean for money and career?", D["career"] + " " + D["money"]),
        (f"Is {s} lucky in Chinese culture?", f"Using traditional homophones, {s} scores {score}/100 on our Chinese luck scale — {lucky}."),
        (f"What should I do when I keep seeing {s}?", f"Pause and note what you were thinking at that moment. Then act on the message: {D['action']}"),
    ]
    bc_html, bc_schema = breadcrumbs(r, [("angel-numbers/", "Angel Numbers"), ("", s)])
    rel = "".join(f'<a href="{r}angel-numbers/{x}/">{x}<small>{DIGITS[x[0]]["name"].split(" ")[0]}</small></a>' for x in related(s))
    title = f"{s} Angel Number Meaning: Love, Twin Flame, Career & Money | 55388"
    desc = f"What does {s} mean? Spiritual meaning, love, twin flame, career, money and Chinese luck of angel number {s} — plus what to do next. Free reading included."
    body = f"""
<section class="section-tight"><div class="container">
{bc_html}
<div class="article">
<article class="prose">
  <span class="eyebrow">Angel number · {plabel}</span>
  <h1>{s} Angel Number Meaning</h1>
  <p class="lead" style="font-size:1.15rem">{e(intro)}</p>
  <div class="keyfacts">
    <div><b>Root number</b><span>{root} · {ri['name']}</span></div>
    <div><b>Pattern</b><span>{plabel}</span></div>
    <div><b>Core energy</b><span>{dom} · {D['name']}</span></div>
    <div><b>Chinese luck</b><span>{score}/100</span></div>
  </div>
  <button class="btn btn-ghost" data-share="Angel number {s} meaning">Share this meaning ↗</button>
  {ad("header")}
  <h2 id="meaning">What does {s} mean?</h2>
  <p>{D['core']}</p>
  <p><strong>Pattern:</strong> {ptext}</p>
  <p><strong>Numerology reduction:</strong> {reduction}. {ri['core']}</p>
  <table><thead><tr><th>Digit</th><th>Energy</th><th>Keywords</th></tr></thead><tbody>{digits_rows}</tbody></table>
  {layers}
  {birthday_inline(r, s)}
  <h2 id="love">{s} meaning in love & relationships</h2>
  <p>{D['love']}</p>
  <h3>{s} and twin flames</h3>
  <p>For twin-flame seekers, {s} is commonly read as {TWIN[dom]}</p>
  {ad("inArticle")}
  <h2 id="career">{s} meaning for career & business</h2>
  <p>{D['career']}</p>
  <h2 id="money">{s} and money</h2>
  <p>{D['money']}</p>
  <p><a class="btn btn-ghost" href="{r}business-lucky-number-audit/">Using {s} in a phone number, address or launch date? Get a business number audit →</a></p>
  <h2 id="chinese">{s} in Chinese number symbolism</h2>
  <p>Digits: {ch_digits}. On our homophone-based scale {s} scores <strong>{score}/100</strong> — {lucky}.</p>
  {"<ul>" + combo_txt + "</ul>" if combo_txt else ""}
  <p><a href="{r}tools/chinese-lucky-number-checker/?n={s}">Check any phone or plate number's Chinese luck →</a></p>
  <h2 id="action">What to do when you see {s}</h2>
  <ol><li><strong>Pause & note:</strong> write down what you were thinking or doing when {s} appeared — that's the context of the message.</li>
  <li><strong>Act:</strong> {D['action']}</li>
  <li><strong>Personalize it:</strong> compare {s} with your own Life Path number to see whether it supports or challenges your natural path. <a href="{r}tools/life-path-calculator/">Calculate yours free</a>.</li></ol>
  {ad("inArticle")}
  <h2 id="faq">{s} angel number FAQ</h2>
  {faq_html(qas)}
  <h2>Related numbers</h2>
  <div class="num-grid">{rel}</div>
  <p class="small muted" style="margin-top:20px">For entertainment and self-reflection. Meanings are drawn from Pythagorean numerology and popular Chinese homophone traditions. <a href="{r}disclaimer/">Disclaimer</a>.</p>
</article>
{sidebar(r)}
</div></div></section>
{newsletter_band(r)}"""
    schema = [bc_schema, faq_schema(qas), {"@context": "https://schema.org", "@type": "Article", "headline": f"{s} Angel Number Meaning", "description": desc,
              "author": {"@type": "Organization", "name": "55388 Editorial"}, "publisher": {"@type": "Organization", "name": "55388"}, "mainEntityOfPage": f"https://55388.com/{path}"}]
    return path, page(path, title, desc, body, active="angel-numbers/", schema=schema, og_type="article")

def sidebar(r):
    from layout import MODE
    if MODE["jekyll"] and not MODE.get("raw"):
        return "{% include sidebar.html %}"
    return _sidebar(r)

def _sidebar(r):
    return f"""<aside class="sidebar">
  <div class="card"><span class="badge">Free</span><h3 style="margin-top:8px">Your Number Blueprint</h3>
    <p class="muted small">Life Path, Destiny, Soul Urge & lucky numbers — calculated in 30 seconds.</p>
    <a class="btn btn-primary btn-block" href="{r}reading/">Get My Free Reading</a></div>
  <div class="card" data-notd><p class="muted">Loading today's number…</p></div>
  <div class="card"><h3>Talk to a real reader</h3><p class="muted small">Want a live, personal interpretation? Connect with a vetted advisor.</p>
    <a class="btn btn-grad btn-block" data-aff="liveReading" href="{r}reading/#live">Connect With a Reader</a></div>
  {ad("sidebar", tall=True)}
  <div class="card"><h3>Popular tools</h3><ul class="checklist small">
    <li><a href="{r}tools/life-path-calculator/">Life Path Calculator</a></li><li><a href="{r}tools/name-numerology-calculator/">Name Numerology</a></li>
    <li><a href="{r}tools/chinese-lucky-number-checker/">Chinese Lucky Number Checker</a></li><li><a href="{r}tools/lottery-number-generator/">Lottery Number Generator</a></li></ul></div>
</aside>"""

GROUPS = [
  ("Triple numbers", [str(d) * 3 for d in range(10)]),
  ("Quadruple numbers", [str(d) * 4 for d in range(10)]),
  ("Double numbers", [str(d) * 2 for d in range(1, 10)]),
  ("Mirror & clock numbers", ["0101", "1010", "1212", "1221", "1313", "1414", "1515", "1717", "2020", "2121", "2323"]),
  ("Paired & sequence numbers", ["1122", "1133", "1144", "1155", "123", "1234", "12345", "321", "4321", "369", "911"]),
  ("Special & cultural numbers", ["168", "520", "1314", "5555", "888888", "55388"]),
]

def angel_index():
    path = "angel-numbers/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("", "Angel Numbers")])
    groups = "".join(
        f'<h2 style="margin-top:36px">{g}</h2><div class="num-grid">' +
        "".join(f'<a href="{r}angel-numbers/{n}/">{n}<small>{DIGITS[n[0]]["name"].split(" ")[0]}</small></a>' for n in nums) + "</div>"
        for g, nums in GROUPS)
    digit_cards = "".join(
        f'<div class="card"><div class="stat">{d}</div><h3>{v["name"]}</h3><p class="muted small">{v["short"]}</p><a href="{r}angel-numbers/{d*3}/">See {d*3} →</a></div>'
        for d, v in DIGITS.items())
    body = f"""<section class="hero"><div class="container">{bc_html}
  <span class="eyebrow">Angel number meanings</span>
  <h1>Every angel number, <span class="grad-text">decoded</span>.</h1>
  <p class="lead">Keep seeing 111, 444 or 1212? Look up any number — from single digits to long sequences — and get its meaning for love, career, money and spiritual growth.</p>
  <form class="hero-search" data-lookup role="search"><label class="sr-only" for="an-q">Number</label><input id="an-q" inputmode="numeric" placeholder="Type any number, e.g. 717 or 2244" maxlength="12"><button class="btn btn-primary" type="submit">Find My Angel Number Now</button></form>
</div></section>
<section class="section-tight"><div class="container">{ad("header")}{groups}</div></section>
<section><div class="container"><div class="section-head"><span class="eyebrow">The building blocks</span><h2>What each digit means</h2><p class="muted">Every angel number is built from these ten energies. Learn them once and you can read any sequence.</p></div>
<div class="grid g4">{digit_cards}</div>
<p style="margin-top:24px"><a class="btn btn-ghost" href="{r}guides/how-to-read-number-sequences/">How to read any number sequence →</a></p></div></section>
{newsletter_band(r)}"""
    return path, page(path, "Angel Numbers: Meanings of 111, 222, 333, 444, 555, 1111 & More | 55388",
                      "Look up any angel number meaning — love, twin flame, career and money. 70+ in-depth guides plus a free lookup for any number sequence.",
                      body, active="angel-numbers/", schema=[bc_schema])

def lookup_page():
    path = "angel-numbers/lookup/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("angel-numbers/", "Angel Numbers"), ("", "Lookup")])
    body = f"""<section class="section-tight"><div class="container">{bc_html}
<div class="article"><div>
  <span class="eyebrow">Angel number lookup</span>
  <h1 id="lk-title">Angel number meaning</h1>
  <form class="hero-search" data-lookup role="search"><label class="sr-only" for="lk-q">Number</label><input id="lk-q" name="n" inputmode="numeric" placeholder="Type any number" maxlength="12"><button class="btn btn-primary" type="submit">Look Up</button></form>
  <div id="lk-out" class="prose" data-tool="lookup"></div>
  {ad("inArticle")}
  {birthday_inline(r)}
</div>{sidebar(r)}</div></div></section>"""
    return path, page(path, "Angel Number Lookup — Meaning of Any Number | 55388", "Instant meaning for any number sequence: pattern, numerology root, love, career, money and Chinese luck.",
                      body, active="angel-numbers/", schema=[bc_schema], scripts=("tools.js",))

def angel_data(s):
    """Compact per-number data for the Jekyll/Liquid angel template (_layouts/angel.html)."""
    total = dsum(s); root = reduce(total)
    plabel, ptext = pattern(s)
    counts = {c: s.count(c) for c in dict.fromkeys(s)}
    dom = sorted(counts.items(), key=lambda kv: (-kv[1], -int(kv[0])))[0][0]
    score, combos = chinese_score(s)
    d = dict(root=str(root), red=" + ".join(s) + f" = {total}" + (f" → {root}" if total != root else ""),
             pl=plabel, pt=ptext, dom=dom, counts=[[c, n] for c, n in counts.items()], score=score,
             combos=[[c["n"], c["meaning"]] for c in combos],
             ch=" · ".join(f"{c} {CHINESE['digits'][c]['hanzi']} ({CHINESE['digits'][c]['pinyin']})" for c in dict.fromkeys(s)),
             rel=related(s))
    if s in INTROS: d["intro"] = INTROS[s]
    if len(s) >= 3 and len(set(s)) > 1:
        d["layers"] = dict(cause=s[0], core=s[1:-1], cu=list(dict.fromkeys(s[1:-1])), out=s[-1])
    return d

def roots_data():
    out = {k: dict(name=v["name"], core=v["core"]) for k, v in DIGITS.items()}
    out.update({str(k): dict(name=v["name"], core=v["core"]) for k, v in MASTERS.items()})
    return out

def angel_front(s):
    import json
    t = f"{s} Angel Number Meaning: Love, Twin Flame, Career & Money | 55388"
    ds = f"What does {s} mean? Spiritual meaning, love, twin flame, career, money and Chinese luck of angel number {s} — plus what to do next. Free reading included."
    return f"---\nlayout: angel\nn: \"{s}\"\ntitle: {json.dumps(t, ensure_ascii=False)}\ndescription: {json.dumps(ds, ensure_ascii=False)}\nactive: \"angel-numbers/\"\nog_type: article\n---\n"
