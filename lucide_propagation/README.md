# Lucide — Propagation du retrait des sources nominatives

**Date :** 3 mai 2026
**Destinataire :** Claude Code
**Niveau :** Modification éditoriale ciblée, deux fichiers à corriger

## Décision éditoriale

David, l'éditeur de Lucide, a décidé de **retirer toutes les références
nominatives à des chercheurs et à des bases scientifiques** des supports
publics. Cette décision protège l'avantage stratégique de la sélection
bibliographique de Lucide.

Concrètement, les noms suivants ne doivent **plus apparaître** sur le
site lucide.health, dans l'app, ni dans la fiche App Store :

- McCabe-Sellers
- Walker
- Shulman
- Gillman
- Van den Eynde
- Hanington
- USDA (National Nutrient Database)
- ANSES Ciqual
- EFSA Journal
- Journal of Food Composition and Analysis
- Journal of Clinical Psychiatry
- Journal of Clinical Psychopharmacology
- Journal of Neural Transmission

Ce qui les remplace : la formule **« plusieurs dizaines de références
scientifiques publiques »** dans les 3 langues, sans donner de noms.

## Deux fichiers à modifier

```
1. website/sources.html       (page Sources du site)
2. App-main/i18n/{fr,en,ru}.json   (clé sourcesIntro de l'onglet Info)
```

## Modification 1 : page sources.html du site

Localiser le fichier `website/sources.html` (ou `sources.html` à la
racine si tu as livré sans sous-dossier). Le contenu actuel comprend
3 sections : Méthodologie générale, Sources principales, Contact.

### Section "Sources principales" : à supprimer

Supprimer **entièrement** la section `<h2>Sources principales</h2>`
ainsi que le paragraphe d'intro et la liste à puces (`<ul>` avec les
8 références).

### Section "Contact" : à supprimer

Supprimer **entièrement** la section `<h2>Contact</h2>` ainsi que son
paragraphe contenant `sources@lucide.health`. David ne souhaite pas
inciter aux demandes opportunistes. Les utilisateurs qui ont
réellement besoin de référence sauront utiliser l'email général
`contact@lucide.health` qui figure déjà dans le footer.

### Section "Méthodologie générale" : à enrichir

La section actuelle est conservée. Lui ajouter une phrase et une
sous-section pour valoriser le travail éditorial sans dévoiler le
contenu.

**Voici le contenu complet attendu de la nouvelle page sources.html :**

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Sources scientifiques · Lucide</title>
  <meta name="description" content="Méthodologie scientifique de la base d'aliments de Lucide." />
  <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..700&family=Public+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/styles.css" />
</head>
<body>
  <header>
    <a href="/" class="brand">
      <span class="brand-name">Lucide</span>
      <span class="brand-tagline">aide à la lecture des repas</span>
    </a>
  </header>

  <main>
    <h1>Sources scientifiques</h1>
    <p class="lead"><em>Dernière mise à jour : 30 avril 2026</em></p>

    <p>Lucide affiche des valeurs de tyramine pour plus de quatre cents aliments. Ces valeurs s'appuient sur plusieurs dizaines de références scientifiques publiques.</p>

    <h2>Méthodologie générale</h2>

    <p>Pour chaque aliment de Lucide, nous documentons une valeur médiane de teneur en tyramine en mg pour 100 g de produit. Lorsque la littérature rapporte une fourchette (souvent large pour les produits fermentés), nous retenons la médiane. Lorsque plusieurs sources convergent, nous privilégions les plus récentes et les plus rigoureuses méthodologiquement, avec une préférence pour les analyses par chromatographie liquide haute performance (HPLC) ou spectrométrie de masse en tandem (LC-MS/MS).</p>

    <p>La courbe théorique sur quatre heures repose sur un modèle pharmacocinétique simplifié dérivé des études de pression artérielle après ingestion de tyramine pure.</p>

    <h2>Une démarche éditoriale</h2>

    <p>Lucide se distingue par la rigueur de sa sélection bibliographique. Chaque aliment de la base a fait l'objet d'une vérification croisée entre plusieurs sources scientifiques avant intégration. Cette double vérification est ce qui nous permet de défendre la fiabilité de l'application au quotidien.</p>

    <p>Pour qu'un nouvel aliment soit ajouté à la base, votre proposition doit s'appuyer sur deux sources scientifiques concordantes issues de bases reconnues.</p>
  </main>

  <footer>
    <nav class="footer-nav">
      <a href="/">Accueil</a>
      <a href="/privacy">Confidentialité</a>
      <a href="/support">Support</a>
      <a href="/sources">Sources</a>
      <a href="/subscription">Abonnement</a>
    </nav>
    <p class="footer-legal">
      &copy; 2026 Valdoria · SIREN 983 729 146 ·
      <a href="mailto:contact@lucide.health">contact@lucide.health</a>
    </p>
  </footer>
</body>
</html>
```

## Modification 2 : i18n sourcesIntro de l'app

Localiser les trois fichiers `i18n/fr.json`, `i18n/en.json`, `i18n/ru.json`
dans le repo de l'app.

Trouver la clé `sourcesIntro` et la remplacer par les valeurs ci-dessous.

### `i18n/fr.json`

**Avant :**
```json
"sourcesIntro": "Données issues de la littérature publique. Les valeurs sont celles documentées et ne sont pas la valeur exacte de vos aliments."
```

**Après :**
```json
"sourcesIntro": "Les valeurs s'appuient sur plusieurs dizaines de références scientifiques publiques. Elles sont documentées et ne représentent pas la valeur exacte de vos aliments."
```

### `i18n/en.json`

**Avant :**
```json
"sourcesIntro": "Data drawn from the publicly available literature. The values are the documented ones, not the exact value of your specific food."
```

**Après :**
```json
"sourcesIntro": "Values are drawn from several dozens of publicly available scientific references. They are documented and do not represent the exact value of your specific food."
```

### `i18n/ru.json`

**Avant :**
```json
"sourcesIntro": "Данные из открытой научной литературы. Указанные значения являются документированными и не являются точным значением для вашего конкретного продукта."
```

**Après :**
```json
"sourcesIntro": "Значения опираются на несколько десятков научных источников из открытой литературы. Они документированы и не представляют точного значения для вашего конкретного продукта."
```

## Vérification finale

Après les deux modifications, lancer :

```bash
# Plus aucune référence nominative dans le repo de l'app
cd App-main
grep -rn "McCabe-Sellers\|Walker\|Shulman\|Gillman\|USDA\|ANSES\|EFSA\|Hanington\|Van den Eynde" \
  --include="*.json" --include="*.html" --include="*.js" --include="*.md" .
# Résultat attendu : aucun résultat (sauf éventuellement dans sources.js
# qui est le fichier de données interne, à conserver tel quel)

# Plus aucune référence nominative dans le site
cd ../website
grep -rn "McCabe-Sellers\|Walker\|Shulman\|Gillman\|USDA\|ANSES\|EFSA\|Hanington\|Van den Eynde" \
  --include="*.html" --include="*.md" .
# Résultat attendu : aucun résultat
```

## Important : `sources.js` à NE PAS modifier

Le fichier `sources.js` qui contient la base bibliographique réelle de
30 références est un fichier de données interne. **Il doit être conservé
tel quel dans le repo de l'app**. Il n'est pas affiché à l'utilisateur,
il sert juste de référence interne pour la documentation des aliments.

Toutefois, ce fichier est techniquement accessible à toute personne qui
inspecterait le code source d'une PWA via les DevTools du navigateur.
Pour atténuer ce risque, deux pistes possibles plus tard (hors périmètre
de ce correctif) :

1. **Minification agressive** du `sources.js` au build de production.
2. **Déplacement** des références complètes dans un fichier serveur non
   livré au client (mais cela complique la maintenance).

Pour l'instant, la modification ne porte que sur **les supports publics
visibles** (site, fiche App Store, onglet Info de l'app).

## Récapitulatif

| Fichier | Action |
|---|---|
| `website/sources.html` | Refonte complète selon le contenu fourni dans ce brief |
| `App-main/i18n/fr.json` | Modifier la clé `sourcesIntro` |
| `App-main/i18n/en.json` | Modifier la clé `sourcesIntro` |
| `App-main/i18n/ru.json` | Modifier la clé `sourcesIntro` |
| `App-main/sources.js` | NE PAS TOUCHER |

## Probité, rappel

David accorde une importance majeure à la probité. Les modifications
ci-dessus sont des consignes éditoriales fermes. Aucun ajout, aucun
retrait supplémentaire de soi-même. Si quelque chose paraît ambigu,
demander avant de modifier.
