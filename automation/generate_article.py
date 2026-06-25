# -*- coding: utf-8 -*-
"""
Génère automatiquement un article de blog Dans Ma Bulle.
- Choisit le prochain sujet non utilisé dans topics.json
- Demande à l'API Anthropic un article structuré (règles SEO + GEO appliquées)
- Garde-fou qualité (longueur, tableau, FAQ, liens internes)
- Rend la page via blog.render_article_page, met à jour posts.json + index + sitemap
- Marque le sujet comme utilisé UNIQUEMENT si tout a réussi

Variables d'environnement : ANTHROPIC_API_KEY (obligatoire).
Usage : python automation/generate_article.py
"""
import os, re, json, sys, datetime, unicodedata
import urllib.request
import blog

MODEL = "claude-sonnet-4-6"          # modèle API (modifiable)
MAX_TOKENS = 4000
HERE = os.path.dirname(os.path.abspath(__file__))
TOPICS = os.path.join(HERE, "topics.json")

# Images de couverture par catégorie (rotation pour varier)
COVER = {
    "Idées sorties": ["bulle-nuit", "dome-jour", "guitare-vin", "table-deux-ciel"],
    "Demande en mariage": ["roses-intime", "mot-doux", "diner-vignes-crepuscule"],
    "Anniversaire": ["brunch-ballons", "brunch-table", "installation"],
    "Saint-Valentin": ["diner-vignes-crepuscule", "roses-intime", "table-deux-ciel"],
    "Brunch": ["brunch-table", "brunch-vue-dessus", "gourmand-detail"],
    "Dîner romantique": ["diner-vignes-crepuscule", "roses-intime", "table-deux-bois"],
    "Cadeau": ["detail-livre", "mot-doux", "dome-jour"],
}
DEFAULT_COVERS = ["dome-jour", "bulle-nuit", "table-deux-ciel", "guitare-vin"]

def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9\s-]", "", text).strip().lower()
    return re.sub(r"[\s-]+", "-", text)[:70]

def pick_cover(category, slug):
    pool = COVER.get(category, DEFAULT_COVERS)
    idx = sum(ord(c) for c in slug) % len(pool)
    return f"/assets/images/{pool[idx]}-1600.webp"

def extract_json(text):
    """Extraction robuste du bloc JSON renvoyé par le modèle."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(json)?", "", text).rsplit("```", 1)[0]
    start = text.find("{"); end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("Pas de JSON trouvé")
    return json.loads(text[start:end + 1])

def call_anthropic(prompt):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("ERREUR : ANTHROPIC_API_KEY manquant.")
    payload = json.dumps({
        "model": MODEL, "max_tokens": MAX_TOKENS,
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=payload,
        headers={"x-api-key": key, "anthropic-version": "2023-06-01",
                 "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.loads(r.read())
    return "".join(b.get("text", "") for b in data.get("content", []))

def build_prompt(topic):
    return f"""Tu es rédacteur SEO et GEO expert pour Dans Ma Bulle, une expérience de brunch et dîner dans une bulle transparente, au cœur des vignobles bordelais (à deux ou jusqu'à 6 convives, 2h30, tout compris).

Rédige un article de blog en français qui vise le mot-clé : "{topic['keyword']}".
Catégorie : {topic['category']}.

RÈGLES STRICTES (SEO + GEO) :
- 700 à 1000 mots, français naturel, ton chaleureux et concret, sans langue de bois.
- AUCUN tiret cadratin (—). Pas d'emojis.
- La TOUTE PREMIÈRE phrase du corps doit répondre directement à l'intention de recherche, de façon extractible par une IA (commence par une affirmation claire, en gras avec <strong>).
- Titres de section en <h2> formulés si possible en question.
- Inclure au moins UN tableau comparatif HTML pertinent.
- Inclure 2 à 3 liens internes vers ces pages quand c'est naturel : /experiences/diner-en-bulle.html, /experiences/brunch-en-bulle.html, /occasions/demande-en-mariage.html, /occasions/saint-valentin.html, /carte-cadeau.html.
- Corps en HTML simple : <p>, <h2>, <h3>, <ul><li>, <table>, <strong>, <a href>. Pas de <html>, <head>, <h1>, ni styles.
- Rester honnête et utile : pas de remplissage.

Réponds UNIQUEMENT avec un objet JSON valide, sans texte autour, au format :
{{
  "title": "titre accrocheur avec le mot-clé, 55-65 caractères",
  "description": "méta description 140-155 caractères avec le mot-clé et un bénéfice",
  "takeaways": ["3 points clés", "courts", "actionnables"],
  "faqs": [["Question 1 ?", "Réponse courte et factuelle."], ["Question 2 ?", "Réponse."]],
  "body_html": "le corps complet de l'article en HTML"
}}"""

def quality_ok(art):
    body = art.get("body_html", "")
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    checks = {
        "longueur >= 550 mots": words >= 550,
        "contient un tableau": "<table" in body,
        "contient des H2": body.count("<h2") >= 2,
        "au moins 1 lien interne": ("/experiences/" in body or "/occasions/" in body or "/carte-cadeau" in body),
        "2 FAQ minimum": isinstance(art.get("faqs"), list) and len(art["faqs"]) >= 2,
        "3 takeaways": isinstance(art.get("takeaways"), list) and len(art["takeaways"]) >= 3,
        "titre present": bool(art.get("title")),
        "description present": bool(art.get("description")),
    }
    failed = [k for k, v in checks.items() if not v]
    return (len(failed) == 0), failed, words

def main():
    os.chdir(HERE)
    topics = json.load(open(TOPICS, encoding="utf-8"))
    pending = [t for t in topics if not t.get("used")]
    if not pending:
        print("Plus aucun sujet disponible dans topics.json."); return
    topic = pending[0]
    print(f"Sujet : {topic['keyword']} ({topic['category']})")

    art = extract_json(call_anthropic(build_prompt(topic)))
    ok, failed, words = quality_ok(art)
    print(f"Mots : {words} | Qualité : {'OK' if ok else 'ÉCHEC'}")
    if not ok:
        sys.exit("Article rejeté par le garde-fou qualité : " + ", ".join(failed))

    slug = slugify(art["title"])
    meta = {
        "slug": slug, "title": art["title"], "description": art["description"],
        "category": topic["category"], "date": datetime.date.today().isoformat(),
        "image": pick_cover(topic["category"], slug), "keyword": topic["keyword"],
        "takeaways": art["takeaways"], "faqs": [tuple(f) for f in art["faqs"]],
    }
    html = blog.render_article_page(meta, art["body_html"])
    out = os.path.join(blog.ROOT, "blog", f"{slug}.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(html)
    print("Article écrit :", out)

    # manifeste (sans takeaways/faqs/corps)
    posts = blog.load_posts()
    if not any(p["slug"] == slug for p in posts):
        posts.append({k: meta[k] for k in ("slug", "title", "description", "category", "date", "image", "keyword")})
    blog.save_posts(posts)
    blog.build_index(posts)
    blog.build_sitemap(posts)

    # marquer le sujet utilisé seulement maintenant
    topic["used"] = True
    topic["published"] = meta["date"]
    json.dump(topics, open(TOPICS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("Terminé. Sujet marqué comme publié.")

if __name__ == "__main__":
    main()
