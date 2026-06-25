# Dans Ma Bulle — site

Site vitrine statique multi-pages (HTML/CSS/JS, sans framework) + journal automatisé.
Pensé pour Cloudflare Pages : gratuit, déploiement automatique à chaque commit, zéro FTP.

## Structure

```
/
├── index.html                      Accueil
├── experiences/                    diner-en-bulle, brunch-en-bulle, sur-mesure
├── occasions/                      demande-en-mariage, anniversaire, saint-valentin
├── carte-cadeau.html
├── blog/                           index.html + articles (générés)
├── css/styles.css                  design partagé (charte)
├── js/main.js                      interactions + formulaire
├── assets/images/                  photos WebP (noms parlants)
├── assets/logo.jpg, favicon.svg
├── sitemap.xml, robots.txt, llms.txt, site.webmanifest
├── automation/                     moteur du journal
│   ├── build_pages.py              régénère les pages internes
│   ├── blog.py                     rendu article + index + sitemap
│   ├── generate_article.py         génère 1 article via l'API Anthropic
│   ├── seed_articles.py            articles de départ
│   └── topics.json                 file de mots-clés (45 sujets)
└── .github/workflows/blog.yml      publie 1 article (lun/mer/ven)
```

## Mettre en ligne (Cloudflare Pages, recommandé)

1. Pousse le dossier sur un dépôt GitHub.
2. Cloudflare dashboard > Workers & Pages > Create > Pages > Connect to Git.
3. Sélectionne le dépôt. Build command : VIDE. Build output directory : `/` (racine).
   (Le site est déjà du HTML statique, aucun build nécessaire.)
4. Deploy. Tu obtiens une URL en quelques secondes.
5. Domaine : dans Cloudflare Pages > Custom domains, ajoute dansma-bulle.fr, puis chez OVH
   pointe le DNS du domaine vers Cloudflare (CNAME/enregistrements fournis par Cloudflare).

Résultat : chaque `git push` redéploie automatiquement. Aucun FTP, aucun abonnement.

## Activer le formulaire

Le formulaire (page d'accueil) ouvre la messagerie par défaut. Pour recevoir les demandes
par email : crée une clé gratuite sur https://web3forms.com (avec contact@dansma-bulle.fr),
puis colle-la en haut de `js/main.js` à la place de `VOTRE_CLE_WEB3FORMS`.

## Activer le journal automatique

1. Dans le dépôt GitHub : Settings > Secrets and variables > Actions > New secret.
   Nom : `ANTHROPIC_API_KEY`. Valeur : ta clé API Anthropic.
2. C'est tout. Le workflow publie un article lundi, mercredi et vendredi (modifiable dans
   `.github/workflows/blog.yml`). Déclenchement manuel possible via l'onglet Actions.
3. Chaque article généré met à jour `blog/index.html` et `sitemap.xml`, et le commit
   redéploie le site via Cloudflare.

Garde-fou qualité : un article n'est publié que s'il respecte la longueur, contient un
tableau, des liens internes et une FAQ. Sinon le job échoue proprement (rien n'est publié).
Coût indicatif : ~0,20 à 0,30 € par article.

### Ajouter / modifier des sujets
Édite `automation/topics.json` (liste de mots-clés + catégorie). Les sujets non utilisés
sont traités dans l'ordre.

### Régénérer les pages internes après une modif de contenu
`cd` à la racine puis `python automation/build_pages.py` (expériences, occasions, carte cadeau)
et `python automation/blog.py` (index + sitemap).

## Tes images

Les photos sont dans `assets/images/` en WebP (deux largeurs : `-800` et `-1600`), nommées
par contenu (ex. `bulle-nuit`, `brunch-table`, `roses-intime`). Pour remplacer une image,
écrase le fichier WebP correspondant en gardant le même nom, ou change le chemin dans le HTML.

## À confirmer

- Tarifs affichés : Dîner 180€ tout compris pour deux, Brunch 55€/pers, Sur-mesure sur devis.
- Lieu : positionné "vignobles de Bordeaux" (concept mobile). À préciser si domaine fixe.
- Avis clients de la page d'accueil : exemples à remplacer par de vrais avis.
