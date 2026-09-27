# 55388.com — Concept & Phase-wise Build Prompt

## 1. The winning concept

**55388.com → "55388 — The Number Universe": angel numbers + numerology + Chinese lucky numbers + free number tools.**

### Why this idea (numbers, not vibes)

| Option considered | Verdict | Reason |
|---|---|---|
| Hyperlocal site for ZIP 55388 (Watertown, MN) | ✗ | ~6,000 residents; hard traffic ceiling; low RPM |
| Generic numeric-domain "brandable" | ✗ | No search demand, no story |
| **Number-meaning + number-tools hub** | ✓ | Exact-match brand fit (the domain *is* a number); massive evergreen search demand; several revenue layers |

**Demand signals** (US monthly Google searches reported by ProWritingAid / Journal-Courier):

| Query | Searches/mo |
|---|---|
| angel number 444 | 163,000 |
| angel number 222 | 118,000 |
| angel number 333 | 112,000 |
| angel number 111 | 64,000 |
| angel number 1111 | 55,000 |

On top of that, 67–84% of the volume for each number comes from outside the US. Tool queries (random number, lottery quick pick, number to words) add evergreen utility traffic that isn't tied to any trend.

**The domain's built-in story:** 5 + 5 + 3 + 8 + 8 = 29 → **11**, a master number. Read in layers:

- 55 = change
- 3 = expression
- 88 = double prosperity, which is also 发发 ("double fortune") in Chinese

**Revenue stack (highest value first):**

1. **Psychic-reading affiliates.** Keen pays ~$100 per new customer, Kasamba $125–150, Psychic Source $100.
2. **Paid reports.** The market prices them at $17 / $37 / $57, or $19.95 per report. The ClickBank numerology offers average $10–45 per sale.
3. **B2B "Business Lucky Number Audit".** Covers brand name, phone, address and launch date, sold as custom quotes.
4. **Google AdSense.** This is the base layer, at an estimated $3–8 per 1,000 pageviews. Move to Mediavine or Raptive once traffic qualifies, for an estimated $10–20+.
5. **Sponsorships.** Sponsored tools, a homepage feature, newsletter sponsors and a contest partner.
6. **YouTube.** An embedded library now; your own channel later, cross-linked to the matching pages.
7. **Donations and pledges.** These pay for operations, hires, promotion, contests and prizes.

## 2. Research: 44 sites audited

Numerology & angel numbers:
- numerology.com
- numerologist.com (free reading, readings, angel index, calculator, partners)
- Sacred Scribes (blogspot)
- affinitynumerology.com
- worldnumerology.com
- seventhlifepath.com
- numerologysign.com
- angelnumber.org
- individualogist.com
- thelawofattraction.com
- thecoolist.com
- checkangelnumbers.com
- symbolsage.com
- askastrology.com
- astro-seek.com
- gotohoroscope.com

Magazines:
- mindbodygreen.com
- today.com
- refinery29.com
- almanac.com
- astrology.com

Astrology & psychic platforms:
- cafeastrology.com
- horoscope.com
- astrostyle.com
- costarastrology.com
- tarot.com
- labyrinthos.co
- keen.com
- kasamba.com
- californiapsychics.com
- psychicsource.com

Number tools:
- random.org
- calculator.net
- omnicalculator.com
- calculatorsoup.com
- timeanddate.com
- lottery.net
- lotteryusa.com

Chinese numbers:
- chinahighlights.com
- travelchinaguide.com
- toneperfect.app
- hutong-school.com

**Patterns adopted:**

- One page per number, with a fixed template: meaning, love, twin flame, career, money, Chinese reading, action, FAQ and related numbers.
- A lookup box plus "tap a digit" browsing.
- Tool first, explanation second.
- Button copy in the first person ("Reveal My Life Path", "Find My Angel Number Now").
- A free partial result, then an email unlock.
- Birthday forms placed inside articles.
- "100% free, unsubscribe anytime" trust lines.
- A price ladder with a "Most popular" badge.
- Honest disclaimers: entertainment use, affiliates, and lottery tools marked unofficial.
- FAQ, HowTo and Breadcrumb schema.
- A daily "Number of the Day" loop.
- A donation page, following the Sacred Scribes and Affinity model.
- Monthly contests.

## 3. Phase-wise build prompt (copy each phase into your AI builder)

> **Global rules for every phase:**
> - Static HTML/CSS/vanilla JS only, deployable on the **GitHub Pages free plan**. No server and no build step at runtime.
> - All paths go through `{{ site.baseurl }}`, so the site works at `username.github.io/55388-com/` and later at `55388.com`.
> - Mobile-first and accessible (WCAG AA). Dark and light themes.
> - The **top of every page** shows: "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership", linked to `https://web.works/contact`.
> - **All forms and contact actions route to one inbox** (the owner's email — supplied privately, never committed in plain text). The address must **never appear in page text or HTML**. Store it encoded in `config.js`, decode it only in memory at submit or click time, and post through FormSubmit's AJAX endpoint. Support swapping in FormSubmit's random alias after activation.
> - Do not use "55388" as a claimed trademark. Include a trademark, copyright and affiliate disclosure page.

### Phase 0 — Foundations
Create the repo structure:

- `assets/css/style.css` (design tokens, dark/light themes, components)
- `assets/js/config.js` (all editable settings)
- `assets/js/engine.js` (pure numerology, angel-number, Chinese-luck and tool functions)
- `assets/js/main.js` (theme, nav, consent, ads, forms, video facade, share, sticky CTA, exit-intent)
- `_src/` Python generator that renders every page from one data file into Jekyll layouts, includes and `_data` (GitHub Pages builds Jekyll for free, with no Actions needed)

Then add `robots.txt`, `sitemap.xml`, `ads.txt` (template), `manifest.webmanifest`, the favicon and the OG image.

### Phase 1 — Brand & design system
- **Palette:** a cosmic navy base, gold (8 = prosperity), and violet and teal accents, with a gradient for highlights.
- **Type:** Fraunces for display text, Inter for UI.
- **Components:** cards, pills, badges, number grids, key-fact tiles, FAQ accordions, lead boxes, price cards, a meter, lottery balls, a video facade, the consent banner, the sticky CTA bar, and a modal.
- **Header, top banner and footer:** the footer carries four link columns plus the legal note.

### Phase 2 — Content engine (SEO core)
Generate:

- **56 angel-number pages (expandable from data).** Cover 000–999, 0000–9999, 11–99, mirror and clock numbers, sequences, and the cultural numbers 168, 520 and 1314, plus 55388. Each page includes:
  - root reduction, pattern type and a digit table
  - a layered cause → core → outcome reading
  - love, twin flame, career and money sections
  - a Chinese homophone score
  - an action plan, a 6-question FAQ (FAQPage schema) and related numbers
  - 3 ad slots and an in-article birthday lead form
- **An angel-numbers hub** with grouped grids, plus a **dynamic lookup page** for any number (`?n=`).
- **A numerology hub** and 12 Life Path pages (1–9, 11, 22, 33).
- **A Chinese lucky numbers guide:** a digit table and a lucky/unlucky combos table.
- **Three guides:** what angel numbers are, how to read sequences, and lucky numbers around the world.
- **Metadata** on every page: title and meta patterns, canonical URLs, Open Graph tags, and JSON-LD (WebSite + SearchAction, Organization, Article, BreadcrumbList).

### Phase 3 — Interactive tools (traffic magnets)
Build nine tools. Each has a tool-first layout with how-to steps, an FAQ, and HowTo + WebApplication schema:

- Life Path calculator
- Name numerology (Destiny, Soul Urge, Personality)
- Personal Year / Month / Day forecast
- Compatibility calculator
- Personal angel number finder
- Chinese lucky number checker (0–100 score, homophones, combos)
- Lottery generator (Powerball, Mega Millions, 6/49, Lotto Max, EuroMillions, UK Lotto, Pick 3/4), using Web Crypto randomness with an unofficial / responsible-play notice
- Random number, dice and coin tool
- Number-to-words, with cheque format, currencies, letter case and US/UK styles

### Phase 4 — Lead generation (dedicated, high-converting)
1. **`/reading/` — Free Number Blueprint funnel** in three steps:
   - details → instant preview (Life Path, Destiny, Soul Urge, Personal Year) with a blurred teaser
   - email + consent unlock
   - full on-screen blueprint, printable to PDF
   - upsells to a live reader (affiliate) and to the business audit
   - the lead is posted with all the calculated numbers
2. **`/business-lucky-number-audit/` — B2B lead form:** business, domain, numbers, audit tier, budget and message.
3. **Lead capture across the site:** in-article birthday forms on every meaning page, a newsletter band, the sticky CTA after 40% scroll (dismissible for 7 days), an exit-intent modal (desktop, once every 14 days), and sidebar lead cards.

### Phase 5 — Monetization layers
- **AdSense:** consent-gated loader. Named slots (header, inArticle, sidebar, footer) switch on once `adsenseClient` is set. Non-personalized ads are requested when the visitor picks "Essential only".
- **Affiliates:** `data-aff` links are swapped from config (liveReading, fullReport, shop) and marked `rel="sponsored"`.
- **YouTube:** a click-to-load facade (youtube-nocookie) and a video library by topic. A "Subscribe" button appears when `youtubeChannel` is set.
- **`/advertise/`:** a rate card (Sponsored Tool, Homepage Feature, Newsletter, Contest Partner), plus tool licensing, affiliate partners and a domain-acquisition link, with an inquiry form.

### Phase 6 — Community, donations, contests & hiring
- **`/support/` (donations):**
  - tiers of $5 / $25 / $88 / $388
  - the planned allocation: operations 30%, content & hiring 25%, promotion & marketing 20%, contests & prizes 20%, reserve 5%
  - Stripe / PayPal / Ko-fi / Buy Me a Coffee buttons driven by config
  - a pledge form covering purpose, frequency and recognition
  - "fund a prize / hire / campaign" cards
- **`/contests/`:** the monthly Lucky Number Challenge (story, video, art), with prizes of $88 / $55 / $38.
  - It is skill-judged, with no purchase necessary and entry limited to 18+.
  - Include the rules summary, an entry form and a sponsor form.
- **`/careers/`:** seven roles (writer, numerologist, video creator, Chinese culture contributor, SEO, front-end dev, moderator) and an application form.

### Phase 7 — Trust, legal & compliance
- **Pages:** About, Contact (form + hidden-mail button + domain-interest card), Privacy & Cookies (AdSense wording, GDPR / PIPEDA / Quebec Law 25 / CCPA rights), and Terms (contests, donations, no-advice).
- **Disclaimer page:** trademark disclosure, copyright notice, DMCA process, entertainment, affiliate, lottery and advertising disclosures.
- **Consent banner** on every page.

### Phase 8 — QA, deploy & growth
- **QA:** a link checker (0 broken links), a scan confirming the email appears nowhere, Playwright tests of every tool and form, mobile checks for horizontal overflow, and a Lighthouse pass.
- **Deploy:** push to `WEBWORKSA1/55388-com` and enable Pages (main branch, root).
- **Go-live checklist:**
  - Activate FormSubmit (the first submission sends an activation email) and paste the alias into `config.js`.
  - Add the AdSense ID and `ads.txt`.
  - Add the affiliate links.
  - Add the donation links.
  - Point 55388.com DNS at GitHub Pages and add a `CNAME` file.
- **Growth roadmap:**
  - Expand to all 0–9999 numbers with unique copy.
  - Add sub-intent pages (/444/love/, /444/biblical/).
  - Add an email service provider for the Daily Number sequence.
  - Create 3 Shorts a week, each linking to its number page.
  - Offer own PDF reports at $19–37.
  - Launch seasonal hubs: Lunar New Year, 8/8, 11/11.
