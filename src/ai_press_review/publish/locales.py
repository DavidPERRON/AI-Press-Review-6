"""Locale catalog for AI Press Review (English + French).

Each locale is a self-contained dict with everything templates need:
identity (title, subtitle, descriptions), URL paths, R2 audio prefix,
UI strings, six pillars (translated), and the full how-it-works copy.

Adding a new locale = adding a new key here + ensuring publish_episode
iterates over all locales.
"""
from __future__ import annotations

# ── Six editorial pillars ────────────────────────────────────────────────────

PILLARS_EN = [
    ("01", "AI News",
     "Verified announcements from labs, companies, institutions."),
    ("02", "Research & Breakthroughs",
     "Peer-reviewed publications and lab releases."),
    ("03", "Use Cases",
     "Documented enterprise and sector deployments."),
    ("04", "Tools & Practice",
     "Practitioner releases, APIs, frameworks."),
    ("05", "Weak Signals",
     "Early patterns not yet in mainstream coverage."),
    ("06", "Education",
     "Concepts and context for non-technical audiences."),
]

PILLARS_FR = [
    ("01", "Actualité IA",
     "Annonces vérifiées des labos, entreprises, institutions."),
    ("02", "Recherche & avancées",
     "Publications peer-reviewed et résultats de laboratoires."),
    ("03", "Cas d'usage",
     "Déploiements en entreprise documentés, par secteur."),
    ("04", "Outils & pratique",
     "Releases, APIs, frameworks utiles aux praticiens."),
    ("05", "Signaux faibles",
     "Patterns émergents avant qu'ils n'atteignent le mainstream."),
    ("06", "Pédagogie",
     "Concepts et contexte accessibles aux non-techniques."),
]

# ── Full locale dictionaries ─────────────────────────────────────────────────

LOCALES = {
    "en": {
        # Identity
        "lang": "en",
        "title": "AI Press Review",
        "subtitle": "40 sources. 15 minutes. What matters in AI today.",
        "description_short": "AI Press Review is a daily AI news briefing — 40+ sources, 15 minutes, weekday mornings.",
        "intro_paragraph": (
            "AI Press Review is a daily AI news briefing, "
            "published every morning at 7\u202fAM CET, Monday to Saturday. "
            "Each episode draws from 40+ weighted global sources."
        ),
        "tagline_note": "An editorial podcast \u00b7 Mon\u2013Sat, 7\u202fAM CET",
        # Path & R2
        "site_path": "",  # served at the site root
        "audio_prefix": "pressreview/",
        "feed_filename": "podcast-feed.xml",
        # UI labels
        "nav_home": "Home",
        "nav_how": "How it works",
        "nav_rss": "RSS",
        "nav_other_label": "Version française",
        "nav_other_path": "/fr/",
        "subscribe_label": "Subscribe",
        "subscribe_invite": "Subscribe via Apple, Spotify, YouTube, or RSS to be notified.",
        "first_episode_meta": "Coming soon",
        "first_episode_h": "First episode publishing within days.",
        "latest_episodes": "Latest episodes",
        "how_link_label": "How it works \u2192",
        "rss_link_label": "RSS \u2192",
        "transcript_link_label": "Transcript & episode page",
        "listen_label": "Listen",
        "sources_label": "Sources",
        "min_label": "min",
        "footer_hosted_by": "Hosted by",
        "footer_rss": "RSS feed",
        # Pillars block
        "pillars": PILLARS_EN,
        "pillars_heading": "Six editorial pillars",
        "pillars_subhead": "One continuous 14\u201318 minute briefing across all six.",
        # How it works page
        "how_page_title": "How it works — AI Press Review",
        "how_page_desc": "How AI Press Review selects, weights, and verifies sources. Editorial method behind the daily AI briefing.",
        "how_lead": (
            "40+ sources. 15 minutes. What matters in AI today. "
            "Here is exactly how each episode is built."
        ),
        "how_s01_num": "01 \u00b7 How episodes are structured",
        "how_s01_h": "Six pillars, one continuous narrative",
        "how_s01_p1": (
            "Each daily episode runs 14 to 18 minutes as a single continuous narrative "
            "across the six editorial pillars. No segments, no jingles between sections, "
            "no filler. The pillars themselves are listed on the home page."
        ),
        "how_s01_p2_strong": "Saturday weekly recap.",
        "how_s01_p2": (
            "The Saturday episode steps back from the daily news to identify the five "
            "trends that defined the week and flag what is likely to matter next week."
        ),
        "how_s02_num": "02 \u00b7 How sources are selected and weighted",
        "how_s02_h": "40+ sources, weighted by editorial standards",
        "how_s02_p1_strong": "40+ is a minimum threshold, not a target.",
        "how_s02_p1": (
            " Each episode draws from at least forty global sources gathered in the 12 "
            "hours preceding publication. Sources are not treated equally. Each carries "
            "a weight score based on editorial standards, domain authority, and "
            "primary-source proximity."
        ),
        "how_s02_th": ("Tier", "Weight", "Examples", "Rationale"),
        "how_s02_rows": [
            ("Primary / Official", "2.0\u00d7",
             "openai.com, deepmind.com, anthropic.com, arxiv.org",
             "Official announcements, peer-reviewed research"),
            ("Tier-1 Press", "1.5\u00d7",
             "reuters.com, ft.com, mit.edu, nature.com",
             "Editorial standards, original reporting"),
            ("Specialist Tech Press", "1.0\u00d7",
             "techcrunch.com, wired.com, venturebeat.com",
             "Industry coverage, verified editorially"),
        ],
        "how_s02_p2": (
            "Each episode's source manifest, with the actual domains and articles used, "
            "is published alongside the episode page."
        ),
        "how_s03_num": "03 \u00b7 What each episode covers",
        "how_s03_h": "The substance of each briefing",
        "how_s03_lead": "Daily episodes draw from concrete activity in artificial intelligence:",
        "how_s03_items": [
            ("Model releases and benchmarks.",
             " New models from frontier labs, capability shifts, comparative results that change the practitioner picture."),
            ("Enterprise deployments.",
             " Real implementations with measurable outcomes: cost, time, accuracy, scale. What worked, what didn't."),
            ("Infrastructure shifts.",
             " Chips, datacenters, cloud capacity, energy footprint. The plumbing that decides who can build what."),
            ("Open-source and tooling.",
             " APIs, frameworks, agents, and tools that change what a practitioner can do this week versus last week."),
            ("Research and breakthroughs.",
             " Peer-reviewed and lab-published work, translated for non-experts in 30 seconds."),
            ("Vertical applications.",
             " Finance, banking, healthcare, legal, consulting, public sector. AI where decisions actually get made."),
            ("Weak signals.",
             " Early patterns surfacing across multiple stories before they reach mainstream coverage."),
        ],
        "how_s04_num": "04 \u00b7 What we exclude, and why",
        "how_s04_items": [
            ("Regulatory speculation and policy rumors.",
             " Unverified regulatory moves produce noise that is almost always revised. We wait for official filings."),
            ("Unverified announcements without independent corroboration.",
             " If only one source carries a claim, it doesn't air."),
            ("Opinion and editorial commentary.",
             " AI Press Review reports what happened, not what commentators think about it. Interpretation is yours."),
            ("Funding rounds below $50M and pre-seed announcements.",
             " Capital events dominate AI coverage and crowd out operational signal."),
            ("Engagement-optimized content.",
             " Social media posts, thought-leadership, and content farms are excluded regardless of virality."),
        ],
        "how_s05_num": "05 \u00b7 About the host",
        "how_s05_tag": "Senior global trade solutions professional \u00b7 AI practitioner \u00b7 Paris",
        "how_s05_bio": (
            "Twenty years in front-office banking and trade finance at JPMorgan, Barclays "
            "and HSBC. Executive Master in Artificial Intelligence, Institut Mines-Télécom "
            "(2025). AI Press Review extends my daily professional practice of monitoring AI "
            "developments across finance, enterprise and research. The result is a format I "
            "would actually want to listen to. I am responsible for the editorial decisions, "
            "source weighting, and quality of every episode."
        ),
        "how_s06_num": "06 \u00b7 Feedback",
        "how_s06_h": "Feedback is welcome",
        "how_s06_p_template": (
            "If you spot a factual error, a source that should be excluded, or a domain "
            "underrepresented in coverage, write to <a href='mailto:{email}'>{email}</a>."
        ),
    },
    "fr": {
        # Identity
        "lang": "fr",
        "title": "Revue de Presse IA",
        "subtitle": "40 sources. 15 minutes. L'essentiel de l'IA chaque matin.",
        "description_short": "Revue de Presse IA — un briefing quotidien sur l'actualité IA, 40+ sources, 15 minutes, du lundi au samedi.",
        "intro_paragraph": (
            "La Revue de Presse IA est un briefing quotidien sur l'actualité de "
            "l'intelligence artificielle, publié chaque matin à 7\u202fh CET, "
            "du lundi au samedi. Chaque épisode s'appuie sur 40+ sources "
            "internationales pondérées."
        ),
        "tagline_note": "Un podcast éditorial \u00b7 Lun\u2013Sam, 7\u202fh CET",
        # Path & R2
        "site_path": "fr",
        "audio_prefix": "pressreview-fr/",
        "feed_filename": "podcast-feed.xml",
        # UI labels
        "nav_home": "Accueil",
        "nav_how": "Méthode",
        "nav_rss": "RSS",
        "nav_other_label": "English version",
        "nav_other_path": "/",
        "subscribe_label": "S'abonner",
        "subscribe_invite": "Abonnez-vous via Apple, Spotify, YouTube ou RSS pour être notifié.",
        "first_episode_meta": "Bientôt",
        "first_episode_h": "Premier épisode publié dans les jours qui viennent.",
        "latest_episodes": "Derniers épisodes",
        "how_link_label": "Méthode \u2192",
        "rss_link_label": "RSS \u2192",
        "transcript_link_label": "Transcription & page épisode",
        "listen_label": "Écouter",
        "sources_label": "Sources",
        "min_label": "min",
        "footer_hosted_by": "Animé par",
        "footer_rss": "Flux RSS",
        # Pillars block
        "pillars": PILLARS_FR,
        "pillars_heading": "Six piliers éditoriaux",
        "pillars_subhead": "Un récit continu de 14 à 18 minutes traversant les six piliers.",
        # How it works page
        "how_page_title": "Méthode — Revue de Presse IA",
        "how_page_desc": "Comment la Revue de Presse IA sélectionne, pondère et vérifie ses sources. La méthode éditoriale derrière le briefing quotidien.",
        "how_lead": (
            "40+ sources. 15 minutes. L'essentiel de l'IA aujourd'hui. "
            "Voici exactement comment chaque épisode est construit."
        ),
        "how_s01_num": "01 \u00b7 Comment chaque épisode est structuré",
        "how_s01_h": "Six piliers, un récit continu",
        "how_s01_p1": (
            "Chaque épisode quotidien dure 14 à 18 minutes, sous la forme d'un récit "
            "continu traversant les six piliers éditoriaux. Pas de segments, pas de "
            "jingles entre les sections, pas de remplissage. Les piliers eux-mêmes "
            "sont présentés sur la page d'accueil."
        ),
        "how_s01_p2_strong": "Récap hebdomadaire du samedi.",
        "how_s01_p2": (
            " L'épisode du samedi prend du recul pour identifier les cinq tendances "
            "qui ont marqué la semaine et signaler ce qui devrait compter la "
            "semaine suivante."
        ),
        "how_s02_num": "02 \u00b7 Comment les sources sont sélectionnées et pondérées",
        "how_s02_h": "40+ sources, pondérées selon des standards éditoriaux",
        "how_s02_p1_strong": "40+ est un seuil minimum, pas une cible.",
        "how_s02_p1": (
            " Chaque épisode s'appuie sur au moins quarante sources internationales "
            "collectées dans les 12 heures précédant la publication. Toutes les sources "
            "ne sont pas traitées de la même façon. Chacune reçoit un score de pondération "
            "fondé sur les standards éditoriaux, l'autorité du domaine et la proximité "
            "avec la source primaire."
        ),
        "how_s02_th": ("Niveau", "Pondération", "Exemples", "Justification"),
        "how_s02_rows": [
            ("Primaire / Officiel", "2.0\u00d7",
             "openai.com, deepmind.com, anthropic.com, arxiv.org",
             "Annonces officielles, recherche peer-reviewed"),
            ("Presse de référence", "1.5\u00d7",
             "reuters.com, ft.com, mit.edu, nature.com",
             "Standards éditoriaux, journalisme original"),
            ("Presse tech spécialisée", "1.0\u00d7",
             "techcrunch.com, wired.com, venturebeat.com",
             "Couverture sectorielle, vérifiée éditorialement"),
        ],
        "how_s02_p2": (
            "Le manifeste de sources de chaque épisode, avec les domaines et articles "
            "réellement utilisés, est publié à côté de la page épisode."
        ),
        "how_s03_num": "03 \u00b7 Ce que chaque épisode couvre",
        "how_s03_h": "La substance de chaque briefing",
        "how_s03_lead": "Les épisodes quotidiens s'appuient sur l'activité concrète de l'IA :",
        "how_s03_items": [
            ("Sorties de modèles et benchmarks.",
             " Nouveaux modèles des labos de pointe, sauts de capacité, résultats comparatifs qui changent la donne pour les praticiens."),
            ("Déploiements en entreprise.",
             " Implémentations réelles avec résultats mesurables : coût, temps, précision, échelle. Ce qui a fonctionné, ce qui n'a pas."),
            ("Évolutions d'infrastructure.",
             " Puces, datacenters, capacité cloud, empreinte énergétique. La plomberie qui décide qui peut construire quoi."),
            ("Open source et outillage.",
             " APIs, frameworks, agents, outils qui changent ce qu'un praticien peut faire cette semaine par rapport à la semaine dernière."),
            ("Recherche et avancées.",
             " Travaux peer-reviewed et publiés en labo, traduits pour les non-experts en 30 secondes."),
            ("Applications verticales.",
             " Finance, banque, santé, juridique, conseil, secteur public. L'IA là où les décisions se prennent réellement."),
            ("Signaux faibles.",
             " Patterns émergents repérés sur plusieurs stories avant qu'ils n'atteignent la couverture mainstream."),
        ],
        "how_s04_num": "04 \u00b7 Ce que nous excluons, et pourquoi",
        "how_s04_items": [
            ("Spéculations réglementaires et rumeurs politiques.",
             " Les manœuvres réglementaires non vérifiées produisent un bruit presque toujours révisé. Nous attendons les dépôts officiels."),
            ("Annonces non vérifiées sans corroboration indépendante.",
             " Si une seule source porte une affirmation, elle ne passe pas à l'antenne."),
            ("Opinion et commentaires éditoriaux.",
             " La Revue de Presse IA rapporte ce qui s'est passé, pas ce que les commentateurs en pensent. L'interprétation vous appartient."),
            ("Levées de fonds inférieures à 50 M$ et annonces pré-seed.",
             " Les événements de capital saturent la couverture IA et étouffent les signaux opérationnels."),
            ("Contenus optimisés pour l'engagement.",
             " Posts réseaux sociaux, thought leadership et fermes à contenu sont exclus quelle que soit leur viralité."),
        ],
        "how_s05_num": "05 \u00b7 À propos de l'animateur",
        "how_s05_tag": "Senior global trade solutions \u00b7 Praticien IA \u00b7 Paris",
        "how_s05_bio": (
            "Vingt ans en front-office banking et trade finance chez JPMorgan, Barclays "
            "et HSBC. Executive Master en Intelligence Artificielle, Institut Mines-Télécom "
            "(2025). La Revue de Presse IA prolonge ma pratique professionnelle quotidienne "
            "de veille IA dans les domaines de la finance, de l'entreprise et de la recherche. "
            "Le résultat est un format que j'aurais moi-même envie d'écouter. Je suis "
            "responsable des décisions éditoriales, de la pondération des sources et de la "
            "qualité de chaque épisode."
        ),
        "how_s06_num": "06 \u00b7 Retours",
        "how_s06_h": "Vos retours sont les bienvenus",
        "how_s06_p_template": (
            "Si vous repérez une erreur factuelle, une source à exclure ou un domaine "
            "sous-représenté dans la couverture, écrivez à "
            "<a href='mailto:{email}'>{email}</a>."
        ),
    },
}


ALL_LOCALES = list(LOCALES.keys())
DEFAULT_LOCALE = "en"


def get_locale(code: str) -> dict:
    return LOCALES.get(code, LOCALES[DEFAULT_LOCALE])


def alternate_locales(code: str) -> list[str]:
    return [c for c in ALL_LOCALES if c != code]
