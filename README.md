# Dans Ma Bulle — site vitrine

Landing page complète, responsive et animée pour Dans Ma Bulle (brunch et dîners
insolites en bulle transparente, vignobles de Bordeaux).

Site statique : HTML + CSS + JS, sans dépendance à un serveur. Prêt pour GitHub,
Vercel, puis OVH via FileZilla.

## Structure

```
dans-ma-bulle/
├── index.html          # la page (toutes les sections + le formulaire)
├── css/styles.css      # tout le design (charte, animations, responsive)
├── js/main.js          # interactions + envoi du formulaire
├── assets/
│   ├── logo.jpg        # le logo rond
│   └── images/         # tes photos (voir IMAGES.md)
├── favicon.svg
├── site.webmanifest
├── robots.txt
├── sitemap.xml
├── IMAGES.md           # carte des 14 emplacements d'images
└── README.md
```

## 1. Aperçu en local

Ouvre `index.html` dans un navigateur. Pour que tout marche à l'identique (polices,
formulaire), sers le dossier en local :

```
cd dans-ma-bulle
python3 -m http.server 8000
# puis ouvre http://localhost:8000
```

## 2. Mettre en ligne sur GitHub + Vercel

1. Crée un dépôt GitHub, pousse tout le dossier.
2. Sur vercel.com : New Project, importe le dépôt.
3. Framework Preset : **Other**. Aucune commande de build, dossier racine.
4. Deploy. Tu obtiens une URL d'aperçu en quelques secondes.

## 3. Mettre en ligne sur OVH (FileZilla)

1. Connecte-toi à ton FTP OVH avec FileZilla.
2. Envoie **le contenu** du dossier (pas le dossier lui-même) dans `www/`.
3. Le site est en ligne sur ton domaine. C'est du statique, rien d'autre à faire.

## 4. Activer le formulaire (important)

Par défaut, le formulaire ouvre la messagerie avec la demande pré-remplie. Pour
recevoir les demandes directement par email (sur Vercel ET OVH) :

1. Va sur https://web3forms.com, crée une clé gratuite avec `contact@dansma-bulle.fr`.
2. Ouvre `js/main.js`, tout en haut, remplace `VOTRE_CLE_WEB3FORMS` par ta clé.
3. C'est tout. Les demandes arrivent dans la boîte mail. Anti-spam (honeypot) déjà en place.

## 5. Tes images

Tout est dans **IMAGES.md** : les 14 emplacements, leur rôle, l'orientation idéale.
Deux façons de mettre tes photos :
- renomme tes fichiers selon les noms d'emplacements et dépose-les dans `assets/images/`,
  puis fais pointer chaque `src` vers `assets/images/NOM.jpg` ;
- ou colle directement l'URL de tes images dans le `src`.

## 6. Personnaliser

| Quoi | Où |
|---|---|
| Couleurs (charte) | `css/styles.css`, bloc `:root` en haut |
| Polices | balise `<link>` Google Fonts dans `<head>` + variables `--brush/--serif/--sans` |
| Tarifs / textes | directement dans `index.html` |
| Téléphone / email / Instagram | `index.html` (header, formulaire, footer) + `js/main.js` (constantes en haut) |
| Avis clients | section `temoignages` dans `index.html` (placeholders à remplacer par de vrais avis) |

## À confirmer avec toi

- **Tarifs** affichés : Romantique 180€ tout compris pour deux, Brunch 55€/pers
  (jusqu'à 6), Sur-Mesure sur devis. (L'ancien site indiquait Brunch 65€ / Dîner 90€.)
- **Lieu** : positionné en "vignobles de Bordeaux" (concept mobile/éphémère) plutôt
  que figé sur le Château Lauduc. Dis-moi si c'est encore Lauduc et je le verrouille.
- **Avis clients** : ceux en place sont des exemples, à remplacer avant la mise en ligne.
