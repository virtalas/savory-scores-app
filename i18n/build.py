#!/usr/bin/env python3
"""Build the Finnish and Japanese versions of the website.

The English pages in website/ are the source of truth for structure and data.
Translations live next to this script:

    i18n/<lang>/strings.py           shared UI text, guide titles, data-table wording
    i18n/<lang>/index.html           the home page <main> content
    i18n/<lang>/guides/<slug>.html   each guide's article body

Data tables (<!--data:N|Heading--> in a guide body) are copied from the English
guide and translated here, so after updating the English data just re-run:

    python3 i18n/build.py

It also adds the language switcher and hreflang links to the English pages and
rewrites website/sitemap.xml.
"""
import html
import json
import re
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parent / "website"
BASE = "https://virtalas.github.io/savory-scores-app/website/"
APP_STORE = "https://apps.apple.com/fi/app/savory-scores/id6499091159"
TERMS = "https://virtalas.github.io/savory-scores-app/terms.html"
PRIVACY = "https://virtalas.github.io/savory-scores-app/privacy-policy.html"
UPDATED = "2026-10-28"

LANGS = ["en", "fi", "ja"]
LOCALES = {"en": "en_US", "fi": "fi_FI", "ja": "ja_JP"}
LANG_LABELS = {"en": ("EN", "English"), "fi": ("FI", "Suomi"), "ja": ("JA", "日本語")}

# Same order as the guide grid on the English home page.
GUIDES = [
    ("japanese-restaurants-helsinki", "🏮"),
    ("best-ramen-helsinki", "🍜"),
    ("best-sushi-helsinki", "🍣"),
    ("authentic-japanese-restaurant", "🔍"),
    ("donburi-helsinki", "🍚"),
    ("izakaya-helsinki", "🍶"),
    ("japanese-lunch-helsinki", "🍱"),
    ("japanese-grocery-helsinki", "🛒"),
    ("japanese-food-finland", "🇫🇮"),
    ("rate-restaurant-dishes", "⭐"),
]
SLUGS = [slug for slug, _ in GUIDES]


def esc(text):
    return html.escape(text, quote=True)


def strip_tags(fragment):
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


def page_url(lang, slug=None):
    path = "" if lang == "en" else f"{lang}/"
    if slug:
        path += f"guides/{slug}.html"
    return BASE + path


def rel_link(from_lang, from_slug, to_lang, to_slug=None):
    """Relative link between two pages of the site."""
    depth = (0 if from_lang == "en" else 1) + (1 if from_slug else 0)
    target = ("" if to_lang == "en" else f"{to_lang}/") + (f"guides/{to_slug}.html" if to_slug else "")
    return ("../" * depth + target) or "./"


def ld_json(obj):
    return ('        <script type="application/ld+json">\n'
            + json.dumps(obj, ensure_ascii=False, indent=4)
            + "\n        </script>")


def read_ld_blocks(page):
    return [json.loads(block) for block in
            re.findall(r'<script type="application/ld\+json">(.*?)</script>', page, re.S)]


# Shared chrome --------------------------------------------------------------

def alternate_links(slug):
    lines = [f'        <link rel="alternate" hreflang="{lang}" href="{page_url(lang, slug)}">' for lang in LANGS]
    lines.append(f'        <link rel="alternate" hreflang="x-default" href="{page_url("en", slug)}">')
    return "\n".join(lines)


def og_locale_alternates(lang):
    return "\n".join(f'        <meta property="og:locale:alternate" content="{LOCALES[other]}">'
                     for other in LANGS if other != lang)


def lang_switch(lang, slug, label, indent):
    pad = " " * indent
    links = []
    for other in LANGS:
        short, name = LANG_LABELS[other]
        current = ' aria-current="page"' if other == lang else ""
        links.append(f'{pad}    <a href="{rel_link(lang, slug, other, slug)}" hreflang="{other}" lang="{other}" '
                     f'title="{name}"{current}>{short}</a>')
    return f'{pad}<div class="lang-switch" role="group" aria-label="{esc(label)}">\n' + "\n".join(links) + f"\n{pad}</div>"


def footer_langs(lang, slug, label):
    links = "\n".join(f'                <a href="{rel_link(lang, slug, other, slug)}" hreflang="{other}" lang="{other}">'
                      f'{LANG_LABELS[other][1]}</a>' for other in LANGS)
    return f'            <nav class="footer-langs" aria-label="{esc(label)}">\n{links}\n            </nav>'


def head(lang, slug, title, description, og_type, ld_blocks):
    a = "../" * (1 + (1 if slug else 0))
    url = page_url(lang, slug)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{esc(title)}</title>
        <meta name="description" content="{esc(description)}">
        <link rel="canonical" href="{url}">
{alternate_links(slug)}
        <meta property="og:type" content="{og_type}">
        <meta property="og:site_name" content="Savory Scores">
        <meta property="og:title" content="{esc(title)}">
        <meta property="og:description" content="{esc(description)}">
        <meta property="og:url" content="{url}">
        <meta property="og:image" content="{BASE}assets/og-image.png">
        <meta property="og:locale" content="{LOCALES[lang]}">
{og_locale_alternates(lang)}
        <meta name="twitter:card" content="summary_large_image">
        <meta name="twitter:title" content="{esc(title)}">
        <meta name="twitter:description" content="{esc(description)}">
        <meta name="twitter:image" content="{BASE}assets/og-image.png">
        <meta name="geo.region" content="FI-18">
        <meta name="geo.placename" content="Helsinki">

        <link rel="icon" type="image/png" sizes="32x32" href="{a}assets/favicon-32.png">
        <link rel="icon" type="image/png" sizes="16x16" href="{a}assets/favicon-16.png">
        <link rel="apple-touch-icon" href="{a}assets/apple-touch-icon.png">
        <meta name="theme-color" content="#0a6cff">
        <meta name="apple-itunes-app" content="app-id=6499091159">

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c:wght@700;800&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="{a}styles.css">
        <script src="{a}script.js" defer></script>
{chr(10).join(ld_blocks)}
    </head>"""


def top_bar(lang, slug, S):
    a = "../" * (1 + (1 if slug else 0))
    home = "../" if slug else "./"
    anchor = home if slug else ""
    return f"""        <div class="score-stripe" aria-hidden="true"><span></span><span></span><span></span></div>
        <a class="skip-link" href="#main">{S['skip']}</a>
        <div class="top-bar">
            <a class="brand" href="{home}">
                <img src="{a}assets/favicon-32.png" srcset="{a}assets/apple-touch-icon.png 2x" width="38" height="38" alt="{esc(S['icon_alt'])}">
                Savory Scores
            </a>
            <nav class="top-nav" aria-label="{esc(S['nav_label'])}">
                <a href="{anchor}#screenshots">{S['nav_screenshots']}</a>
                <a href="{anchor}#how-it-works">{S['nav_how']}</a>
                <a href="{anchor}#guides">{S['nav_guides']}</a>
                <a href="{anchor}#faq">{S['nav_faq']}</a>
{lang_switch(lang, slug, S['languages'], 16)}
                <a class="nav-cta" href="{APP_STORE}">{S['nav_cta']}</a>
            </nav>
        </div>"""


def footer(lang, slug, S):
    a = "../" * (1 + (1 if slug else 0))
    home = "../" if slug else "./"
    guide_prefix = "" if slug else "guides/"
    guide_links = "\n".join(f'                <a href="{guide_prefix}{g}.html">{esc(S["guides"][g]["name"])}</a>'
                            for g in SLUGS)
    return f"""        <footer class="site-footer">
            <a class="footer-brand" href="{home}">
                <img src="{a}assets/favicon-32.png" srcset="{a}assets/apple-touch-icon.png 2x" width="32" height="32" alt="" aria-hidden="true">
                Savory Scores
            </a>
            <p class="footer-tag">{S['footer_tag']}</p>
            <nav class="footer-guides" aria-label="{esc(S['nav_guides'])}">
{guide_links}
            </nav>
            <nav aria-label="{esc(S['footer_label'])}">
                <a href="{APP_STORE}">{S['footer_download']}</a>
                <a href="{TERMS}">{S['terms']}</a>
                <a href="{PRIVACY}">{S['privacy']}</a>
            </nav>
{footer_langs(lang, slug, S['languages'])}
            <p class="copyright">&copy; 2026 Lasse Virtanen · {S['made_in']}</p>
        </footer>
    </body>
</html>
"""


# Data tables ----------------------------------------------------------------

DATA_NOTE = re.compile(
    r"Based on (?P<n>\d+) ratings(?: of Japanese (?P<of>dishes|products))? at (?P<m>\d+) (?P<where>places|stores) "
    r"in the Helsinki area(?:; places with at least (?P<k>\d+)(?P<auth> authenticity)? ratings)?, as of October 2026\. "
    r"Scores and authenticity are averages out of 10\. .*? Rate it in Savory Scores\.")
THUMB_ALT = re.compile(r'alt="(.+) at ([^"]+?), (Helsinki|Vantaa), photographed by a Savory Scores reviewer"')
LAST_RATED = re.compile(r"<td>(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{4})</td>")
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def translate_data_box(box, heading, S):
    T = S["data"]
    box = box.replace('src="../assets/', 'src="../../assets/')
    box = re.sub(r'aria-label="[^"]*"', f'aria-label="{esc(heading)}"', box, count=1)
    box = re.sub(r"<h2>.*?</h2>", f"<h2>{heading}</h2>", box, count=1)
    box = box.replace('<p class="data-kicker">From the Savory Scores data</p>',
                      f'<p class="data-kicker">{T["kicker"]}</p>')
    box = box.replace('<span class="sr-only">Photo</span>', f'<span class="sr-only">{T["Photo"]}</span>')
    box = re.sub(r"<th([^>]*)>([^<]+)</th>",
                 lambda m: f"<th{m.group(1)}>{T.get(m.group(2), m.group(2))}</th>", box)
    box = THUMB_ALT.sub(lambda m: f'alt="{T["alt"](m.group(1), m.group(2), S["cities"][m.group(3)])}"', box)
    box = re.sub(r'<span class="city">(\w+)</span>',
                 lambda m: f'<span class="city">{S["cities"][m.group(1)]}</span>', box)
    box = LAST_RATED.sub(lambda m: f"<td>{T['date'](MONTHS.index(m.group(1)) + 1, int(m.group(2)))}</td>", box)

    def note(m):
        return T["note"](n=int(m["n"]), m=int(m["m"]), of=m["of"], stores=m["where"] == "stores",
                         k=int(m["k"]) if m["k"] else None, auth=bool(m["auth"]))
    box, count = DATA_NOTE.subn(note, box)
    if count != 1:
        raise SystemExit(f"Unrecognised data note in box '{heading}'")
    return box


# Pages ------------------------------------------------------------------------

def build_index(lang, S, en_index):
    body = (HERE / lang / "index.html").read_text()
    cards = []
    for slug, emoji in GUIDES:
        g = S["guides"][slug]
        cards.append(f"""                    <li><a class="guide-card" href="guides/{slug}.html">
                        <span class="emoji" aria-hidden="true">{emoji}</span>
                        <h3>{esc(g['name'])}</h3>
                        <p>{esc(g['desc'])}</p>
                        <span class="read-more">{S['read_guide']}</span>
                    </a></li>""")
    body = body.replace("<!--guide-cards-->", "\n".join(cards).strip())

    app, _, _ = read_ld_blocks(en_index)
    app["description"] = S["app_ld_description"]
    app["url"] = page_url(lang)
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": strip_tags(q),
             "acceptedAnswer": {"@type": "Answer", "text": strip_tags(ans)}}
            for q, ans in re.findall(r"<summary>(.*?)</summary>\s*<div class=\"faq-answer\">\s*<p>(.*?)</p>", body, re.S)
        ],
    }
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": "Savory Scores",
            "url": page_url(lang), "inLanguage": lang}

    page = (head(lang, None, S["home_title"], S["home_description"], "website",
                 [ld_json(app), ld_json(faq), ld_json(site)])
            + "\n    <body>\n" + top_bar(lang, None, S)
            + '\n\n        <main id="main">\n' + body.rstrip() + "\n        </main>\n\n"
            + footer(lang, None, S))
    write(SITE / lang / "index.html", page)


def build_guide(lang, slug, S, en_page):
    g = S["guides"][slug]
    body = (HERE / lang / "guides" / f"{slug}.html").read_text().strip()
    h1 = re.search(r"<h1>(.*?)</h1>", body).group(1)
    body = body.replace(f"<h1>{h1}</h1>", f'<h1>{h1}</h1>\n                    <p class="article-meta">{S["article_meta"]}</p>', 1)

    boxes = re.findall(r'<section class="data-box".*?</section>', en_page, re.S)

    def data_box(m):
        return translate_data_box(boxes[int(m.group(1)) - 1], m.group(2), S)
    body = re.sub(r"<!--data:(\d+)\|(.*?)-->", data_box, body)

    related = re.findall(r'<li><a href="([\w-]+)\.html">',
                         re.search(r'<div class="related">.*?</ul>', en_page, re.S).group(0))
    next_slug = re.search(r'<nav class="article-footer-nav".*?<a href="([\w-]+)\.html">', en_page, re.S).group(1)
    en_article = next(b for b in read_ld_blocks(en_page) if b["@type"] == "Article")

    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": strip_tags(h1),
        "description": g["description"],
        "image": en_article["image"],
        "datePublished": en_article["datePublished"],
        "dateModified": UPDATED,
        "inLanguage": lang,
        "author": en_article["author"],
        "publisher": en_article["publisher"],
        "mainEntityOfPage": page_url(lang, slug),
        "about": {"@type": "City", "name": S["cities"]["Helsinki"]},
    }
    crumbs = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Savory Scores", "item": page_url(lang)},
            {"@type": "ListItem", "position": 2, "name": S["nav_guides"], "item": page_url(lang) + "#guides"},
            {"@type": "ListItem", "position": 3, "name": g["name"]},
        ],
    }

    related_items = "\n".join(
        f'                        <li><a href="{r}.html">{esc(S["guides"][r]["name"])}</a>{S["colon"]}{esc(S["guides"][r]["desc"])}</li>'
        for r in related)
    main = f"""        <main id="main">
            <div class="article-wrap">
                <nav class="breadcrumbs" aria-label="{esc(S['breadcrumb_label'])}">
                    <a href="../">{S['home']}</a> › <a href="../#guides">{S['nav_guides']}</a> › {esc(g['name'])}
                </nav>

                <article class="guide">
                    {body}

                    <div class="app-cta">
                        <img class="cta-icon" src="../../assets/icon-512.png" alt="{esc(S['icon_alt'])}" width="84" height="84" loading="lazy">
                        <div>
                            <p><strong>{S['cta_strong']}</strong> {S['cta_text']}</p>
                            <a class="store-cta" href="{APP_STORE}"><img class="app-store-badge" src="../../app_store_badge_en.svg" alt="{esc(S['badge_alt'])}" width="180" height="60" loading="lazy"></a>
                        </div>
                    </div>

                    <div class="related">
                        <h2>{S['related']}</h2>
                        <ul>
{related_items}
                        </ul>
                    </div>
                </article>

                <nav class="article-footer-nav" aria-label="{esc(S['more_guides'])}">
                    <a href="../">{S['back_home']}</a>
                    <a href="{next_slug}.html">{S['next'].format(name=esc(S['guides'][next_slug]['name']))}</a>
                </nav>
            </div>
        </main>
"""
    page = (head(lang, slug, g["title"], g["description"], "article", [ld_json(article), ld_json(crumbs)])
            + '\n    <body class="article-page">\n' + top_bar(lang, slug, S) + "\n\n" + main + "\n"
            + footer(lang, slug, S))
    write(SITE / lang / "guides" / f"{slug}.html", page)


# English pages: add hreflang, language switcher and footer language links ----

EN_LABELS = {"languages": "Language"}


def update_english(path, slug):
    page = path.read_text()
    page = re.sub(r'\n\s*<link rel="alternate" hreflang="[^"]*" href="[^"]*">', "", page)
    page = re.sub(r'\n\s*<meta property="og:locale:alternate" content="[^"]*">', "", page)
    page = re.sub(r'\n\s*<div class="lang-switch".*?</div>', "", page, flags=re.S)
    page = re.sub(r'\n\s*<nav class="footer-langs".*?</nav>', "", page, flags=re.S)

    page = re.sub(r'(<link rel="canonical" href="[^"]*">)', lambda m: m.group(1) + "\n" + alternate_links(slug), page, count=1)
    page = re.sub(r'(<meta property="og:locale" content="[^"]*">)', lambda m: m.group(1) + "\n" + og_locale_alternates("en"), page, count=1)
    page = re.sub(r'\n(\s*)<a class="nav-cta"',
                  lambda m: "\n" + lang_switch("en", slug, EN_LABELS["languages"], len(m.group(1))) + m.group(0), page, count=1)
    page = re.sub(r'\n\s*<p class="copyright">',
                  lambda m: "\n" + footer_langs("en", slug, EN_LABELS["languages"]) + m.group(0), page, count=1)
    write(path, page)


def build_sitemap():
    entries = []
    for slug in [None] + SLUGS:
        for lang in LANGS:
            alts = "\n".join(f'        <xhtml:link rel="alternate" hreflang="{other}" href="{page_url(other, slug)}"/>'
                             for other in LANGS)
            entries.append(f"""    <url>
        <loc>{page_url(lang, slug)}</loc>
        <lastmod>{UPDATED}</lastmod>
{alts}
        <xhtml:link rel="alternate" hreflang="x-default" href="{page_url('en', slug)}"/>
    </url>""")
    write(SITE / "sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
          + "\n".join(entries) + "\n</urlset>\n")


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def main():
    en_index = (SITE / "index.html").read_text()
    en_guides = {slug: (SITE / "guides" / f"{slug}.html").read_text() for slug in SLUGS}
    built = []
    for lang in LANGS[1:]:
        if not (HERE / lang / "strings.py").exists():
            continue
        S = runpy.run_path(str(HERE / lang / "strings.py"))["STRINGS"]
        if (HERE / lang / "index.html").exists():
            build_index(lang, S, en_index)
            built.append(f"{lang}/index.html")
        for slug in SLUGS:
            if (HERE / lang / "guides" / f"{slug}.html").exists():
                build_guide(lang, slug, S, en_guides[slug])
                built.append(f"{lang}/guides/{slug}.html")
    update_english(SITE / "index.html", None)
    for slug in SLUGS:
        update_english(SITE / "guides" / f"{slug}.html", slug)
    build_sitemap()
    print(f"Built {len(built)} pages:", ", ".join(built))


if __name__ == "__main__":
    main()
