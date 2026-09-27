"""Build 55388.com: regenerates the Jekyll source (pages, _data, _layouts, _includes) at the repo root.
GitHub Pages then builds it for free (Settings -> Pages -> Deploy from branch -> main / root).
Usage:  python3 _src/build.py            # Jekyll source
        python3 _src/build.py --static   # + fully rendered preview in _static/
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import DIGITS, MASTERS, LIFE_PATH, FEATURED, CHINESE, LOTTERIES
import angel, tools_pages, pages
from layout import SITE

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ROOT = REPO

def write(rel, content):
    fp = os.path.join(ROOT, rel if not rel.endswith("/") else rel + "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)

def collect():
    out = [pages.home(), angel.angel_index(), angel.lookup_page(), tools_pages.tools_index(), tools_pages.chinese_page(),
           pages.reading(), pages.business_audit(), pages.videos(), pages.support(), pages.contests(), pages.careers(),
           pages.advertise(), pages.contact(), pages.about()]
    out += [angel.angel_page(n) for n in FEATURED]
    out += tools_pages.all_tools() + tools_pages.numerology_pages() + pages.guides() + pages.legal()
    return out

def build_jekyll(dest):
    """Emit a Jekyll source tree (GitHub Pages builds it for free, no Actions needed)."""
    import layout
    global ROOT
    os.makedirs(dest, exist_ok=True)
    old = ROOT; ROOT = dest
    layout.MODE["jekyll"] = True
    out = collect()
    for path, html in out:
        if path.startswith("angel-numbers/") and path.count("/") == 2 and "lookup" not in path:
            html = angel.angel_front(path.split("/")[1])
        elif path.startswith("numerology/life-path/"):
            html = tools_pages.lifepath_front(int(path.split("/")[2]))
        write(path, html)
    write("_data/angels.json", json.dumps({n: angel.angel_data(n) for n in FEATURED}, ensure_ascii=False, separators=(",", ":")))
    write("_data/digits.json", json.dumps(DIGITS, ensure_ascii=False, separators=(",", ":")))
    write("_data/twin.json", json.dumps(angel.TWIN, ensure_ascii=False, separators=(",", ":")))
    write("_data/roots.json", json.dumps(angel.roots_data(), ensure_ascii=False, separators=(",", ":")))
    write("_data/lifepath.json", json.dumps(tools_pages.lifepath_data(), ensure_ascii=False, separators=(",", ":")))
    write("_layouts/lifepath.html", open(os.path.join(os.path.dirname(__file__), "jekyll", "lifepath.html"), encoding="utf-8").read())
    write("_layouts/angel.html", open(os.path.join(os.path.dirname(__file__), "jekyll", "angel.html"), encoding="utf-8").read())
    write("404.html", pages.not_found()[1].replace('<a class="btn btn-ghost" href="/55388-com/">Project home</a>', '').replace('href="/"', 'href="{{ site.baseurl }}/"'))
    layout.MODE["raw"] = True
    B = layout.BASE
    write("_includes/sidebar.html", angel._sidebar(B))
    write("_includes/newsletter.html", layout._newsletter_band(B))
    write("_includes/birthday.html", layout._birthday_inline(B))
    write("_includes/birthday-num.html", layout._birthday_inline(B, "{{ include.ctx }}"))
    layout.MODE["raw"] = False
    write("_layouts/default.html", layout.jekyll_layout())
    write("_config.yml", "title: 55388\nurl: https://webworksa1.github.io\nbaseurl: /55388-com   # set to \"\" after pointing 55388.com at GitHub Pages\nmarkdown: kramdown\nexclude: [_src, README.md, PROMPT.md, Gemfile, Gemfile.lock, node_modules]\n")
    layout.MODE["jekyll"] = False
    ROOT = old
    print("Jekyll tree:", dest, len(out) + 1, "pages")

SITEMAP_LIQUID = """---
layout: null
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{%- for p in site.pages -%}
{%- unless p.noindex or p.url contains 'lookup' or p.url contains '.xml' or p.url contains '.txt' or p.url contains '.webmanifest' %}
  <url><loc>https://55388.com{{ p.url | replace: 'index.html', '' }}</loc><lastmod>{{ site.time | date: '%Y-%m-%d' }}</lastmod></url>
{%- endunless -%}
{%- endfor %}
</urlset>
"""

def write_meta():
    write("sitemap.xml", SITEMAP_LIQUID)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nUser-agent: Mediapartners-Google\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    write("ads.txt", "# Replace pub-XXXXXXXXXXXXXXXX with your AdSense publisher ID, then remove the leading '#'.\n# google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0\n")
    write("manifest.webmanifest", json.dumps({"name": "55388 — The Number Universe", "short_name": "55388", "start_url": "./", "display": "standalone",
          "background_color": "#0b0d1a", "theme_color": "#0b0d1a", "icons": [{"src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=2, ensure_ascii=False))

def build_static(dest):
    """Fully rendered HTML (no Jekyll) for local preview: python3 _src/build.py --static"""
    import shutil
    global ROOT
    old, ROOT = ROOT, dest
    shutil.rmtree(os.path.join(dest, "assets"), ignore_errors=True)
    shutil.copytree(os.path.join(REPO, "assets"), os.path.join(dest, "assets"))
    out = collect()
    for path, html in out:
        write(path, html)
    p, html = pages.not_found()
    base_js = "<script>document.write('<base href=\"'+(location.hostname.endsWith('github.io')?'/55388-com/':'/')+'\">')</script>"
    write(p, html.replace('<meta charset="utf-8">', '<meta charset="utf-8">' + base_js, 1).replace('href="/"', 'href="./"').replace('<a class="btn btn-ghost" href="/55388-com/">Project home</a>', ''))
    write(".nojekyll", "")
    ROOT = old
    print(f"Static preview: {len(out) + 1} pages in {dest}")

def main():
    """Default: regenerate the Jekyll source (pages, _data, _layouts, _includes) at the repo root."""
    js = {"digits": DIGITS, "masters": {str(k): v for k, v in MASTERS.items()}, "lifePath": {str(k): v for k, v in LIFE_PATH.items()},
          "featured": FEATURED, "chinese": CHINESE, "lotteries": LOTTERIES}
    write("assets/js/data.js", "/* generated by _src/build.py */\nwindow.N55_DATA=" + json.dumps(js, ensure_ascii=False, separators=(",", ":")) + ";\n")
    write_meta()
    build_jekyll(REPO)
    if "--static" in sys.argv:
        build_static(os.path.join(REPO, "_static"))

if __name__ == "__main__":
    main()
