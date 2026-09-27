# 55388.com — The Number Universe

Angel numbers, numerology, Chinese lucky numbers and free number tools. It is a static site built for the **GitHub Pages free plan**.

- **Concept, research & phase-wise build prompt:** see [PROMPT.md](PROMPT.md)
- **Live (GitHub Pages):** https://webworksa1.github.io/55388-com/

## What's inside

| Area | Pages |
|---|---|
| Angel numbers | Hub, 56 number pages (data-driven, expandable), dynamic lookup for any number |
| Numerology | Hub + 12 Life Path pages |
| Chinese lucky numbers | Guide + checker tool |
| Tools (9) | Life Path, Name, Personal Year, Compatibility, Angel Finder, Chinese Luck, Lottery, Random/Dice/Coin, Number-to-Words |
| Lead generation | `/reading/` 3-step funnel, `/business-lucky-number-audit/`, in-article forms, newsletter, sticky CTA, exit-intent |
| Monetization | AdSense slots (consent-gated), affiliate hooks, YouTube library, `/advertise/` |
| Community | `/support/` donations & pledges, `/contests/` monthly prizes, `/careers/` hiring |
| Legal | Privacy & Cookies, Terms, Disclaimer + Trademark/Copyright disclosure |

## How it's built

GitHub Pages builds the site with **Jekyll** for free, so no Actions workflow is needed:

- `_layouts/default.html`: the shared shell. It holds the top interest banner, header, footer, consent banner, sticky CTA and exit-intent modal.
- `_layouts/angel.html` + `_data/angels.json`: the 56 angel-number pages are rendered from data.
- `_includes/`: the sidebar, newsletter band and in-article birthday forms.
- `assets/`: CSS, JS (the `engine.js` number engine, `main.js`, `tools.js`, `reading.js`, `config.js`) and images.

All content lives in `_src/` (Python 3, no dependencies). After editing, regenerate:

```bash
python3 _src/build.py            # regenerate the Jekyll source at the repo root
python3 _src/build.py --static   # plus a fully rendered preview in _static/ (git-ignored)
```

All settings live in `assets/js/config.js`: AdSense ID, GA4, affiliate links, donation links, YouTube channel and FormSubmit alias.
When you move to the custom domain, set `baseurl: ""` in `_config.yml`.

## Go-live checklist

1. **Forms:** the first form submission triggers a FormSubmit activation email to the site inbox. Click *Activate*. Optionally paste the random alias FormSubmit gives you into `formAlias` in `config.js`. The inbox address is stored encoded and never appears in page text or source.
2. **AdSense:**
   - Set `adsenseClient` (and the slot IDs) in `config.js`.
   - Uncomment the line in `ads.txt` and put in your publisher ID.
   - For AdSense in the EEA/UK, enable a Google-certified CMP.
3. **Affiliates and donations:** fill in `affiliate.*` and `donateLinks.*`.
4. **Custom domain:** in the DNS for 55388.com, add the four GitHub Pages A records (185.199.108–111.153) and a `www` CNAME pointing to `webworksa1.github.io`. Then add a `CNAME` file containing `55388.com`, set `baseurl: ""` in `_config.yml`, and set the custom domain in *Settings → Pages*.

## Disclosure

© 2026 55388.com. All original content, design and code: all rights reserved. "55388" is used only as a number and domain name. It is not affiliated with any ZIP code area, lottery or company. Third-party trademarks and embedded videos belong to their owners. Content is for entertainment and self-reflection.
