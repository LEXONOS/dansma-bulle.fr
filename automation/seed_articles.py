# -*- coding: utf-8 -*-
"""Crée les articles initiaux du journal et reconstruit l'index + le sitemap."""
import os
import blog

IMG = "/assets/images/"

A1_BODY = """
<p><strong>Pour un moment à deux vraiment mémorable à Bordeaux, le plus simple est de sortir des sentiers battus :</strong> troquer le restaurant classique contre une expérience qui surprend, qui dépayse et qui se raconte longtemps après. Voici nos idées préférées pour une sortie romantique autour de Bordeaux, de la plus connue à la plus insolite.</p>

<h2>Un dîner dans une bulle transparente au cœur des vignes</h2>
<p>C'est sans doute l'idée la plus marquante de cette liste. Imaginez une bulle transparente posée face aux vignes, une table dressée pour deux, des bougies et le ciel pour seul décor. On profite du plein air tout en étant à l'abri et au chaud, en toute saison. C'est exactement ce que propose <a href="/experiences/diner-en-bulle.html">notre dîner romantique en bulle</a> : une parenthèse de 2h30 rien qu'à vous, tout compris. Parfait pour un anniversaire de couple, une déclaration ou simplement pour se retrouver.</p>

<h2>Une balade au coucher du soleil sur les quais</h2>
<p>Les quais de la Garonne au coucher du soleil restent un classique imbattable. Du Miroir d'eau au pont de pierre, la lumière de fin de journée transforme la ville. À combiner avec un verre en terrasse pour prolonger le moment.</p>

<h2>Une dégustation en amoureux dans un château</h2>
<p>On ne visite pas Bordeaux sans goûter à son vignoble. Une dégustation à deux dans un château du Médoc ou de Saint-Émilion, c'est l'occasion d'apprendre, de partager et de repartir avec une jolie bouteille. Beaucoup de domaines proposent des formules intimistes.</p>

<h2>Un brunch insolite pour les amoureux du matin</h2>
<p>Tout le monde n'est pas du soir. Pour un week-end qui démarre en douceur, <a href="/experiences/brunch-en-bulle.html">un brunch dans une bulle</a> au calme des vignes change tout : viennoiseries, produits frais et douceurs à partager, loin des cafés bondés.</p>

<h2>Comparatif rapide</h2>
<table>
<thead><tr><th>Idée</th><th>Ambiance</th><th>Idéal pour</th></tr></thead>
<tbody>
<tr><td>Dîner en bulle</td><td>Intime, magique</td><td>Anniversaire, demande, retrouvailles</td></tr>
<tr><td>Balade sur les quais</td><td>Romantique, libre</td><td>Premier rendez-vous, soirée simple</td></tr>
<tr><td>Dégustation au château</td><td>Découverte, conviviale</td><td>Amateurs de vin</td></tr>
<tr><td>Brunch en bulle</td><td>Lumineuse, gourmande</td><td>Grasse matinée à deux</td></tr>
</tbody>
</table>

<p>Si vous cherchez l'option qui sort vraiment de l'ordinaire, la bulle dans les vignes coche toutes les cases : le cadre, l'intimité et le souvenir. Et pour une grande occasion, jetez un œil à notre page dédiée à la <a href="/occasions/demande-en-mariage.html">demande en mariage</a>.</p>
"""

A2_BODY = """
<p><strong>Pour une demande en mariage originale à Bordeaux, le lieu compte autant que les mots :</strong> c'est ce dont votre moitié se souviendra en premier. Plutôt qu'un restaurant classique, misez sur un décor qui crée l'émotion et préserve l'intimité. Voici nos pistes, et la mise en scène que nous préférons.</p>

<h2>Pourquoi le cadre fait tout</h2>
<p>Une demande réussie, c'est une bulle de temps suspendu, sans regards extérieurs ni interruption. Le vignoble bordelais au coucher du soleil offre un décor naturel difficile à battre : les rangs de vignes, la lumière dorée, le calme de la campagne à quelques minutes de la ville.</p>

<h2>Notre idée préférée : la demande dans une bulle transparente</h2>
<p>Une bulle transparente posée dans les vignes, des bougies, des pétales, une table dressée pour deux : le décor parfait pour poser LA question. On installe tout en amont et en toute discrétion, pour que votre partenaire ne se doute de rien. C'est précisément ce que nous mettons en scène avec <a href="/occasions/demande-en-mariage.html">notre expérience demande en mariage</a>, et que vous pouvez prolonger par <a href="/experiences/diner-en-bulle.html">un dîner romantique tout compris</a>.</p>

<h2>Les détails qui font la différence</h2>
<ul>
<li>Une attention personnelle : un mot, une photo, une musique qui vous est propre.</li>
<li>La météo anticipée : une bulle fermée et abritée met votre moment à l'abri de la pluie.</li>
<li>Un photographe discret pour immortaliser le oui, si vous le souhaitez.</li>
<li>Le timing : viser la lumière de fin de journée sur les vignes.</li>
</ul>

<h2>Combien de temps à l'avance s'y prendre ?</h2>
<p>Plus vous anticipez, mieux c'est, surtout au printemps et à l'automne où les dates partent vite. Comptez idéalement plusieurs semaines pour caler la mise en scène et les prestations annexes.</p>

<p>Envie d'en faire un moment inoubliable ? Découvrez notre <a href="/occasions/demande-en-mariage.html">page demande en mariage</a> et dites-nous tout : on imagine, vous validez.</p>
"""

POSTS = [
    {
        "slug": "que-faire-a-bordeaux-en-amoureux",
        "title": "Que faire à Bordeaux en amoureux : 8 idées romantiques (dont une bulle dans les vignes)",
        "description": "Nos idées de sorties romantiques à Bordeaux : dîner insolite en bulle dans les vignes, balade au coucher du soleil, dégustation au château, brunch original. De quoi surprendre votre moitié.",
        "category": "Idées sorties",
        "date": "2026-06-16",
        "image": IMG + "diner-vignes-crepuscule-1600.webp",
        "keyword": "que faire à Bordeaux en amoureux",
        "takeaways": [
            "L'option la plus marquante : un dîner en bulle transparente au cœur des vignes.",
            "Des classiques qui marchent toujours : quais au coucher du soleil, dégustation au château.",
            "Pour une grande occasion, pensez à une mise en scène dédiée.",
        ],
        "faqs": [
            ("Quelle est l'activité la plus romantique à faire à Bordeaux ?", "Un dîner en tête-à-tête dans une bulle transparente posée dans les vignes figure parmi les expériences les plus marquantes : intimité totale, décor naturel et souvenir garanti."),
            ("Que faire à Bordeaux en amoureux quand il pleut ?", "Optez pour une expérience abritée comme une bulle fermée et chauffée, où l'on profite de la vue sur les vignes tout en restant au sec et au chaud."),
        ],
        "body": A1_BODY,
    },
    {
        "slug": "demande-en-mariage-originale-bordeaux",
        "title": "Demande en mariage originale à Bordeaux : nos idées pour un oui inoubliable",
        "description": "Où et comment faire une demande en mariage originale à Bordeaux : l'idée du dîner en bulle dans les vignes, les détails qui font la différence et le bon timing pour tout réussir.",
        "category": "Demande en mariage",
        "date": "2026-06-19",
        "image": IMG + "roses-intime-1600.webp",
        "keyword": "demande en mariage originale Bordeaux",
        "takeaways": [
            "Le lieu compte autant que les mots : misez sur l'intimité et l'émotion.",
            "Notre favori : une demande dans une bulle transparente dans les vignes.",
            "Anticipez plusieurs semaines, surtout au printemps et à l'automne.",
        ],
        "faqs": [
            ("Où faire une demande en mariage originale près de Bordeaux ?", "Le vignoble bordelais au coucher du soleil est un décor idéal. Une bulle transparente dressée dans les vignes offre intimité, romantisme et un souvenir unique."),
            ("Peut-on garder la surprise jusqu'au bout ?", "Oui : l'installation se fait en amont et en toute discrétion pour que votre partenaire ne se doute de rien."),
        ],
        "body": A2_BODY,
    },
]

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    posts = []
    for p in POSTS:
        html = blog.render_article_page(p, p["body"])
        out = os.path.join(blog.ROOT, "blog", f"{p['slug']}.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        print("  article écrit:", p["slug"])
        # métadonnées (sans le corps) pour le manifeste
        meta = {k: p[k] for k in ("slug", "title", "description", "category", "date", "image", "keyword")}
        posts.append(meta)
    blog.save_posts(posts)
    blog.build_index(posts)
    blog.build_sitemap(posts)
    print("Articles initiaux OK.")

if __name__ == "__main__":
    main()
