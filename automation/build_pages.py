# -*- coding: utf-8 -*-
"""
Génère les pages internes statiques de Dans Ma Bulle (header/footer partagés,
SEO + schema.org par page). Sortie : fichiers HTML à la racine du site.
Lancer depuis la racine du site : python automation/build_pages.py
"""
import json, os

SITE = "https://dansma-bulle.fr"
PHONE_TEL = "0614838109"
PHONE = "06 14 83 81 09"
EMAIL = "contact@dansma-bulle.fr"
IG = "https://www.instagram.com/dansmabulle.bordeaux/"

# ---------------------------------------------------------------- composants
def head(title, desc, path, og_image, schemas):
    canonical = SITE + path
    og = SITE + og_image
    sch = "\n  ".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
        for s in schemas)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#F3F5F4">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
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
  <link rel="apple-touch-icon" href="/assets/logo.jpg">
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

def header():
    return """
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
      <button class="burger" data-menu-toggle aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="drawer">
        <span></span><span></span><span></span>
      </button>
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
      <a href="tel:%s">%s</a>
      <a href="mailto:%s">%s</a>
      <a href="%s" target="_blank" rel="noopener">Instagram</a>
    </div>
  </div>
  <div class="drawer__scrim" data-menu-close aria-hidden="true"></div>
""" % (PHONE_TEL, PHONE, EMAIL, EMAIL, IG)

def footer():
    return """
  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <a class="brand brand--footer" href="/">
            <img class="brand__mark" src="/assets/logo.jpg" width="56" height="56" alt="">
            <span class="brand__name">Dans Ma Bulle</span>
          </a>
          <p class="footer__tagline">Brunch et dîners insolites dans une bulle transparente, au cœur des vignobles bordelais. Fignolé avec amour.</p>
          <a class="ig-link ig-link--foot" href="%s" target="_blank" rel="noopener">@dansmabulle.bordeaux</a>
        </div>
        <nav class="footer__col" aria-label="Navigation pied de page">
          <h3>Les formules</h3>
          <ul>
            <li><a href="/experiences/diner-en-bulle.html">Le Dîner romantique</a></li>
            <li><a href="/experiences/brunch-en-bulle.html">Le Brunch</a></li>
            <li><a href="/experiences/sur-mesure.html">Sur-Mesure</a></li>
            <li><a href="/carte-cadeau.html">Carte cadeau</a></li>
          </ul>
        </nav>
        <nav class="footer__col" aria-label="Occasions">
          <h3>Occasions</h3>
          <ul>
            <li><a href="/occasions/demande-en-mariage.html">Demande en mariage</a></li>
            <li><a href="/occasions/anniversaire.html">Anniversaire</a></li>
            <li><a href="/occasions/saint-valentin.html">Saint-Valentin</a></li>
            <li><a href="/blog/">Le journal</a></li>
          </ul>
        </nav>
        <div class="footer__col">
          <h3>Nous joindre</h3>
          <ul>
            <li><a href="tel:%s">%s</a></li>
            <li><a href="mailto:%s">%s</a></li>
            <li>Vignobles de Bordeaux</li>
          </ul>
        </div>
      </div>
      <div class="footer__bottom">
        <p>© <span data-year>2026</span> Dans Ma Bulle · Vignobles de Bordeaux</p>
        <a class="footer__top-link" href="#top">Haut de page ↑</a>
      </div>
    </div>
  </footer>
  <script src="/js/main.js" defer></script>
</body>
</html>""" % (IG, PHONE_TEL, PHONE, EMAIL, EMAIL)

def crumb(items):
    parts = []
    for i, (label, url) in enumerate(items):
        if url and i < len(items) - 1:
            parts.append(f'<a href="{url}">{label}</a>')
        else:
            parts.append(f'<span aria-current="page">{label}</span>')
        if i < len(items) - 1:
            parts.append('<span aria-hidden="true">›</span>')
    return f'<nav class="crumb" aria-label="Fil d\'ariane"><div class="crumb__in">{"".join(parts)}</div></nav>'

def accordion(faqs):
    items = ""
    for q, a in faqs:
        items += f'''<div class="acc"><button class="acc__q" aria-expanded="false"><span>{q}</span><span class="acc__icon" aria-hidden="true"></span></button><div class="acc__a"><p>{a}</p></div></div>'''
    return f'<div class="accordion reveal">{items}</div>'

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def breadcrumb_schema(items):
    el = []
    for i, (label, url) in enumerate(items):
        node = {"@type": "ListItem", "position": i + 1, "name": label}
        if url:
            node["item"] = SITE + url
        el.append(node)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": el}

def offer_schema(name, desc, price, url):
    s = {"@context": "https://schema.org", "@type": "Product", "name": name,
         "description": desc, "brand": {"@type": "Brand", "name": "Dans Ma Bulle"},
         "url": SITE + url}
    if price:
        s["offers"] = {"@type": "Offer", "price": str(price), "priceCurrency": "EUR",
                       "availability": "https://schema.org/InStock", "url": SITE + url}
    return s

def related(cards):
    """cards: list of (href, img, title, text)"""
    inner = ""
    for href, img, title, text in cards:
        inner += f'''<a class="linkcard" href="{href}"><span class="linkcard__media"><img loading="lazy" src="{img}" alt="{title}"></span><span class="linkcard__body"><h3>{title}</h3><p>{text}</p><span class="linkcard__more">Découvrir<span aria-hidden="true">→</span></span></span></a>'''
    return f'<div class="linkcards reveal">{inner}</div>'

def cta_band(title, text):
    return f'''<section class="section"><div class="container"><div class="cta-band reveal"><h2>{title}</h2><p>{text}</p><a class="btn btn--solid btn--lg" href="/#reserver">Réserver votre bulle<span class="btn__arrow" aria-hidden="true">→</span></a></div></div></section>'''

def write(path, html):
    full = os.path.join(OUT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("  écrit:", path)

OUT = os.getcwd()

# ---------------------------------------------------------------- gabarit page expérience / occasion
def landing_page(path, title, desc, og, h1, eyebrow, intro, facts, hero_img,
                 crumb_items, lead_title, lead_html, incl_title, incl, price_num,
                 price_unit, split_img, split_alt, faqs, rel_cards, schemas):
    facts_li = "".join(f"<li>{x}</li>" for x in facts)
    incl_li = "".join(f"<li>{x}</li>" for x in incl)
    html = head(title, desc, path, og, schemas)
    html += header()
    html += f'''
  <main id="main">
    <section class="phero">
      <div class="phero__media"><img src="{hero_img}" alt="{split_alt}" fetchpriority="high"><div class="phero__veil"></div></div>
      <div class="phero__inner">
        <p class="phero__eyebrow">{eyebrow}</p>
        <h1>{h1}</h1>
        <p class="phero__intro">{intro}</p>
        <div class="phero__actions">
          <a class="btn btn--solid btn--lg" href="/#reserver">Réserver<span class="btn__arrow" aria-hidden="true">→</span></a>
          <a class="btn btn--glass btn--lg" href="#details">En savoir plus</a>
        </div>
        <ul class="phero__facts">{facts_li}</ul>
      </div>
    </section>
    {crumb(crumb_items)}

    <section class="section" id="details">
      <div class="container">
        <div class="split">
          <div class="split__text reveal">
            <p class="eyebrow">{eyebrow}</p>
            <h2>{lead_title}</h2>
            <div class="lead">{lead_html}</div>
          </div>
          <figure class="split__media reveal" data-delay="1"><img loading="lazy" src="{split_img}" alt="{split_alt}"></figure>
        </div>
      </div>
    </section>

    <section class="section section--sage">
      <div class="container">
        <div class="split split--reverse">
          <figure class="split__media reveal"><img loading="lazy" src="{hero_img}" alt="{split_alt}"></figure>
          <div class="split__text reveal" data-delay="1">
            <h2>{incl_title}</h2>
            <ul class="incl">{incl_li}</ul>
            <div class="pricebar">
              <span class="price"><span class="price__num">{price_num}</span><span class="price__unit">{price_unit}</span></span>
              <a class="btn btn--solid" href="/#reserver">Réserver maintenant<span class="btn__arrow" aria-hidden="true">→</span></a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container container--narrow">
        <header class="section-head reveal"><p class="eyebrow">Avant de réserver</p><h2>Les questions fréquentes</h2></header>
        {accordion(faqs)}
      </div>
    </section>

    <section class="section section--blush">
      <div class="container">
        <header class="section-head reveal"><p class="eyebrow">À découvrir aussi</p><h2>D'autres façons de vivre la bulle</h2></header>
        {related(rel_cards)}
      </div>
    </section>

    {cta_band("Prêt à réserver votre parenthèse ?", "Dites-nous la date et l'occasion, on revient vers vous sous 24h pour tout composer.")}
  </main>'''
    html += footer()
    write(path, html)


IMG = "/assets/images/"

# ================================================================ EXPÉRIENCES
landing_page(
    "/experiences/diner-en-bulle.html",
    "Dîner romantique en bulle dans les vignes — Bordeaux | Dans Ma Bulle",
    "Un dîner insolite et romantique dans une bulle transparente, au cœur des vignobles bordelais. Table dressée pour deux, 2h30 d'intimité, tout compris à 180€.",
    IG + "diner-vignes-crepuscule-1600.webp",
    "Un dîner romantique en bulle, au cœur des vignes",
    "Dîner insolite · Vignobles de Bordeaux",
    "Le temps d'un soir, installez-vous en tête-à-tête dans une bulle transparente posée face aux vignes. Une table dressée, des bougies, le ciel pour décor et le monde qui s'efface.",
    ["Pour deux", "2h30 d'intimité", "Au cœur des vignes"],
    IMG + "diner-vignes-crepuscule-1600.webp",
    [("Accueil", "/"), ("Le dîner romantique", None)],
    "Un dîner dont on se souvient, pas juste un repas.",
    "<p>Dans Ma Bulle réunit l'intimité d'un salon privé et la magie du plein air. À l'intérieur, une table soignée et une lumière douce. Dehors, le calme du domaine et la lumière de fin de journée sur les vignes. Vous arrivez, tout est dressé. Vous n'avez qu'à savourer.</p>",
    "Ce qui est compris",
    ["Bulle transparente dressée et décorée pour deux", "Dîner gourmand, du salé au sucré", "2h30 d'intimité totale, rien qu'à vous", "Installation et rangement à notre charge"],
    "180€", "tout compris, pour deux",
    IMG + "roses-intime-800.webp",
    "Table dressée pour deux et roses dans une bulle au crépuscule",
    [
        ("Le dîner se déroule-t-il en intérieur ou en extérieur ?", "Dans une bulle transparente, fermée et abritée, posée en extérieur au cœur du vignoble. Vous profitez de la vue et du plein air tout en étant au sec, au chaud et à l'abri du vent, en toute saison."),
        ("Le repas est-il vraiment compris dans les 180€ ?", "Oui. Les 180€ couvrent la bulle dressée et décorée pour deux, le dîner gourmand et les 2h30 d'expérience. Aucun supplément caché."),
        ("Peut-on adapter le menu à nos goûts ou allergies ?", "Bien sûr. Indiquez vos envies, régimes et allergies à la réservation et nous composons en conséquence."),
        ("Peut-on en faire une demande en mariage ?", "Avec plaisir, c'est l'un de nos moments préférés. Découvrez la page dédiée à la demande en mariage pour la mise en scène."),
    ],
    [
        ("/experiences/brunch-en-bulle.html", IMG + "brunch-table-800.webp", "Le Brunch en bulle", "Le rendez-vous gourmand du week-end, jusqu'à 6 convives."),
        ("/occasions/demande-en-mariage.html", IMG + "mot-doux-800.webp", "Demande en mariage", "Le décor parfait pour poser la question."),
        ("/occasions/saint-valentin.html", IMG + "table-deux-ciel-800.webp", "Saint-Valentin", "Un tête-à-tête loin des restaurants bondés."),
    ],
    [offer_schema("Dîner romantique en bulle", "Dîner en tête-à-tête dans une bulle transparente, tout compris pour deux, au cœur des vignobles bordelais.", 180, "/experiences/diner-en-bulle.html"),
     breadcrumb_schema([("Accueil", "/"), ("Dîner romantique en bulle", "/experiences/diner-en-bulle.html")]),
     faq_schema([
        ("Le dîner se déroule-t-il en intérieur ou en extérieur ?", "Dans une bulle transparente, fermée et abritée, posée en extérieur au cœur du vignoble, confortable en toute saison."),
        ("Le repas est-il compris dans les 180€ ?", "Oui, les 180€ couvrent la bulle dressée et décorée pour deux, le dîner gourmand et les 2h30 d'expérience, sans supplément caché."),
        ("Peut-on adapter le menu aux allergies ?", "Oui, indiquez vos régimes et allergies à la réservation et le menu est composé en conséquence."),
     ])],
)

landing_page(
    "/experiences/brunch-en-bulle.html",
    "Brunch insolite en bulle dans les vignes — Bordeaux | Dans Ma Bulle",
    "Un brunch insolite et gourmand dans une bulle transparente au cœur des vignes bordelaises. Jusqu'à 6 convives, 2h30 au calme, dès 55€ par personne.",
    IMG + "brunch-table-1600.webp",
    "Un brunch insolite, au cœur des vignes",
    "Brunch original · Vignobles de Bordeaux",
    "Le rendez-vous gourmand du week-end, version hors du commun. Viennoiseries, produits frais et douceurs à partager, dans la lumière du matin et la chaleur d'une bulle rien qu'à vous.",
    ["Jusqu'à 6 convives", "2h30 au calme", "Dès 55€/personne"],
    IMG + "brunch-table-1600.webp",
    [("Accueil", "/"), ("Le brunch en bulle", None)],
    "Le brunch du dimanche, mais inoubliable.",
    "<p>Entre amis, en famille ou en amoureux, on s'installe dans la bulle posée au cœur des vignes. La table est dressée, le brunch est prêt, le temps ralentit. Une bulle d'air pour bien commencer la journée, loin de l'agitation et des cafés bondés.</p>",
    "Ce qui est compris",
    ["Bulle transparente dressée et décorée", "Brunch salé et sucré à partager", "Jusqu'à 6 convives", "2h30 au calme des vignes"],
    "55€", "par personne",
    IMG + "brunch-vue-dessus-800.webp",
    "Brunch gourmand dressé dans une bulle, vue du dessus",
    [
        ("Combien de personnes peut accueillir le brunch ?", "Jusqu'à 6 convives dans une même bulle. Pour un groupe plus grand ou un format particulier, contactez-nous, on s'adapte."),
        ("Que comprend le brunch ?", "Un assortiment salé et sucré à partager, viennoiseries, produits frais et douceurs, servis directement dans votre bulle."),
        ("Le brunch est-il adapté aux enfants ?", "Oui, le brunch se prête très bien à un moment en famille. Dites-nous l'âge des enfants pour qu'on adapte."),
        ("À quel moment de la matinée se déroule-t-il ?", "Le créneau est calé avec vous à la réservation, selon les disponibilités du domaine."),
    ],
    [
        ("/experiences/diner-en-bulle.html", IMG + "diner-vignes-crepuscule-800.webp", "Le Dîner romantique", "Un tête-à-tête sous les étoiles, tout compris pour deux."),
        ("/occasions/anniversaire.html", IMG + "brunch-ballons-800.webp", "Anniversaire", "Fêter l'année qui passe autrement."),
        ("/carte-cadeau.html", IMG + "detail-livre-800.webp", "Carte cadeau", "Offrir un moment plutôt qu'un objet."),
    ],
    [offer_schema("Brunch insolite en bulle", "Brunch gourmand dans une bulle transparente, jusqu'à six convives, au cœur des vignobles bordelais.", 55, "/experiences/brunch-en-bulle.html"),
     breadcrumb_schema([("Accueil", "/"), ("Brunch insolite en bulle", "/experiences/brunch-en-bulle.html")]),
     faq_schema([
        ("Combien de personnes peut accueillir le brunch ?", "Jusqu'à 6 convives dans une même bulle ; pour un groupe plus grand, un format sur-mesure est possible."),
        ("Que comprend le brunch ?", "Un assortiment salé et sucré à partager, viennoiseries, produits frais et douceurs, servis dans la bulle."),
        ("Le brunch est-il adapté aux enfants ?", "Oui, le brunch se prête très bien à un moment en famille."),
     ])],
)

landing_page(
    "/experiences/sur-mesure.html",
    "Expérience sur-mesure en bulle — Bordeaux | Dans Ma Bulle",
    "Une expérience en bulle entièrement composée autour de votre occasion : décor, format et mise en scène personnalisés, au cœur des vignobles bordelais. Sur devis.",
    IMG + "table-deux-ciel-1600.webp",
    "Votre occasion, sa propre mise en scène",
    "Sur-mesure · Vignobles de Bordeaux",
    "Anniversaire, déclaration, fiançailles, célébration ou simple envie de marquer le coup : on compose l'expérience entièrement autour de vous, du décor au moindre détail.",
    ["Format adapté", "Décor personnalisé", "On imagine, vous validez"],
    IMG + "table-deux-ciel-1600.webp",
    [("Accueil", "/"), ("Sur-mesure", None)],
    "Quand l'occasion mérite son propre scénario.",
    "<p>Certaines occasions ne rentrent dans aucune case. On part de votre histoire, de l'émotion que vous voulez créer, et on bâtit l'expérience autour : la déco, l'ambiance, les surprises, le timing. Vous nous dites tout, on imagine, vous validez.</p>",
    "Ce qu'on peut composer",
    ["Décor et mise en scène entièrement personnalisés", "Format adapté à votre projet et au nombre de convives", "Attentions et surprises sur demande", "Un accompagnement de A à Z"],
    "Sur devis", "selon vos envies",
    IMG + "installation-800.webp",
    "Installation complète d'une bulle dressée pour une occasion spéciale",
    [
        ("Comment se passe un devis sur-mesure ?", "Vous nous racontez votre projet via le formulaire. On revient vers vous avec une proposition et un tarif adaptés, sans engagement."),
        ("Quel délai prévoir ?", "Plus vous anticipez, mieux c'est, surtout pour une mise en scène élaborée. Contactez-nous dès que la date est en tête."),
        ("Peut-on combiner plusieurs envies (déco, photographe, fleurs) ?", "Oui, on coordonne les détails et les prestations annexes selon votre projet."),
    ],
    [
        ("/occasions/demande-en-mariage.html", IMG + "mot-doux-800.webp", "Demande en mariage", "La mise en scène parfaite pour le grand oui."),
        ("/occasions/anniversaire.html", IMG + "brunch-ballons-800.webp", "Anniversaire", "Une fête intime dans une bulle rien qu'à vous."),
        ("/experiences/diner-en-bulle.html", IMG + "diner-vignes-crepuscule-800.webp", "Le Dîner romantique", "La base romantique, tout compris pour deux."),
    ],
    [{"@context": "https://schema.org", "@type": "Service", "name": "Expérience sur-mesure en bulle",
      "description": "Expérience en bulle personnalisée pour toute occasion, au cœur des vignobles bordelais.",
      "provider": {"@type": "LocalBusiness", "name": "Dans Ma Bulle"}, "areaServed": "Bordeaux", "url": SITE + "/experiences/sur-mesure.html"},
     breadcrumb_schema([("Accueil", "/"), ("Sur-mesure", "/experiences/sur-mesure.html")]),
     faq_schema([
        ("Comment se passe un devis sur-mesure ?", "Vous décrivez votre projet via le formulaire ; on revient avec une proposition et un tarif adaptés, sans engagement."),
        ("Quel délai prévoir ?", "Anticipez autant que possible, surtout pour une mise en scène élaborée."),
     ])],
)

# ================================================================ OCCASIONS
landing_page(
    "/occasions/demande-en-mariage.html",
    "Demande en mariage originale à Bordeaux : dîner en bulle dans les vignes | Dans Ma Bulle",
    "Une demande en mariage originale et inoubliable à Bordeaux : un dîner en bulle transparente dans les vignes, bougies, pétales et intimité totale. On met en scène votre oui.",
    IMG + "roses-intime-1600.webp",
    "Une demande en mariage qu'elle n'oubliera jamais",
    "Demande en mariage · Bordeaux",
    "Le décor parfait pour poser LA question : une bulle transparente posée dans les vignes, des bougies, des pétales, et le monde entier qui s'efface le temps d'un instant suspendu.",
    ["Intimité totale", "Mise en scène", "Au cœur des vignes"],
    IMG + "roses-intime-1600.webp",
    [("Accueil", "/"), ("Occasions", "/#occasions"), ("Demande en mariage", None)],
    "Le lieu dont elle se souviendra en premier.",
    "<p>On dit que le lieu d'une demande est ce dont on se souvient le plus. Une bulle transparente dans les vignes au coucher du soleil, c'est un décor qui se passe de filtre et de discours. On installe la table, les bougies, les pétales, la petite attention qui fait monter l'émotion. Vous n'avez plus qu'à vous lancer.</p>",
    "Ce qu'on met en place",
    ["Bulle dressée et décorée pour l'occasion", "Ambiance romantique : bougies, pétales, lumière douce", "Attentions et surprises personnalisées", "Discrétion totale pour préserver l'effet de surprise"],
    "Sur devis", "à composer ensemble",
    IMG + "mot-doux-800.webp",
    "Mot doux et décor romantique préparés dans la bulle pour une demande en mariage",
    [
        ("Pouvez-vous garder la surprise jusqu'au bout ?", "C'est notre métier. On cale tout avec vous en amont et on s'occupe de l'installation pour que votre moitié ne se doute de rien."),
        ("Peut-on ajouter un photographe ou des fleurs ?", "Oui, on coordonne les prestations annexes (photographe, fleurs, champagne) selon votre projet."),
        ("Et si la météo s'annonce mauvaise ?", "La bulle est fermée et abritée : pluie ou fraîcheur, le moment est préservé. En cas de météo extrême, on s'adapte avec vous."),
        ("Combien de temps à l'avance faut-il réserver ?", "Anticipez dès que la date est en tête, surtout en haute saison, pour qu'on ait le temps de tout fignoler."),
    ],
    [
        ("/experiences/diner-en-bulle.html", IMG + "diner-vignes-crepuscule-800.webp", "Le Dîner romantique", "La base du moment : tout compris pour deux."),
        ("/occasions/saint-valentin.html", IMG + "table-deux-ciel-800.webp", "Saint-Valentin", "Un tête-à-tête loin des restaurants bondés."),
        ("/carte-cadeau.html", IMG + "detail-livre-800.webp", "Carte cadeau", "Offrir l'expérience à deux amoureux."),
    ],
    [{"@context": "https://schema.org", "@type": "Service", "name": "Demande en mariage en bulle à Bordeaux",
      "description": "Mise en scène d'une demande en mariage dans une bulle transparente au cœur des vignobles bordelais.",
      "provider": {"@type": "LocalBusiness", "name": "Dans Ma Bulle"}, "areaServed": "Bordeaux", "url": SITE + "/occasions/demande-en-mariage.html"},
     breadcrumb_schema([("Accueil", "/"), ("Occasions", "/#occasions"), ("Demande en mariage", "/occasions/demande-en-mariage.html")]),
     faq_schema([
        ("Pouvez-vous garder la surprise ?", "Oui, tout est calé en amont et on s'occupe de l'installation pour préserver l'effet de surprise."),
        ("Et si la météo est mauvaise ?", "La bulle est fermée et abritée ; le moment est préservé par tous les temps."),
        ("Peut-on ajouter un photographe ?", "Oui, les prestations annexes comme un photographe ou des fleurs sont possibles."),
     ])],
)

landing_page(
    "/occasions/anniversaire.html",
    "Anniversaire original à Bordeaux : brunch ou dîner en bulle dans les vignes | Dans Ma Bulle",
    "Fêter un anniversaire autrement à Bordeaux : un brunch ou un dîner dans une bulle transparente au cœur des vignes, à deux ou entre proches. Un souvenir, pas juste une fête.",
    IMG + "brunch-ballons-1600.webp",
    "Un anniversaire qu'on raconte encore",
    "Anniversaire · Bordeaux",
    "Soufflez vos bougies autrement : dans une bulle transparente posée au cœur des vignes, à deux ou entre proches, autour d'une table que personne n'oubliera.",
    ["À deux ou en groupe", "Brunch ou dîner", "Décor festif"],
    IMG + "brunch-ballons-1600.webp",
    [("Accueil", "/"), ("Occasions", "/#occasions"), ("Anniversaire", None)],
    "Marquer le coup, pour de vrai.",
    "<p>Un anniversaire mérite mieux qu'un énième restaurant. Dans une bulle rien qu'à vous, on installe le décor festif, la table gourmande et l'ambiance qui transforme un repas en souvenir. En amoureux pour un anniversaire de couple, ou entre proches pour fêter l'année qui passe.</p>",
    "Ce qu'on met en place",
    ["Bulle dressée et décorée pour la fête", "Brunch ou dîner gourmand au choix", "Touches festives : ballons, attentions, surprises", "Format à deux ou entre proches"],
    "Sur devis", "selon la formule et le nombre",
    IMG + "brunch-table-800.webp",
    "Table de brunch dressée avec ballons pour un anniversaire dans la bulle",
    [
        ("Combien de personnes peut-on inviter ?", "Jusqu'à 6 convives pour le format brunch. Pour un groupe plus grand, parlons-en, on s'adapte."),
        ("Peut-on personnaliser la déco aux couleurs de la fête ?", "Oui, dites-nous le thème et l'ambiance souhaitée, on compose autour."),
        ("Brunch ou dîner, que choisir ?", "Les deux fonctionnent. Le brunch pour un moment lumineux en journée, le dîner pour une ambiance plus intime au coucher du soleil."),
    ],
    [
        ("/experiences/brunch-en-bulle.html", IMG + "brunch-table-800.webp", "Le Brunch en bulle", "Jusqu'à 6 convives, dès 55€/personne."),
        ("/experiences/diner-en-bulle.html", IMG + "diner-vignes-crepuscule-800.webp", "Le Dîner romantique", "Pour un anniversaire de couple à deux."),
        ("/carte-cadeau.html", IMG + "detail-livre-800.webp", "Carte cadeau", "Offrir l'expérience pour un anniversaire."),
    ],
    [{"@context": "https://schema.org", "@type": "Service", "name": "Anniversaire en bulle à Bordeaux",
      "description": "Brunch ou dîner d'anniversaire dans une bulle transparente au cœur des vignobles bordelais.",
      "provider": {"@type": "LocalBusiness", "name": "Dans Ma Bulle"}, "areaServed": "Bordeaux", "url": SITE + "/occasions/anniversaire.html"},
     breadcrumb_schema([("Accueil", "/"), ("Occasions", "/#occasions"), ("Anniversaire", "/occasions/anniversaire.html")]),
     faq_schema([
        ("Combien de personnes peut-on inviter ?", "Jusqu'à 6 convives pour le brunch ; un format plus grand est possible sur demande."),
        ("Peut-on personnaliser la déco ?", "Oui, la décoration s'adapte au thème et à l'ambiance souhaitée."),
     ])],
)

landing_page(
    "/occasions/saint-valentin.html",
    "Saint-Valentin à Bordeaux : dîner romantique en bulle dans les vignes | Dans Ma Bulle",
    "Une Saint-Valentin loin des restaurants bondés : un dîner romantique dans une bulle transparente au cœur des vignes bordelaises, en tête-à-tête sous les étoiles.",
    IMG + "diner-vignes-crepuscule-1600.webp",
    "Une Saint-Valentin loin de la foule",
    "Saint-Valentin · Bordeaux",
    "Le 14 février mérite mieux qu'un restaurant bondé et une table collée aux voisins. Un tête-à-tête dans une bulle transparente posée dans les vignes, rien que vous deux sous les étoiles.",
    ["En tête-à-tête", "Sous les étoiles", "À l'abri, au chaud"],
    IMG + "diner-vignes-crepuscule-1600.webp",
    [("Accueil", "/"), ("Occasions", "/#occasions"), ("Saint-Valentin", None)],
    "Le tête-à-tête, version inoubliable.",
    "<p>La Saint-Valentin au restaurant, c'est souvent bruyant et sans surprise. Dans une bulle rien qu'à vous, c'est une autre histoire : la table dressée, les bougies, les vignes et le silence. Un cocon chaud et romantique, même quand il fait froid dehors. Le cadre idéal pour se retrouver vraiment.</p>",
    "Ce qui est compris",
    ["Bulle transparente dressée et décorée pour deux", "Dîner gourmand romantique", "Ambiance bougies et lumière douce", "2h30 d'intimité, sous les étoiles"],
    "180€", "tout compris, pour deux",
    IMG + "roses-intime-800.webp",
    "Dîner de Saint-Valentin aux bougies dans une bulle transparente",
    [
        ("Faut-il réserver tôt pour le 14 février ?", "Oui, la Saint-Valentin part vite. Réservez le plus tôt possible pour être sûr d'avoir votre bulle."),
        ("Fait-il assez chaud en février ?", "La bulle est fermée et chauffée : on y est confortablement installé même en plein hiver, avec la vue en plus."),
        ("Peut-on ajouter une surprise (fleurs, demande) ?", "Oui, dites-nous votre projet, on ajoute les attentions et on peut même mettre en scène une demande."),
    ],
    [
        ("/experiences/diner-en-bulle.html", IMG + "diner-vignes-crepuscule-800.webp", "Le Dîner romantique", "Le même tête-à-tête, toute l'année."),
        ("/occasions/demande-en-mariage.html", IMG + "mot-doux-800.webp", "Demande en mariage", "Et si la Saint-Valentin devenait LE jour ?"),
        ("/carte-cadeau.html", IMG + "detail-livre-800.webp", "Carte cadeau", "Offrir le moment plutôt qu'un bouquet."),
    ],
    [{"@context": "https://schema.org", "@type": "Service", "name": "Dîner de Saint-Valentin en bulle à Bordeaux",
      "description": "Dîner romantique de Saint-Valentin dans une bulle transparente au cœur des vignobles bordelais.",
      "provider": {"@type": "LocalBusiness", "name": "Dans Ma Bulle"}, "areaServed": "Bordeaux", "url": SITE + "/occasions/saint-valentin.html"},
     breadcrumb_schema([("Accueil", "/"), ("Occasions", "/#occasions"), ("Saint-Valentin", "/occasions/saint-valentin.html")]),
     faq_schema([
        ("Faut-il réserver tôt pour le 14 février ?", "Oui, la Saint-Valentin part vite ; réservez le plus tôt possible."),
        ("Fait-il assez chaud en février ?", "La bulle est fermée et chauffée, confortable même en plein hiver."),
     ])],
)

# ================================================================ CARTE CADEAU
landing_page(
    "/carte-cadeau.html",
    "Carte cadeau : offrir un dîner ou un brunch en bulle — Bordeaux | Dans Ma Bulle",
    "Offrez une expérience inoubliable plutôt qu'un objet : une carte cadeau Dans Ma Bulle pour un brunch ou un dîner en bulle dans les vignes bordelaises.",
    IMG + "detail-livre-1600.webp",
    "Offrez un souvenir, pas un objet",
    "Carte cadeau · Bordeaux",
    "Anniversaire, Noël, remerciement ou simple envie de faire plaisir : offrez un moment dans une bulle au cœur des vignes. À eux de choisir la date, à vous le plaisir de la surprise.",
    ["Toutes les formules", "Validité souple", "La surprise garantie"],
    IMG + "detail-livre-1600.webp",
    [("Accueil", "/"), ("Carte cadeau", None)],
    "Le cadeau dont on se souvient.",
    "<p>Un objet finit dans un placard. Un moment, lui, reste. La carte cadeau Dans Ma Bulle, c'est l'assurance d'offrir une parenthèse rare : un brunch entre proches ou un dîner en amoureux dans une bulle posée face aux vignes. Vous choisissez la formule ou le montant, on s'occupe du reste.</p>",
    "Comment ça marche",
    ["Choisissez une formule ou un montant", "On vous envoie une jolie carte à offrir", "Les bénéficiaires réservent la date qui leur convient", "Il ne reste plus qu'à profiter"],
    "Sur demande", "selon la formule choisie",
    IMG + "detail-livre-800.webp",
    "Carte cadeau et coffret présentés dans la bulle",
    [
        ("Quelle est la durée de validité ?", "On cale une validité confortable avec vous lors de la commande. Dites-nous si c'est pour une occasion précise."),
        ("Peut-on offrir un montant libre ?", "Oui, vous pouvez offrir une formule précise ou un montant au choix, à compléter librement par les bénéficiaires."),
        ("Comment reçoit-on la carte ?", "On vous transmet une carte à offrir. Contactez-nous pour les détails et les délais."),
    ],
    [
        ("/experiences/diner-en-bulle.html", IMG + "diner-vignes-crepuscule-800.webp", "Le Dîner romantique", "Le cadeau parfait pour un couple."),
        ("/experiences/brunch-en-bulle.html", IMG + "brunch-table-800.webp", "Le Brunch en bulle", "À offrir entre amis ou en famille."),
        ("/occasions/demande-en-mariage.html", IMG + "mot-doux-800.webp", "Demande en mariage", "Pour des amoureux prêts à se lancer."),
    ],
    [offer_schema("Carte cadeau Dans Ma Bulle", "Carte cadeau pour un brunch ou un dîner en bulle dans les vignobles bordelais.", None, "/carte-cadeau.html"),
     breadcrumb_schema([("Accueil", "/"), ("Carte cadeau", "/carte-cadeau.html")]),
     faq_schema([
        ("Quelle est la durée de validité ?", "Une validité confortable est calée avec vous lors de la commande."),
        ("Peut-on offrir un montant libre ?", "Oui, une formule précise ou un montant au choix sont possibles."),
     ])],
)

print("Pages internes générées.")
