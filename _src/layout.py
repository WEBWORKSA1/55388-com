"""Shared layout for every page of 55388.com."""
import json, html

SITE = "https://55388.com"
NAME = "55388"
TAGLINE = "The Number Universe"
INTEREST_URL = "https://web.works/contact"

NAV = [
  ("angel-numbers/", "Angel Numbers"),
  ("numerology/", "Numerology"),
  ("chinese-lucky-numbers/", "Chinese Luck"),
  ("tools/", "Tools"),
  ("videos/", "Videos"),
  ("contests/", "Contests"),
  ("support/", "Support"),
]

LOGO = """<svg class="logo" viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f5c451"/><stop offset=".5" stop-color="#ff9f6e"/><stop offset="1" stop-color="#8b7bff"/></linearGradient></defs><circle cx="32" cy="32" r="30" fill="none" stroke="url(#lg)" stroke-width="4"/><path d="M20 22a8 8 0 1 1 0 .1M20 38a8 8 0 1 0 0 .1M44 22a8 8 0 1 1 0 .1M44 38a8 8 0 1 0 0 .1" fill="none" stroke="url(#lg)" stroke-width="4" stroke-linecap="round"/></svg>"""

e = html.escape

MODE = {"jekyll": False}
BASE = "{{ site.baseurl }}/"

def depth_prefix(path):
    if MODE["jekyll"]:
        return BASE
    p = path.strip("/")
    if not p or p.endswith(".html"):
        return "" if "/" not in p else "../" * p.count("/")
    return "../" * (p.count("/") + 1)

def ad(slot="inArticle", tall=False):
    return f'<div class="ad-slot{" tall" if tall else ""}" data-slot="{slot}" aria-label="Advertisement">Advertisement</div>'

def page(path, title, desc, body, active="", schema=None, scripts=(), og_type="website", noindex=False):
    r = depth_prefix(path)
    url = SITE + "/" + (path if path != "index.html" else "")
    cur = ' aria-current="page"'
    nav = "".join(
        f'<li><a href="{r}{href}"{cur if active == href else ""}>{label}</a></li>' for href, label in NAV)
    ld = [{
        "@context": "https://schema.org", "@type": "WebSite", "name": NAME, "alternateName": f"{NAME} — {TAGLINE}", "url": SITE + "/",
        "potentialAction": {"@type": "SearchAction", "target": SITE + "/angel-numbers/lookup/?n={search_term_string}", "query-input": "required name=search_term_string"}}]
    if schema:
        ld += schema if isinstance(schema, list) else [schema]
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in ld)
    if MODE["jekyll"]:
        fm = ["---", "layout: default", "title: " + json.dumps(title, ensure_ascii=False), "description: " + json.dumps(desc, ensure_ascii=False)]
        if active: fm.append("active: " + json.dumps(active))
        if scripts: fm.append("scripts: " + json.dumps(list(scripts)))
        if og_type != "website": fm.append("og_type: " + og_type)
        if noindex: fm.append("noindex: true")
        fm.append("---")
        return "\n".join(fm) + "\n" + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld[1:]) + "\n" + body + "\n"
    extra = "".join(f'<script src="{r}assets/js/{s}" defer></script>' for s in scripts)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{'<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'}
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.svg"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0d1a">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{r}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
{ld_html}
</head>
<body data-root="{r}">
<a class="skip" href="#main">Skip to content</a>
<div class="topbar" role="note"><a href="{INTEREST_URL}" target="_blank" rel="noopener">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership</a></div>
<header class="site-header">
  <nav class="container nav" aria-label="Main">
    <a class="brand" href="{r}index.html" aria-label="{NAME} home">{LOGO}<span>{NAME}<small>{TAGLINE}</small></span></a>
    <button class="icon-btn menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="menu">☰</button>
    <ul class="menu" id="menu">{nav}
      <li><a class="cta" href="{r}reading/">Free Reading</a></li>
      <li><button class="icon-btn" data-theme-toggle aria-label="Toggle light/dark theme">◐</button></li>
    </ul>
  </nav>
</header>
<main id="main">
{body}
</main>
{footer(r)}
<div class="sticky-cta" role="complementary"><span>✦ Discover your personal numbers — free, in 30 seconds.</span><a class="btn btn-primary" href="{r}reading/">Get My Free Reading</a><button class="x" aria-label="Dismiss">×</button></div>
<div class="modal" id="exit-modal" role="dialog" aria-modal="true" aria-labelledby="exit-title"><div class="box lead-box">
  <button class="close" data-close aria-label="Close">×</button>
  <span class="eyebrow">Before you go</span>
  <h2 id="exit-title">Get your Daily Number — free</h2>
  <p class="muted">One short email each morning: today's universal number, its meaning, and one action to take. Join free, unsubscribe anytime.</p>
  <form data-form="newsletter" data-subject="Newsletter signup (exit intent)" data-success="You're in! Watch your inbox for your first Daily Number.">
    <input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
    <div class="field"><label for="ex-name">First name</label><input id="ex-name" name="name" required autocomplete="given-name"></div>
    <div class="field"><label for="ex-email">Email</label><input id="ex-email" name="email" type="email" required autocomplete="email"></div>
    <button class="btn btn-primary btn-block" type="submit">Send Me My Daily Number</button>
    <p class="small muted center" style="margin-top:8px">🔒 Never sold. Never shared. 100% free.</p>
  </form>
</div></div>
<div class="consent" role="dialog" aria-label="Cookie consent">
  <strong>Cookies & ads</strong>
  <p class="small muted" style="margin:6px 0 0">We use cookies to run ads (Google AdSense) and measure traffic so {NAME} stays free. Choose how we may use them. See our <a href="{r}privacy/">Privacy Policy</a>.</p>
  <div class="actions"><button class="btn btn-primary" data-consent="all">Accept all</button><button class="btn btn-ghost" data-consent="essential">Essential only</button></div>
</div>
<script src="{r}assets/js/config.js" defer></script>
<script src="{r}assets/js/data.js" defer></script>
<script src="{r}assets/js/engine.js" defer></script>
<script src="{r}assets/js/main.js" defer></script>
{extra}
</body>
</html>
"""

def footer(r):
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{r}index.html">{LOGO}<span>{NAME}<small>{TAGLINE}</small></span></a>
        <p class="muted" style="margin-top:12px">Angel numbers, numerology, lucky numbers and free number tools — decoded clearly, for curious minds everywhere.</p>
        <button class="btn btn-ghost" data-share="Explore what your numbers mean on 55388">Share {NAME} ↗</button>
      </div>
      <div><h4>Explore</h4><ul>
        <li><a href="{r}angel-numbers/">Angel Numbers</a></li><li><a href="{r}numerology/">Numerology</a></li>
        <li><a href="{r}chinese-lucky-numbers/">Chinese Lucky Numbers</a></li><li><a href="{r}guides/">Guides</a></li><li><a href="{r}videos/">Videos</a></li></ul></div>
      <div><h4>Free Tools</h4><ul>
        <li><a href="{r}tools/life-path-calculator/">Life Path Calculator</a></li><li><a href="{r}tools/name-numerology-calculator/">Name Numerology</a></li>
        <li><a href="{r}tools/lottery-number-generator/">Lottery Number Generator</a></li><li><a href="{r}tools/number-to-words/">Number to Words</a></li><li><a href="{r}tools/">All tools →</a></li></ul></div>
      <div><h4>Get Involved</h4><ul>
        <li><a href="{r}reading/">Free Number Reading</a></li><li><a href="{r}business-lucky-number-audit/">Business Number Audit</a></li>
        <li><a href="{r}advertise/">Advertise & Sponsor</a></li><li><a href="{r}contests/">Contests & Prizes</a></li>
        <li><a href="{r}careers/">Careers & Talent</a></li><li><a href="{r}support/">Support Us / Donate</a></li></ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="{r}about/">About</a></li><li><a href="{r}contact/">Contact</a></li><li><a href="{INTEREST_URL}" target="_blank" rel="noopener">Buy / Partner on this domain</a></li>
        <li><a href="{r}privacy/">Privacy & Cookies</a></li><li><a href="{r}terms/">Terms of Use</a></li><li><a href="{r}disclaimer/">Disclaimer & Trademark</a></li></ul></div>
    </div>
    <div class="legal-note">
      <p>© <span data-year>2026</span> 55388.com. All original content and design are protected by copyright. “55388” is used here only as a number and domain name; it is not a registered trademark of this site, and the site is not affiliated with any postal service, municipality, lottery operator, or company that uses the same digits. Third-party names, logos and videos belong to their respective owners. Numerology and angel-number content is for entertainment and self-reflection only — not financial, medical, legal or psychological advice. Some links may be affiliate links. <a href="{r}disclaimer/">Full disclosure</a>.</p>
    </div>
  </div>
</footer>"""

def breadcrumbs(r, items):
    parts = [f'<a href="{r}index.html">Home</a>']
    schema_items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    for i, (href, label) in enumerate(items, start=2):
        parts.append(f'<a href="{r}{href}">{e(label)}</a>' if href else f"<span>{e(label)}</span>")
        schema_items.append({"@type": "ListItem", "position": i, "name": label, **({"item": SITE + "/" + href} if href else {})})
    return '<nav class="breadcrumbs" aria-label="Breadcrumb">' + " › ".join(parts) + "</nav>", {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": schema_items}

def faq_schema(qas):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]}

def faq_html(qas):
    return '<div class="faq">' + "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in qas) + "</div>"

def form_open(name, subject, success=None, custom=False, cls=""):
    s = f' data-success="{e(success)}"' if success else ""
    c = " data-custom" if custom else ""
    return f'<form data-form="{name}" data-subject="{e(subject)}"{s}{c} class="{cls}"><input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'

def newsletter_band(r):
    if MODE["jekyll"] and not MODE.get("raw"):
        return "{% include newsletter.html %}"
    return _newsletter_band(r)

def _newsletter_band(r):
    return f"""<section class="section-tight"><div class="container"><div class="band">
  <div class="grid g2" style="align-items:center">
    <div><h2>Your Daily Number, delivered.</h2><p style="margin:0">Today's universal number, what it means for love, work and money, plus one action — in a 60-second morning email.</p></div>
    <div>{form_open("newsletter", "Newsletter signup", "You're in! Your first Daily Number arrives soon.")}
      <label class="sr-only" for="nl-email">Email</label><input id="nl-email" type="email" name="email" placeholder="you@email.com" required autocomplete="email">
      <button class="btn" type="submit">Join Free</button></form>
      <p class="small" style="margin:8px 0 0">100% free · Unsubscribe anytime · Never sold</p></div>
  </div></div></div></section>"""

def birthday_inline(r, context=""):
    if MODE["jekyll"] and not MODE.get("raw"):
        return f'{{% include birthday-num.html ctx="{context}" %}}' if context else "{% include birthday.html %}"
    return _birthday_inline(r, context)

def _birthday_inline(r, context=""):
    return f"""<div class="lead-box" style="margin:28px 0">
  <span class="badge">Free personal reading</span>
  <h3 style="margin-top:10px">{('What does ' + e(context) + ' mean for <em>you</em> specifically?') if context else 'What do your numbers say about <em>you</em>?'}</h3>
  <p class="muted">Enter your birthday and name — we'll calculate your Life Path, Destiny and Soul Urge numbers instantly and show how they interact{(' with ' + e(context)) if context else ''}.</p>
  <form action="{r}reading/" method="get" class="row">
    <div><label for="bi-name-{e(context)}">First name</label><input id="bi-name-{e(context)}" name="fullname" required autocomplete="given-name"></div>
    <div><label for="bi-dob-{e(context)}">Birthday</label><input id="bi-dob-{e(context)}" name="dob" type="date" required></div>
    <div style="align-self:end"><button class="btn btn-primary btn-block" type="submit">Reveal My Numbers →</button></div>
  </form>
</div>"""

def jekyll_layout():
    """_layouts/default.html — same chrome as page(), driven by Liquid."""
    r = BASE
    cur = '{% if page.active == "ACT" %} aria-current="page"{% endif %}'
    nav = "".join(f'<li><a href="{r}{href}"{cur.replace("ACT", href)}>{label}</a></li>' for href, label in NAV)
    website = json.dumps({"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "alternateName": f"{NAME} — {TAGLINE}", "url": SITE + "/",
        "potentialAction": {"@type": "SearchAction", "target": SITE + "/angel-numbers/lookup/?n={search_term_string}", "query-input": "required name=search_term_string"}}, ensure_ascii=False)
    MODE["jekyll"] = False
    shell = page("x/", "TITLE", "DESC", "BODY", active="", schema=None, scripts=())
    MODE["jekyll"] = True
    head_end = shell.index("<link rel=\"icon\"")
    # rebuild the head with Liquid variables, keep the rest of the chrome verbatim with BASE prefixes
    head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{{{ page.title | escape }}}}</title>
<meta name="description" content="{{{{ page.description | escape }}}}">
{{% if page.noindex %}}<meta name="robots" content="noindex">{{% else %}}<meta name="robots" content="index,follow,max-image-preview:large">{{% endif %}}
<link rel="canonical" href="{SITE}{{{{ page.url | replace: 'index.html', '' }}}}">
<meta property="og:type" content="{{{{ page.og_type | default: 'website' }}}}"><meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{{{{ page.title | escape }}}}"><meta property="og:description" content="{{{{ page.description | escape }}}}"><meta property="og:url" content="{SITE}{{{{ page.url | replace: 'index.html', '' }}}}">
<meta property="og:image" content="{SITE}/assets/img/og.svg"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0d1a">
"""
    rest = shell[head_end:]
    rest = rest.replace('href="../', 'href="' + r).replace('src="../', 'src="' + r).replace('data-root="../"', 'data-root="' + r + '"')
    rest = rest.replace('<script type="application/ld+json">', '<script type="application/ld+json">' + website + '</script>\n<script type="application/ld+json">', 0)
    # swap nav, body, extra scripts
    import re
    rest = re.sub(r'<ul class="menu" id="menu">.*?<li><a class="cta"', '<ul class="menu" id="menu">' + nav + '\n      <li><a class="cta"', rest, flags=re.S)
    rest = rest.replace("BODY", "{{ content }}")
    rest = rest.replace("</body>", '{% for s in page.scripts %}<script src="' + r + 'assets/js/{{ s }}" defer></script>{% endfor %}\n</body>')
    # JSON-LD WebSite block in head
    rest = re.sub(r'<script type="application/ld\+json">.*?</script>\n</head>', '<script type="application/ld+json">' + website + '</script>\n</head>', rest, flags=re.S)
    return head + rest
