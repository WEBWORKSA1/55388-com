"""Home, lead-gen funnels, community / monetization pages, guides and legal."""
from data import DIGITS, VIDEOS, LIFE_PATH
from layout import page, ad, breadcrumbs, faq_schema, faq_html, birthday_inline, newsletter_band, e, depth_prefix, form_open, INTEREST_URL
from tools_pages import TOOLS

def video_card(v):
    vid, title, ch, _ = v
    return f'<div><div class="video" data-yt="{vid}" data-title="{e(title)}"></div><div class="video-meta"><strong>{e(title)}</strong><div class="small muted">{e(ch)} · via YouTube</div></div></div>'

def home():
    path = "index.html"; r = ""
    popular = ["111", "222", "333", "444", "555", "777", "888", "1111", "1212", "55388"]
    quick = "".join(f'<a href="angel-numbers/{n}/">{n}</a>' for n in popular)
    tools = "".join(f'<a class="card card-link" href="tools/{s}/"><div style="font-size:1.8rem">{ic}</div><h3>{t}</h3><p class="muted small">{d}</p></a>' for s, t, d, ic in TOOLS[:6])
    lp = "".join(f'<a href="numerology/life-path/{k}/">{k}<small>{v[0].replace("The ", "")}</small></a>' for k, v in LIFE_PATH.items())
    vids = "".join(video_card(v) for v in VIDEOS[:3])
    qas = [("What are angel numbers?", "Angel numbers are repeating number sequences — like 111, 444 or 1212 — that many people notice at meaningful moments and interpret as guidance. Numerology gives each digit a meaning, so sequences can be decoded."),
           ("Is 55388 free to use?", "Yes. Every meaning page and tool is free. We're supported by advertising, optional readings, sponsors and reader donations."),
           ("Do you store my birth date?", "Calculators run in your browser. We only receive details you choose to submit in a form, such as a reading request."),
           ("What does 55388 mean?", "5 + 5 + 3 + 8 + 8 = 29 → 11, a master number of insight. Read in layers: change (55) → expression (3) → double abundance (88).")]
    body = f"""
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="eyebrow">Angel numbers · Numerology · Lucky numbers</span>
    <h1>Every number is <span class="grad-text">trying to tell you something</span>.</h1>
    <p class="lead">Decode angel numbers, discover your Life Path, check if a number is lucky, and use 9 free number tools — all in one place.</p>
    <form class="hero-search" data-lookup role="search"><label class="sr-only" for="home-q">Enter a number</label>
      <input id="home-q" inputmode="numeric" placeholder="What number do you keep seeing?" maxlength="12"><button class="btn btn-primary" type="submit">Decode It</button></form>
    <div class="quick-nums" aria-label="Popular numbers">{quick}</div>
    <div class="trust-line"><span>✓ 70+ in-depth number guides</span><span>✓ 9 free tools</span><span>✓ Private — runs in your browser</span></div>
  </div>
  <div class="orb" aria-hidden="true"><div class="big grad-text">55388</div><div class="caption">5+5+3+8+8 = 29 → <strong>11</strong><br>the master number of insight</div></div>
</div></section>
<section class="section-tight"><div class="container"><div class="card" data-notd><p class="muted">Loading today's number…</p></div></div></section>
<section><div class="container">
  <div class="grid g2" style="align-items:center">
    <div><span class="eyebrow">Free personal reading</span><h2>Your numbers, decoded in 30 seconds.</h2>
      <p class="muted">Enter your name and birthday to reveal your Life Path, Destiny, Soul Urge, Personal Year and personal angel number — with a forecast for love, career and money.</p>
      <ul class="checklist"><li>Instant, on-screen results</li><li>Your lucky numbers & personal angel number</li><li>12-month personal year forecast</li><li>Free — no card, no catch</li></ul></div>
    <div class="lead-box"><h3>Start your Number Blueprint</h3>
      <form action="reading/" method="get">
        <div class="field"><label for="h-name">Full name</label><input id="h-name" name="fullname" required autocomplete="name"></div>
        <div class="field"><label for="h-dob">Birthday</label><input id="h-dob" name="dob" type="date" required></div>
        <button class="btn btn-primary btn-block" type="submit">Reveal My Numbers →</button>
        <p class="small muted center" style="margin:8px 0 0">🔒 Private · Free · 30 seconds</p></form></div>
  </div></div></section>
{ad("header")}
<section><div class="container"><div class="section-head"><span class="eyebrow">Most searched</span><h2>Popular angel numbers</h2></div>
<div class="num-grid">{"".join(f'<a href="angel-numbers/{n}/">{n}<small>{DIGITS[n[0]]["name"].split(" ")[0]}</small></a>' for n in ["000","111","222","333","444","555","666","777","888","999","1111","1212","1234","2222","5555","88","168","520","1314","55388"])}</div>
<p style="margin-top:18px"><a class="btn btn-ghost" href="angel-numbers/">Browse all angel numbers →</a></p></div></section>
<section><div class="container"><div class="section-head"><span class="eyebrow">Free tools</span><h2>Number tools people bookmark</h2></div><div class="grid g3">{tools}</div>
<p style="margin-top:18px"><a class="btn btn-ghost" href="tools/">All 9 tools →</a></p></div></section>
<section><div class="container"><div class="section-head"><span class="eyebrow">Numerology</span><h2>Find your Life Path</h2><p class="muted">Twelve paths — nine core numbers and three master numbers.</p></div><div class="num-grid">{lp}</div></div></section>
<section><div class="container"><div class="grid g2" style="align-items:center">
  <div><span class="eyebrow">Chinese lucky numbers</span><h2>Is your phone number lucky?</h2><p class="muted">In Chinese culture, 8 sounds like "prosper" and 4 sounds like "death". Score any phone number, plate, address or price from 1 to 100.</p>
  <a class="btn btn-primary" href="tools/chinese-lucky-number-checker/">Check My Number</a> <a class="btn btn-ghost" href="chinese-lucky-numbers/">Read the guide</a></div>
  <div class="card"><div class="digit-row"><div><div class="d">8</div>八 bā<div class="small muted">发 prosper</div></div><div><div class="d">6</div>六 liù<div class="small muted">流 smooth</div></div><div><div class="d">9</div>九 jiǔ<div class="small muted">久 lasting</div></div><div><div class="d">4</div>四 sì<div class="small muted">死 avoided</div></div></div></div>
</div></div></section>
<section><div class="container"><div class="section-head"><span class="eyebrow">Watch</span><h2>Numbers, explained on video</h2></div><div class="grid g3">{vids}</div>
<p style="margin-top:18px"><a class="btn btn-ghost" href="videos/">More videos →</a> <a class="btn btn-ghost" data-yt-channel hidden href="#">Subscribe on YouTube</a></p></div></section>
<section><div class="container"><div class="grid g3">
  <div class="card"><span class="eyebrow">Win</span><h3>Monthly Lucky Number Challenge</h3><p class="muted">Share your number story, video or art. Cash & gift prizes every month.</p><a href="contests/">Enter the contest →</a></div>
  <div class="card"><span class="eyebrow">Business</span><h3>Lucky Number Audit</h3><p class="muted">Brand name, phone number, address and launch date — scored and optimized.</p><a href="business-lucky-number-audit/">Request an audit →</a></div>
  <div class="card"><span class="eyebrow">Support</span><h3>Keep 55388 free</h3><p class="muted">Fuel new tools, writers, contests and prizes. Every contribution counts.</p><a href="support/">Support us →</a></div>
</div></div></section>
<section><div class="container" style="max-width:860px"><h2>FAQ</h2>{faq_html(qas)}</div></section>
{newsletter_band(r)}"""
    schema = [faq_schema(qas), {"@context": "https://schema.org", "@type": "Organization", "name": "55388", "url": "https://55388.com/", "logo": "https://55388.com/assets/img/favicon.svg"}]
    return path, page(path, "55388 — Angel Numbers, Numerology & Lucky Number Tools", "Decode any angel number, find your Life Path, check Chinese lucky numbers and use free number tools. 70+ guides — free, private and instant.", body, schema=schema)

def reading():
    path = "reading/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("", "Free Reading")])
    qas = [("Is the reading really free?", "Yes. Your Number Blueprint is calculated instantly and shown on screen at no cost."),
           ("Why do you ask for my email?", "To unlock your full blueprint, send you your Daily Number and occasional offers. Unsubscribe anytime; we never sell your data."),
           ("Is numerology scientifically proven?", "No. Numerology is a symbolic system used for reflection and entertainment. Use it as a lens, not as a rulebook.")]
    body = f"""<section class="hero"><div class="container">{bc_html}
<div class="hero-grid top">
<div><span class="eyebrow">Free Number Blueprint</span><h1>Discover what your numbers <span class="grad-text">say about you</span>.</h1>
<p class="lead">Your name and birthday hold five core numbers. See them instantly — then unlock your full blueprint with lucky numbers, your personal angel number and a 12-month forecast.</p>
<ul class="checklist"><li>Life Path, Destiny, Soul Urge & Personality numbers</li><li>Personal Year forecast for love, career & money</li><li>Your lucky numbers and personal angel number</li><li>Printable / save as PDF</li></ul>
<div class="trust-line"><span>🔒 Never sold</span><span>⚡ Results in 30 seconds</span><span>✓ Free</span></div></div>
<div class="lead-box">
<form id="blueprint" data-form="blueprint-lead" data-subject="Free Number Blueprint lead" data-custom>
  <input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
  <div class="steps" aria-hidden="true"><span class="on"></span><span></span><span></span></div>
  <div class="step active"><h2 style="font-size:1.5rem">Step 1 · Your details</h2>
    <div class="field"><label for="bp-name">Full birth name</label><input id="bp-name" name="fullname" autocomplete="name" placeholder="e.g. Maya Grace Lee"></div>
    <div class="field"><label for="bp-dob">Birthday</label><input id="bp-dob" name="dob" type="date"></div>
    <div class="field"><label for="bp-goal">What do you most want clarity on?</label><select id="bp-goal" name="goal"><option value="love">Love & relationships</option><option value="career">Career & business</option><option value="money">Money & abundance</option><option value="purpose">Life purpose</option></select></div>
    <button class="btn btn-primary btn-block" type="button" data-next>Reveal My Numbers →</button></div>
  <div class="step"><h2 style="font-size:1.5rem">Step 2 · Your free preview</h2><div id="preview"></div>
    <div class="field"><label for="bp-email">Email to unlock your full blueprint</label><input id="bp-email" name="email" type="email" autocomplete="email" placeholder="you@email.com"></div>
    <div class="field"><label for="bp-country">Country (optional)</label><input id="bp-country" name="country" autocomplete="country-name"></div>
    <label class="check"><input type="checkbox" name="consent" value="yes"> I agree to receive my blueprint, the Daily Number email and occasional offers. Unsubscribe anytime. See <a href="{r}privacy/">Privacy</a>.</label>
    <button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Unlock My Full Blueprint</button>
    <button class="btn btn-ghost btn-block" type="button" data-back style="margin-top:8px">← Edit details</button></div>
  <div class="step"><div id="full"></div></div>
</form></div></div></div></section>
<section id="live"><div class="container"><div class="section-head center"><span class="eyebrow">Choose your path</span><h2>Three ways to go deeper</h2></div>
<div class="grid g3">
  <div class="card price-card"><span class="pill">Free</span><h3 style="margin-top:10px">Number Blueprint</h3><div class="price">$0</div><ul class="checklist small"><li>5 core numbers</li><li>Year-ahead theme</li><li>Lucky numbers</li></ul><a class="btn btn-ghost btn-block" href="#blueprint">Start free</a></div>
  <div class="card price-card featured"><span class="badge">Most popular</span><h3 style="margin-top:10px">Live reading with an advisor</h3><div class="price">Intro offers</div><p class="muted small">Talk or chat with a vetted numerology / intuitive advisor. Partner platforms typically offer discounted first minutes.</p><a class="btn btn-grad btn-block" data-aff="liveReading" href="{r}contact/?topic=Live%20reading">Connect With a Reader</a></div>
  <div class="card price-card"><span class="pill">Business</span><h3 style="margin-top:10px">Lucky Number Audit</h3><div class="price">Custom</div><ul class="checklist small"><li>Brand & domain name</li><li>Phone, address, plate</li><li>Launch-date timing</li></ul><a class="btn btn-primary btn-block" href="{r}business-lucky-number-audit/">Request audit</a></div>
</div>
<p class="small muted center" style="margin-top:14px">Some links are affiliate links; we may earn a commission at no extra cost to you. <a href="{r}disclaimer/">Disclosure</a>.</p></div></section>
<section><div class="container" style="max-width:860px"><h2>FAQ</h2>{faq_html(qas)}</div></section>"""
    return path, page(path, "Free Numerology Reading: Your Number Blueprint in 30 Seconds | 55388", "Get a free personalized numerology reading — Life Path, Destiny, Soul Urge, lucky numbers and your personal angel number.", body, schema=[bc_schema, faq_schema(qas)], scripts=("reading.js",))

def business_audit():
    path = "business-lucky-number-audit/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("", "Business Lucky Number Audit")])
    body = f"""<section class="hero"><div class="container">{bc_html}<div class="hero-grid">
<div><span class="eyebrow">For founders, brands & property owners</span><h1>Make your numbers <span class="grad-text">work for your brand</span>.</h1>
<p class="lead">Numbers shape first impressions — especially with Chinese, Indian and numerology-aware customers. We audit your brand name, domain, phone number, address, pricing and launch date, and recommend stronger alternatives.</p>
<ul class="checklist"><li>Name & domain numerology (Pythagorean + Chaldean)</li><li>Chinese homophone check for phone, plate, unit & price</li><li>Auspicious launch / opening date shortlist</li><li>Clear written report with recommendations</li></ul>
<div class="grid g3" style="margin-top:20px"><div><div class="stat">3</div><div class="small muted">audit tiers</div></div><div><div class="stat">48h</div><div class="small muted">target first reply</div></div><div><div class="stat">1:1</div><div class="small muted">follow-up call option</div></div></div></div>
<div class="lead-box">{form_open("business-audit", "Business Lucky Number Audit request", "Request received! We'll reply with scope and pricing shortly.")}
  <h2 style="font-size:1.4rem">Request your audit</h2>
  <div class="row"><div class="field"><label for="ba-n">Your name</label><input id="ba-n" name="name" required autocomplete="name"></div><div class="field"><label for="ba-e">Work email</label><input id="ba-e" name="email" type="email" required autocomplete="email"></div></div>
  <div class="row"><div class="field"><label for="ba-b">Business / brand name</label><input id="ba-b" name="business" required></div><div class="field"><label for="ba-w">Website or domain</label><input id="ba-w" name="website" placeholder="example.com"></div></div>
  <div class="field"><label for="ba-num">Numbers to audit</label><input id="ba-num" name="number" placeholder="Phone, address, unit, plate, price…"></div>
  <div class="row"><div class="field"><label for="ba-t">Audit type</label><select id="ba-t" name="audit_type"><option>Quick score (1–3 numbers)</option><option>Brand audit (name + domain + numbers)</option><option>Full launch package (incl. date selection)</option><option>Not sure — advise me</option></select></div>
  <div class="field"><label for="ba-bud">Budget</label><select id="ba-bud" name="budget"><option>Under $100</option><option>$100–$500</option><option>$500–$2,000</option><option>$2,000+</option></select></div></div>
  <div class="field"><label for="ba-m">Anything else?</label><textarea id="ba-m" name="message" placeholder="Launch date, target market, goals…"></textarea></div>
  <label class="check"><input type="checkbox" required name="consent" value="yes"> I agree to be contacted about my request.</label>
  <button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Get My Audit Proposal</button>
</form></div></div></div></section>
<section class="section-tight"><div class="container prose" style="max-width:860px">
<h2>Who it's for</h2><ul><li><strong>Startups & e-commerce</strong> choosing a brand name, domain or launch date.</li><li><strong>Restaurants, retail & hospitality</strong> serving Chinese, Vietnamese, Indian and other number-conscious communities.</li><li><strong>Real estate agents & developers</strong> pricing listings and naming units.</li><li><strong>Individuals</strong> choosing a phone number, plate, wedding date or baby name.</li></ul>
<p class="small muted">Audits are cultural and symbolic guidance, not legal, financial or trademark advice.</p></div></section>"""
    return path, page(path, "Business Lucky Number Audit — Brand, Phone, Address & Launch Date | 55388", "Audit your brand name, domain, phone number, address, pricing and launch date with numerology and Chinese number symbolism.", body, schema=[bc_schema])

def videos():
    path = "videos/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("", "Videos")])
    sections = ""
    for key, label in [("angel", "Angel numbers"), ("numerology", "Numerology & Life Path"), ("chinese", "Chinese lucky numbers")]:
        sections += f'<h2 style="margin-top:36px">{label}</h2><div class="grid g3">' + "".join(video_card(v) for v in VIDEOS if v[3] == key) + "</div>"
    body = f"""<section class="hero"><div class="container">{bc_html}<span class="eyebrow">Video library</span><h1>Numbers, <span class="grad-text">explained on video</span>.</h1>
<p class="lead">Hand-picked explainers on angel numbers, numerology and Chinese number culture. Videos load only when you press play.</p>
<a class="btn btn-primary" data-yt-channel hidden href="#">Subscribe to our channel</a></div></section>
<section class="section-tight"><div class="container">{ad("header")}{sections}
<div class="card" style="margin-top:36px"><h3>Are you a creator?</h3><p class="muted">Submit your number-related video to be featured, or join our paid creator program.</p><a class="btn btn-ghost" href="{r}careers/#apply">Apply as a creator</a> <a class="btn btn-ghost" href="{r}contests/">Enter the video contest</a></div>
<p class="small muted" style="margin-top:18px">Videos are embedded via YouTube's standard player and remain the property of their creators. Inclusion does not imply endorsement or affiliation.</p></div></section>{newsletter_band(r)}"""
    return path, page(path, "Angel Number & Numerology Videos | 55388", "Watch the best explainers on angel numbers, life path numerology and Chinese lucky numbers.", body, active="videos/", schema=[bc_schema])

GUIDES = [
  ("what-are-angel-numbers", "What Are Angel Numbers? A Clear, No-Hype Guide",
   "What angel numbers are, why you keep seeing them, and how to interpret them without overthinking.",
   """<p>Angel numbers are repeating or patterned number sequences — 111, 444, 1212 — that people notice at meaningful moments and interpret as guidance. The idea blends <strong>Pythagorean numerology</strong> (each digit carries a meaning) with modern spirituality (the belief that the universe, guides or your own intuition communicate through patterns).</p>
<h2>Why do I keep seeing the same number?</h2><p>Two things are true at once. Psychologically, once a number feels significant your brain's <em>reticular activating system</em> flags it more often — a form of frequency illusion. Symbolically, many people find that pausing when a number appears is a useful cue to check in with themselves. You don't need to pick a side to benefit: treat each sighting as a prompt to reflect.</p>
<h2>How to interpret any angel number in 3 steps</h2><ol><li><strong>Identify the dominant digit.</strong> In 4447, the 4 dominates: stability and foundations.</li><li><strong>Check the pattern.</strong> Repeating = amplified message; mirror = reflection; ascending = progress; mixed = read as cause → core → outcome.</li><li><strong>Reduce to a root.</strong> Add the digits and reduce (4+4+4+7 = 19 → 10 → 1). The root adds the overall theme.</li></ol>
<h2>The ten digit meanings</h2><table><thead><tr><th>Digit</th><th>Meaning</th></tr></thead><tbody>""" + "".join(f"<tr><td>{d}</td><td>{v['name']} — {v['short']}</td></tr>" for d, v in DIGITS.items()) + """</tbody></table>
<h2>Common mistakes</h2><ul><li>Treating a number as a command. It's a prompt, not an order.</li><li>Ignoring context. What you were thinking when you saw it matters most.</li><li>Fear-based readings. Even "scary" numbers like 666 carry constructive meanings in numerology.</li></ul>"""),
  ("how-to-read-number-sequences", "How to Read Any Number Sequence (Cause → Core → Outcome)",
   "A simple method for decoding long or mixed number sequences like 4417, 7340 or 55388.",
   """<p>Single repeating numbers are easy. But what about 7340 or 55388? Use the <strong>layered method</strong> popularized by long-time angel-number writers: the first digit(s) show the <em>cause</em>, the middle digits show the <em>core message</em>, and the last digit(s) show the likely <em>outcome</em>.</p>
<h2>Worked example: 55388</h2><ul><li><strong>Cause — 55:</strong> doubled change and freedom. A shift is underway.</li><li><strong>Core — 3:</strong> expression and growth. Speak, create, publish.</li><li><strong>Outcome — 88:</strong> doubled abundance. The change, expressed well, leads to prosperity.</li><li><strong>Root:</strong> 5+5+3+8+8 = 29 → 11, the master number of insight.</li></ul>
<h2>Weighting rules</h2><ol><li>A digit that appears more than once is louder.</li><li>Zeros amplify their neighbours.</li><li>Master numbers (11, 22, 33) inside a sequence add intensity.</li></ol>
<p><a class="btn btn-primary" href="../../angel-numbers/lookup/?n=55388">Try the lookup tool →</a></p>"""),
  ("lucky-numbers-around-the-world", "Lucky & Unlucky Numbers Around the World",
   "From China's 8 to Italy's 17 — how cultures assign luck to numbers, and why it matters for business.",
   """<p>Number superstitions are global, and they move real money — from licence-plate auctions to skipped hotel floors.</p>
<table><thead><tr><th>Culture</th><th>Lucky</th><th>Unlucky</th><th>Why</th></tr></thead><tbody>
<tr><td>China</td><td>8, 6, 9</td><td>4</td><td>8 sounds like "prosper", 4 like "death".</td></tr>
<tr><td>Japan</td><td>7, 8</td><td>4, 9</td><td>4 (shi) sounds like death; 9 (ku) like suffering.</td></tr>
<tr><td>Western countries</td><td>7</td><td>13</td><td>Seven's religious and natural significance; 13's association with bad luck.</td></tr>
<tr><td>Italy</td><td>13 (sometimes)</td><td>17</td><td>XVII rearranges to VIXI, "I have lived" — i.e. I'm dead.</td></tr>
<tr><td>India</td><td>varies by tradition</td><td>varies</td><td>Vedic numerology links numbers to planets; odd amounts (101, 501) are common for gifts.</td></tr>
</tbody></table>
<h2>Why it matters for business</h2><p>Pricing (ending in 8), phone numbers, launch dates and even floor numbering can influence how customers feel. If you serve multicultural audiences, a quick <a href="../../business-lucky-number-audit/">number audit</a> is cheap insurance.</p>"""),
]

def guides():
    out = []
    path = "guides/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("", "Guides")])
    cards = "".join(f'<a class="card card-link" href="{r}guides/{s}/"><h3>{e(t)}</h3><p class="muted small">{e(d)}</p></a>' for s, t, d, _ in GUIDES)
    body = f"""<section class="hero"><div class="container">{bc_html}<span class="eyebrow">Guides</span><h1>Learn to read numbers <span class="grad-text">yourself</span>.</h1></div></section>
<section class="section-tight"><div class="container"><div class="grid g3">{cards}</div></div></section>{newsletter_band(r)}"""
    out.append((path, page(path, "Number Guides: Angel Numbers, Sequences & Lucky Numbers | 55388", "In-depth guides to angel numbers, reading number sequences and lucky numbers around the world.", body, schema=[bc_schema])))
    from angel import sidebar
    for s, t, d, content in GUIDES:
        p = f"guides/{s}/"; r = depth_prefix(p)
        bc_html, bc_schema = breadcrumbs(r, [("guides/", "Guides"), ("", t)])
        body = f"""<section class="section-tight"><div class="container">{bc_html}<div class="article"><article class="prose"><span class="eyebrow">Guide</span><h1>{e(t)}</h1><p class="lead muted">{e(d)}</p>
{ad("header")}{content}{birthday_inline(r)}{ad("inArticle")}<p class="small muted">By the 55388 Editorial team · For entertainment and self-reflection.</p></article>{sidebar(r)}</div></div></section>{newsletter_band(r)}"""
        out.append((p, page(p, f"{t} | 55388", d, body, schema=[bc_schema, {"@context": "https://schema.org", "@type": "Article", "headline": t, "description": d, "author": {"@type": "Organization", "name": "55388 Editorial"}}], og_type="article")))
    return out

def support():
    path = "support/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("", "Support 55388")])
    tiers = [("5", "Supporter", "Covers a day of hosting & tools"), ("25", "Booster", "Funds one new number guide"), ("88", "Prosperity Patron", "Funds a monthly contest prize"), ("388", "Sponsor Circle", "Funds a new tool + public thanks")]
    tier_html = "".join(f'<button type="button" class="tier" data-amt="{a}"><div class="amt">${a}</div><strong>{n}</strong><div class="small muted">{d}</div></button>' for a, n, d in tiers)
    alloc = [("Operations — hosting, tools, security", 30), ("Content & hiring talent — writers, numerologists, creators, developers", 25), ("Promotion & marketing — growth, social, video", 20), ("Contests & prizes — monthly challenges", 20), ("Reserve", 5)]
    alloc_html = "".join(f'<div><div style="display:flex;justify-content:space-between"><span>{a}</span><strong>{p}%</strong></div><div class="bar"><i style="width:{p}%"></i></div></div>' for a, p in alloc)
    body = f"""<section class="hero"><div class="container">{bc_html}<div class="hero-grid"><div>
<span class="eyebrow">Support independent publishing</span><h1>Help keep 55388 <span class="grad-text">free for everyone</span>.</h1>
<p class="lead">Every meaning page and tool on 55388 is free. Your support pays for operations, new tools, paid writers and creators, marketing, and the prizes in our monthly contests.</p>
<div class="card alloc"><h3>Where your contribution goes</h3>{alloc_html}<p class="small muted" style="margin:0">Planned allocation; updated in our public changelog as the project grows.</p></div></div>
<div class="lead-box" id="give"><h2 style="font-size:1.5rem">Choose an amount</h2><div class="tiers">{tier_html}</div>
<div style="display:grid;gap:10px;margin-top:18px">
  <a class="btn btn-primary btn-block" data-donate="stripe" data-hide-if-empty hidden href="#">Give by card (Stripe)</a>
  <a class="btn btn-primary btn-block" data-donate="paypal" data-hide-if-empty hidden href="#">Give with PayPal</a>
  <a class="btn btn-ghost btn-block" data-donate="kofi" data-hide-if-empty hidden href="#">Support on Ko-fi</a>
  <a class="btn btn-ghost btn-block" data-donate="buymeacoffee" data-hide-if-empty hidden href="#">Buy us a coffee</a></div>
<h3 style="margin-top:20px">Pledge or sponsor directly</h3>
{form_open("donation-pledge", "Donation / support pledge", "Thank you! We'll send secure payment details and a receipt to your email.")}
  <div class="row"><div class="field"><label for="dn-n">Name</label><input id="dn-n" name="name" required autocomplete="name"></div><div class="field"><label for="dn-e">Email</label><input id="dn-e" name="email" type="email" required autocomplete="email"></div></div>
  <div class="row"><div class="field"><label for="dn-a">Amount (USD)</label><input id="dn-a" name="amount" inputmode="decimal" required placeholder="e.g. 88"></div>
  <div class="field"><label for="dn-p">Put it toward</label><select id="dn-p" name="purpose"><option>Where it's needed most</option><option>Operations & hosting</option><option>Promotions & marketing</option><option>Hiring talent (writers, creators, developers)</option><option>Contests & prizes</option><option>A specific new tool</option></select></div></div>
  <div class="row"><div class="field"><label for="dn-f">Frequency</label><select id="dn-f" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div>
  <div class="field"><label for="dn-c">Public thanks?</label><select id="dn-c" name="recognition"><option>Yes, list my name</option><option>Yes, list my business (sponsors)</option><option>No, keep me anonymous</option></select></div></div>
  <div class="field"><label for="dn-m">Message (optional)</label><textarea id="dn-m" name="message" style="min-height:80px"></textarea></div>
  <button class="btn btn-primary btn-block" type="submit">Pledge My Support</button>
  <p class="small muted" style="margin-top:8px">We never ask for card details by email or in this form. Contributions are not tax-deductible unless stated on your receipt.</p>
</form></div></div></div></section>
<section class="section-tight"><div class="container"><div class="grid g3">
<div class="card"><h3>🏆 Fund a prize</h3><p class="muted">Sponsor a monthly contest prize and get featured on the contest page and winner announcement.</p><a href="{r}contests/#sponsor">Sponsor a contest →</a></div>
<div class="card"><h3>🧑‍💻 Fund a hire</h3><p class="muted">Pay for a writer, numerologist, video creator or developer for a month. Named credit on what they build.</p><a href="{r}careers/">See open roles →</a></div>
<div class="card"><h3>📣 Fund a campaign</h3><p class="muted">Back a promotion push — social, video, or a partnership launch — and receive a results report.</p><a href="{r}advertise/">Partner with us →</a></div>
</div></div></section>
<script>document.addEventListener("DOMContentLoaded",()=>{{document.querySelectorAll(".tier").forEach(t=>t.addEventListener("click",()=>{{document.querySelectorAll(".tier").forEach(x=>x.classList.remove("sel"));t.classList.add("sel");const a=document.getElementById("dn-a");if(a)a.value=t.dataset.amt;a&&a.focus();}}));}});</script>"""
    return path, page(path, "Support 55388 — Donate, Sponsor or Fund a Prize", "Support free number tools and guides. Donate, pledge monthly, fund contest prizes, hires or promotions.", body, active="support/", schema=[bc_schema])

def contests():
    path = "contests/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("", "Contests & Prizes")])
    qas = [("Is this a lottery?", "No. Winners are selected by judges on skill and creativity against published criteria. No purchase or donation is necessary to enter or win."),
           ("Who can enter?", "Anyone 18+ (or the age of majority where you live), where not prohibited by law."),
           ("How are winners announced?", "On this page and by email within 14 days after each monthly deadline."),
           ("Who owns my entry?", "You do. By entering you grant 55388 a non-exclusive licence to display and promote your entry with credit.")]
    body = f"""<section class="hero"><div class="container">{bc_html}<span class="eyebrow">Monthly contest</span>
<h1>The <span class="grad-text">Lucky Number Challenge</span></h1>
<p class="lead">Tell us the story of a number that changed your life — in words, video or art. Judges pick the most creative, heartfelt entries every month.</p>
<div class="grid g3" style="margin-top:24px">
  <div class="card center"><div class="stat">🥇 $88</div><strong>1st prize</strong><p class="small muted">+ featured story & winner badge</p></div>
  <div class="card center"><div class="stat">🥈 $55</div><strong>2nd prize</strong><p class="small muted">+ featured on our socials</p></div>
  <div class="card center"><div class="stat">🥉 $38</div><strong>3rd prize</strong><p class="small muted">+ honorable mention</p></div></div>
<p class="small muted" style="margin-top:10px">Prizes paid as cash or gift card equivalent. Sponsor prizes may be added each month.</p></div></section>
<section class="section-tight"><div class="container"><div class="grid g2">
<div class="prose"><h2>Categories</h2><ul><li><strong>✍️ Number Story</strong> — up to 500 words about a number that appeared at a key moment.</li><li><strong>🎬 Short Video</strong> — under 90 seconds (YouTube, TikTok or Instagram link).</li><li><strong>🎨 Number Art</strong> — illustration, design or photo inspired by a number.</li></ul>
<h2>Judging criteria</h2><ul><li>Creativity & originality — 40%</li><li>Storytelling / craft — 40%</li><li>Connection to numbers & meaning — 20%</li></ul>
<h2>Official rules (summary)</h2><ul><li>No purchase, donation or subscription necessary. Skill-based contest; not a game of chance.</li><li>18+ (or age of majority). Void where prohibited.</li><li>One entry per person per category per month. Entries must be your original work and must not infringe anyone's rights.</li><li>Deadline: last day of each month, 23:59 UTC. Winners notified by email within 14 days and must reply within 14 days to claim.</li><li>Winners may need to provide ID/tax forms where legally required. Taxes are the winner's responsibility.</li><li>55388 may cancel or modify a contest if fraud or technical issues occur. Full terms: <a href="{r}terms/">Terms of Use</a>.</li></ul>
<h2>FAQ</h2>{faq_html(qas)}</div>
<div class="lead-box" id="enter">{form_open("contest-entry", "Contest entry — Lucky Number Challenge", "Entry received! Good luck — winners are announced within 14 days of the deadline.")}
  <h2 style="font-size:1.5rem">Enter this month's challenge</h2>
  <div class="row"><div class="field"><label for="ct-n">Full name</label><input id="ct-n" name="name" required autocomplete="name"></div><div class="field"><label for="ct-e">Email</label><input id="ct-e" name="email" type="email" required autocomplete="email"></div></div>
  <div class="row"><div class="field"><label for="ct-c">Category</label><select id="ct-c" name="category"><option>Number Story</option><option>Short Video</option><option>Number Art</option></select></div><div class="field"><label for="ct-num">Your number</label><input id="ct-num" name="number" inputmode="numeric" required placeholder="e.g. 1111"></div></div>
  <div class="field"><label for="ct-l">Link to your entry (video, art, doc)</label><input id="ct-l" name="entry_link" type="url" placeholder="https://"></div>
  <div class="field"><label for="ct-s">Your story (up to 500 words)</label><textarea id="ct-s" name="story" maxlength="3500"></textarea></div>
  <div class="field"><label for="ct-cn">Country</label><input id="ct-cn" name="country" required autocomplete="country-name"></div>
  <label class="check"><input type="checkbox" name="age_rules" value="yes" required> I'm 18+ (or the age of majority), the entry is my original work, and I accept the official rules.</label>
  <label class="check"><input type="checkbox" name="newsletter" value="yes"> Send me the Daily Number email too.</label>
  <button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Submit My Entry</button></form></div>
</div></div></section>
<section id="sponsor" class="section-tight"><div class="container"><div class="card"><div class="grid g2" style="align-items:center">
<div><span class="eyebrow">Sponsors</span><h2>Sponsor a month's prizes</h2><p class="muted">Put your brand in front of an engaged, curious audience. Sponsors get logo placement on the contest page, a mention in the winner announcement and newsletter, and a "presented by" credit.</p></div>
<div>{form_open("contest-sponsor", "Contest sponsorship inquiry", "Thanks! We'll send the sponsorship pack shortly.")}
<div class="row"><div class="field"><label for="sp-n">Name</label><input id="sp-n" name="name" required></div><div class="field"><label for="sp-e">Email</label><input id="sp-e" name="email" type="email" required></div></div>
<div class="row"><div class="field"><label for="sp-c">Company</label><input id="sp-c" name="company" required></div><div class="field"><label for="sp-b">Prize budget</label><select id="sp-b" name="budget"><option>$100–$250</option><option>$250–$1,000</option><option>$1,000+</option><option>Product prizes</option></select></div></div>
<button class="btn btn-primary" type="submit">Become a Sponsor</button></form></div></div></div></div></section>"""
    return path, page(path, "Lucky Number Challenge — Monthly Contest & Prizes | 55388", "Enter the monthly Lucky Number Challenge: share your number story, video or art and win cash prizes. Free to enter.", body, active="contests/", schema=[bc_schema, faq_schema(qas)])

def careers():
    path = "careers/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("", "Careers & Talent")])
    roles = [("Numerology & spirituality writer", "Freelance · Remote", "Write in-depth, well-researched number guides. Paid per article."),
             ("Certified numerologist / reader", "Freelance · Remote", "Deliver personal and business readings; review content for accuracy."),
             ("Short-form video creator", "Freelance · Remote", "Create Shorts/Reels/TikToks about angel numbers and lucky numbers."),
             ("Chinese culture contributor", "Freelance · Remote", "Mandarin/Cantonese speaker to expand our Chinese number content."),
             ("SEO & growth marketer", "Contract · Remote", "Own keyword strategy, internal linking and partnerships."),
             ("Front-end developer", "Contract · Remote", "Build new tools in vanilla JS; performance and accessibility minded."),
             ("Community & contest moderator", "Part-time · Remote", "Run monthly contests, judge entries and engage the community.")]
    role_cards = "".join(f'<div class="card"><span class="pill">{t}</span><h3 style="margin-top:10px">{n}</h3><p class="muted small">{d}</p><a href="#apply" onclick="document.getElementById(\'cr-r\').value=\'{n}\'">Apply →</a></div>' for n, t, d in roles)
    options = "".join(f"<option>{n}</option>" for n, _, _ in roles)
    body = f"""<section class="hero"><div class="container">{bc_html}<span class="eyebrow">Work with us</span><h1>Build the internet's best <span class="grad-text">home for numbers</span>.</h1>
<p class="lead">We're a small, remote-first team hiring freelance and contract talent. Flexible hours, paid work, credit for what you create.</p></div></section>
<section class="section-tight"><div class="container"><div class="grid g3">{role_cards}</div></div></section>
<section id="apply" class="section-tight"><div class="container" style="max-width:760px"><div class="lead-box">
{form_open("talent-application", "Talent application", "Application received! If there's a fit we'll be in touch within 10 business days.")}
<h2 style="font-size:1.5rem">Apply / join our talent pool</h2>
<div class="row"><div class="field"><label for="cr-n">Full name</label><input id="cr-n" name="name" required autocomplete="name"></div><div class="field"><label for="cr-e">Email</label><input id="cr-e" name="email" type="email" required autocomplete="email"></div></div>
<div class="row"><div class="field"><label for="cr-r">Role</label><select id="cr-r" name="role">{options}<option>Other / open application</option></select></div><div class="field"><label for="cr-l">Location & time zone</label><input id="cr-l" name="location" required></div></div>
<div class="row"><div class="field"><label for="cr-p">Portfolio / LinkedIn / channel</label><input id="cr-p" name="portfolio" type="url" placeholder="https://"></div><div class="field"><label for="cr-rate">Expected rate</label><input id="cr-rate" name="rate" placeholder="e.g. $40/hr or $150/article"></div></div>
<div class="field"><label for="cr-a">Availability</label><select id="cr-a" name="availability"><option>Under 10 hrs/week</option><option>10–20 hrs/week</option><option>20–40 hrs/week</option><option>Project-based</option></select></div>
<div class="field"><label for="cr-m">Why you, in a few lines</label><textarea id="cr-m" name="message" required></textarea></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree that my application details may be stored for up to 12 months for hiring purposes.</label>
<button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Send Application</button></form></div></div></section>"""
    return path, page(path, "Careers — Writers, Numerologists, Creators & Developers | 55388", "Join 55388: freelance writers, numerologists, video creators, Chinese culture contributors, SEO and developers.", body, schema=[bc_schema])

def advertise():
    path = "advertise/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("", "Advertise & Partner")])
    packs = [("Sponsored Tool", "from $188/mo", ["'Presented by' on one tool page", "Logo + link in tool results", "Monthly performance report"]),
             ("Homepage Feature", "from $388/mo", ["Hero-adjacent brand placement", "Featured card in 'Popular' section", "Newsletter mention"], True),
             ("Newsletter Sponsor", "from $88/issue", ["Top-of-email placement", "Custom copy + CTA", "Click reporting"]),
             ("Contest Partner", "Custom", ["'Presented by' on monthly contest", "Prize branding", "Social & email promotion"])]
    pc = "".join(f'<div class="card price-card{" featured" if len(p) > 3 else ""}">{"<span class=badge>Best value</span>" if len(p) > 3 else ""}<h3 style="margin-top:8px">{p[0]}</h3><div class="price" style="font-size:1.6rem">{p[1]}</div><ul class="checklist small">{"".join(f"<li>{x}</li>" for x in p[2])}</ul><a class="btn btn-ghost btn-block" href="#inquire">Inquire</a></div>' for p in packs)
    body = f"""<section class="hero"><div class="container">{bc_html}<span class="eyebrow">Advertising · Sponsorship · Partnerships</span>
<h1>Reach people who are <span class="grad-text">searching for meaning</span>.</h1>
<p class="lead">55388 serves readers looking up angel numbers, numerology, lucky numbers and everyday number tools — a curious, high-intent, global audience. Perfect for wellness, spirituality, astrology, jewelry, books, education, finance-literacy and lifestyle brands.</p>
<p><a class="btn btn-primary" href="#inquire">Request the media kit</a> <a class="btn btn-ghost" href="{INTEREST_URL}" target="_blank" rel="noopener">Interested in the domain itself?</a></p></div></section>
<section class="section-tight"><div class="container"><div class="grid g4">{pc}</div>
<p class="small muted" style="margin-top:12px">Indicative starting rates; final pricing depends on dates and placement. All sponsored content is clearly labelled. We don't accept gambling-operator ads targeting minors, misleading health claims, or adult content.</p></div></section>
<section class="section-tight"><div class="container"><div class="grid g3">
<div class="card"><h3>🤝 Affiliate & content partners</h3><p class="muted">Readings platforms, report publishers, jewelry and book brands — we integrate relevant offers contextually.</p></div>
<div class="card"><h3>🔌 Tool licensing</h3><p class="muted">Embed our calculators on your site with your branding. White-label options available.</p></div>
<div class="card"><h3>🌐 Domain & website</h3><p class="muted">Interested in acquiring or co-developing 55388.com? <a href="{INTEREST_URL}" target="_blank" rel="noopener">Contact the owner</a>.</p></div>
</div></div></section>
<section id="inquire" class="section-tight"><div class="container" style="max-width:780px"><div class="lead-box">
{form_open("advertising-inquiry", "Advertising / Sponsorship / Partnership inquiry", "Thanks! We'll reply with the media kit and availability.")}
<h2 style="font-size:1.5rem">Tell us about your campaign</h2>
<div class="row"><div class="field"><label for="ad-n">Name</label><input id="ad-n" name="name" required autocomplete="name"></div><div class="field"><label for="ad-e">Work email</label><input id="ad-e" name="email" type="email" required autocomplete="email"></div></div>
<div class="row"><div class="field"><label for="ad-c">Company</label><input id="ad-c" name="company" required></div><div class="field"><label for="ad-w">Website</label><input id="ad-w" name="website" placeholder="example.com"></div></div>
<div class="row"><div class="field"><label for="ad-t">Interest</label><select id="ad-t" name="interest"><option>Advertising</option><option>Sponsorship</option><option>Partnership / affiliate</option><option>Tool licensing</option><option>Domain / website acquisition</option></select></div>
<div class="field"><label for="ad-b">Budget</label><select id="ad-b" name="budget"><option>Under $500</option><option>$500–$2,500</option><option>$2,500–$10,000</option><option>$10,000+</option></select></div></div>
<div class="field"><label for="ad-m">Goals, dates & target markets</label><textarea id="ad-m" name="message" required></textarea></div>
<button class="btn btn-primary btn-block" type="submit">Send Inquiry</button></form></div></div></section>"""
    return path, page(path, "Advertise, Sponsor or Partner with 55388", "Advertising, sponsorship and partnership opportunities on 55388 — sponsored tools, homepage features, newsletter and contest partnerships.", body, schema=[bc_schema])

def contact():
    path = "contact/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("", "Contact")])
    body = f"""<section class="hero"><div class="container">{bc_html}<span class="eyebrow">Contact</span><h1>Let's talk.</h1>
<p class="lead">Questions, corrections, partnerships or press — send us a message and we'll reply as soon as we can.</p></div></section>
<section class="section-tight"><div class="container"><div class="grid g2">
<div class="lead-box">{form_open("contact", "Contact form", "Message sent! We'll get back to you soon.")}
<div class="row"><div class="field"><label for="co-n">Name</label><input id="co-n" name="name" required autocomplete="name"></div><div class="field"><label for="co-e">Email</label><input id="co-e" name="email" type="email" required autocomplete="email"></div></div>
<div class="field"><label for="co-t">Topic</label><select id="co-t" name="topic"><option>General question</option><option>Live reading</option><option>Correction / feedback</option><option>Advertising / sponsorship</option><option>Partnership</option><option>Domain / website acquisition</option><option>Press</option><option>Privacy request</option></select></div>
<div class="field"><label for="co-m">Message</label><textarea id="co-m" name="message" required></textarea></div>
<button class="btn btn-primary btn-block" type="submit">Send Message</button></form></div>
<div class="grid" style="align-content:start">
<div class="card"><h3>Prefer email?</h3><p class="muted">Open a pre-addressed message in your email app.</p><a class="btn btn-ghost" href="#" data-mail="Inquiry from 55388.com">Email us</a></div>
<div class="card"><h3>Buy, sponsor or partner on this domain</h3><p class="muted">Interested in this website, the domain name, sponsorship, advertising or partnership?</p><a class="btn btn-primary" href="{INTEREST_URL}" target="_blank" rel="noopener">Contact the owner ↗</a></div>
<div class="card"><h3>Quick links</h3><ul class="checklist small"><li><a href="{r}advertise/">Advertise & sponsor</a></li><li><a href="{r}careers/">Careers</a></li><li><a href="{r}contests/">Contests</a></li><li><a href="{r}support/">Support / donate</a></li></ul></div>
</div></div></div></section>"""
    return path, page(path, "Contact 55388", "Contact 55388 for questions, readings, partnerships, advertising or press.", body, schema=[bc_schema])

def about():
    path = "about/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("", "About")])
    body = f"""<section class="hero"><div class="container">{bc_html}<span class="eyebrow">About</span><h1>Why a website <span class="grad-text">named after a number</span>?</h1></div></section>
<section class="section-tight"><div class="container prose" style="max-width:820px">
<p>Because numbers are everywhere, and people want to know what they mean. 55388 is an independent publisher of clear, well-structured content on angel numbers, numerology and cultural number symbolism, plus free tools for everyday number tasks.</p>
<h2>Our number</h2><p>5 + 5 + 3 + 8 + 8 = 29 → 11 — a master number associated with insight and illumination. Read in layers it tells a story we like: <strong>change (55) → expression (3) → abundance (88)</strong>.</p>
<h2>Editorial principles</h2><ul><li><strong>Clarity over mystique.</strong> We explain how meanings are derived — digits, patterns, reduction — so you can read numbers yourself.</li><li><strong>Honest framing.</strong> Numerology is a symbolic and cultural system, not science. We say so.</li><li><strong>Culturally informed.</strong> Chinese homophones and other traditions are presented with context.</li><li><strong>Privacy first.</strong> Calculators run in your browser.</li></ul>
<h2>How we're funded</h2><p>Advertising, affiliate partnerships (always disclosed), optional readings and audits, sponsors, and reader support. <a href="{r}support/">Support us</a> · <a href="{r}advertise/">Advertise</a>.</p>
</div></section>{newsletter_band(r)}"""
    return path, page(path, "About 55388 — The Number Universe", "About 55388: an independent publisher of angel number, numerology and lucky number guides and free tools.", body, schema=[bc_schema])

def legal():
    out = []
    today = "September 27, 2026"
    docs = {
      "privacy/": ("Privacy & Cookie Policy", f"""<p><em>Last updated: {today}</em></p>
<h2>What we collect</h2><ul><li><strong>Form submissions</strong> — only the details you type (e.g. name, email, birth date, message) when you submit a form. These are delivered to our inbox via the FormSubmit service.</li><li><strong>Calculator inputs</strong> — processed in your browser and not sent to us unless you submit them in a form.</li><li><strong>Cookies & similar technologies</strong> — used by Google AdSense (advertising) and, if enabled, Google Analytics, only according to your consent choice. We store your consent choice and theme preference in your browser's local storage.</li></ul>
<h2>Advertising</h2><p>Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits. You may opt out of personalized advertising at <a href="https://www.google.com/settings/ads" rel="noopener" target="_blank">Google Ads Settings</a> or <a href="https://www.aboutads.info/choices/" rel="noopener" target="_blank">aboutads.info</a>. Choosing "Essential only" in our banner requests non-personalized ads.</p>
<h2>How we use data</h2><p>To reply to you, deliver requested readings, newsletters and contest administration, and to improve the site. We do not sell personal information.</p>
<h2>Retention</h2><p>Inquiries: up to 24 months. Job applications: up to 12 months. Newsletter: until you unsubscribe.</p>
<h2>Your rights</h2><p>Depending on where you live (e.g. GDPR, UK GDPR, PIPEDA, Quebec Law 25, CCPA/CPRA), you may request access, correction, deletion or portability of your data, or withdraw consent. Use the <a href="../contact/">contact form</a> and choose "Privacy request".</p>
<h2>Children</h2><p>This site is not directed to children under 13 (or 16 in the EEA). Contests are 18+.</p>
<h2>Hosting</h2><p>The site is hosted on GitHub Pages, which may log IP addresses for security. Fonts are loaded from Google Fonts; videos load from YouTube only when you press play.</p>"""),
      "terms/": ("Terms of Use", f"""<p><em>Last updated: {today}</em></p>
<h2>Use of the site</h2><p>You may use 55388 for personal, non-commercial purposes. Do not scrape, republish or frame content at scale without written permission.</p>
<h2>No professional advice</h2><p>All numerology, angel number, lucky number and reading content is for entertainment and self-reflection. It is not medical, psychological, legal, financial, investment or gambling advice. Make important decisions with qualified professionals.</p>
<h2>Tools</h2><p>Tools are provided "as is" without warranty. Lottery and random tools do not affect the odds of any official draw.</p>
<h2>Contests</h2><p>Skill-based; no purchase necessary; 18+; void where prohibited. We may verify eligibility and disqualify fraudulent entries. Entrants keep ownership and grant a non-exclusive, royalty-free licence to display entries with credit. Prizes are non-transferable; substitutions of equal value may be made.</p>
<h2>Donations & pledges</h2><p>Contributions are voluntary, support the operation and growth of the site, and are non-refundable except where required by law. Contributions are not tax-deductible unless explicitly stated on a receipt.</p>
<h2>Third-party links & affiliates</h2><p>We link to third-party services, some as affiliates. We are not responsible for their content, products or policies.</p>
<h2>Limitation of liability</h2><p>To the maximum extent permitted by law, 55388 is not liable for indirect or consequential losses arising from use of the site.</p>
<h2>Changes</h2><p>We may update these terms; continued use means acceptance.</p>"""),
      "disclaimer/": ("Disclaimer, Trademark & Copyright Disclosure", f"""<p><em>Last updated: {today}</em></p>
<h2>Trademark disclosure</h2><ul><li>“55388” is used on this website solely as a number and as the domain name 55388.com. It is used descriptively and is not claimed as a registered trademark by this site.</li><li>55388.com is <strong>not affiliated with, endorsed by, or sponsored by</strong> any postal service or ZIP code area (including ZIP code 55388), any municipality or government body, any lottery operator, or any company, product or brand that uses the same or similar digits.</li><li>All third-party names, trademarks, service marks and logos mentioned (for example Google, YouTube, AdSense, PayPal, Stripe, Ko-fi, Powerball, Mega Millions, Lotto 6/49, Lotto Max, EuroMillions) are the property of their respective owners and are used only for identification and descriptive purposes. Their mention does not imply endorsement.</li></ul>
<h2>Copyright notice</h2><ul><li>© 2026 55388.com. All original text, page designs, graphics, the logo mark and source code on this website are protected by copyright. All rights reserved unless otherwise stated.</li><li>Number meanings are compiled from widely known public traditions (Pythagorean numerology, Chinese homophones); the specific wording, structure and tools on this site are original.</li><li>Embedded YouTube videos remain the copyright of their creators and are shown via YouTube's standard embedded player under YouTube's Terms of Service. We do not host or re-upload third-party videos.</li><li>Brief quotations with attribution and a link are welcome. For other reuse, <a href="../contact/">contact us</a>.</li></ul>
<h2>Copyright complaints (DMCA / notice-and-takedown)</h2><p>If you believe content here infringes your rights, send a notice via the <a href="../contact/">contact form</a> with: identification of the work, the URL of the material, your contact details, a good-faith statement, and a statement of accuracy with your signature. We respond promptly and remove infringing material.</p>
<h2>Entertainment disclaimer</h2><p>Numerology, angel numbers and lucky-number interpretations are symbolic and cultural systems with no proven scientific basis. Content is for entertainment, cultural education and self-reflection.</p>
<h2>Affiliate disclosure</h2><p>Some links are affiliate links. If you click and purchase or sign up, we may earn a commission at no extra cost to you. This helps keep the site free and never changes our editorial opinions.</p>
<h2>Lottery & gambling disclaimer</h2><p>Our lottery tools are unofficial and not affiliated with any lottery. No tool can predict or improve the odds of a draw. Play responsibly and only where legal; if gambling is causing harm, contact a local problem-gambling helpline.</p>
<h2>Advertising disclosure</h2><p>This site displays advertising, including Google AdSense. Sponsored placements are labelled.</p>
<h2>Domain & website inquiries</h2><p>For interest in this website, the domain name, sponsorship, advertisement or partnership, <a href="{INTEREST_URL}" target="_blank" rel="noopener">contact the owner</a>.</p>"""),
    }
    for p, (t, content) in docs.items():
        r = depth_prefix(p)
        bc_html, bc_schema = breadcrumbs(r, [("", t)])
        body = f'<section class="section-tight"><div class="container prose" style="max-width:860px">{bc_html}<h1>{t}</h1>{content}</div></section>'
        out.append((p, page(p, f"{t} | 55388", f"{t} for 55388.com.", body, schema=[bc_schema])))
    return out

def not_found():
    body = """<section class="hero"><div class="container center"><div class="stat" style="font-size:5rem">404</div><h1>This number doesn't exist… yet.</h1>
<p class="lead" style="margin:0 auto 20px">4 + 0 + 4 = 8 — abundance. Let's find what you were looking for.</p>
<form class="hero-search" data-lookup style="max-width:560px;margin:0 auto 20px"><input inputmode="numeric" placeholder="Look up a number"><button class="btn btn-primary">Decode</button></form>
<a class="btn btn-ghost" href="/">Go home</a> <a class="btn btn-ghost" href="/55388-com/">Project home</a></div></section>"""
    return "404.html", page("404.html", "Page not found | 55388", "Page not found.", body, noindex=True)
