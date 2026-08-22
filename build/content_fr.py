# French content for DJORESTIS.com
# Translators: translate every visible string; keep all HTML tags, class names
# and {link:...} / {FORM} / {PLACEHOLDER_PHOTO} / {PLACEHOLDER_VIDEO} markers intact.

LANG = "fr"

STRINGS = {
    "tagline": "Votre événement, tel que vous le rêvez",
    "skip": "Aller au contenu",
    "cta_quote": "Demander un devis",
    "cta_services": "Découvrir les services",
    "faq_heading": "Questions fréquentes",
    "cases_back": "Toutes les études de cas",
    "cases_index": {
        "title": "Études de cas — Entreprise, mariage &amp; résidence | DJ Orestis",
        "desc": "Trois études de cas détaillées : une réception de fin d'année à Bruxelles, un mariage gréco-belge, et une résidence de quatre ans en restaurant.",
        "kicker": "Études de cas",
        "h1": "Comment la soirée <span class='gold'>s'est vraiment passée</span>",
        "sub": "Trois événements en détail — le brief, les décisions, et ce qui s'est passé sur la piste.",
        "read_more": "Lire l'étude de cas",
        "cta": "Vous préparez quelque chose de similaire ?",
    },
    "facts_heading": "En bref",
    "photo_ph": "Photo bientôt disponible",
    "video_ph": "Vidéo bientôt disponible",
    "footer_sge": "Cofondateur de",
    "footer_services": "Services",
    "footer_explore": "Explorer",
    "footer_contact": "Contact",
    "footer_based": "Basé à Bruxelles, Belgique",
    "footer_areas": "Disponible en Belgique · Pays-Bas · France · Allemagne · Royaume-Uni · Grèce",
    "footer_rights": "Tous droits réservés.",
    "whatsapp_label": "Discuter sur WhatsApp",
    "cookie": {
        "text": "Ce site utilise des cookies uniquement à des fins de statistiques de visite anonymes.",
        "accept": "Accepter",
        "decline": "Refuser",
    },
    "blog": {
        "index_title": "Blog — Récits & guides depuis les platines | DJ Orestis",
        "index_desc": "Récits d'événements et guides pratiques signés DJ Orestis : soirées d'entreprise, mariages et soirées grecques à Bruxelles et partout en Europe.",
        "h1": "Depuis <span class='gold'>les platines</span>",
        "sub": "Récits d'événements, leçons du terrain et guides pratiques — mariages, soirées d'entreprise et fêtes grecques aux quatre coins de l'Europe.",
        "read_more": "Lire le récit",
        "back": "Tous les articles",
        "cta": "Vous préparez quelque chose de similaire ?",
    },
    "nav": {
        "home": "Accueil",
        "about": "À propos",
        "services": "Services",
        "corporate": "Événements d'entreprise",
        "wedding": "Mariages & baptêmes",
        "greek": "Soirées grecques",
        "party": "Fêtes privées",
        "fullpackage": "Formules tout compris",
        "restaurant": "DJ restaurant",
        "mykonos": "DJ en Europe",
        "blog": "Blog",
        "weddingguide": "Guide musique mariage",
        "corporateguide": "Guide musique entreprise",
        "music": "Musique",
        "events": "Événements passés",
        "contact": "Contact",
        "privacy": "Politique de confidentialité",
    },
    "form": {
        "name": "Votre nom *",
        "email": "E-mail *",
        "phone": "GSM / WhatsApp",
        "event_type": "Type d'événement",
        "event_types": ["Événement d'entreprise / réception", "Mariage", "Baptême", "Fête privée",
                        "Soirée grecque / événement communautaire", "Club / établissement", "Autre"],
        "date": "Date de l'événement",
        "location": "Lieu",
        "location_ph": "Ville, pays ou nom de la salle",
        "guests": "Nombre d'invités",
        "budget": "Budget indicatif",
        "budget_ph": "Facultatif — m'aide à affiner la proposition",
        "extras": "Services complémentaires souhaités",
        "x_sound": "Matériel son & lumière",
        "x_photo": "Photographie",
        "x_video": "Vidéo",
        "message": "Parlez-moi de votre événement",
        "message_ph": "L'occasion, l'ambiance recherchée, vos préférences musicales…",
        "submit": "Envoyer la demande",
        "note": "Vous recevrez une proposition personnalisée — en général endéans les 48 heures. Sans engagement.",
        "sent": "Merci ! Votre demande a bien été envoyée. Je vous réponds très vite.",
        "error": "Une erreur s'est produite. Merci de m'écrire directement par e-mail.",
        "mailto_subject": "Demande de devis — DJORESTIS.com",
    },
}

PAGES = {
    # ---------------------------------------------------------------- HOME
    "home": {
        "title": "DJ à Bruxelles — Entreprise, Mariage & Soirées Grecques | DJ Orestis",
        "desc": "DJ professionnel à Bruxelles pour soirées d'entreprise, mariages et soirées grecques en Belgique, aux Pays-Bas, en France, en Allemagne, au Royaume-Uni et en Grèce. Musique grecque, électro, afro, latino & RnB. Votre événement, tel que vous le rêvez.",
        "kicker": "Bruxelles · Belgique · Europe",
        "h1": "Votre événement, <span class='gold'>tel que vous le rêvez</span>",
        "sub": "DJ Orestis — DJ basé à Bruxelles pour vos événements d'entreprise, mariages et fêtes inoubliables. Musique grecque, électro, afro, latino et RnB, mixées pour votre public.",
        "body": """
<section class="section trustbar">
  <div class="wrap">
    <p class="kicker center">Ils m'ont fait confiance</p>
    <ul class="client-list">
      <li>Freshfields</li><li>Boston Consulting Group</li><li>Brussels Greek Food Festival</li>
      <li>Papillon Schuman</li><li>AHEPA</li><li>Dames Hellènes</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>Ce que je peux faire pour <span class="gold">votre événement</span></h2>
    <div class="card-grid">
      <a class="card" href="{link:corporate}">
        <h3>Événements d'entreprise</h3>
        <p>Réceptions, fêtes du personnel et moments de marque pour des entreprises exigeantes — de l'élégance en fond sonore à une piste de danse comble.</p>
        <span class="card-more">DJ soirée d'entreprise →</span>
      </a>
      <a class="card" href="{link:wedding}">
        <h3>Mariages &amp; baptêmes</h3>
        <p>Célébrations grecques, internationales et mixtes. Un seul DJ qui comprend les deux familles — et les fait toutes danser.</p>
        <span class="card-more">DJ mariage →</span>
      </a>
      <a class="card" href="{link:greek}">
        <h3>Soirées grecques</h3>
        <p>La soirée grecque dans les règles de l'art : des laïkà aux classiques des îles jusqu'aux tubes actuels, pour les communautés et les fêtes de toute l'Europe.</p>
        <span class="card-more">DJ grec →</span>
      </a>
      <a class="card" href="{link:party}">
        <h3>Fêtes privées</h3>
        <p>Anniversaires, jubilés et fêtes à domicile avec un DJ open format professionnel — électro, afro, latino, RnB et tout ce qu'il y a entre les deux.</p>
        <span class="card-more">DJ de soirée →</span>
      </a>
      <a class="card wide" href="{link:fullpackage}">
        <h3>Formules événementielles tout compris</h3>
        <p>DJ, son &amp; lumière professionnels, photographie et vidéo — un seul partenaire pour vos événements jusqu'à 500 invités. Un contact, une facture, zéro stress.</p>
        <span class="card-more">Découvrir la formule complète →</span>
      </a>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap split">
    <div>
      <h2>Neuf ans derrière les platines, <span class="gold">deux capitales de la musique</span></h2>
      <p>J'ai appris mon métier dans la vie nocturne de Mykonos — trois saisons d'été face à l'un des publics les plus exigeants d'Europe — avant de l'affiner pendant six ans à Bruxelles, où je suis DJ résident au Papillon Schuman, pour la quatrième année consécutive.</p>
      <p>Aujourd'hui, je mixe pour les réceptions d'entreprises comme Freshfields et Boston Consulting Group, des mariages partout en Europe, et les événements de la communauté grecque qui ont fait ma réputation — du Brussels Greek Food Festival aux soirées étudiantes de Vienne, Louvain et Lille.</p>
      <a class="btn btn-ghost" href="{link:about}">En savoir plus sur moi</a>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section">
  <div class="wrap stats">
    <div class="stat"><span class="stat-n">9+</span><span class="stat-l">années d'expérience</span></div>
    <div class="stat"><span class="stat-n">6</span><span class="stat-l">pays desservis</span></div>
    <div class="stat"><span class="stat-n">5</span><span class="stat-l">univers musicaux — grec, électro, afro, latino, RnB</span></div>
    <div class="stat"><span class="stat-n">500</span><span class="stat-l">invités — capacité de production complète</span></div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Un projet en tête ?</h2>
    <p>Parlez-moi de votre événement et recevez une proposition sur mesure — en général endéans les 48 heures.</p>
    <a class="btn btn-gold" href="{link:contact}">Demander un devis</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- ABOUT
    "about": {
        "title": "À propos de DJ Orestis — DJ à Bruxelles, formé à Mykonos",
        "desc": "DJ Orestis : 3 ans dans la vie nocturne de Mykonos, 6 ans à Bruxelles, DJ résident au Papillon Schuman et cofondateur de Sounds Greek Events. Événements d'entreprise, mariages et soirées grecques dans toute l'Europe.",
        "kicker": "L'homme derrière les platines",
        "h1": "À propos de <span class='gold'>DJ Orestis</span>",
        "sub": "Des beach clubs de Mykonos aux réceptions d'entreprise bruxelloises — une seule constante : une piste de danse qui fonctionne.",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Mon parcours</h2>
      <p>J'ai commencé là où les DJ se forgent à la dure : <strong>Mykonos</strong>. Trois saisons dans la vie nocturne de l'île m'ont appris à lire un public international en quelques secondes — parce qu'à Mykonos, on ne vous accorde pas quelques minutes.</p>
      <p>Il y a six ans, je me suis installé à <strong>Bruxelles</strong>, devenue mon port d'attache. Je suis aujourd'hui DJ résident au <strong>Papillon Schuman</strong> — pour la quatrième année consécutive — et j'ai mixé dans de nombreuses salles de la ville : La Place 33, Capital, Kosmos, YAYA, Meatropolis, Machina, AKT et bien d'autres. Chaque été, je retourne à Mykonos pour des sets en guest.</p>
      <p>En parallèle du travail en club, j'ai développé une seconde spécialité : <strong>l'événementiel</strong>. J'ai cofondé <a href="https://soundsgreekevents.be" rel="noopener">Sounds Greek Events</a>, animé deux éditions du <strong>Brussels Greek Food Festival</strong>, et je suis devenu le DJ de référence des communautés grecques d'Europe — Vienne, Louvain, Lille et au-delà. Les entreprises ont suivi : j'ai mixé pour des événements d'entreprise de <strong>Freshfields</strong>, du <strong>Boston Consulting Group</strong> et d'autres grandes maisons bruxelloises.</p>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Ma façon de travailler</h2>
    <div class="card-grid">
      <div class="card"><h3>La préparation d'abord</h3><p>Chaque événement commence par une conversation : l'occasion, les invités, les moments qui comptent. La playlist est construite pour votre salle, jamais recyclée de la précédente.</p></div>
      <div class="card"><h3>Lire la piste</h3><p>Un grand set est un dialogue. J'observe la piste en permanence et j'ajuste en temps réel — plus d'énergie quand la salle le demande, plus de retenue quand le moment l'exige.</p></div>
      <div class="card"><h3>Cinq univers musicaux</h3><p>Grec, électro, afro, latino et RnB — en profondeur, pas en surface. Cette amplitude fait des publics mixtes et internationaux ma spécialité.</p></div>
      <div class="card"><h3>Professionnel, toujours</h3><p>Ponctuel, discret, correctement équipé et dûment assuré. Le niveau d'exigence des clients corporate — appliqué à chaque événement, y compris privé.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    <h2>Communauté &amp; culture</h2>
    <p>La musique, c'est aussi ma manière de rendre. Je mixe <strong>bénévolement</strong> pour la Communauté grecque de Bruxelles, les Dames Hellènes et Hellenic United Women, je soutiens la Chorale grecque de Bruxelles et des troupes de théâtre locales — y compris en photographie et en vidéo — et je collabore avec le réseau diplomatique hellénique Argo, AHEPA et d'autres organisations de la diaspora grecque.</p>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Parlons de votre événement</h2>
    <a class="btn btn-gold" href="{link:contact}">Demander un devis</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- SERVICES
    "services": {
        "title": "Services DJ à Bruxelles & en Belgique — Entreprise, Mariage, Fêtes",
        "desc": "Services de DJ professionnel à Bruxelles et dans toute l'Europe : événements d'entreprise, mariages et baptêmes, soirées grecques, fêtes privées, ainsi que des formules complètes son, lumière, photo et vidéo jusqu'à 500 invités.",
        "kicker": "Ce que je propose",
        "h1": "Services",
        "sub": "Un partenaire professionnel, cinq spécialités — en Belgique, aux Pays-Bas, en France, en Allemagne, au Royaume-Uni et en Grèce.",
        "body": """
<section class="section">
  <div class="wrap">
    <div class="svc-list">
      <a class="svc" href="{link:corporate}">
        <div><h2>Événements d'entreprise</h2>
        <p>Réceptions, fêtes de fin d'année, lancements de produits et événements d'équipe pour les entreprises de Bruxelles et d'ailleurs. Des sets d'ambiance élégants, un accompagnement fluide de votre programme et une piste de danse qui s'enflamme au bon moment.</p></div>
        <span class="card-more">En savoir plus →</span>
      </a>
      <a class="svc" href="{link:wedding}">
        <div><h2>Mariages &amp; baptêmes</h2>
        <p>Les plus belles fêtes de votre vie, préparées avec soin : rendez-vous de préparation, playlists sur mesure, sonorisation de la cérémonie et du dîner, et une soirée qui réunit les deux familles sur la piste.</p></div>
        <span class="card-more">En savoir plus →</span>
      </a>
      <a class="svc" href="{link:greek}">
        <div><h2>Soirées grecques &amp; événements communautaires</h2>
        <p>La fête grecque authentique — pour les communautés, associations et célébrations de toute l'Europe. Des moments zeïbékiko aux sets estivaux des îles.</p></div>
        <span class="card-more">En savoir plus →</span>
      </a>
      <a class="svc" href="{link:party}">
        <div><h2>Fêtes privées</h2>
        <p>Anniversaires, jubilés, remises de diplôme et fêtes à domicile avec un professionnel open format : électro, afro, latino, RnB, musique grecque et les grands classiques.</p></div>
        <span class="card-more">En savoir plus →</span>
      </a>
      <a class="svc" href="{link:fullpackage}">
        <div><h2>Formules événementielles tout compris</h2>
        <p>DJ + son &amp; lumière professionnels + photographie + vidéo, pour des événements et petits spectacles jusqu'à 500 personnes. Un contact, une installation, une facture.</p></div>
        <span class="card-more">En savoir plus →</span>
      </a>
      <a class="svc" href="{link:restaurant}">
        <div><h2>Soirées en restaurant &amp; en salle</h2>
        <p>Des soirées à thème récurrentes qui fidélisent un public — la formule derrière mes quatre années de résidence au Papillon Schuman, disponible pour votre établissement.</p></div>
        <span class="card-more">En savoir plus →</span>
      </a>
      <a class="svc" href="{link:mykonos}">
        <div><h2>Événements de destination partout en Europe</h2>
        <p>Un DJ grec formé à Mykonos pour vos événements aux Pays-Bas, en France, en Allemagne, au Royaume-Uni et en Grèce — y compris à Mykonos même.</p></div>
        <span class="card-more">En savoir plus →</span>
      </a>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap narrow center">
    <h2>Au-delà des frontières</h2>
    <p>Basé à Bruxelles, à l'aise partout : je mixe régulièrement aux Pays-Bas, en France, en Allemagne, au Royaume-Uni et en Grèce. Pour les événements hors de Belgique, le déplacement et le logement s'ajoutent simplement au devis — tout le reste fonctionne exactement de la même manière.</p>
    <a class="btn btn-gold" href="{link:contact}">Demander un devis</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- CORPORATE
    "corporate": {
        "title": "DJ Soirée d'Entreprise à Bruxelles & en Belgique | DJ Orestis",
        "desc": "DJ pour soirées d'entreprise à Bruxelles : réceptions, fêtes du personnel, lancements de produits et événements professionnels — notamment pour Freshfields et BCG. Professionnel, discret, son & lumière disponibles. Belgique & Europe.",
        "kicker": "L'événement d'entreprise, dans les règles de l'art",
        "h1": "DJ soirée d'entreprise à <span class='gold'>Bruxelles</span>",
        "sub": "De la musique pour les entreprises qui attendent de leur DJ le même niveau d'exigence que de leur traiteur : Freshfields, Boston Consulting Group et d'autres grandes maisons l'ont déjà adopté.",
        "price": "À partir de 600 € HTVA", "price_note": "DJ seul — son &amp; lumière sur devis séparé", "price_amount": "600",
        "facts": [("Prix de départ", "600 € HTVA, DJ seul"),
                  ("Durée habituelle", "4 à 6 heures, prolongeable"),
                  ("Capacité", "Jusqu'à 500 invités en production complète"),
                  ("Langues", "Grec, anglais, français, néerlandais"),
                  ("Base &amp; déplacements", "Bruxelles ; toute la Belgique, et l'Europe sur demande"),
                  ("Installation", "2 à 3 heures avant l'ouverture des portes, en toute discrétion")],
        "service_type": "DJ événement d'entreprise",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Pourquoi les entreprises me choisissent</h2>
      <p>Un événement d'entreprise peut échouer de deux manières : une musique dont personne ne remarque qu'elle dérape, ou une musique dont tout le monde le remarque. J'ai passé six ans à Bruxelles à veiller à ce que ni l'une ni l'autre ne se produise — cocktails, fêtes de fin d'année, dîners de conférence et lancements pour des cabinets internationaux.</p>
      <ul class="ticks">
        <li><strong>Discrétion et élégance</strong> — tenue adaptée, installation ponctuelle, attitude irréprochable avec vos invités comme avec votre direction.</li>
        <li><strong>Sens du programme</strong> — discours, remises de prix et surprises tombent à l'heure ; la musique respire autour de votre agenda, jamais par-dessus.</li>
        <li><strong>Amplitude musicale</strong> — sets d'ambiance raffinés pendant le dîner, tubes internationaux ensuite ; grec, électro, afro, latino et RnB pour des équipes réellement internationales.</li>
        <li><strong>Production complète si nécessaire</strong> — son et lumière jusqu'à 500 invités, plus photographie et vidéo via mes <a href="{link:fullpackage}">formules tout compris</a>.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Formats habituels</h2>
    <div class="card-grid">
      <div class="card"><h3>Cocktails &amp; réceptions</h3><p>Des sets élégants et propices à la conversation, qui élèvent l'énergie de la salle sans faire élever la voix.</p></div>
      <div class="card"><h3>Fêtes du personnel &amp; de fin d'année</h3><p>De l'ambiance du dîner à une piste de danse pleine — la montée en puissance que votre équipe mérite après une longue année.</p></div>
      <div class="card"><h3>Lancements &amp; moments de marque</h3><p>Une identité sonore accordée à votre marque, calée sur votre programme, coordonnée avec votre agence.</p></div>
      <div class="card"><h3>Conférences &amp; dîners</h3><p>Musique d'accueil et de sortie, virgules sonores, sets de dîner — un accompagnement audiovisuel fiable toute la journée.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Vous préparez un événement d'entreprise ?</h2>
    <p>Envoyez la date, le lieu et le nombre d'invités — vous recevrez une proposition claire, en général endéans les 48 heures.</p>
    <a class="btn btn-gold" href="{link:contact}">Demander un devis entreprise</a>
  </div>
</section>
""",
        "faq": [
            ("Fournissez-vous le matériel son et lumière pour les événements d'entreprise ?",
             "Oui. Grâce à mes formules tout compris, je fournis une sonorisation et un éclairage professionnels pour des événements jusqu'à 500 invités — vous n'avez donc pas besoin d'un prestataire audiovisuel séparé. Je peux aussi travailler avec l'installation existante de votre salle."),
            ("Pouvez-vous mixer pour un public international et multiculturel ?",
             "C'est précisément ma spécialité. Je mixe musique grecque, électro, afro, latino et RnB et je m'adapte en temps réel à la salle — exactement ce dont les équipes internationales de Bruxelles ont besoin."),
            ("Vous déplacez-vous en dehors de Bruxelles pour des événements professionnels ?",
             "Oui — partout en Belgique, ainsi qu'aux Pays-Bas, en France, en Allemagne, au Royaume-Uni et en Grèce. Pour les événements à l'étranger, le déplacement et le logement s'ajoutent au devis."),
            ("Combien de temps à l'avance faut-il réserver ?",
             "Pour la saison des fêtes de fin d'année (novembre–décembre), 2 à 3 mois à l'avance est prudent. Pour les autres dates, 4 à 6 semaines suffisent généralement — mais demandez quand même : des solutions de dernière minute sont souvent possibles."),
        ],
    },

    # ---------------------------------------------------------------- WEDDING
    "wedding": {
        "title": "DJ Mariage à Bruxelles & en Belgique — Mariages Grecs & Internationaux",
        "desc": "DJ mariage à Bruxelles et dans toute la Belgique pour mariages grecs, internationaux et mixtes, ainsi que baptêmes. Playlists sur mesure, de la cérémonie à la dernière danse, son & lumière compris si besoin. Aussi NL, FR, DE, UK, GR.",
        "kicker": "La plus belle fête de votre vie",
        "h1": "DJ mariage à <span class='gold'>Bruxelles &amp; en Belgique</span>",
        "sub": "Mariages grecs, internationaux et joliment mixtes — un seul DJ qui fait danser les deux côtés de la salle sur le même tempo.",
        "price": "À partir de 600 € HTVA", "price_note": "DJ seul — son &amp; lumière sur devis séparé", "price_amount": "600",
        "facts": [("Prix de départ", "600 € HTVA, DJ seul"),
                  ("Couverture", "Cérémonie, dîner et soirée — une seule installation"),
                  ("Micros", "Micros sans fil compris pour les vœux et les discours"),
                  ("Capacité", "Jusqu'à 500 invités en production complète"),
                  ("Langues", "Grec, anglais, français, néerlandais"),
                  ("Préparation", "Un rendez-vous de préparation avant chaque mariage")],
        "service_type": "DJ mariage",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Votre mariage, votre bande-son</h2>
      <p>Deux mariages ne devraient jamais se ressembler. Nous nous rencontrons avant le grand jour, nous passons chaque moment en revue — cérémonie, entrée, dîner, première danse, soirée — et nous construisons la bande-son autour de votre histoire et de vos invités.</p>
      <ul class="ticks">
        <li><strong>Mariages mixtes &amp; internationaux</strong> — mon terrain de prédilection. Grec et belge, français et latino, toutes les combinaisons : les deux familles sur la piste, ensemble.</li>
        <li><strong>Les moments grecs, dans les règles</strong> — un kalamatianó qui a l'approbation des grands-parents, un zeïbékiko avec la gravité qu'il mérite, les tubes des îles pour l'air de l'été.</li>
        <li><strong>Une couverture complète</strong> — sonorisation de la cérémonie, micros sans fil pour les discours, ambiance du dîner et soirée dansante, en un seul flux continu.</li>
        <li><strong>Les baptêmes aussi</strong> — des fêtes de famille élégantes, avec le même soin, à l'échelle de la journée.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Comment ça se passe</h2>
    <div class="card-grid">
      <div class="card"><h3>1 · On se parle</h3><p>Une conversation de préparation détendue : votre histoire, vos incontournables, vos interdits, le déroulé de la journée.</p></div>
      <div class="card"><h3>2 · Je prépare</h3><p>Un programme sur mesure pour chaque étape de la fête, coordonné avec votre salle, votre photographe et votre wedding planner.</p></div>
      <div class="card"><h3>3 · Vous célébrez</h3><p>Le jour J, tout fonctionne, tout simplement — vous dansez, je m'occupe du reste. Son et lumière compris si vous en avez besoin.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Vous vous mariez ?</h2>
    <p>Donnez-moi votre date et votre lieu — je vous dirai honnêtement si je suis le bon DJ pour votre mariage.</p>
    <a class="btn btn-gold" href="{link:contact}">Vérifier ma disponibilité</a>
  </div>
</section>
""",
        "faq": [
            ("Animez-vous aussi bien des mariages grecs qu'internationaux ?",
             "Oui — et surtout les mariages qui sont les deux à la fois. J'ai grandi dans la musique grecque et passé des années à mixer électro, afro, latino et RnB pour des publics internationaux : les mariages mixtes sont mon point fort."),
            ("Pouvez-vous aussi assurer la musique de la cérémonie et des discours ?",
             "Oui. Je couvre toute la journée : sonorisation de la cérémonie, micros sans fil pour les vœux et les discours, ambiance du dîner et soirée dansante — une seule installation, un seul contact."),
            ("Mixez-vous pour des mariages en dehors de la Belgique ?",
             "Régulièrement — aux Pays-Bas, en France, en Allemagne, au Royaume-Uni et en Grèce. Le déplacement et le logement s'ajoutent au devis ; tout le reste ne change pas."),
            ("Pouvons-nous vous donner une playlist et une liste de morceaux à éviter ?",
             "Surtout, faites-le. Vos incontournables et vos interdits forment le squelette de la soirée ; mon travail consiste à construire un set vivant autour d'eux et à garder la piste pleine."),
        ],
    },

    # ---------------------------------------------------------------- GREEK
    "greek": {
        "title": "DJ Grec à Bruxelles — Soirées Grecques en Europe | DJ Orestis",
        "desc": "DJ grec à Bruxelles : soirées grecques authentiques pour communautés, associations et fêtes privées en Belgique et dans toute l'Europe. DJ du Brussels Greek Food Festival, résident au Papillon Schuman.",
        "kicker": "Ελληνικές βραδιές — l'authentique",
        "h1": "DJ grec à <span class='gold'>Bruxelles</span>",
        "sub": "Du Brussels Greek Food Festival aux fêtes communautaires de Vienne, Louvain et Lille — la soirée grecque, comme elle le mérite.",
        "price": "À partir de 400 € HTVA", "price_note": "À Bruxelles — déplacement en sus au-delà", "price_amount": "400",
        "facts": [("Prix de départ", "400 € HTVA à Bruxelles, DJ seul"),
                  ("Répertoire", "Laïkà, éntekhna, nisiótika, rebétiko, tubes grecs actuels"),
                  ("Soirées mixtes", "Heures grecques mêlées d'afro, de latino, de RnB et d'international"),
                  ("Animation", "Annonces en grec, anglais, français ou néerlandais"),
                  ("Références", "Brussels Greek Food Festival ×2 ; communautés de Vienne, Louvain, Lille"),
                  ("Base &amp; déplacements", "Bruxelles ; toute la Belgique, l'Europe et la Grèce")],
        "service_type": "DJ grec",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Le DJ que la communauté grecque connaît déjà</h2>
      <p>Pour la diaspora grecque de Belgique et d'ailleurs, je ne suis probablement pas un inconnu : j'ai animé deux éditions du <strong>Brussels Greek Food Festival</strong>, mixé pour les <strong>Dames Hellènes</strong>, la <strong>Chorale grecque de Bruxelles</strong> et les <strong>communautés grecques de Vienne, Louvain et Lille</strong>, et je joue bénévolement pour la Communauté grecque de Bruxelles et Hellenic United Women.</p>
      <p>Ma résidence au <strong>Papillon Schuman</strong> — quatre ans déjà — est l'adresse bruxelloise des soirées grecques. Et chaque été, je rentre au pays : des sets en guest à <strong>Mykonos</strong>, là où j'ai appris le métier.</p>
      <ul class="ticks">
        <li><strong>Tout le spectre grec</strong> — laïkà, éntekhna, nisiótika, moments rebétiko, classiques des années 90 et tubes d'aujourd'hui.</li>
        <li><strong>La vraie culture du zeïbékiko</strong> — l'espace, le respect, le bon moment.</li>
        <li><strong>Des soirées mixtes</strong> — des heures grecques qui glissent vers des sets internationaux, pour que chaque invité se sente à sa place.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Qui réserve mes soirées grecques</h2>
    <div class="card-grid">
      <div class="card"><h3>Communautés &amp; associations</h3><p>Bals annuels, fêtes nationales, collectes de fonds et soirées étudiantes en Belgique et dans toute l'Europe.</p></div>
      <div class="card"><h3>Restaurants &amp; établissements</h3><p>Des soirées grecques récurrentes qui fidélisent un public — la formule Papillon Schuman.</p></div>
      <div class="card"><h3>Familles</h3><p>Mariages, baptêmes et fêtes de prénom où le répertoire grec doit être irréprochable.</p></div>
      <div class="card"><h3>Entreprises</h3><p>Soirées d'entreprise à thème grec — de plus en plus prisées, étonnamment efficaces.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Πάμε;</h2>
    <p>Parlez-moi de votre soirée grecque — en grec, en français, en anglais ou en néerlandais.</p>
    <a class="btn btn-gold" href="{link:contact}">Demander un devis</a>
  </div>
</section>
""",
        "faq": [
            ("Jouez-vous uniquement de la musique grecque lors des soirées grecques ?",
             "Seulement si c'est ce que vous souhaitez. Les meilleures soirées grecques respirent : de belles heures grecques, entrecoupées d'afro, de latino, de RnB et de tubes internationaux, pour que chaque invité — grec ou non — reste sur la piste."),
            ("Vous déplacez-vous auprès des communautés grecques hors de Belgique ?",
             "Oui — je mixe déjà pour les communautés grecques de Vienne, Louvain et Lille, et je suis disponible aux Pays-Bas, en France, en Allemagne, au Royaume-Uni et en Grèce. Le déplacement et le logement s'ajoutent au devis."),
            ("Pouvez-vous aussi animer ou présenter l'événement en grec ?",
             "Oui — annonces et animation en grec, en français, en anglais ou en néerlandais, selon les besoins de votre public."),
        ],
    },

    # ---------------------------------------------------------------- PARTY
    "party": {
        "title": "DJ Soirée Privée à Bruxelles — Anniversaires & Fêtes | DJ Orestis",
        "desc": "DJ pour fêtes privées à Bruxelles : anniversaires, jubilés, remises de diplôme et célébrations avec un DJ open format professionnel. Électro, afro, latino, RnB et musique grecque. Son & lumière disponibles. Belgique & Europe.",
        "kicker": "Votre fête, au volume professionnel",
        "h1": "DJ de soirée à <span class='gold'>Bruxelles</span>",
        "sub": "Anniversaires, jubilés, remises de diplôme, fêtes à domicile — l'énergie d'un club, le professionnalisme compatible avec votre salon.",
        "price": "À partir de 400 € HTVA", "price_note": "À Bruxelles — déplacement en sus au-delà", "price_amount": "400",
        "facts": [("Prix de départ", "400 € HTVA à Bruxelles, DJ seul"),
                  ("Formats", "Anniversaires, jubilés, remises de diplôme, fêtes à domicile"),
                  ("Échelle", "De l'appartement à une salle de 500 invités"),
                  ("Musique", "Open format — électro, afro, latino, RnB, grec, pop"),
                  ("Matériel", "Installation compacte adaptée à un appartement ou production complète"),
                  ("Base &amp; déplacements", "Bruxelles et toute la Belgique")],
        "service_type": "DJ fête privée",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Un vrai DJ fait toute la différence</h2>
      <p>Une playlist ne voit pas votre piste de danse. Neuf ans d'expérience en club et en événementiel — la vie nocturne de Mykonos, des résidences bruxelloises, des centaines d'événements privés — c'est l'assurance d'un professionnel qui lit la salle, accueille les demandes avec élégance et maintient l'énergie exactement là où vous la voulez.</p>
      <ul class="ticks">
        <li><strong>Open format</strong> — électro, afro, latino, RnB, musique grecque, pop et les grands classiques, mixés pour votre public.</li>
        <li><strong>Toutes les échelles</strong> — de l'anniversaire dans un salon à une salle louée pour 500 invités, avec <a href="{link:fullpackage}">son &amp; lumière compris</a> si vous en avez besoin.</li>
        <li><strong>Vos règles</strong> — incontournables, interdits, moments surprises : nous planifions tout ensemble à l'avance.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Une date en tête ?</h2>
    <p>Dites-moi l'occasion et le lieu — je m'occupe du reste.</p>
    <a class="btn btn-gold" href="{link:contact}">Demander un devis</a>
  </div>
</section>
""",
        "faq": [
            ("Combien coûte un DJ pour une fête privée à Bruxelles ?",
             "Cela dépend de la durée, du lieu et du besoin éventuel en matériel son et lumière. Envoyez les informations essentielles via le formulaire de contact et vous recevrez un devis clair et personnalisé — en général endéans les 48 heures, sans engagement."),
            ("Apportez-vous votre propre matériel pour les fêtes à domicile ?",
             "Oui — je peux venir avec une installation complète adaptée à un appartement, ou avec un dispositif son et lumière complet pour une salle louée jusqu'à 500 invités. Décrivez-moi l'espace et je vous proposerai la bonne configuration."),
            ("Acceptez-vous les demandes de morceaux pendant la fête ?",
             "Avec plaisir — les demandes font partie d'une bonne fête. Je les intègre quand elles servent la piste, et je respecte toujours votre liste de morceaux à éviter."),
        ],
    },

    # ---------------------------------------------------------------- FULL PACKAGE
    "fullpackage": {
        "title": "Formule Tout Compris — DJ, Son, Lumière, Photo & Vidéo | Bruxelles",
        "desc": "Un seul partenaire pour tout votre événement à Bruxelles et au-delà : DJ professionnel, son et lumière jusqu'à 500 invités, plus photographie et vidéo. Un contact, une installation, une facture.",
        "kicker": "Un partenaire, tout l'événement",
        "h1": "Formules événementielles <span class='gold'>tout compris</span>",
        "sub": "DJ + son &amp; lumière professionnels + photographie + vidéo — pour des événements et petits spectacles jusqu'à 500 personnes.",
        "price": "À partir de 1 000 € HTVA", "price_note": "DJ, enceintes, micros et lumière", "price_amount": "1000",
        "facts": [("Prix de départ", "1 000 € HTVA pour la formule premium complète"),
                  ("Taille maximale", "500 invités"),
                  ("Sur demande", "Son, lumière, photographie, vidéo"),
                  ("Micros", "Micros sans fil pour les discours et les cérémonies"),
                  ("Coordination", "Préparation technique avec la salle prise en charge directement"),
                  ("Facturation", "Un contact, une facture pour tout l'événement")],
        "service_type": "Production événementielle (DJ, son, lumière, photo, vidéo)",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Pourquoi un partenaire vaut mieux que quatre prestataires</h2>
      <p>Coordonner un DJ, une société audiovisuelle, un photographe et un vidéaste, c'est quatre contrats, quatre plannings et quatre personnes qui n'ont jamais travaillé ensemble. Je propose l'alternative : une équipe, un plan technique, une seule personne responsable de la réussite de toute la soirée — moi.</p>
      <ul class="ticks">
        <li><strong>Sonorisation professionnelle</strong> — dimensionnée à votre salle, de 20 à 500 invités, avec micros sans fil pour les discours et les cérémonies.</li>
        <li><strong>Éclairage</strong> — un design d'ambiance élégant pour les réceptions et dîners, un éclairage complet de piste pour la soirée.</li>
        <li><strong>Photographie &amp; vidéo</strong> — une couverture assurée par une équipe qui accompagne depuis des années des productions culturelles et des troupes de théâtre.</li>
        <li><strong>Petits spectacles &amp; productions</strong> — son et lumière de scène pour représentations, productions communautaires et showcases.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Idéal pour</h2>
    <div class="card-grid">
      <div class="card"><h3>Réceptions d'entreprise</h3><p>Une facture et un seul interlocuteur responsable — exactement comme les services achats l'apprécient.</p></div>
      <div class="card"><h3>Mariages &amp; baptêmes</h3><p>Musique, micros, lumière et souvenirs, pensés comme une seule production sans couture.</p></div>
      <div class="card"><h3>Galas &amp; spectacles communautaires</h3><p>Productions scéniques, bals annuels et soirées culturelles jusqu'à 500 personnes.</p></div>
      <div class="card"><h3>Événements en salle</h3><p>Soirées club éphémères et soirées à thème, entièrement produites.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Décrivez-moi votre événement</h2>
    <p>Nombre d'invités, lieu, date — vous recevrez une proposition claire qui couvre tout.</p>
    <a class="btn btn-gold" href="{link:contact}">Demander un devis tout compris</a>
  </div>
</section>
""",
        "faq": [
            ("Jusqu'à quelle taille d'événement assurez-vous la production complète ?",
             "Jusqu'à 500 personnes, avec sonorisation et éclairage professionnels. Au-delà du matériel, cela comprend la préparation technique avec votre salle ainsi que le montage et le démontage selon votre horaire."),
            ("Puis-je ne réserver qu'une partie de la formule ?",
             "Bien sûr. DJ seul, DJ + son & lumière, ou la formule complète avec photo et vidéo — le devis est construit autour de ce dont vous avez réellement besoin."),
            ("Vous chargez-vous de la coordination technique avec la salle ?",
             "Oui — alimentation électrique, accès, normes sonores, horaires : je m'entretiens directement avec la salle, pour que vous n'ayez pas à faire l'interprète entre prestataires."),
        ],
    },

    # ---------------------------------------------------------------- RESTAURANT
    "restaurant": {
        "title": "DJ Résident pour Restaurants & Bars à Bruxelles | DJ Orestis",
        "desc": "Engagez un DJ résident pour votre restaurant ou votre bar à Bruxelles. Des soirées à thème récurrentes qui remplissent les soirs creux et font grimper le chiffre du bar. Quatre ans de résidence au Papillon Schuman. Soirée pilote possible.",
        "kicker": "Pour restaurants & établissements",
        "h1": "DJ résident pour <span class='gold'>restaurants &amp; bars</span>",
        "sub": "Pour les restaurateurs et gérants de bars à Bruxelles : une soirée à thème récurrente qui remplit un soir de semaine calme et fait grimper le chiffre du bar — la formule derrière mes quatre années de résidence au Papillon Schuman.",
        "price": "Cachet par soirée, devis établi pour la série", "price_note": "Soirée pilote possible avant tout engagement",
        "facts": [("Engagement", "Résidence hebdomadaire, mensuelle ou saisonnière"),
                  ("Essai", "Une soirée pilote, sans engagement de longue durée"),
                  ("Service du dîner", "Volume propice à la conversation jusqu'à la fin du service"),
                  ("Matériel", "Système compact fourni, ou utilisation de votre installation"),
                  ("Format éprouvé", "Papillon Schuman, quatre années consécutives"),
                  ("Public", "Une communauté grecque et internationale déjà fidèle à Bruxelles")],
        "service_type": "DJ résident de restaurant",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Pourquoi engager un DJ résident dans un restaurant ?</h2>
      <p>Une bonne soirée à thème est un véritable atout commercial : elle remplit un soir de semaine calme, fidélise un public qui réserve sa table à l'avance et donne à votre établissement une réputation qui dépasse sa carte. C'est exactement ce que j'ai construit au <strong>Papillon Schuman</strong> — quatre ans déjà, et cela continue — après avoir mixé dans de nombreuses salles bruxelloises : La Place 33, Capital, Kosmos, YAYA, Meatropolis, Machina, AKT.</p>
      <ul class="ticks">
        <li><strong>Un concept, pas seulement un DJ</strong> — nous concevons la soirée ensemble : soirées grecques, soirées latino, sessions afro &amp; RnB, ou un format élégant du dîner à la piste de danse.</li>
        <li><strong>La maîtrise du volume</strong> — le service reste propice à la conversation ; l'énergie ne monte que lorsque les assiettes quittent les tables.</li>
        <li><strong>Un public qui suit</strong> — ma communauté bruxelloise me suit d'adresse en adresse, surtout pour les soirées grecques.</li>
        <li><strong>Aucune infrastructure nécessaire</strong> — je peux apporter une sonorisation et un éclairage compacts, adaptés à un restaurant.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Quel format de résidence convient à votre établissement ?</h2>
    <div class="card-grid">
      <div class="card"><h3>Résidence hebdomadaire ou mensuelle</h3><p>Une soirée fixe et identifiable que vos clients peuvent planifier — le meilleur moyen de construire un public fidèle.</p></div>
      <div class="card"><h3>Lancement d'une soirée grecque</h3><p>Un concept éprouvé : un service de dîner grec qui glisse vers les laïkà et les tubes des îles. Des années de succès à Bruxelles.</p></div>
      <div class="card"><h3>Saisonnier &amp; éphémère</h3><p>Étés en terrasse, programmation festive de décembre, soirées à thème ponctuelles.</p></div>
      <div class="card"><h3>Privatisation de votre salle</h3><p>Votre restaurant accueille un événement privé ? Je prends en charge tout le volet musical, <a href="{link:fullpackage}">production comprise</a>.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Vous gérez un restaurant, un bar ou un hôtel à Bruxelles ?</h2>
    <p>Parlons d'une soirée pilote — une seule soirée, des chiffres clairs, aucun engagement à long terme.</p>
    <a class="btn btn-gold" href="{link:contact}">Proposer une soirée pilote</a>
  </div>
</section>
""",
        "faq": [
            ("Comment fonctionne une résidence DJ en restaurant sur le plan commercial ?",
             "En général, un cachet fixe par soirée, convenu sous forme de série hebdomadaire ou mensuelle. Nous commençons par une soirée pilote, pour que vous puissiez mesurer les couverts et le chiffre du bar avant de vous engager sur une série."),
            ("La musique ne sera-t-elle pas trop forte pendant le service ?",
             "Non — c'est tout l'art du métier. Pendant le dîner, les sets restent au niveau de la conversation, avec une programmation élégante ; le volume et l'énergie ne montent qu'une fois le service terminé. Je calibre le système en fonction de votre salle."),
            ("Apportez-vous votre propre matériel ?",
             "Si nécessaire, oui — une sonorisation et un éclairage compacts, adaptés à un restaurant, qui s'installent en toute discrétion. Si votre établissement dispose d'une installation existante, je travaille avec celle-ci."),
        ],
    },

    # ---------------------------------------------------------------- MYKONOS / EUROPE
    "mykonos": {
        "title": "DJ Grec pour Événements en Europe — Formé à Mykonos | DJ Orestis",
        "desc": "Réservez un DJ grec formé à Mykonos pour vos événements de destination partout en Europe : mariages, événements d'entreprise et soirées grecques aux Pays-Bas, en France, en Allemagne, au Royaume-Uni et en Grèce — y compris à Mykonos même.",
        "kicker": "Basé à Bruxelles, présent dans toute l'Europe",
        "h1": "DJ grec partout en <span class='gold'>Europe</span>",
        "sub": "Formé au fil de trois saisons dans la vie nocturne de Mykonos, basé à Bruxelles et régulièrement sur la route : votre événement ne doit pas se trouver en Belgique pour sonner juste.",
        "price": "À partir de 600 € HTVA + déplacement", "price_note": "Déplacement et logement détaillés séparément", "price_amount": "600",
        "facts": [("Prix de départ", "600 € HTVA plus déplacement et logement"),
                  ("Pays desservis", "Belgique, Pays-Bas, France, Allemagne, Royaume-Uni, Autriche, Grèce"),
                  ("Matériel à l'étranger", "Voyage léger avec matériel sur place, ou production complète près de la Belgique"),
                  ("Îles grecques", "Mykonos chaque été — renseignez-vous sur mes dates de saison"),
                  ("Langues", "Grec, anglais, français, néerlandais")],
        "service_type": "DJ événements de destination",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Un DJ, six pays</h2>
      <p>Certains événements exigent un DJ qui comprend un public bien précis — un mariage grec en Allemagne, un gala de la diaspora à Vienne, une fête d'entreprise estivale à Amsterdam, une célébration à Mykonos même. Je me déplace déjà pour exactement cela : la <strong>communauté étudiante grecque de Vienne</strong>, les <strong>communautés grecques de Louvain et de Lille</strong>, et chaque été, des <strong>sets en guest à Mykonos</strong>, où j'ai passé trois saisons complètes dans la vie nocturne de l'île.</p>
      <ul class="ticks">
        <li><strong>Une logistique simple</strong> — le déplacement et le logement s'ajoutent au devis en toute transparence ; tout le reste fonctionne exactement comme une réservation à Bruxelles.</li>
        <li><strong>Installation compacte ou complète</strong> — je peux voyager léger et utiliser le matériel sur place, ou organiser une production complète pour les événements proches de la Belgique.</li>
        <li><strong>L'expérience Mykonos</strong> — pour les mariages et fêtes de destination en Grèce, vous avez un DJ qui a réellement travaillé dans ces salles et connaît le rythme de l'île.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Réservations habituelles à l'étranger</h2>
    <div class="card-grid">
      <div class="card"><h3>Mariages de destination</h3><p>Mariages grecs et internationaux en Grèce, en France et au-delà — y compris Mykonos et les îles.</p></div>
      <div class="card"><h3>Événements de la diaspora</h3><p>Galas, fêtes nationales et soirées étudiantes pour les communautés grecques de toute l'Europe.</p></div>
      <div class="card"><h3>Séminaires d'entreprise</h3><p>Retraites d'équipe et fêtes d'été où votre équipe mérite mieux qu'une playlist.</p></div>
      <div class="card"><h3>Mykonos &amp; Grèce</h3><p>Fêtes en villa, événements pré-mariage et sets en guest pendant la saison estivale.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Vous préparez un événement à l'étranger ?</h2>
    <p>Dites-moi la ville et la date — vous recevrez un devis clair, déplacement compris.</p>
    <a class="btn btn-gold" href="{link:contact}">Demander un devis</a>
  </div>
</section>
""",
        "faq": [
            ("Quels pays couvrez-vous ?",
             "La Belgique est mon port d'attache ; je mixe régulièrement aux Pays-Bas, en France, en Allemagne, au Royaume-Uni, en Autriche et en Grèce. D'autres destinations sont possibles — demandez."),
            ("Comment fonctionne la tarification pour les événements hors de Belgique ?",
             "Le même cachet que pour une réservation en Belgique, plus des frais de déplacement et de logement transparents, détaillés séparément dans le devis. Pour la Grèce en été, j'y suis souvent déjà — renseignez-vous sur mes dates de saison à Mykonos."),
            ("Pouvez-vous mixer pour un mariage de destination à Mykonos ou dans les îles grecques ?",
             "Oui — c'est là que j'ai appris le métier. Je connais les lieux, le rythme d'une journée de mariage sur une île, et l'art de marier le répertoire grec à un public international."),
        ],
    },

    # ---------------------------------------------------------------- MUSIC
    "music": {
        "title": "Musique & Sets — Grec, Électro, Afro, Latino & RnB | DJ Orestis",
        "desc": "Écoutez DJ Orestis : cinq univers musicaux — grec, électro, afro, latino et RnB — mixés pour les événements d'entreprise, mariages et fêtes à Bruxelles et dans toute l'Europe.",
        "kicker": "Écouter",
        "h1": "Cinq univers musicaux, <span class='gold'>un seul DJ</span>",
        "sub": "L'amplitude, c'est tout l'intérêt : quel que soit votre public, il y a un set pour lui.",
        "body": """
<section class="section">
  <div class="wrap">
    <div class="card-grid">
      <div class="card"><h3>Musique grecque</h3><p>Laïkà, éntekhna, nisiótika, rebétiko, classiques des années 90 et hits d'aujourd'hui — tout le spectre, avec la culture nécessaire pour savoir quoi jouer et quand.</p></div>
      <div class="card"><h3>Électro</h3><p>House, deep et sets mélodiques façonnés par trois saisons à Mykonos — de l'élégance du coucher de soleil à l'intensité du peak time.</p></div>
      <div class="card"><h3>Afro</h3><p>Afrobeats, afro house et amapiano — le son qui règne sur les pistes de danse européennes d'aujourd'hui.</p></div>
      <div class="card"><h3>Latino</h3><p>Reggaeton, salsa, bachata et pop latino — l'effet immédiat garanti sur les publics internationaux.</p></div>
      <div class="card"><h3>RnB</h3><p>RnB et hip-hop, classiques comme contemporains — le fil conducteur de tout grand set open format.</p></div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Sets &amp; aftermovies</h2>
    <p class="center muted">De nouveaux enregistrements arrivent bientôt — en attendant, venez m'écouter en live chaque mois au Papillon Schuman à Bruxelles.</p>
    <div class="media-grid">
      {PLACEHOLDER_VIDEO}
      {PLACEHOLDER_VIDEO}
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Vous voulez ce son à votre événement ?</h2>
    <a class="btn btn-gold" href="{link:contact}">Demander un devis</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- EVENTS
    "events": {
        "title": "Événements Passés & Résidences — DJ Orestis | Bruxelles & Europe",
        "desc": "Une sélection d'événements de DJ Orestis : résidence au Papillon Schuman, Brussels Greek Food Festival, événements d'entreprise pour Freshfields et BCG, fêtes des communautés grecques de Vienne, Louvain et Lille, sets à Mykonos.",
        "kicker": "Références",
        "h1": "Événements passés &amp; <span class='gold'>résidences</span>",
        "sub": "Neuf ans, des centaines de soirées. Une sélection.",
        "body": """
<section class="section">
  <div class="wrap">
    <div class="events-cols">
      <div>
        <h2>Résidences &amp; salles</h2>
        <ul class="event-list">
          <li><strong>Papillon Schuman</strong> — DJ résident, 4e année <span class="muted">· Bruxelles</span></li>
          <li><strong>La Place 33</strong> <span class="muted">· Bruxelles</span></li>
          <li><strong>Capital</strong> <span class="muted">· Bruxelles</span></li>
          <li><strong>Kosmos</strong> <span class="muted">· Bruxelles</span></li>
          <li><strong>YAYA</strong> <span class="muted">· Bruxelles</span></li>
          <li><strong>Meatropolis</strong> <span class="muted">· Bruxelles</span></li>
          <li><strong>Machina</strong> <span class="muted">· Bruxelles</span></li>
          <li><strong>AKT</strong> <span class="muted">· Bruxelles</span></li>
          <li><strong>Mykonos</strong> — sets en guest chaque année ; 3 saisons complètes dans la vie nocturne de l'île</li>
        </ul>
      </div>
      <div>
        <h2>Entreprises</h2>
        <ul class="event-list">
          <li><strong>Freshfields</strong> — événements d'entreprise <span class="muted">· Bruxelles</span></li>
          <li><strong>Boston Consulting Group</strong> — événements d'entreprise <span class="muted">· Bruxelles</span></li>
          <li>D'autres grandes entreprises bruxelloises <span class="muted">· références sur demande</span></li>
        </ul>
        <h2>Festivals &amp; communauté</h2>
        <ul class="event-list">
          <li><strong>Brussels Greek Food Festival</strong> (festival gastronomique grec de Bruxelles) — DJ animateur, deux éditions</li>
          <li><strong>Dames Hellènes</strong> — événements &amp; célébrations</li>
          <li><strong>Chorale grecque de Bruxelles</strong></li>
          <li><strong>Communauté étudiante grecque de Vienne</strong> — soirées <span class="muted">· Autriche</span></li>
          <li><strong>Communauté grecque de Louvain</strong> — soirées</li>
          <li><strong>Communauté grecque de Lille</strong> — soirées <span class="muted">· France</span></li>
          <li><strong>Communauté grecque de Bruxelles</strong> — bénévolat</li>
          <li><strong>Hellenic United Women</strong> — bénévolat</li>
          <li><strong>Réseau diplomatique hellénique Argo, AHEPA</strong> — collaborations</li>
        </ul>
      </div>
    </div>
    <p class="muted">Plus d'événements sur <a href="https://soundsgreekevents.be" rel="noopener">Sounds Greek Events</a>, dont je suis cofondateur.</p>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Votre événement pourrait être le prochain</h2>
    <a class="btn btn-gold" href="{link:contact}">Demander un devis</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- CONTACT
    "contact": {
        "title": "Réserver DJ Orestis — Devis | Bruxelles, Belgique & Europe",
        "desc": "Réservez DJ Orestis pour votre événement d'entreprise, mariage ou fête à Bruxelles, en Belgique ou partout en Europe. Remplissez le formulaire de devis et recevez une proposition personnalisée, en général endéans les 48 heures.",
        "kicker": "Parlons-en",
        "h1": "Demander un <span class='gold'>devis</span>",
        "sub": "Plus vous m'en dites, plus la proposition sera précise. Réponse en général endéans les 48 heures — toujours sans engagement.",
        "body": """
<section class="section">
  <div class="wrap split-form">
    <div>
      {FORM}
    </div>
    <aside class="contact-aside">
      <h2>Contact direct</h2>
      <p><a href="mailto:info@djorestis.com">info@djorestis.com</a></p>
      <p class="muted">Basé à Bruxelles, Belgique.<br>Disponible en Belgique, aux Pays-Bas, en France, en Allemagne, au Royaume-Uni et en Grèce — pour les événements à l'étranger, le déplacement et le logement s'ajoutent au devis.</p>
      <h2>Langues</h2>
      <p class="muted">Grec · Anglais · Français · Néerlandais</p>
    </aside>
  </div>
</section>
""",
    },


    # ---------------------------------------------------------------- GUIDE
    "weddingguide": {
        "title": "Guide musique de mariage — Timeline &amp; questions à poser",
        "desc": "Guide gratuit pour la musique de votre mariage, par un DJ bruxellois : le déroulé de la journée, la liste des incontournables, dix questions à poser, et les prix réels en Belgique.",
        "kicker": "Guide gratuit",
        "h1": "Le guide de la <span class='gold'>musique de mariage</span>",
        "sub": "Le déroulé qui fait vivre une piste de danse, ce qu'il faut dire à votre DJ, et ce que coûte réellement un DJ de mariage en Belgique — écrit après neuf ans de terrain.",
        "body": """{GUIDE:WEDDING-GUIDE-FR}

<section class="section cta-band">
  <div class="wrap center">
    <h2>Vous préparez votre mariage ?</h2>
    <p>Donnez-moi votre date et votre lieu — je vous dirai honnêtement si je suis le bon DJ pour vous.</p>
    <a class="btn btn-gold" href="{link:contact}">Vérifier ma disponibilité</a>
  </div>
</section>
""",
    },


    "corporateguide": {
        "title": "Guide musique pour événements d'entreprise | DJ Orestis",
        "desc": "Guide gratuit pour les organisateurs d'événements d'entreprise : programmer la musique autour de votre agenda, gérer les discours, et réussir le passage à la piste de danse.",
        "kicker": "Guide gratuit",
        "h1": "Le guide musique des <span class='gold'>événements d'entreprise</span>",
        "sub": "Comment programmer la musique autour des discours, des remises de prix et d'une salle de quinze nationalités — par un DJ qui travaille les événements d'entreprise bruxellois.",
        "body": """{GUIDE:CORPORATE-PLAYBOOK-FR}

<section class="section cta-band">
  <div class="wrap center">
    <h2>Vous organisez un événement d'entreprise ?</h2>
    <p>Envoyez la date, le lieu et le nombre d'invités — vous recevrez une proposition claire, généralement endéans les 48 heures.</p>
    <a class="btn btn-gold" href="{link:contact}">Demander une proposition</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- PRIVACY
    "privacy": {
        "title": "Politique de confidentialité | DJORESTIS",
        "desc": "Politique de confidentialité de DJORESTIS.com : quelles données personnelles sont collectées via le formulaire de contact, comment elles sont utilisées, et vos droits en vertu du RGPD.",
        "h1": "Politique de confidentialité",
        "sub": "Courte, honnête, conforme au RGPD.",
        "body": """
<section class="section">
  <div class="wrap narrow legal">
    <h2>Qui suis-je</h2>
    <p>Ce site, djorestis.com, est exploité par Orestis Vasileiadis (DJ Orestis), Bruxelles, Belgique — TVA BE 0785.520.639 (« je », « moi »). Contact : <a href="mailto:info@djorestis.com">info@djorestis.com</a>.</p>
    <h2>Quelles données je collecte</h2>
    <p>Lorsque vous utilisez le formulaire de demande de devis, je reçois les informations que vous y introduisez : votre nom, votre adresse e-mail, votre numéro de téléphone facultatif et les détails de votre événement. Je les utilise dans un seul but : répondre à votre demande et préparer une proposition.</p>
    <h2>Ce que je ne fais pas</h2>
    <p>Je ne vends ni ne partage vos données avec des tiers à des fins de marketing. Je n'envoie pas de newsletters, sauf si vous demandez explicitement à être tenu informé. Ce site n'installe aucun cookie publicitaire.</p>
    <h2>Statistiques</h2>
    <p>Ce site peut utiliser des statistiques de fréquentation respectueuses de la vie privée afin de comprendre quelles pages sont utiles. Si des outils d'analyse nécessitant un consentement sont utilisés, celui-ci vous sera d'abord demandé.</p>
    <h2>Durée de conservation de vos données</h2>
    <p>Les e-mails de demande sont conservés le temps nécessaire au traitement de votre événement et à une gestion administrative raisonnable, puis supprimés sur simple demande.</p>
    <h2>Vos droits</h2>
    <p>En vertu du RGPD, vous pouvez à tout moment demander l'accès à vos données personnelles, leur rectification ou leur suppression — un simple e-mail suffit. Vous pouvez également introduire une réclamation auprès de l'Autorité de protection des données belge (<a href="https://www.autoriteprotectiondonnees.be" rel="noopener">autoriteprotectiondonnees.be</a>).</p>
  </div>
</section>
""",
    },
}
