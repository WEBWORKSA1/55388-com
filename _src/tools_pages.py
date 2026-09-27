"""Numerology, Chinese luck and tool pages."""
from data import DIGITS, MASTERS, LIFE_PATH, CHINESE, LOTTERIES
from layout import page, ad, breadcrumbs, faq_schema, faq_html, birthday_inline, newsletter_band, e, depth_prefix, form_open
from angel import sidebar

TOOLS = [
  ("life-path-calculator", "Life Path Number Calculator", "Your most important number, from your birth date.", "🧭"),
  ("name-numerology-calculator", "Name Numerology Calculator", "Destiny, Soul Urge & Personality from your name.", "✍️"),
  ("personal-year-calculator", "Personal Year Calculator", "Forecast the theme of your year, month and day.", "📅"),
  ("compatibility-calculator", "Numerology Compatibility", "Compare two Life Path numbers for love or business.", "💞"),
  ("angel-number-finder", "Find My Angel Number", "Your personal angel number from birthday + name.", "✨"),
  ("chinese-lucky-number-checker", "Chinese Lucky Number Checker", "Score any phone, plate or house number 0–100.", "🧧"),
  ("lottery-number-generator", "Lottery Number Generator", "Quick picks for Powerball, Mega Millions, 6/49 & more.", "🎱"),
  ("random-number-generator", "Random Number Generator", "True-random numbers, dice rolls and coin flips.", "🎲"),
  ("number-to-words", "Number to Words Converter", "Spell out numbers — cheque format, currencies, cases.", "🔤"),
]

def tool_shell(slug, title, desc, inner, explain, qas, howto_steps):
    path = f"tools/{slug}/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("tools/", "Tools"), ("", title)])
    schema = [bc_schema, faq_schema(qas),
              {"@context": "https://schema.org", "@type": "WebApplication", "name": title, "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": f"https://55388.com/{path}"},
              {"@context": "https://schema.org", "@type": "HowTo", "name": f"How to use the {title}", "step": [{"@type": "HowToStep", "text": s} for s in howto_steps]}]
    others = "".join(f'<li><a href="{r}tools/{s}/">{t}</a></li>' for s, t, _, _ in TOOLS if s != slug)
    body = f"""<section class="section-tight"><div class="container">{bc_html}
<div class="article"><div>
  <span class="eyebrow">Free tool</span><h1>{title}</h1><p class="lead muted">{desc}</p>
  <div class="tool" data-tool="{slug}">{inner}<div class="out" aria-live="polite"></div></div>
  {ad("inArticle")}
  <div class="prose">{explain}
  <h2>How to use it</h2><ol>{"".join(f"<li>{e(s)}</li>" for s in howto_steps)}</ol>
  <h2>FAQ</h2>{faq_html(qas)}
  <h2>More free tools</h2><ul>{others}</ul></div>
</div>{sidebar(r)}</div></div></section>{newsletter_band(r)}"""
    return path, page(path, f"{title} — Free & Instant | 55388", desc + " Free, private, no sign-up.", body, active="tools/", schema=schema, scripts=("tools.js",))

def dob_fields(p="t"):
    return f'<div class="row"><div><label for="{p}-dob">Birth date</label><input id="{p}-dob" name="dob" type="date" required></div></div>'

def all_tools():
    out = []
    lp_expl = "<h2>What is a Life Path number?</h2><p>Your Life Path number is the single most important number in Pythagorean numerology. It is calculated from your full date of birth and describes your natural strengths, challenges and the kind of work and relationships that fit you best. We reduce the month, day and year separately (the traditional method), then add them and reduce again — keeping the master numbers 11, 22 and 33.</p><table><thead><tr><th>Life Path</th><th>Archetype</th><th>Core trait</th></tr></thead><tbody>" + "".join(f"<tr><td><a href='../../numerology/life-path/{k}/'>{k}</a></td><td>{v[0]}</td><td>{e(v[1])}</td></tr>" for k, v in LIFE_PATH.items()) + "</tbody></table>"
    out.append(tool_shell("life-path-calculator", "Life Path Number Calculator", "Discover your Life Path number and what it says about your purpose, career and relationships.",
        f'<form data-calc>{dob_fields("lp")}<button class="btn btn-primary" type="submit">Reveal My Life Path</button></form>', lp_expl,
        [("How is the Life Path number calculated?", "Reduce your birth month, day and year to single digits (keeping 11, 22 and 33), add them together, and reduce the total again."),
         ("What are master numbers?", "11, 22 and 33 are not reduced further; they carry an intensified version of 2, 4 and 6."),
         ("Is my data stored?", "No. The calculation runs entirely in your browser.")],
        ["Enter your full date of birth.", "Press Reveal My Life Path.", "Read your archetype, then open the full Life Path guide."]))
    out.append(tool_shell("name-numerology-calculator", "Name Numerology Calculator", "Calculate your Destiny (Expression), Soul Urge and Personality numbers from your full birth name.",
        '<form data-calc><div class="field"><label for="nm">Full birth name</label><input id="nm" name="fullname" required placeholder="As on your birth certificate"></div><button class="btn btn-primary" type="submit">Calculate My Chart</button></form>',
        "<h2>The Pythagorean letter chart</h2><p>Each letter maps to a digit: A J S = 1, B K T = 2, C L U = 3, D M V = 4, E N W = 5, F O X = 6, G P Y = 7, H Q Z = 8, I R = 9. Your <strong>Destiny</strong> number uses every letter, your <strong>Soul Urge</strong> uses vowels (A E I O U), and your <strong>Personality</strong> number uses consonants.</p><p>Use your full birth name for your core chart; compare it with your current name to see how a name change shifts your energy — useful for brand and business names too.</p>",
        [("Should I use my birth name or current name?", "Your birth name gives your core chart. Your current or brand name shows the energy you present today."),
         ("Is Y a vowel?", "We treat Y as a consonant for consistency; some numerologists treat it as a vowel when it sounds like one."),
         ("Can I check a business name?", "Yes — type the business name to see its Destiny number, or request a full business number audit.")],
        ["Type your full name.", "Press Calculate My Chart.", "Compare Destiny, Soul Urge and Personality numbers."]))
    out.append(tool_shell("personal-year-calculator", "Personal Year Calculator", "Find the theme of your current personal year, month and day in the 9-year numerology cycle.",
        f'<form data-calc>{dob_fields("py")}<button class="btn btn-primary" type="submit">Show My Forecast</button></form>',
        "<h2>The 9-year cycle</h2><p>Numerology moves in nine-year cycles. Year 1 plants seeds, year 5 brings change, year 8 harvests results and year 9 completes the cycle. Your Personal Year = your birth month + birth day + the current year, reduced to one digit.</p>",
        [("When does a personal year start?", "Most numerologists use January 1; some use your birthday. Our calculator uses the calendar year."),
         ("What is a personal day?", "Personal year + current month + current day, reduced — a quick daily theme.")],
        ["Enter your birth date.", "See your personal year, month and day.", "Plan big moves in years 1, 5 and 8."]))
    out.append(tool_shell("compatibility-calculator", "Numerology Compatibility Calculator", "Compare two birth dates to see how two Life Path numbers work together — in love or in business.",
        '<form data-calc><div class="row"><div><label for="c1">Your birth date</label><input id="c1" name="dob1" type="date" required></div><div><label for="c2">Their birth date</label><input id="c2" name="dob2" type="date" required></div></div><button class="btn btn-primary" type="submit">Check Compatibility</button></form>',
        "<h2>How compatibility works</h2><p>Life Paths fall into three natural families: the thinkers (1, 5, 7), the builders (2, 4, 8) and the creatives (3, 6, 9). Numbers in the same family understand each other easily; cross-family pairs can be powerful but need more conscious effort.</p>",
        [("Does a low score mean we're incompatible?", "No. It shows where effort is needed. Many strong partnerships are cross-family pairs."),
         ("Can I use this for co-founders?", "Yes — the same logic applies to business partnerships.")],
        ["Enter both birth dates.", "Press Check Compatibility.", "Read strengths and friction points."]))
    out.append(tool_shell("angel-number-finder", "Find My Angel Number", "Get your personal angel number from your birthday and name — and what it's trying to tell you.",
        '<form data-calc><div class="row"><div><label for="af-n">First name</label><input id="af-n" name="fullname" required></div><div><label for="af-d">Birth date</label><input id="af-d" name="dob" type="date" required></div></div><button class="btn btn-primary" type="submit">Find My Angel Number Now</button></form>',
        "<h2>How we find your personal angel number</h2><p>Your personal angel number combines your Life Path (your purpose) with your Destiny number (your talents) into a repeating sequence — for example Life Path 3 and Destiny 7 become <strong>337</strong>. It's the number to watch for as a sign you're aligned.</p>",
        [("Is this the same as the numbers I keep seeing?", "Not necessarily — numbers you see repeatedly are situational messages. Your personal angel number is a lifelong signature.")],
        ["Type your first name and birth date.", "Press Find My Angel Number Now.", "Open the full meaning page."]))
    out.append(tool_shell("chinese-lucky-number-checker", "Chinese Lucky Number Checker", "Score any phone number, licence plate, house number or price from 1–100 using traditional Chinese homophones.",
        '<form data-calc><div class="field"><label for="cn">Number to check</label><input id="cn" name="n" inputmode="numeric" required placeholder="e.g. 168 8888 or your phone number"></div><button class="btn btn-primary" type="submit">Check My Number\'s Luck</button></form>',
        "<h2>Why numbers matter in Chinese culture</h2><p>In Mandarin and Cantonese many digits sound like other words. 8 (bā) sounds like 发 fā — to prosper — so it's the luckiest digit; 4 (sì) sounds like 死 sǐ — death — so it's avoided. That's why phone numbers and licence plates full of 8s sell for real money, and many buildings skip the 4th floor.</p><p>Our score averages each digit's traditional value, then adds bonuses for famous lucky combinations (168, 518, 888, 1314) and penalties for unlucky ones (14, 74, 250).</p><p><a href='../../chinese-lucky-numbers/'>Full guide to Chinese lucky numbers →</a></p>",
        [("What is the luckiest Chinese number?", "8, and combinations like 88, 888, 168 and 518."),
         ("Why is 4 unlucky?", "Because 四 sì sounds like 死 sǐ, 'death'."),
         ("Does this apply to Cantonese too?", "Mostly yes — the 8 and 4 associations are shared, with some regional differences.")],
        ["Type any number.", "Press Check.", "Read the digit-by-digit reading, score and lucky combinations."]))
    lot_opts = "".join(f'<option value="{k}">{n}</option>' for k, n, *_ in LOTTERIES)
    out.append(tool_shell("lottery-number-generator", "Lottery Number Generator", "Instant cryptographically-random quick picks for Powerball, Mega Millions, Lotto 6/49, Lotto Max, EuroMillions and more.",
        f'<form data-calc><div class="row"><div><label for="lg">Game</label><select id="lg" name="game">{lot_opts}</select></div><div><label for="lq">Lines</label><select id="lq" name="lines"><option>1</option><option selected>3</option><option>5</option><option>10</option></select></div><div><label for="ll">Include my lucky number (optional)</label><input id="ll" name="lucky" inputmode="numeric" placeholder="e.g. 8"></div></div><button class="btn btn-primary" type="submit">Generate My Numbers</button></form>',
        "<h2>How it works</h2><p>Numbers are drawn with your browser's cryptographically secure random generator (Web Crypto), without repeats, and sorted. No pattern or 'lucky' method can change the odds of an official draw — every combination is equally likely.</p><blockquote><strong>Unofficial tool.</strong> 55388 is not affiliated with any lottery operator. Always confirm current game rules and number ranges with the official lottery. Play responsibly — 18+/19+ where applicable. If gambling stops being fun, contact a local problem-gambling helpline.</blockquote>",
        [("Can a generator improve my odds?", "No. Each official draw is random; all combinations have equal probability."),
         ("Are ranges up to date?", "They reflect the rules as of 2026. Games occasionally change, so confirm on the official site.")],
        ["Choose a game and number of lines.", "Optionally add your lucky number.", "Press Generate and copy your picks."]))
    out.append(tool_shell("random-number-generator", "Random Number Generator", "Generate true-random numbers in any range, roll dice or flip a coin — instantly.",
        '<form data-calc><div class="row"><div><label for="rmin">Min</label><input id="rmin" name="min" type="number" value="1"></div><div><label for="rmax">Max</label><input id="rmax" name="max" type="number" value="100"></div><div><label for="rc">How many</label><input id="rc" name="count" type="number" value="1" min="1" max="500"></div><div><label for="ru">Unique?</label><select id="ru" name="unique"><option value="1">No repeats</option><option value="0">Allow repeats</option></select></div></div><div style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn btn-primary" type="submit">Generate</button><button class="btn btn-ghost" type="button" data-dice>Roll 2 Dice</button><button class="btn btn-ghost" type="button" data-coin>Flip a Coin</button></div></form>',
        "<h2>Random you can trust</h2><p>We use the Web Crypto API (<code>crypto.getRandomValues</code>), the same source browsers use for security keys, rather than the predictable <code>Math.random</code>. Perfect for giveaways, classroom picks, raffles and games.</p><p>Running a giveaway? <a href='../../contests/'>See how our contests pick winners</a>.</p>",
        [("Is it truly random?", "It uses a cryptographically secure pseudo-random generator seeded by your device's entropy — suitable for everyday draws and giveaways."),
         ("What's the maximum range?", "Any whole numbers between about ±9 quadrillion; up to 500 numbers at once.")],
        ["Set min, max and quantity.", "Choose unique or repeats.", "Press Generate (or roll dice / flip a coin)."]))
    out.append(tool_shell("number-to-words", "Number to Words Converter", "Spell out any number in English words — including cheque-writing format with currencies and letter-case options.",
        '<form data-calc><div class="field"><label for="nw">Number</label><input id="nw" name="n" required inputmode="decimal" placeholder="e.g. 55388 or 1250.75"></div><div class="row"><div><label for="nwm">Format</label><select id="nwm" name="mode"><option value="words">Words</option><option value="cheque">Cheque / check</option></select></div><div><label for="nwc">Currency</label><select id="nwc" name="cur"><option>dollars</option><option>euros</option><option>pounds</option><option>rupees</option><option>yuan</option></select></div><div><label for="nwk">Case</label><select id="nwk" name="case"><option value="sentence">Sentence case</option><option value="lower">lower case</option><option value="upper">UPPER CASE</option><option value="title">Title Case</option></select></div><div><label for="nwu">Style</label><select id="nwu" name="style"><option value="us">US (no "and")</option><option value="uk">UK ("and")</option></select></div></div><button class="btn btn-primary" type="submit">Convert</button></form>',
        "<h2>Writing numbers on cheques</h2><p>On a cheque, write the whole amount in words followed by the cents as a fraction over 100 — for example <em>One thousand two hundred fifty dollars and 75/100</em>. Draw a line through any unused space to prevent alterations.</p>",
        [("How do I write 55388 in words?", "Fifty-five thousand three hundred eighty-eight."),
         ("Does it support decimals?", "Yes — as 'point' digits in word mode or as a /100 fraction in cheque mode.")],
        ["Type the number.", "Choose words or cheque format, currency and case.", "Press Convert and copy."]))
    return out

def tools_index():
    path = "tools/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("", "Tools")])
    cards = "".join(f'<a class="card card-link" href="{r}tools/{s}/"><div style="font-size:2rem">{ic}</div><h3>{t}</h3><p class="muted small">{d}</p></a>' for s, t, d, ic in TOOLS)
    body = f"""<section class="hero"><div class="container">{bc_html}<span class="eyebrow">Free number tools</span><h1>Number tools that just <span class="grad-text">work</span>.</h1>
<p class="lead">Numerology calculators, lucky-number checkers, lottery quick picks and everyday utilities. Private (everything runs in your browser), free, no sign-up.</p></div></section>
<section class="section-tight"><div class="container"><div class="grid g3">{cards}</div>{ad("footer")}</div></section>{newsletter_band(r)}"""
    return path, page(path, "Free Number Tools: Numerology, Lucky Numbers, Lottery & More | 55388", "Free numerology calculators, Chinese lucky number checker, lottery generator, random numbers and number-to-words — instant and private.", body, active="tools/", schema=[bc_schema])

def numerology_pages():
    out = []
    path = "numerology/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("", "Numerology")])
    lp_cards = "".join(f'<a class="card card-link" href="{r}numerology/life-path/{k}/"><div class="stat">{k}</div><h3>{v[0]}</h3><p class="muted small">{e(v[1])}</p></a>' for k, v in LIFE_PATH.items())
    body = f"""<section class="hero"><div class="container">{bc_html}<span class="eyebrow">Numerology</span>
<h1>Numerology, made <span class="grad-text">practical</span>.</h1><p class="lead">Numerology assigns meaning to numbers derived from your birth date and name. Use it as a lens for self-reflection, timing and decision-making — with clear, no-fluff explanations.</p>
<div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-primary" href="{r}tools/life-path-calculator/">Calculate My Life Path</a><a class="btn btn-ghost" href="{r}tools/name-numerology-calculator/">Name Calculator</a></div></div></section>
<section class="section-tight"><div class="container"><div class="section-head"><h2>The 12 Life Path numbers</h2><p class="muted">Nine core paths plus three master numbers.</p></div><div class="grid g4">{lp_cards}</div></div></section>
<section class="section-tight"><div class="container prose" style="max-width:820px">{ad("inArticle")}
<h2>The five core numbers in your chart</h2>
<table><thead><tr><th>Number</th><th>From</th><th>Reveals</th></tr></thead><tbody>
<tr><td>Life Path</td><td>Full birth date</td><td>Your purpose and natural path</td></tr>
<tr><td>Destiny / Expression</td><td>All letters of birth name</td><td>Talents and how you express them</td></tr>
<tr><td>Soul Urge</td><td>Vowels of birth name</td><td>Inner desires and motivation</td></tr>
<tr><td>Personality</td><td>Consonants of birth name</td><td>How others see you</td></tr>
<tr><td>Birthday</td><td>Day of birth</td><td>A special gift you carry</td></tr></tbody></table>
<h2>Pythagorean vs. Chaldean numerology</h2><p>Pythagorean numerology (used on this site) maps letters to 1–9 in sequence and is the most widely used system in the West. Chaldean numerology is older, maps letters by sound vibration to 1–8, and treats 9 as sacred. Results differ, so always compare like with like.</p>
{birthday_inline(r)}</div></section>{newsletter_band(r)}"""
    out.append((path, page(path, "Numerology: Life Path, Destiny & Soul Urge Numbers Explained | 55388", "Clear, practical numerology: the 12 Life Path numbers, name numbers, master numbers and free calculators.", body, active="numerology/", schema=[bc_schema])))
    for k, (arch, trait, chal, careers) in LIFE_PATH.items():
        p = f"numerology/life-path/{k}/"; r = depth_prefix(p)
        info = DIGITS[str(k)] if k <= 9 else MASTERS[k]
        base = DIGITS[str(k if k <= 9 else {11: 2, 22: 4, 33: 6}[k])]
        bc_html, bc_schema = breadcrumbs(r, [("numerology/", "Numerology"), ("", f"Life Path {k}")])
        comp = {1: "3, 5, 7", 2: "4, 6, 8", 3: "1, 5, 9", 4: "2, 6, 8", 5: "1, 3, 7", 6: "2, 4, 9", 7: "1, 5, 4", 8: "2, 4, 6", 9: "3, 6, 1", 11: "2, 4, 6, 22", 22: "4, 8, 11", 33: "6, 9, 3"}[k]
        qas = [(f"What does Life Path {k} mean?", f"Life Path {k} is {arch}: {trait}"),
               (f"What is the biggest challenge for Life Path {k}?", chal),
               (f"Best careers for Life Path {k}?", careers),
               (f"Who is Life Path {k} compatible with?", f"Typically most at ease with Life Paths {comp}.")]
        body = f"""<section class="section-tight"><div class="container">{bc_html}<div class="article"><article class="prose">
<span class="eyebrow">Life Path number</span><h1>Life Path {k}: {arch}</h1><p class="lead" style="font-size:1.15rem">{e(trait)} {e(info['core'])}</p>
<div class="keyfacts"><div><b>Archetype</b><span>{arch}</span></div><div><b>Keywords</b><span>{', '.join(info['kw'][:3])}</span></div><div><b>Best matches</b><span>{comp}</span></div></div>
{ad("header")}
<h2>Strengths</h2><p>{e(trait)} {base['core']}</p>
<h2>Challenges</h2><p>{e(chal)} Awareness is the fix: notice the pattern and choose the opposite on purpose.</p>
<h2>Love & relationships</h2><p>{base['love']}</p>
<h2>Career & money</h2><p><strong>Ideal fields:</strong> {careers} {base['career']} {base['money']}</p>
{birthday_inline(r)}
<h2>Your life path in action</h2><p>{base['action']}</p>
{ad("inArticle")}
<h2>FAQ</h2>{faq_html(qas)}
<p><a class="btn btn-ghost" href="{r}tools/compatibility-calculator/">Check compatibility with someone →</a></p>
</article>{sidebar(r)}</div></div></section>{newsletter_band(r)}"""
        out.append((p, page(p, f"Life Path Number {k} Meaning: {arch} — Love, Career & Compatibility | 55388", f"Life Path {k} ({arch}) meaning: strengths, challenges, love, careers and best matches. Free calculator.", body, active="numerology/", schema=[bc_schema, faq_schema(qas)], og_type="article")))
    return out

def chinese_page():
    path = "chinese-lucky-numbers/"; r = depth_prefix(path)
    bc_html, bc_schema = breadcrumbs(r, [("", "Chinese Lucky Numbers")])
    rows = "".join(f"<tr><td><strong>{d}</strong></td><td>{v['hanzi']}</td><td>{v['pinyin']}</td><td>{e(v['sounds'])}</td><td>{v['score']}/100</td><td>{e(v['note'])}</td></tr>" for d, v in CHINESE["digits"].items())
    combos = "".join(f"<tr><td><strong>{c['n']}</strong></td><td>{e(c['meaning'])}</td><td>{'Lucky' if c['bonus'] > 0 else 'Avoided'}</td></tr>" for c in CHINESE["combos"])
    qas = [("What is the luckiest number in Chinese culture?", "8 — because 八 bā sounds like 发 fā, 'to prosper'. 88, 888, 168 and 518 are all prized."),
           ("What number is unlucky in China?", "4, because 四 sì sounds like 死 sǐ, 'death'. 14 and 74 are also avoided."),
           ("What does 520 mean?", "520 sounds like 'wǒ ài nǐ' — 'I love you'. May 20 is celebrated as a romantic day."),
           ("What does 55388 mean in Chinese?", "Read playfully: 五五 (the five elements, doubled balance), 三 (sān, sounding like 生 shēng — life, growth) and 八八 (fā fā — double prosperity): balance → growth → double fortune.")]
    body = f"""<section class="hero"><div class="container">{bc_html}<span class="eyebrow">Chinese number symbolism</span>
<h1>Chinese lucky numbers: why <span class="grad-text">8</span> is gold and 4 is avoided</h1>
<p class="lead">In Chinese, numbers are chosen for how they sound. Here's every digit, the famous combinations, and a free checker for any phone, plate or house number.</p>
<a class="btn btn-primary" href="{r}tools/chinese-lucky-number-checker/">Check My Number's Luck</a></div></section>
<section class="section-tight"><div class="container prose" style="max-width:960px">{bc_html if False else ""}
<h2>Digits 0–9</h2><table><thead><tr><th>Digit</th><th>Hanzi</th><th>Pinyin</th><th>Sounds like</th><th>Luck</th><th>Notes</th></tr></thead><tbody>{rows}</tbody></table>
{ad("inArticle")}
<h2>Famous lucky and unlucky combinations</h2><table><thead><tr><th>Number</th><th>Meaning</th><th>Status</th></tr></thead><tbody>{combos}</tbody></table>
<h2>Where it matters</h2><ul><li><strong>Phone numbers & licence plates:</strong> numbers heavy in 8 and 6 command premium prices at auctions.</li><li><strong>Addresses & floors:</strong> many buildings skip 4, 14 and 24.</li><li><strong>Prices:</strong> retailers use endings like 8 and 88 to signal good fortune.</li><li><strong>Dates:</strong> weddings and launches favour dates with 6, 8 and 9 — the Beijing Olympics opened 8/8/2008 at 8:08 pm.</li></ul>
<h2>FAQ</h2>{faq_html(qas)}
<p class="small muted">Sound-based associations vary between Mandarin, Cantonese and regional dialects. Presented for cultural interest and entertainment.</p>
<div class="grid g2" style="margin-top:28px"><a class="card card-link" href="{r}angel-numbers/88/"><h3>88 meaning →</h3><p class="muted small">Double prosperity & double happiness.</p></a><a class="card card-link" href="{r}angel-numbers/168/"><h3>168 meaning →</h3><p class="muted small">Prosperity all the way.</p></a></div>
</div></section>{newsletter_band(r)}"""
    return path, page(path, "Chinese Lucky Numbers: Meanings of 8, 6, 9, 4, 168, 520 & 1314 | 55388", "Chinese lucky and unlucky numbers explained — digits 0–9, famous combinations, and a free lucky number checker.", body, active="chinese-lucky-numbers/", schema=[bc_schema, faq_schema(qas)])

COMP = {1: "3, 5, 7", 2: "4, 6, 8", 3: "1, 5, 9", 4: "2, 6, 8", 5: "1, 3, 7", 6: "2, 4, 9", 7: "1, 5, 4", 8: "2, 4, 6", 9: "3, 6, 1", 11: "2, 4, 6, 22", 22: "4, 8, 11", 33: "6, 9, 3"}

def lifepath_data():
    out = {}
    for k, (arch, trait, chal, careers) in LIFE_PATH.items():
        info = DIGITS[str(k)] if k <= 9 else MASTERS[k]
        out[str(k)] = dict(arch=arch, trait=trait, chal=chal, careers=careers, core=info["core"], kw=", ".join(info["kw"][:3]),
                           comp=COMP[k], base=str(k if k <= 9 else {11: 2, 22: 4, 33: 6}[k]))
    return out

def lifepath_front(k):
    import json
    arch = LIFE_PATH[k][0]
    t = f"Life Path Number {k} Meaning: {arch} — Love, Career & Compatibility | 55388"
    d = f"Life Path {k} ({arch}) meaning: strengths, challenges, love, careers and best matches. Free calculator."
    return f"---\nlayout: lifepath\nlp: \"{k}\"\ntitle: {json.dumps(t, ensure_ascii=False)}\ndescription: {json.dumps(d, ensure_ascii=False)}\nactive: \"numerology/\"\nog_type: article\n---\n"
