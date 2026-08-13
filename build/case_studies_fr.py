# Études de cas clients pour DJORESTIS.com (FR).
# Consommé par build/generate.py — ne pas lancer la génération depuis ici.
#
# ---------------------------------------------------------------------------
# AVERTISSEMENT D'HONNÊTETÉ — À LIRE AVANT TOUTE MODIFICATION OU PUBLICATION
# ---------------------------------------------------------------------------
# Cas 1 "corporate-year-end-reception-brussels"  -> CAS COMPOSITE ANONYMISÉ.
# Cas 2 "greek-belgian-wedding-two-families"     -> CAS COMPOSITE ANONYMISÉ.
#
#   Ces deux cas ne sont PAS le compte rendu d'un événement réel précis. Ce
#   sont des composites construits à partir de plusieurs réservations
#   comparables, écrits pour illustrer la manière dont le travail est
#   réellement mené. Délibérément, ils ne contiennent : aucun nom de client ou
#   de couple, aucune date, aucun nom de salle, aucune affirmation vérifiable
#   de fréquentation pour un événement nommé, aucun prix ni récompense, aucune
#   métrique, et AUCUNE citation de client (le champ "quote" vaut "" pour les
#   deux, et doit le rester tant qu'aucune citation réelle et autorisée n'est
#   reçue). Chacun des deux porte un paragraphe de divulgation affiché à la fin
#   de son champ "outcome". Ne supprimez pas ce paragraphe. Si vous ajoutez un
#   jour une étude de cas réelle et nominative, créez-lui sa propre entrée
#   plutôt que de modifier celles-ci.
#
# Cas 3 "papillon-schuman-greek-night-residency" -> RÉEL.
#   Il s'agit de la résidence de DJ d'Orestis lui-même, quatre années durant, au
#   Papillon Schuman à Bruxelles. L'établissement est nommé parce qu'il s'agit
#   de sa propre résidence et qu'il peut en parler de première main. La citation
#   de ce cas est faite de ses propres mots, et lui est attribuée — pas à
#   l'établissement ni à un client. Les résultats restent volontairement
#   observationnels : aucun chiffre d'affaires, aucun nombre de couverts, aucun
#   pourcentage.
#
# Faits maison que rien ici ne peut contredire :
#   prix de départ 600 € HTVA (DJ seul) · jusqu'à 500 invités en production
#   complète · langues : grec, anglais, français, néerlandais.
# ---------------------------------------------------------------------------

CASES = [

    # ------------------------------------------------ 1. COMPOSITE — ENTREPRISE
    {
        "slug": "corporate-year-end-reception-brussels",
        "title": "Étude de cas : réception de fin d'année à Bruxelles",
        "desc": "Comment la réception de fin d'année d'un cabinet international à Bruxelles est passée des discours à une piste de danse comble, sans perdre la salle.",
        "h1": "Du mode réception à une <span class='gold'>piste de danse comble</span>",
        "sub": "Une soirée de fin d'année pour un cabinet international à Bruxelles, où la partie officielle devait se dérouler impeccablement — et où la salle devait tout de même finir par danser.",
        "client": "Cabinet international de services professionnels",
        "event_type": "Réception de fin d'année et fête du personnel",
        "guests": "Environ 200",
        "location": "Bruxelles, Belgique",
        "services": "DJ, sonorisation, micros sans fil pour les discours, éclairage de piste",

        "challenge": """
<p>Un cabinet international installé à Bruxelles réserve une soirée par an pour remercier ses équipes. Environ 200 invités, plus d'une douzaine de nationalités dans la salle, et un programme avec du contenu réel : un mot d'accueil de la direction, des discours et une remise de prix. Le brief de l'équipe événementielle était celui que j'entends le plus souvent — <strong>de l'élégance d'abord, mais il faut que les gens dansent vraiment</strong>.</p>
<p>Quatre éléments rendaient cela plus difficile qu'il n'y paraît :</p>
<ul>
<li><strong>Deux événements dans une seule salle.</strong> Une réception debout avec un programme officiel, puis une fête — même espace, mêmes invités, à environ une heure d'intervalle.</li>
<li><strong>L'intelligibilité des discours.</strong> Une remise de prix et des remerciements ne servent à rien si le fond de la salle n'entend pas, et un système réglé uniquement pour la musique gère rarement bien un micro main.</li>
<li><strong>Un public réellement international.</strong> Aucun répertoire national de valeurs sûres n'aurait suffi à couvrir cette salle.</li>
<li><strong>Des collègues, pas des inconnus.</strong> Personne n'a acheté de ticket, chacun se tient à côté de son manager, et personne n'a envie d'être le premier sur une piste vide.</li>
</ul>
""",

        "approach": """
<p>La préparation a commencé par le programme, pas par la playlist. J'ai demandé le déroulé par écrit à l'équipe événementielle — ouverture des portes, mot d'accueil, dîner ou walking dinner, discours, remise de prix et heure de fin souhaitée — puis j'ai réglé les détails pratiques directement avec la salle et le traiteur : électricité, accès, limites de bruit, et créneau d'installation. Le montage et les balances étaient terminés bien avant l'ouverture des portes, si bien qu'aucun invité n'a jamais vu passer un câble.</p>
<ul>
<li><strong>Une sonorisation pensée d'abord pour la parole.</strong> Le système a été configuré pour qu'un micro main sans fil sonne clair et maîtrisé partout dans la salle ; la musique vient ensuite s'installer dans cette même configuration. Une seule installation couvre toute la soirée, donc aucun changement de matériel.</li>
<li><strong>L'accueil et le dîner au niveau de la conversation.</strong> Une programmation chaleureuse et discrète, qui donne à la salle un sentiment de soin et laisse les gens parler sans hausser la voix. La musique s'effaçait proprement pour chaque intervenant et revenait sous les applaudissements.</li>
<li><strong>Une transition construite, pas un hasard.</strong> Le passage du programme à la fête a été pensé comme une séquence : d'abord des morceaux familiers, à tempo moyen, immédiatement reconnaissables. Les premiers titres de la piste servent à donner la permission, pas à faire découvrir.</li>
<li><strong>Une colonne vertébrale internationale.</strong> Un set qui traverse les valeurs sûres internationales avec des clins d'œil délibérés aux différents coins de la salle — un classique français, un refrain italien repris en chœur, une séquence latino, un moment grec — pour que chacun entende qu'on a pensé à son côté du bureau. Les annonces peuvent se faire en grec, en anglais, en français ou en néerlandais, selon ce dont la salle a besoin.</li>
<li><strong>Repérer les entraîneurs.</strong> Chaque entreprise compte trois ou quatre personnes dont la danse donne à toutes les autres la permission d'y aller. C'est pour elles que se jouent les vingt premières minutes de la fête.</li>
</ul>
<p>Le client a pris le DJ ainsi que le son et la lumière, afin de n'avoir qu'un seul interlocuteur pour tout le volet musical et technique de la soirée ; la même soirée peut aussi se dérouler en <a href="{link:fullpackage}">formule tout compris</a> lorsqu'une entreprise préfère briefer un prestataire unique pour l'ensemble.</p>
""",

        "outcome": """
<p>Le soir même, la partie officielle s'est déroulée sans le moindre problème de micro : les discours et la remise de prix étaient audibles depuis le fond de la salle, et la musique revenait chaque fois sous les applaudissements plutôt que de démarrer à froid.</p>
<p>La transition a fonctionné comme elle doit fonctionner lorsqu'elle a été construite plutôt qu'espérée. Le premier titre reconnaissable a sorti une poignée de personnes, les entraîneurs ont suivi en un ou deux morceaux, les vestes sont tombées, et <strong>la piste s'est remplie après les discours et est restée pleine jusqu'à la fin de la soirée</strong>.</p>
<ul>
<li>Les invités sont restés jusqu'au bout au lieu de s'éclipser une fois le dîner desservi.</li>
<li>La piste ne s'est pas vidée entre les morceaux — le signe habituel d'un rythme juste.</li>
<li>Les demandes sont venues de plusieurs nationalités différentes présentes dans la salle, ce qui est la vraie mesure du bon fonctionnement d'un set international.</li>
<li>L'équipe événementielle n'a plus rien eu à gérer côté technique une fois la soirée lancée.</li>
</ul>
<p><strong>À propos de cette étude de cas :</strong> il s'agit d'un cas composite anonymisé, construit à partir de plusieurs réceptions d'entreprise comparables à Bruxelles, et non du compte rendu d'un événement précis. Les informations clients restent confidentielles par professionnalisme : aucune entreprise, aucune salle ni aucune date n'est citée, et aucun chiffre n'est présenté comme le résultat d'une soirée particulière. Vous préparez une réception d'entreprise ? <a href="{link:corporate}">Découvrez comment se déroule une réservation d'entreprise</a> ou <a href="{link:contact}">écrivez-moi</a> avec votre date, votre lieu et le nombre de participants.</p>
""",

        "quote": "",
        "quote_by": "",
    },

    # -------------------------------------------------- 2. COMPOSITE — MARIAGE
    {
        "slug": "greek-belgian-wedding-two-families",
        "title": "Étude de cas : un mariage gréco-belge, deux familles",
        "desc": "Un mariage gréco-belge en Belgique : de la cérémonie à la fin de soirée, kalamatianó et zeïbékiko tissés aux tubes internationaux pour deux familles.",
        "h1": "Une seule piste de danse pour <span class='gold'>deux familles</span>",
        "sub": "Un mariage gréco-belge en Belgique, de la cérémonie jusqu'à la fin de soirée, où deux ensembles d'attentes musicales devaient devenir une seule et même nuit.",
        "client": "Un couple gréco-belge se mariant en Belgique",
        "event_type": "Mariage — cérémonie, dîner et soirée dansante",
        "guests": "Environ 150",
        "location": "Domaine à la campagne, en Belgique",
        "services": "DJ de la cérémonie à la dernière danse, micros pour la cérémonie et les discours, son et lumière de piste",

        "challenge": """
<p>Une famille grecque, dont une bonne partie fait le déplacement pour le mariage. Une famille belge, arrivée des quatre coins du pays. Environ 150 invités au total, un seul lieu, et une journée qui va de la cérémonie au dîner puis à la soirée dansante. Pendant les appels de préparation, le couple a dit ce que presque tous les couples de cultures mixtes disent : <strong>nous avons peur qu'un côté danse et que l'autre regarde</strong>.</p>
<p>La vraie difficulté n'était pas le répertoire, mais la structure :</p>
<ul>
<li><strong>Deux idées différentes de ce à quoi ressemble un mariage.</strong> Un côté attend que les moments grecs soient faits dans les règles — kalamatianó, un zeïbékiko avec la gravité qu'il mérite, les laïkà en fin de soirée. L'autre attend les valeurs sûres internationales qu'il associe à un mariage.</li>
<li><strong>Le piège des blocs.</strong> Traitez la soirée comme une heure grecque suivie d'une heure internationale, et la salle se coupe en deux — exactement ce que le couple redoutait.</li>
<li><strong>Le timing entre les générations.</strong> Les danses grecques traditionnelles comptent le plus pour les invités les plus susceptibles de partir tôt : les programmer tard, c'est risquer de ne plus avoir la bonne salle pour eux.</li>
<li><strong>Une seule journée, plusieurs situations techniques.</strong> Les vœux et les lectures, les discours pendant le dîner, puis une vraie fête — sans le moindre moment où le couple doit penser au matériel.</li>
</ul>
""",

        "approach": """
<p>Nous nous sommes rencontrés avant le mariage et nous avons parcouru la journée moment par moment : cérémonie, entrée, dîner, première danse, moments grecs, soirée, dernier morceau. Les deux familles ont fourni leur <strong>liste d'incontournables et d'interdits</strong> — la liste des interdits fait généralement plus de travail que celle des incontournables.</p>
<ul>
<li><strong>Tisser plutôt que cloisonner.</strong> Le set passe des morceaux grecs aux morceaux internationaux avec des tempos raccordés aux jointures, pour que la salle n'ait jamais l'impression d'être cédée d'une famille à l'autre. Un classique grec glisse vers un titre avec lequel chaque invité belge a grandi, et le passage de frontière ne se remarque pas.</li>
<li><strong>Les moments grecs placés à dessein.</strong> Le kalamatianó a été programmé pendant que toute la salle, grands-parents compris, était encore là — une danse en ronde est le moyen le plus simple, pour des invités qui n'en connaissent pas les pas, de participer malgré tout, les mains sur les épaules.</li>
<li><strong>Le zeïbékiko traité avec respect.</strong> Convenu à l'avance avec la personne qui le danse, piste dégagée, cercle formé, aucune annonce par-dessus. Ce n'est pas un morceau de fête et il ne se joue pas comme tel.</li>
<li><strong>Une seule installation, toute la journée.</strong> Micros pour les vœux et les discours, ambiance du dîner et système de soirée : le tout traité comme une installation unique, pour que rien ne doive être remonté en pleine célébration.</li>
<li><strong>Un déroulé avec du jeu.</strong> Convenu à l'avance avec le traiteur et le photographe, et volontairement souple : si la salle est prête pour la première danse plus tôt que prévu, la bonne réponse est de l'avancer.</li>
<li><strong>Des annonces dans les langues de la salle.</strong> Grec, anglais, français ou néerlandais, selon les personnes à qui l'on s'adresse.</li>
</ul>
<p>Des mariages comme celui-ci sont exactement la raison pour laquelle le <a href="{link:wedding}">service mariage</a> et le <a href="{link:greek}">répertoire grec</a> sont construits comme ils le sont.</p>
""",

        "outcome": """
<p>La soirée s'est comportée comme un set tissé doit se comporter. La piste s'est peuplée dès la première danse et l'est restée — des morceaux internationaux vers les morceaux grecs et retour — au lieu de se remplir et de se vider par vagues successives.</p>
<ul>
<li>La ronde du kalamatianó réunissait des invités des deux familles, dont plusieurs qui n'en avaient jamais dansé et que leurs voisins de chaque côté ont entraînés.</li>
<li>Le zeïbékiko a été regardé en silence par une salle dont la moitié des invités n'en avait jamais vu, et les applaudissements qui ont suivi n'ont eu besoin d'aucune explication.</li>
<li>Les invités les plus âgés des deux côtés sont restés nettement plus tard que le couple ne l'avait prévu.</li>
<li>On n'a pas posé au couple une seule question technique entre la cérémonie et le dernier morceau.</li>
</ul>
<p><strong>À propos de cette étude de cas :</strong> il s'agit d'un cas composite anonymisé, construit à partir de plusieurs mariages gréco-belges et d'autres mariages mixtes, et non du compte rendu d'un mariage précis. Par respect pour la vie privée des couples, aucun nom, aucune date ni aucun lieu n'est mentionné, et rien ici n'est présenté comme le résultat mesuré d'une journée particulière. Vous préparez un mariage — grec, belge, ou magnifiquement les deux ? <a href="{link:contact}">Parlons-en</a> et dessinons ensemble la forme de votre journée.</p>
""",

        "quote": "",
        "quote_by": "",
    },

    # ----------------------------------------- 3. RÉEL — RÉSIDENCE EN ÉTABLISSEMENT
    {
        "slug": "papillon-schuman-greek-night-residency",
        "title": "Étude de cas : quatre ans de soirées grecques à Bruxelles",
        "desc": "Comment une soirée grecque récurrente au Papillon Schuman, dans le quartier européen, a grandi en quatre ans — une étude de cas pour restaurants et bars.",
        "h1": "Quatre ans de <span class='gold'>soirées grecques</span> au Papillon Schuman",
        "sub": "Une étude de cas côté établissement : ce qui arrive à un restaurant-bar quand une soirée à thème cesse d'être une expérience et devient un rendez-vous que les clients planifient.",
        "client": "Papillon Schuman — restaurant et bar grec, quartier européen, Bruxelles",
        "event_type": "Soirée grecque récurrente, DJ résident",
        "guests": "Du service du dîner jusqu'au public du bar en fin de soirée",
        "location": "Schuman, Bruxelles",
        "services": "DJ résident, soirée à thème récurrente, programmation du service du dîner jusque tard dans la nuit",

        "challenge": """
<p>Le Papillon Schuman se trouve à quelques pas du rond-point Schuman, au cœur du quartier européen. La salle est grecque, le public ne l'est pas uniquement : fonctionnaires européens, consultants, anciens Erasmus qui ne sont jamais repartis, habitués belges et familles en visite depuis la Grèce. C'est un restaurant et un bar en même temps, et les deux attendent des choses différentes de la musique.</p>
<p>Le problème d'un établissement comme celui-là n'est pas de réserver un DJ. C'est que <strong>les soirées DJ ponctuelles ne construisent rien</strong>. Un bon vendredi est un bon vendredi ; il ne donne à personne une raison de revenir à une date précise. À cela s'ajoute :</p>
<ul>
<li><strong>La musique peut coûter de l'argent à un restaurant.</strong> Jouez trop fort trop tôt et les tables raccourcissent : les clients sautent le dessert et s'en vont. Le service du dîner doit rester propice à la conversation.</li>
<li><strong>Une soirée à thème doit être un vrai concept.</strong> « La musique grecque » est un genre ; une soirée grecque est une promesse sur ce que la soirée va faire ressentir.</li>
<li><strong>La salle doit basculer.</strong> Le même espace doit fonctionner comme salle à manger à 21h et comme piste de danse plus tard, sans qu'on demande à quiconque de se déplacer.</li>
<li><strong>La régularité est la partie difficile.</strong> Les habitués reviennent : le même set ne peut donc pas être rejoué, et une semaine faible coûte plus de confiance qu'une excellente semaine n'en rapporte.</li>
</ul>
""",

        "approach": """
<p>La soirée a été conçue comme un rendez-vous récurrent plutôt que comme une série de réservations, et le format s'est affiné sur quatre années consécutives derrière ces platines — environ deux cents soirées dans la même salle.</p>
<ul>
<li><strong>Un créneau fixe et répétable.</strong> Une soirée que les clients peuvent inscrire à leur agenda, c'est tout le mécanisme. La date est le produit ; la musique est la façon dont elle tient sa promesse.</li>
<li><strong>Le volume comme forme d'hospitalité.</strong> Le service du dîner se joue au niveau de la conversation — laïkà chaleureux, programmation aux accents rebétiko, sonorités des îles. L'énergie ne monte qu'une fois les assiettes parties. C'est cette discipline qui donne à l'établissement l'envie de rappeler le DJ.</li>
<li><strong>Lire les tables, pas la piste.</strong> Dans un restaurant-bar, la piste de danse naît aux tables. Quand les épaules commencent à bouger pendant le dîner, la piste est à une dizaine de minutes, et le set doit être prêt.</li>
<li><strong>Une colonne vertébrale grecque avec des passerelles internationales.</strong> Le grec au centre, avec les moments internationaux, latino et RnB qui gardent ensemble une salle mixte du quartier européen au lieu de la diviser.</li>
<li><strong>Travailler comme membre de l'équipe de la maison.</strong> Avec les propriétaires sur la programmation, avec le personnel de salle sur le timing, avec le bar quand une grande tablée change la physionomie de la soirée.</li>
<li><strong>Des arcs, pas des playlists.</strong> Un arc de dîner en lente montée, un arc de table d'anniversaire, un arc de mardi calme. Les habitués repèrent immédiatement les répétitions, ce qui garde l'ensemble honnête.</li>
</ul>
<p>Pour un établissement qui part de zéro, la même formule commence par une soirée pilote — une seule soirée, un format clair, aucun engagement de longue durée — avant de convenir quoi que ce soit sous forme de série. C'est ainsi que se met en place une <a href="{link:restaurant}">résidence en restaurant ou en bar</a>.</p>
""",

        "outcome": """
<p>Le résultat le plus parlant est le plus simple : <strong>la soirée a continué d'avoir lieu</strong>. Quatre années consécutives, dans la même salle, avec le même DJ résident — un établissement ne reconduit pas une soirée année après année si elle ne fonctionne pas pour lui.</p>
<p>Vu depuis les platines, en termes observables, cela ressemble à ceci :</p>
<ul>
<li>Les mêmes visages reviennent, et ils demandent au personnel quand aura lieu la prochaine plutôt que d'attendre de l'apprendre.</li>
<li>Les clients amènent du monde — des parents en visite, des collègues du bureau, des amis qui n'ont jamais entendu de musique grecque de leur vie.</li>
<li>La salle bascule de façon fiable : le service du dîner se termine et l'on danse dans le même espace, presque chaque semaine, sans que rien ne soit annoncé.</li>
<li>Les habitués belges demandent aujourd'hui des chansons grecques par leur nom, ce qui est long à construire et constitue le signe le plus clair que le concept a pris.</li>
<li>La soirée fait désormais partie de la manière dont les clients eux-mêmes décrivent l'établissement, et pas seulement de son calendrier.</li>
</ul>
<p>Rien de tout cela n'arrive dès la première soirée. Cela apparaît autour de la troisième ou de la quatrième répétition, et c'est exactement pour cette raison que les soirées récurrentes sont plus performantes pour un établissement que les réservations ponctuelles.</p>
<p>Vous gérez un restaurant, un bar ou un hôtel à Bruxelles et vous voulez tester ? <a href="{link:contact}">Proposez une soirée pilote</a> — une seule soirée, vos propres chiffres, aucun engagement au-delà.</p>
""",

        "quote": "Une soirée ponctuelle offre à un établissement un bon vendredi. Une soirée récurrente donne aux gens une raison de revenir — et cela ne commence à se voir qu'à la troisième ou quatrième fois.",
        "quote_by": "DJ Orestis, DJ résident au Papillon Schuman",
    },
]
