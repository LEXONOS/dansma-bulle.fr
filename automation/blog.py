# -*- coding: utf-8 -*-
"""
Lib du journal (blog) Dans Ma Bulle.
- render_article_page(meta, body_html) -> page article complète (SEO + schema)
- build_index(posts) -> /blog/index.html
- build_sitemap(posts) -> /sitemap.xml
Lancé seul, reconstruit l'index et le sitemap depuis automation/posts.json.
"""
import json, os, datetime

SITE = "https://dansma-bulle.fr"
PHONE_TEL = "0614838109"; PHONE = "06 14 83 81 09"
EMAIL = "contact@dansma-bulle.fr"
IG = "https://www.instagram.com/dansmabulle.bordeaux/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # racine du site

# Pages statiques pour le sitemap (priorité)
STATIC_PAGES = [
    ("/", "1.0", "weekly"),
    ("/experiences/diner-en-bulle.html", "0.9", "monthly"),
    ("/experiences/brunch-en-bulle.html", "0.9", "monthly"),
    ("/experiences/sur-mesure.html", "0.8", "monthly"),
    ("/occasions/demande-en-mariage.html", "0.9", "monthly"),
    ("/occasions/anniversaire.html", "0.8", "monthly"),
    ("/occasions/saint-valentin.html", "0.8", "monthly"),
    ("/carte-cadeau.html", "0.7", "monthly"),
    ("/blog/", "0.8", "weekly"),
]

def _head(title, desc, path, og_image, schemas):
    canonical = SITE + path; og = SITE + og_image
    sch = "\n  ".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#F3F5F4">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="article">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:site_name" content="Dans Ma Bulle">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{og}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{og}">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/styles.css">
  <script>document.documentElement.classList.add('js');</script>
  {sch}
</head>
<body>
  <a class="skip-link" href="#main">Aller au contenu</a>
  <div class="bubbles" data-bubbles aria-hidden="true"></div>"""

def _header():
    return f"""
  <header class="header" id="top" data-header>
    <div class="header__inner">
      <a class="brand" href="/" aria-label="Dans Ma Bulle, accueil">
        <img class="brand__mark" src="/assets/logo.jpg" width="48" height="48" alt="">
        <span class="brand__name">Dans Ma Bulle</span>
      </a>
      <nav class="nav" aria-label="Navigation principale">
        <ul class="nav__list">
          <li><a class="nav__link" href="/experiences/diner-en-bulle.html">Dîner</a></li>
          <li><a class="nav__link" href="/experiences/brunch-en-bulle.html">Brunch</a></li>
          <li><a class="nav__link" href="/#occasions">Occasions</a></li>
          <li><a class="nav__link" href="/blog/">Journal</a></li>
        </ul>
      </nav>
      <a class="btn btn--solid header__cta" href="/#reserver">Réserver<span class="btn__arrow" aria-hidden="true">→</span></a>
      <button class="burger" data-menu-toggle aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="drawer"><span></span><span></span><span></span></button>
    </div>
  </header>
  <div class="drawer" id="drawer" aria-hidden="true">
    <nav class="drawer__nav" aria-label="Navigation mobile">
      <a href="/experiences/diner-en-bulle.html">Dîner romantique</a>
      <a href="/experiences/brunch-en-bulle.html">Brunch</a>
      <a href="/experiences/sur-mesure.html">Sur-mesure</a>
      <a href="/#occasions">Occasions</a>
      <a href="/blog/">Le journal</a>
      <a href="/carte-cadeau.html">Carte cadeau</a>
      <a class="drawer__cta" href="/#reserver">Réserver votre bulle</a>
    </nav>
    <div class="drawer__foot">
      <a href="tel:{PHONE_TEL}">{PHONE}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="{IG}" target="_blank" rel="noopener">Instagram</a>
    </div>
  </div>
  <div class="drawer__scrim" data-menu-close aria-hidden="true"></div>"""

def _footer():
    return f"""
  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <a class="brand brand--footer" href="/">
            <img class="brand__mark" src="/assets/logo.jpg" width="56" height="56" alt="">
            <span class="brand__name">Dans Ma Bulle</span>
          </a>
          <p class="footer__tagline">Brunch et dîners insolites dans une bulle transparente, au cœur des vignobles bordelais. Fignolé avec amour.</p>
          <a class="ig-link ig-link--foot" href="{IG}" target="_blank" rel="noopener">@dansmabulle.bordeaux</a>
        </div>
        <nav class="footer__col" aria-label="Les formules"><h3>Les formules</h3><ul>
          <li><a href="/experiences/diner-en-bulle.html">Le Dîner romantique</a></li>
          <li><a href="/experiences/brunch-en-bulle.html">Le Brunch</a></li>
          <li><a href="/experiences/sur-mesure.html">Sur-Mesure</a></li>
          <li><a href="/carte-cadeau.html">Carte cadeau</a></li></ul></nav>
        <nav class="footer__col" aria-label="Occasions"><h3>Occasions</h3><ul>
          <li><a href="/occasions/demande-en-mariage.html">Demande en mariage</a></li>
          <li><a href="/occasions/anniversaire.html">Anniversaire</a></li>
          <li><a href="/occasions/saint-valentin.html">Saint-Valentin</a></li>
          <li><a href="/blog/">Le journal</a></li></ul></nav>
        <div class="footer__col"><h3>Nous joindre</h3><ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Vignobles de Bordeaux</li></ul></div>
      </div>
      <div class="footer__bottom">
        <p>© <span data-year>2026</span> Dans Ma Bulle · Vignobles de Bordeaux</p>
        <a class="footer__top-link" href="#top">Haut de page ↑</a>
      </div>
    </div>
  </footer>
  <script src="/js/main.js" defer></script>
</body>
</html>"""

FR_MONTHS = ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet",
             "août", "septembre", "octobre", "novembre", "décembre"]
def fr_date(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {FR_MONTHS[d.month]} {d.year}"

def render_article_page(meta, body_html):
    """meta: slug,title,description,category,date(iso),image,keyword,faqs[],takeaways[]"""
    path = f"/blog/{meta['slug']}.html"
    img = meta["image"]
    takeaways = ""
    if meta.get("takeaways"):
        lis = "".join(f"<li>{t}</li>" for t in meta["takeaways"])
        takeaways = f'<aside class="takeaways"><h2>L\'essentiel</h2><ul>{lis}</ul></aside>'
    faq_block = ""
    if meta.get("faqs"):
        accs = "".join(
            f'<div class="acc"><button class="acc__q" aria-expanded="false"><span>{q}</span><span class="acc__icon" aria-hidden="true"></span></button><div class="acc__a"><p>{a}</p></div></div>'
            for q, a in meta["faqs"])
        faq_block = f'<section class="section" style="padding-top:1rem"><div class="container container--narrow"><header class="section-head reveal"><p class="eyebrow">Bon à savoir</p><h2>Questions fréquentes</h2></header><div class="accordion reveal">{accs}</div></div></section>'

    schemas = [
        {"@context": "https://schema.org", "@type": "BlogPosting", "headline": meta["title"],
         "description": meta["description"], "image": SITE + img,
         "datePublished": meta["date"], "dateModified": meta["date"],
         "author": {"@type": "Organization", "name": "Dans Ma Bulle"},
         "publisher": {"@type": "Organization", "name": "Dans Ma Bulle",
                       "logo": {"@type": "ImageObject", "url": SITE + "/assets/logo.jpg"}},
         "mainEntityOfPage": {"@type": "WebPage", "@id": SITE + path},
         "keywords": meta.get("keyword", "")},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Journal", "item": SITE + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": meta["title"], "item": SITE + path}]},
    ]
    if meta.get("faqs"):
        schemas.append({"@context": "https://schema.org", "@type": "FAQPage",
                        "mainEntity": [{"@type": "Question", "name": q,
                                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in meta["faqs"]]})

    html = _head(meta["title"], meta["description"], path, img, schemas)
    html += _header()
    html += f"""
  <main id="main">
    <nav class="crumb" aria-label="Fil d'ariane"><div class="crumb__in"><a href="/">Accueil</a><span aria-hidden="true">›</span><a href="/blog/">Journal</a><span aria-hidden="true">›</span><span aria-current="page">{meta['category']}</span></div></nav>
    <article>
      <section class="section" style="padding-bottom:0">
        <div class="container">
          <div class="art-head reveal">
            <p class="post-card__cat">{meta['category']}</p>
            <h1>{meta['title']}</h1>
            <p class="art-head__meta">Publié le {fr_date(meta['date'])} · Dans Ma Bulle</p>
          </div>
          <figure class="art-cover reveal"><img src="{img}" alt="{meta['title']}" fetchpriority="high"></figure>
          <div class="art-body reveal">
            {takeaways}
            <div class="prose">
              {body_html}
            </div>
          </div>
        </div>
      </section>
      {faq_block}
      <section class="section"><div class="container"><div class="cta-band reveal"><h2>Envie de vivre l'expérience ?</h2><p>Un brunch ou un dîner dans une bulle posée au cœur des vignes. Dites-nous la date, on s'occupe du reste.</p><a class="btn btn--solid btn--lg" href="/#reserver">Réserver votre bulle<span class="btn__arrow" aria-hidden="true">→</span></a></div></div></section>
    </article>
  </main>"""
    html += _footer()
    return html

def build_index(posts):
    posts_sorted = sorted(posts, key=lambda p: p["date"], reverse=True)
    cards = ""
    for p in posts_sorted:
        cards += f'''<a class="post-card" href="/blog/{p['slug']}.html"><span class="post-card__media"><img loading="lazy" src="{p['image']}" alt="{p['title']}"></span><span class="post-card__body"><span class="post-card__cat">{p['category']}</span><h3>{p['title']}</h3><p>{p['description']}</p><span class="post-card__date">{fr_date(p['date'])}</span></span></a>'''
    if not posts_sorted:
        cards = '<p class="lead">Les premiers articles arrivent très vite.</p>'
    schemas = [{"@context": "https://schema.org", "@type": "Blog", "name": "Le Journal de Dans Ma Bulle",
                "url": SITE + "/blog/", "description": "Idées de sorties insolites, romantiques et gourmandes autour de Bordeaux."}]
    html = _head("Le Journal — idées de sorties insolites autour de Bordeaux | Dans Ma Bulle",
                 "Idées de dîners romantiques, brunchs originaux et sorties insolites autour de Bordeaux et dans le vignoble. Le journal de Dans Ma Bulle.",
                 "/blog/", "/assets/images/dome-jour-1600.webp", schemas)
    html += _header()
    html += f"""
  <main id="main">
    <section class="section" style="padding-top:8rem">
      <div class="container">
        <header class="section-head reveal">
          <p class="eyebrow">Le journal</p>
          <h2>Des idées pour des moments hors du commun</h2>
          <p class="lead">Dîners romantiques, brunchs originaux, sorties insolites et bonnes adresses autour de Bordeaux et de son vignoble.</p>
        </header>
        <div class="post-grid reveal" data-delay="1">
          {cards}
        </div>
      </div>
    </section>
  </main>"""
    html += _footer()
    with open(os.path.join(ROOT, "blog", "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("  index du blog reconstruit:", len(posts_sorted), "articles")

def build_sitemap(posts):
    today = datetime.date.today().isoformat()
    urls = ""
    for path, prio, freq in STATIC_PAGES:
        urls += f"  <url><loc>{SITE}{path}</loc><changefreq>{freq}</changefreq><priority>{prio}</priority></url>\n"
    for p in sorted(posts, key=lambda x: x["date"], reverse=True):
        urls += f"  <url><loc>{SITE}/blog/{p['slug']}.html</loc><lastmod>{p['date']}</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>\n"
    xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n'
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    print("  sitemap.xml reconstruit")

def load_posts():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts.json")
    if os.path.exists(p):
        return json.load(open(p, encoding="utf-8"))
    return []

def save_posts(posts):
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts.json")
    json.dump(posts, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

if __name__ == "__main__":
    posts = load_posts()
    build_index(posts)
    build_sitemap(posts)
    print("OK")
