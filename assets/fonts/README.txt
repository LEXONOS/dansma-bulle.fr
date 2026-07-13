POLICES — Dans Ma Bulle
=======================

Le site utilise trois familles, chargées automatiquement depuis Google
Fonts (aucun fichier de police n'est nécessaire dans cette archive) :

- Fraunces        — titres et citations (serif douce, élégante)
- Hanken Grotesk  — textes courants et interface
- DM Mono         — données : prix, durées, étiquettes

Le chargement se fait via la balise <link> présente dans le <head> de
chaque page. Une connexion internet est donc requise pour afficher les
polices exactes ; à défaut, des polices système équivalentes prennent
le relais automatiquement.

POUR EMBARQUER LES POLICES EN LOCAL (optionnel)
-----------------------------------------------
1. Téléchargez les fichiers .woff2 des familles ci-dessus.
2. Placez-les dans ce dossier assets/fonts/.
3. Déclarez-les via des règles @font-face en haut de css/styles.css,
   puis retirez la balise <link> Google Fonts des fichiers .html.
