IMAGES — Dans Ma Bulle
======================

Les photographies affichées sur le site sont, pour l'instant, servies
directement depuis le CDN d'origine (assets.zyrosite.com) via les URL
présentes dans les fichiers HTML. Elles s'affichent donc tant que vous
disposez d'une connexion internet, sans qu'aucun fichier image ne soit
embarqué dans cette archive.

POUR HÉBERGER VOS PROPRES IMAGES (recommandé à terme)
-----------------------------------------------------
1. Déposez vos fichiers (.jpg / .webp) dans ce dossier assets/images/.
2. Dans les fichiers .html, remplacez les URL commençant par
   https://assets.zyrosite.com/... par un chemin local, par exemple :
   - depuis index.html :            assets/images/votre-photo.jpg
   - depuis les pages de /pages/ :  ../assets/images/votre-photo.jpg
3. Conservez des attributs alt descriptifs pour le référencement et
   l'accessibilité, et privilégiez le format WebP pour la performance.

Astuce : gardez des images d'environ 1600 px de large pour les grands
visuels et 800 px pour les vignettes, afin d'allier qualité et rapidité.
