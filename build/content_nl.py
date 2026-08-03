# Dutch content for DJORESTIS.com
# Translators: translate every visible string; keep all HTML tags, class names
# and {link:...} / {FORM} / {PLACEHOLDER_PHOTO} / {PLACEHOLDER_VIDEO} markers intact.

LANG = "nl"

STRINGS = {
    "tagline": "Uw evenement zoals u het droomt",
    "skip": "Naar de inhoud",
    "cta_quote": "Offerte aanvragen",
    "cta_services": "Bekijk diensten",
    "faq_heading": "Veelgestelde vragen",
    "facts_heading": "In het kort",
    "photo_ph": "Foto volgt binnenkort",
    "video_ph": "Video volgt binnenkort",
    "footer_sge": "Medeoprichter van",
    "footer_services": "Diensten",
    "footer_explore": "Ontdek",
    "footer_contact": "Contact",
    "footer_based": "Gevestigd in Brussel, België",
    "footer_areas": "Beschikbaar in België · Nederland · Frankrijk · Duitsland · VK · Griekenland",
    "footer_rights": "Alle rechten voorbehouden.",
    "whatsapp_label": "Chat via WhatsApp",
    "cookie": {
        "text": "Deze site gebruikt cookies, uitsluitend voor anonieme bezoekersstatistieken.",
        "accept": "Accepteren",
        "decline": "Weigeren",
    },
    "blog": {
        "index_title": "Blog — Verhalen & gidsen uit de DJ-booth | DJ Orestis",
        "index_desc": "Verhalen over evenementen en praktische gidsen van DJ Orestis: bedrijfsfeesten, bruiloften en Griekse avonden in Brussel en heel Europa.",
        "h1": "Vanuit de <span class='gold'>DJ-booth</span>",
        "sub": "Verhalen over evenementen, lessen uit de praktijk en praktische gidsen — bruiloften, bedrijfsavonden en Griekse feesten in heel Europa.",
        "read_more": "Lees het verhaal",
        "back": "Alle artikelen",
        "cta": "Plant u iets soortgelijks?",
    },
    "nav": {
        "home": "Home",
        "about": "Over mij",
        "services": "Diensten",
        "corporate": "Bedrijfsevenementen",
        "wedding": "Bruiloften & doopfeesten",
        "greek": "Griekse feesten",
        "party": "Privéfeesten",
        "fullpackage": "Totaalpakketten",
        "restaurant": "Restaurant DJ",
        "mykonos": "DJ in heel Europa",
        "blog": "Blog",
        "music": "Muziek",
        "events": "Eerdere evenementen",
        "contact": "Contact",
        "privacy": "Privacybeleid",
    },
    "form": {
        "name": "Uw naam *",
        "email": "E-mail *",
        "phone": "Telefoon / WhatsApp",
        "event_type": "Type evenement",
        "event_types": ["Bedrijfsevenement / receptie", "Bruiloft", "Doopfeest", "Privéfeest",
                        "Griekse avond / gemeenschapsevenement", "Club / zaalboeking", "Anders"],
        "date": "Datum van het evenement",
        "location": "Locatie",
        "location_ph": "Stad, land of zaal",
        "guests": "Aantal gasten",
        "budget": "Indicatief budget",
        "budget_ph": "Optioneel — helpt mij het voorstel op maat te maken",
        "extras": "Extra diensten gewenst",
        "x_sound": "Geluid & lichtinstallatie",
        "x_photo": "Fotografie",
        "x_video": "Video",
        "message": "Vertel mij over uw evenement",
        "message_ph": "De gelegenheid, de sfeer die u wenst, muzikale voorkeuren…",
        "submit": "Aanvraag versturen",
        "note": "U ontvangt een persoonlijk voorstel — meestal binnen 48 uur. Geheel vrijblijvend.",
        "sent": "Dank u wel! Uw aanvraag is verzonden. Ik neem spoedig contact met u op.",
        "error": "Er is iets misgegaan. Stuur mij in dat geval rechtstreeks een e-mail.",
        "mailto_subject": "Offerteaanvraag — DJORESTIS.com",
    },
}

PAGES = {
    # ---------------------------------------------------------------- HOME
    "home": {
        "title": "DJ in Brussel — Bedrijfsfeesten, Bruiloften & Griekse Feesten",
        "desc": "DJ in Brussel voor bedrijfsfeesten, bruiloften en Griekse feesten in België, Nederland, Frankrijk, Duitsland, het VK en Griekenland. Grieks, electronic, Afro, Latin & RnB. Uw evenement zoals u het droomt.",
        "kicker": "Brussel · België · Europa",
        "h1": "Uw evenement, <span class='gold'>zoals u het droomt</span>",
        "sub": "DJ Orestis — DJ in Brussel voor bedrijfsevenementen, bruiloften en onvergetelijke feesten. Grieks, electronic, Afro, Latin en RnB, gemixt voor uw publiek.",
        "body": """
<section class="section trustbar">
  <div class="wrap">
    <p class="kicker center">Zij gingen u voor</p>
    <ul class="client-list">
      <li>Freshfields</li><li>Boston Consulting Group</li><li>Brussels Greek Food Festival</li>
      <li>Papillon Schuman</li><li>AHEPA</li><li>Dames Hellènes</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>Wat ik voor <span class="gold">uw evenement</span> kan doen</h2>
    <div class="card-grid">
      <a class="card" href="{link:corporate}">
        <h3>Bedrijfsevenementen</h3>
        <p>Recepties, personeelsfeesten en merkmomenten voor bedrijven die klasse verwachten — van stijlvolle achtergrondmuziek tot een volle dansvloer.</p>
        <span class="card-more">DJ voor bedrijfsfeesten →</span>
      </a>
      <a class="card" href="{link:wedding}">
        <h3>Bruiloften &amp; doopfeesten</h3>
        <p>Griekse, internationale en gemengde vieringen. Eén DJ die beide kanten van de familie aanvoelt — en voor iedereen de dansvloer vult.</p>
        <span class="card-more">Bruiloft DJ →</span>
      </a>
      <a class="card" href="{link:greek}">
        <h3>Griekse feesten</h3>
        <p>De Griekse avond zoals het hoort: van laïkà tot eilandklassiekers tot moderne hits, voor gemeenschappen en vieringen in heel Europa.</p>
        <span class="card-more">Griekse DJ →</span>
      </a>
      <a class="card" href="{link:party}">
        <h3>Privéfeesten</h3>
        <p>Verjaardagen, jubilea en huisfeesten met een professionele open-format DJ — electronic, Afro, Latin, RnB en alles daartussen.</p>
        <span class="card-more">Feest DJ →</span>
      </a>
      <a class="card wide" href="{link:fullpackage}">
        <h3>Totaalpakketten voor evenementen</h3>
        <p>DJ, professioneel geluid &amp; licht, fotografie en video — één partner voor evenementen tot 500 gasten. Eén aanspreekpunt, één factuur, nul stress.</p>
        <span class="card-more">Ontdek het totaalpakket →</span>
      </a>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap split">
    <div>
      <h2>Negen jaar achter de draaitafels, <span class="gold">twee muziekhoofdsteden</span></h2>
      <p>Ik leerde het vak in het nachtleven van Mykonos — drie zomerseizoenen voor een van de meest veeleisende publieken van Europa — en verfijnde het gedurende zes jaar in Brussel, waar ik al vier jaar resident DJ ben bij Papillon Schuman.</p>
      <p>Vandaag draai ik bedrijfsrecepties voor kantoren als Freshfields en Boston Consulting Group, bruiloften in heel Europa, en de Griekse gemeenschapsevenementen die mijn naam maakten — van het Brussels Greek Food Festival tot studentenfeesten in Wenen, Leuven en Rijsel.</p>
      <a class="btn btn-ghost" href="{link:about}">Meer over mij</a>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section">
  <div class="wrap stats">
    <div class="stat"><span class="stat-n">9+</span><span class="stat-l">jaar ervaring</span></div>
    <div class="stat"><span class="stat-n">6</span><span class="stat-l">landen</span></div>
    <div class="stat"><span class="stat-n">5</span><span class="stat-l">muziekwerelden — Grieks, electronic, Afro, Latin, RnB</span></div>
    <div class="stat"><span class="stat-n">500</span><span class="stat-l">gasten — volledige productiecapaciteit</span></div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Plannen in de maak?</h2>
    <p>Vertel mij over uw evenement en ontvang een voorstel op maat — meestal binnen 48 uur.</p>
    <a class="btn btn-gold" href="{link:contact}">Offerte aanvragen</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- ABOUT
    "about": {
        "title": "Over DJ Orestis — DJ in Brussel, gevormd in het nachtleven van Mykonos",
        "desc": "DJ Orestis: 3 jaar in het nachtleven van Mykonos, 6 jaar in Brussel, resident DJ bij Papillon Schuman en medeoprichter van Sounds Greek Events. Bedrijfsfeesten, bruiloften en Griekse feesten in heel Europa.",
        "kicker": "De mens achter de draaitafels",
        "h1": "Over <span class='gold'>DJ Orestis</span>",
        "sub": "Van de beachclubs van Mykonos tot zakelijke recepties in Brussel — met één constante: een dansvloer die werkt.",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Het verhaal</h2>
      <p>Ik begon waar DJ's op de harde manier worden gevormd: <strong>Mykonos</strong>. Drie seizoenen in het nachtleven van het eiland leerden mij een internationaal publiek in seconden te lezen — want op Mykonos krijgt u geen minuten.</p>
      <p>Zes jaar geleden verhuisde ik naar <strong>Brussel</strong>, en de stad werd mijn thuisbasis. Vandaag ben ik resident DJ bij <strong>Papillon Schuman</strong> — inmiddels het vierde jaar — en draaide ik in zalen over de hele stad: La Place 33, Capital, Kosmos, YAYA, Meatropolis, Machina, AKT en meer. Elke zomer keer ik nog terug naar Mykonos voor gastoptredens.</p>
      <p>Naast het clubwerk bouwde ik een tweede specialiteit uit: <strong>evenementen</strong>. Ik richtte mee <a href="https://soundsgreekevents.be" rel="noopener">Sounds Greek Events</a> op, was tweemaal gastheer van het <strong>Brussels Greek Food Festival</strong> en werd dé DJ voor Griekse gemeenschappen in heel Europa — Wenen, Leuven, Rijsel en verder. De bedrijven volgden: ik draaide bedrijfsevenementen voor <strong>Freshfields</strong>, <strong>Boston Consulting Group</strong> en andere toonaangevende kantoren in Brussel.</p>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Hoe ik werk</h2>
    <div class="card-grid">
      <div class="card"><h3>Voorbereiding eerst</h3><p>Elk evenement begint met een gesprek: de gelegenheid, de gasten, de momenten die ertoe doen. De playlist wordt gebouwd voor uw zaal, niet gerecycleerd van de vorige.</p></div>
      <div class="card"><h3>De dansvloer lezen</h3><p>Een goede set is een dialoog. Ik houd de vloer voortdurend in de gaten en stuur in realtime bij — energie omhoog wanneer de zaal erom vraagt, elegantie wanneer het moment om verfijning vraagt.</p></div>
      <div class="card"><h3>Vijf muziekwerelden</h3><p>Grieks, electronic, Afro, Latin en RnB — echt, niet als symbolisch extraatje. Die reikwijdte is waarom gemengde en internationale publieken mijn specialiteit zijn.</p></div>
      <div class="card"><h3>Altijd professioneel</h3><p>Stipt, discreet, correct uitgerust en correct verzekerd. De standaard die zakelijke klanten verwachten — op elk evenement, ook privé.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    <h2>Gemeenschap &amp; cultuur</h2>
    <p>Muziek is ook mijn manier om iets terug te geven. Ik draai <strong>pro bono</strong> voor de Griekse Gemeenschap van Brussel, Dames Hellènes en Hellenic United Women, ondersteun het Grieks Koor van Brussel en lokale theatergroepen — ook met fotografie en video — en werk samen met het Argo Hellenic diplomatennetwerk, AHEPA en andere organisaties van de Griekse diaspora.</p>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Laten we over uw evenement praten</h2>
    <a class="btn btn-gold" href="{link:contact}">Offerte aanvragen</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- SERVICES
    "services": {
        "title": "DJ Diensten Brussel & België — Bedrijfsfeesten & Bruiloften",
        "desc": "Professionele DJ-diensten in Brussel en heel Europa: bedrijfsevenementen, bruiloften en doopfeesten, Griekse feesten, privévieringen, plus complete pakketten met geluid, licht, foto en video tot 500 gasten.",
        "kicker": "Wat ik aanbied",
        "h1": "Diensten",
        "sub": "Eén professionele partner, vijf specialiteiten — in België, Nederland, Frankrijk, Duitsland, het VK en Griekenland.",
        "body": """
<section class="section">
  <div class="wrap">
    <div class="svc-list">
      <a class="svc" href="{link:corporate}">
        <div><h2>Bedrijfsevenementen</h2>
        <p>Recepties, eindejaarsfeesten, productlanceringen en teamevents voor bedrijven in Brussel en daarbuiten. Stijlvolle achtergrondsets, naadloze ondersteuning van uw programma en een dansvloer die werkt wanneer het tijd is.</p></div>
        <span class="card-more">Meer informatie →</span>
      </a>
      <a class="svc" href="{link:wedding}">
        <div><h2>Bruiloften &amp; doopfeesten</h2>
        <p>De belangrijkste feesten van uw leven, met zorg behandeld: planningsgesprekken, playlists op maat, geluid voor ceremonie en diner, en een feest dat beide families op de dansvloer brengt.</p></div>
        <span class="card-more">Meer informatie →</span>
      </a>
      <a class="svc" href="{link:greek}">
        <div><h2>Griekse avonden &amp; gemeenschapsevenementen</h2>
        <p>Het authentieke Griekse feest — voor gemeenschappen, verenigingen en vieringen in heel Europa. Van zeibekiko-momenten tot zomerse eilandsets.</p></div>
        <span class="card-more">Meer informatie →</span>
      </a>
      <a class="svc" href="{link:party}">
        <div><h2>Privéfeesten</h2>
        <p>Verjaardagen, jubilea, afstudeerfeesten en huisfeesten met een open-format professional: electronic, Afro, Latin, RnB, Grieks en de klassiekers.</p></div>
        <span class="card-more">Meer informatie →</span>
      </a>
      <a class="svc" href="{link:fullpackage}">
        <div><h2>Totaalpakketten voor evenementen</h2>
        <p>DJ + professioneel geluid &amp; licht + fotografie + video, voor evenementen en kleine shows tot 500 personen. Eén aanspreekpunt, één opstelling, één factuur.</p></div>
        <span class="card-more">Meer informatie →</span>
      </a>
      <a class="svc" href="{link:restaurant}">
        <div><h2>Restaurant- &amp; zaalavonden</h2>
        <p>Terugkerende thema-avonden die een trouw publiek opbouwen — de formule achter mijn vierjarige residentie bij Papillon Schuman, nu ook beschikbaar voor uw zaak.</p></div>
        <span class="card-more">Meer informatie →</span>
      </a>
      <a class="svc" href="{link:mykonos}">
        <div><h2>Destination events in heel Europa</h2>
        <p>Een op Mykonos gevormde Griekse DJ voor evenementen in Nederland, Frankrijk, Duitsland, het VK en Griekenland — inclusief Mykonos zelf.</p></div>
        <span class="card-more">Meer informatie →</span>
      </a>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap narrow center">
    <h2>Over de grenzen heen</h2>
    <p>Gevestigd in Brussel, overal thuis: ik draai regelmatig in Nederland, Frankrijk, Duitsland, het VK en Griekenland. Voor evenementen buiten België worden reis en verblijf eenvoudig bij de offerte opgeteld — al het overige werkt precies hetzelfde.</p>
    <a class="btn btn-gold" href="{link:contact}">Offerte aanvragen</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- CORPORATE
    "corporate": {
        "title": "Bedrijfsfeest DJ in Brussel & België | DJ Orestis",
        "desc": "Bedrijfsfeest DJ in Brussel: recepties, personeelsfeesten, productlanceringen en zakelijke evenementen voor o.a. Freshfields en BCG. Professioneel, discreet, volledig geluid & licht mogelijk. België & Europa.",
        "kicker": "Zakelijke evenementen, tot in de puntjes",
        "h1": "Bedrijfsfeest DJ in <span class='gold'>Brussel</span>",
        "sub": "Muziek voor bedrijven die van hun DJ dezelfde standaard verwachten als van hun cateraar: Freshfields, Boston Consulting Group en andere toonaangevende kantoren gingen u voor.",
        "price": "Vanaf € 600 excl. btw", "price_note": "Enkel DJ — geluid &amp; licht apart geoffreerd", "price_amount": "600",
        "facts": [("Vanafprijs", "€ 600 excl. btw, enkel DJ"),
                  ("Gebruikelijke setduur", "4–6 uur, verlengbaar"),
                  ("Capaciteit", "Tot 500 gasten met volledige productie"),
                  ("Talen", "Grieks, Engels, Frans, Nederlands"),
                  ("Thuisbasis &amp; verplaatsing", "Brussel; heel België, en Europa op aanvraag"),
                  ("Opbouwtijd", "2–3 uur vóór aankomst van de gasten, discreet")],
        "service_type": "Bedrijfsfeest DJ",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Waarom bedrijven mij boeken</h2>
      <p>Een bedrijfsevenement kan op twee manieren mislukken: muziek waarvan niemand merkt dat ze fout zit, en muziek waarvan iedereen het merkt. Ik heb zes jaar in Brussel gewerkt om beide te voorkomen — op cocktailrecepties, eindejaarsfeesten, congresdiners en lanceringen voor internationale kantoren.</p>
      <ul class="ticks">
        <li><strong>Discretie en klasse</strong> — gepaste kledij, stipte opbouw, professionele omgang met uw gasten en uw management.</li>
        <li><strong>Oog voor het programma</strong> — toespraken, prijsuitreikingen en verrassingen landen op tijd; de muziek ademt mee met uw agenda, nooit erdoorheen.</li>
        <li><strong>Reikwijdte</strong> — verfijnde achtergrondsets tijdens het diner, internationale dansvloervullers erna; Grieks, electronic, Afro, Latin en RnB voor echt internationale teams.</li>
        <li><strong>Volledige productie indien gewenst</strong> — geluid en licht voor maximaal 500 gasten, plus fotografie en video via mijn <a href="{link:fullpackage}">totaalpakketten</a>.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Veelvoorkomende formats</h2>
    <div class="card-grid">
      <div class="card"><h3>Cocktailrecepties</h3><p>Elegante sets waarbij gesprekken mogelijk blijven — de energie in de zaal stijgt, de stemmen niet.</p></div>
      <div class="card"><h3>Personeels- &amp; eindejaarsfeesten</h3><p>Van dinersfeer tot een volle dansvloer — de opbouw die uw team verdient na een lang jaar.</p></div>
      <div class="card"><h3>Lanceringen &amp; merkmomenten</h3><p>Een geluidsidentiteit afgestemd op uw merk, getimed op uw programma, gecoördineerd met uw bureau.</p></div>
      <div class="card"><h3>Congressen &amp; diners</h3><p>Inloop- en uitloopmuziek, muzikale accenten tussen sessies, dinersets — betrouwbare AV-ondersteuning de hele dag.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Plant u een bedrijfsevenement?</h2>
    <p>Stuur de datum, de locatie en het aantal gasten — u ontvangt een helder voorstel, meestal binnen 48 uur.</p>
    <a class="btn btn-gold" href="{link:contact}">Zakelijke offerte aanvragen</a>
  </div>
</section>
""",
        "faq": [
            ("Voorziet u geluids- en lichtinstallatie voor bedrijfsevenementen?",
             "Ja. Via mijn totaalpakketten lever ik professioneel geluid en licht voor evenementen tot 500 gasten, zodat u geen aparte AV-leverancier nodig heeft. Ik kan ook werken met de vaste installatie van uw locatie."),
            ("Kunt u draaien voor een internationaal publiek met gemengde nationaliteiten?",
             "Dat is precies mijn specialiteit. Ik mix Grieks, electronic, Afro, Latin en RnB en pas mij in realtime aan de zaal aan — exact wat internationale teams in Brussel nodig hebben."),
            ("Reist u buiten Brussel voor zakelijke evenementen?",
             "Ja — overal in België, en naar Nederland, Frankrijk, Duitsland, het VK en Griekenland. Voor evenementen in het buitenland worden reis en verblijf bij de offerte opgeteld."),
            ("Hoe lang op voorhand kunnen we het best boeken?",
             "Voor het eindejaarsseizoen (november–december) is 2 à 3 maanden vooruit verstandig. Voor andere data volstaat doorgaans 4 tot 6 weken — maar vraag het gerust: last-minute oplossingen zijn vaak mogelijk."),
        ],
    },

    # ---------------------------------------------------------------- WEDDING
    "wedding": {
        "title": "Bruiloft DJ in Brussel — Griekse & Internationale Trouwfeesten",
        "desc": "Bruiloft DJ in Brussel en heel België voor Griekse, internationale en gemengde trouwfeesten en doopfeesten. Playlists op maat, van ceremonie tot laatste dans, geluid & licht inbegrepen indien gewenst.",
        "kicker": "Het belangrijkste feest van uw leven",
        "h1": "Bruiloft DJ in <span class='gold'>Brussel &amp; België</span>",
        "sub": "Griekse, internationale en prachtig gemengde trouwfeesten — één DJ die beide kanten van de zaal op hetzelfde ritme laat dansen.",
        "price": "Vanaf € 600 excl. btw", "price_note": "Enkel DJ — geluid &amp; licht apart geoffreerd", "price_amount": "600",
        "facts": [("Vanafprijs", "€ 600 excl. btw, enkel DJ"),
                  ("Dekt", "Ceremonie, diner en feest — één opstelling"),
                  ("Microfoons", "Draadloze microfoons voor geloften en toespraken inbegrepen"),
                  ("Capaciteit", "Tot 500 gasten met volledige productie"),
                  ("Talen", "Grieks, Engels, Frans, Nederlands"),
                  ("Voorbereiding", "Een planningsgesprek vóór elke bruiloft")],
        "service_type": "Bruiloft DJ",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Uw bruiloft, uw soundtrack</h2>
      <p>Geen twee bruiloften horen hetzelfde te klinken. We spreken elkaar vóór de grote dag, lopen elk moment door — ceremonie, entree, diner, openingsdans, feest — en bouwen de soundtrack rond uw verhaal en uw gasten.</p>
      <ul class="ticks">
        <li><strong>Gemengde &amp; internationale bruiloften</strong> — mijn thuisterrein. Grieks en Belgisch, Frans en Latin, elke combinatie: beide families samen op de dansvloer.</li>
        <li><strong>De Griekse momenten, zoals het hoort</strong> — kalamatianó waar grootouders hun goedkeuring aan geven, zeibekiko met de juiste ernst, eilandhits voor het zomergevoel.</li>
        <li><strong>Volledige begeleiding</strong> — geluid voor de ceremonie, draadloze microfoons voor toespraken, dinersfeer en het feest, in één vloeiend geheel.</li>
        <li><strong>Ook doopfeesten</strong> — stijlvolle familievieringen met dezelfde zorg, op maat van de dag.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Zo werkt het</h2>
    <div class="card-grid">
      <div class="card"><h3>1 · We praten</h3><p>Een ontspannen planningsgesprek: uw verhaal, uw must-plays, uw absolute no-go's, het tijdschema van de dag.</p></div>
      <div class="card"><h3>2 · Ik bereid voor</h3><p>Een programma op maat voor elke fase van het feest, afgestemd met uw locatie, fotograaf en weddingplanner.</p></div>
      <div class="card"><h3>3 · U viert</h3><p>Op de dag zelf werkt alles gewoon — u danst, ik regel de rest. Geluid en licht inbegrepen als u dat wenst.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Gaat u trouwen?</h2>
    <p>Geef mij uw datum en uw locatie — ik zeg u eerlijk of ik de juiste DJ ben voor uw bruiloft.</p>
    <a class="btn btn-gold" href="{link:contact}">Controleer mijn beschikbaarheid</a>
  </div>
</section>
""",
        "faq": [
            ("Draait u zowel Griekse als internationale bruiloften?",
             "Ja — en vooral bruiloften die beide zijn. Ik ben opgegroeid met Griekse muziek en heb jarenlang electronic, Afro, Latin en RnB gedraaid voor internationale publieken; gemengde bruiloften zijn dan ook waar ik het sterkst ben."),
            ("Verzorgt u ook de muziek voor de ceremonie en de toespraken?",
             "Ja. Ik dek de hele dag: geluid voor de ceremonie, draadloze microfoons voor geloften en toespraken, dinersfeer en het avondfeest — één opstelling, één aanspreekpunt."),
            ("Draait u ook bruiloften buiten België?",
             "Regelmatig — in Nederland, Frankrijk, Duitsland, het VK en Griekenland. Reis en verblijf worden bij de offerte opgeteld; al het overige blijft hetzelfde."),
            ("Kunnen we u een playlist en een niet-draaien-lijst bezorgen?",
             "Heel graag. Uw must-plays en no-go's vormen het skelet van de avond; mijn taak is daar de levende set omheen te bouwen en de dansvloer vol te houden."),
        ],
    },

    # ---------------------------------------------------------------- GREEK
    "greek": {
        "title": "Griekse DJ in Brussel — Griekse Feesten in heel Europa | DJ Orestis",
        "desc": "Griekse DJ in Brussel: authentieke Griekse avonden voor gemeenschappen, verenigingen en privévieringen in België en heel Europa. Gastheer van het Brussels Greek Food Festival, resident bij Papillon Schuman.",
        "kicker": "Ελληνικές βραδιές — het echte werk",
        "h1": "Griekse DJ in <span class='gold'>Brussel</span>",
        "sub": "Van het Brussels Greek Food Festival tot gemeenschapsfeesten in Wenen, Leuven en Rijsel — de Griekse avond, zoals ze verdient.",
        "price": "Vanaf € 600 excl. btw", "price_note": "Enkel DJ — geluid &amp; licht apart geoffreerd", "price_amount": "600",
        "facts": [("Vanafprijs", "€ 600 excl. btw, enkel DJ"),
                  ("Repertoire", "Laïkà, éntekhna, nisiótika, rebetiko, moderne Griekse hits"),
                  ("Gemengde avonden", "Griekse uren vermengd met Afro, Latin, RnB en internationaal"),
                  ("Presentatie", "Aankondigingen in het Grieks, Engels, Frans of Nederlands"),
                  ("Palmares", "Brussels Greek Food Festival ×2; gemeenschappen van Wenen, Leuven en Rijsel"),
                  ("Thuisbasis &amp; verplaatsing", "Brussel; heel België, Europa en Griekenland")],
        "service_type": "Griekse DJ",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>De DJ die de Griekse gemeenschap al kent</h2>
      <p>Voor de Griekse diaspora in België en daarbuiten ben ik waarschijnlijk geen nieuwe naam: ik was tweemaal gastheer van het <strong>Brussels Greek Food Festival</strong>, draaide voor <strong>Dames Hellènes</strong>, het <strong>Grieks Koor van Brussel</strong> en de <strong>Griekse gemeenschappen van Wenen, Leuven en Rijsel</strong>, en ik draai pro bono voor de Griekse Gemeenschap van Brussel en Hellenic United Women.</p>
      <p>Mijn residentie bij <strong>Papillon Schuman</strong> — al vier jaar op rij — is waar Brussel naartoe komt voor zijn Griekse avonden. En elke zomer ga ik naar huis: gastoptredens op <strong>Mykonos</strong>, waar ik het vak leerde.</p>
      <ul class="ticks">
        <li><strong>Het volledige Griekse spectrum</strong> — laïkà, éntekhna, nisiótika, rebetiko-momenten, klassiekers uit de jaren 90 en de hits van vandaag.</li>
        <li><strong>Echte zeibekiko-cultuur</strong> — de ruimte, het respect, de timing.</li>
        <li><strong>Gemengde avonden</strong> — Griekse uren die overvloeien in internationale sets, zodat elke gast erbij hoort.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Wie mijn Griekse avonden boekt</h2>
    <div class="card-grid">
      <div class="card"><h3>Gemeenschappen &amp; verenigingen</h3><p>Jaarlijkse bals, nationale feestdagen, benefieten en studentenfeesten in België en heel Europa.</p></div>
      <div class="card"><h3>Restaurants &amp; zalen</h3><p>Terugkerende Griekse avonden die een trouw publiek opbouwen — de formule van Papillon Schuman.</p></div>
      <div class="card"><h3>Families</h3><p>Bruiloften, doopfeesten en naamdagvieringen waar het Griekse repertoire gewoon juist moet zitten.</p></div>
      <div class="card"><h3>Bedrijven</h3><p>Bedrijfsavonden met Grieks thema — steeds populairder, verrassend doeltreffend.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Πάμε;</h2>
    <p>Vertel mij over uw Griekse avond — in het Grieks, Engels, Frans of Nederlands.</p>
    <a class="btn btn-gold" href="{link:contact}">Offerte aanvragen</a>
  </div>
</section>
""",
        "faq": [
            ("Draait u op Griekse avonden uitsluitend Griekse muziek?",
             "Alleen als u dat wenst. De meeste geslaagde Griekse avonden ademen: sterke Griekse uren, met Afro, Latin, RnB en internationale hits ertussen geweven, zodat elke gast — Grieks of niet — op de dansvloer blijft."),
            ("Reist u naar Griekse gemeenschappen buiten België?",
             "Ja — ik draai al voor de Griekse gemeenschappen van Wenen, Leuven en Rijsel, en ik ben beschikbaar in Nederland, Frankrijk, Duitsland, het VK en Griekenland. Reis en verblijf worden bij de offerte opgeteld."),
            ("Kunt u het evenement ook presenteren of aankondigen in het Grieks?",
             "Ja — aankondigingen en presentatie in het Grieks, Engels, Frans of Nederlands, naargelang wat uw publiek nodig heeft."),
        ],
    },

    # ---------------------------------------------------------------- PARTY
    "party": {
        "title": "Feest DJ in Brussel — Privéfeesten, Verjaardagen & Meer | DJ Orestis",
        "desc": "DJ voor privéfeesten in Brussel: verjaardagen, jubilea, afstudeerfeesten en vieringen met een professionele open-format DJ. Electronic, Afro, Latin, RnB en Grieks. Geluid & licht mogelijk. België & Europa.",
        "kicker": "Uw feest, professioneel luid",
        "h1": "Feest DJ in <span class='gold'>Brussel</span>",
        "sub": "Verjaardagen, jubilea, afstudeerfeesten, huisfeesten — energie van clubniveau, professionaliteit die ook in de huiskamer past.",
        "price": "Vanaf € 600 excl. btw", "price_note": "Enkel DJ — geluid &amp; licht apart geoffreerd", "price_amount": "600",
        "facts": [("Vanafprijs", "€ 600 excl. btw, enkel DJ"),
                  ("Formats", "Verjaardagen, jubilea, afstudeerfeesten, huisfeesten"),
                  ("Schaal", "Van een appartement tot een zaal met 500 gasten"),
                  ("Muziek", "Open format — electronic, Afro, Latin, RnB, Grieks, pop"),
                  ("Materiaal", "Compacte, appartementvriendelijke opstelling of volledige productie"),
                  ("Thuisbasis &amp; verplaatsing", "Brussel en heel België")],
        "service_type": "DJ voor privéfeesten",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Een echte DJ maakt het verschil</h2>
      <p>Een playlist kan uw dansvloer niet zien. Negen jaar club- en evenementenervaring — het nachtleven van Mykonos, residenties in Brussel, honderden privé-evenementen — betekent dat uw feest een professional krijgt die de zaal leest, verzoekjes elegant inpast en de energie precies houdt waar u ze wilt.</p>
      <ul class="ticks">
        <li><strong>Open format</strong> — electronic, Afro, Latin, RnB, Grieks, pop en de klassiekers, gemixt op maat van uw publiek.</li>
        <li><strong>Elke schaal</strong> — van een verjaardag in de huiskamer tot een gehuurde zaal met 500 gasten, met <a href="{link:fullpackage}">geluid &amp; licht inbegrepen</a> als u dat wenst.</li>
        <li><strong>Uw regels</strong> — must-plays, no-go's, verrassingsmomenten: we plannen het vooraf samen.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Heeft u al een datum in gedachten?</h2>
    <p>Vertel mij de gelegenheid en de locatie — ik zorg voor de rest.</p>
    <a class="btn btn-gold" href="{link:contact}">Offerte aanvragen</a>
  </div>
</section>
""",
        "faq": [
            ("Hoeveel kost een DJ voor een privéfeest in Brussel?",
             "Dat hangt af van de duur, de locatie en of u geluids- en lichtinstallatie nodig heeft. Stuur de basisgegevens via het contactformulier en u ontvangt een heldere, persoonlijke offerte — meestal binnen 48 uur, geheel vrijblijvend."),
            ("Brengt u uw eigen materiaal mee voor huisfeesten?",
             "Ja — ik kan een complete, appartementvriendelijke opstelling meebrengen, of volledig geluid en licht voor een gehuurde zaal tot 500 gasten. Beschrijf de ruimte en ik stel de juiste configuratie voor."),
            ("Neemt u verzoekjes aan tijdens het feest?",
             "Met plezier — verzoekjes horen bij een goed feest. Ik weef ze in wanneer ze de dansvloer dienen, en uw niet-draaien-lijst blijft altijd gerespecteerd."),
        ],
    },

    # ---------------------------------------------------------------- FULL PACKAGE
    "fullpackage": {
        "title": "Totaalpakket Evenementen Brussel — DJ, Geluid, Licht & Video",
        "desc": "Eén partner voor uw hele evenement in Brussel en daarbuiten: professionele DJ, geluid en licht voor maximaal 500 gasten, plus fotografie en video. Eén aanspreekpunt, één opstelling, één factuur.",
        "kicker": "Eén partner, het hele evenement",
        "h1": "Totaalpakketten voor <span class='gold'>evenementen</span>",
        "sub": "DJ + professioneel geluid &amp; licht + fotografie + video — voor evenementen en kleine shows tot 500 personen.",
        "price": "DJ vanaf € 600 excl. btw", "price_note": "Volledige productie per evenement geoffreerd", "price_amount": "600",
        "facts": [("Vanafprijs", "DJ vanaf € 600 excl. btw; productie per evenement geoffreerd"),
                  ("Maximale omvang", "500 gasten"),
                  ("Op aanvraag inbegrepen", "Geluid, licht, fotografie, video"),
                  ("Microfoons", "Draadloze microfoons voor toespraken en ceremonies"),
                  ("Coördinatie", "Technische planning met de locatie rechtstreeks geregeld"),
                  ("Facturatie", "Eén aanspreekpunt, één factuur voor het hele evenement")],
        "service_type": "Evenementproductie (DJ, geluid, licht, foto, video)",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Waarom één partner beter is dan vier leveranciers</h2>
      <p>Een DJ, een AV-bedrijf, een fotograaf en een videograaf coördineren betekent vier contracten, vier planningen en vier mensen die nog nooit hebben samengewerkt. Ik bied het alternatief: één team, één technisch plan, één persoon die verantwoordelijk is voor het slagen van de hele avond — ik.</p>
      <ul class="ticks">
        <li><strong>Professioneel geluid</strong> — op maat van uw zaal, van 20 tot 500 gasten, met draadloze microfoons voor toespraken en ceremonies.</li>
        <li><strong>Licht</strong> — elegant sfeerlicht voor recepties en diners, volledige dansvloerverlichting voor het feest.</li>
        <li><strong>Fotografie &amp; video</strong> — verslaggeving van uw evenement door een team dat al jaren culturele producties en theatergroepen ondersteunt.</li>
        <li><strong>Kleine shows &amp; producties</strong> — podiumgeluid en licht voor voorstellingen, gemeenschapsproducties en showcases.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Perfect voor</h2>
    <div class="card-grid">
      <div class="card"><h3>Bedrijfsrecepties</h3><p>Eén factuur en één verantwoordelijk aanspreekpunt — zoals de aankoopafdeling het graag ziet.</p></div>
      <div class="card"><h3>Bruiloften &amp; doopfeesten</h3><p>Muziek, microfoons, licht en herinneringen, gepland als één naadloze productie.</p></div>
      <div class="card"><h3>Gala's &amp; shows van verenigingen</h3><p>Podiumproducties, jaarlijkse bals en culturele avonden tot 500 personen.</p></div>
      <div class="card"><h3>Zaalevenementen</h3><p>Pop-upclubavonden en thema-avonden, volledig geproduceerd.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Beschrijf uw evenement</h2>
    <p>Aantal gasten, locatie, datum — u ontvangt één helder voorstel dat alles dekt.</p>
    <a class="btn btn-gold" href="{link:contact}">Offerte totaalpakket aanvragen</a>
  </div>
</section>
""",
        "faq": [
            ("Tot welke omvang kunt u een evenement volledig produceren?",
             "Tot 500 personen met professioneel geluid en licht. Naast de apparatuur omvat dat ook technische planning met uw locatie en opbouw en afbraak volgens uw tijdschema."),
            ("Kan ik ook slechts een deel van het pakket boeken?",
             "Uiteraard. Alleen DJ, DJ + geluid & licht, of het complete pakket met foto en video — de offerte wordt opgebouwd rond wat u werkelijk nodig heeft."),
            ("Regelt u de technische afstemming met de locatie?",
             "Ja — stroom, toegang, geluidsnormen, timing: ik overleg rechtstreeks met de locatie, zodat u niet tussen leveranciers hoeft te bemiddelen."),
        ],
    },

    # ---------------------------------------------------------------- RESTAURANT
    "restaurant": {
        "title": "Vaste DJ voor Restaurants & Bars in Brussel | DJ Orestis",
        "desc": "Boek een vaste DJ voor uw restaurant of bar in Brussel. Terugkerende thema-avonden die rustige weekdagen vullen en de baromzet verhogen. Al vier jaar resident bij Papillon Schuman. Proefavond mogelijk.",
        "kicker": "Voor restaurants & zalen",
        "h1": "Vaste DJ voor <span class='gold'>restaurants &amp; bars</span>",
        "sub": "Voor restaurant- en bareigenaars in Brussel: een terugkerende thema-avond die een rustige weekdag vult en de baromzet verhoogt — de formule achter mijn vierjarige residentie bij Papillon Schuman.",
        "price": "Vaste vergoeding per avond, geoffreerd per reeks", "price_note": "Proefavond mogelijk vóór elke verbintenis",
        "facts": [("Samenwerking", "Wekelijkse, maandelijkse of seizoensgebonden residentie"),
                  ("Proefperiode", "Eén proefavond, zonder langetermijnverbintenis"),
                  ("Dinerservice", "Volume op gespreksniveau tot de service afrondt"),
                  ("Materiaal", "Compact systeem meegebracht, of uw vaste installatie gebruikt"),
                  ("Bewezen formule", "Papillon Schuman, vier jaar op rij"),
                  ("Publiek", "Een gevestigde Griekse en internationale aanhang in Brussel")],
        "service_type": "Vaste DJ voor restaurants",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Waarom zou een restaurant een vaste DJ inhuren?</h2>
      <p>Een goede thema-avond is een commerciële troef: ze vult een rustige weekdag, bouwt een terugkerend publiek op dat vooraf tafels reserveert, en geeft uw zaak een reputatie die verder reikt dan de menukaart. Precies dat heb ik opgebouwd bij <strong>Papillon Schuman</strong> — al vier jaar, en het loopt door — en ik draaide in zalen over heel Brussel: La Place 33, Capital, Kosmos, YAYA, Meatropolis, Machina, AKT.</p>
      <ul class="ticks">
        <li><strong>Een concept, niet zomaar een DJ</strong> — we ontwerpen de avond samen: Griekse avonden, Latin-avonden, Afro &amp; RnB-sessies, of een elegant dinner-to-dance-format.</li>
        <li><strong>Volumediscipline</strong> — tijdens de dinerservice blijft een gesprek mogelijk; de energie stijgt pas wanneer de borden van tafel gaan.</li>
        <li><strong>Een publiek dat volgt</strong> — mijn vaste aanhang in Brussel komt met mij mee, zeker voor Griekse avonden.</li>
        <li><strong>Geen infrastructuur nodig</strong> — ik kan compact geluid en licht meebrengen, aangepast aan een restaurant.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Welk residentieformat past bij uw zaak?</h2>
    <div class="card-grid">
      <div class="card"><h3>Wekelijkse of maandelijkse residentie</h3><p>Een vaste avond met een eigen naam waar uw gasten naar uitkijken — de sterkste publieksbouwer.</p></div>
      <div class="card"><h3>Lancering van een Griekse avond</h3><p>Een beproefd concept: Griekse dinerservice die overvloeit in laïkà en eilandhits. Al jaren bewezen in Brussel.</p></div>
      <div class="card"><h3>Seizoensgebonden &amp; pop-up</h3><p>Terraszomers, feestelijke decemberprogrammering, eenmalige thema-avonden.</p></div>
      <div class="card"><h3>Privéverhuur van uw zaal</h3><p>Uw restaurant ontvangt een privé-evenement? Ik verzorg de volledige muzikale kant, <a href="{link:fullpackage}">productie inbegrepen</a>.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Runt u een restaurant, bar of hotel in Brussel?</h2>
    <p>Laten we praten over een proefavond — één avond, heldere cijfers, geen langetermijnverbintenis.</p>
    <a class="btn btn-gold" href="{link:contact}">Stel een proefavond voor</a>
  </div>
</section>
""",
        "faq": [
            ("Hoe werkt een DJ-residentie in een restaurant commercieel?",
             "Doorgaans een vaste vergoeding per avond, afgesproken als wekelijkse of maandelijkse reeks. We starten met een proefavond, zodat u het aantal couverts en de baromzet kunt meten vóór u zich aan een reeks verbindt."),
            ("Wordt de muziek niet te luid tijdens de dinerservice?",
             "Nee — dat is precies het vakmanschap. Dinersets blijven op gespreksniveau, met elegante programmering; het volume en de energie stijgen pas wanneer de service afrondt. Ik stem het systeem af op uw zaal."),
            ("Brengt u uw eigen materiaal mee?",
             "Indien nodig, ja — compact geluid en licht dat bij een restaurant past en discreet wordt opgebouwd. Heeft uw zaak een vaste installatie, dan werk ik daarmee."),
        ],
    },

    # ---------------------------------------------------------------- MYKONOS / EUROPE
    "mykonos": {
        "title": "Griekse DJ in heel Europa — Gevormd op Mykonos | DJ Orestis",
        "desc": "Boek een op Mykonos gevormde Griekse DJ voor destination events in heel Europa: bruiloften, bedrijfsfeesten en Griekse feesten in Nederland, Frankrijk, Duitsland, het VK en Griekenland — inclusief Mykonos zelf.",
        "kicker": "Thuisbasis Brussel, actief in heel Europa",
        "h1": "Griekse DJ in heel <span class='gold'>Europa</span>",
        "sub": "Gevormd in drie seizoenen Mykonos-nachtleven, gevestigd in Brussel en regelmatig onderweg: uw evenement hoeft niet in België te zijn om goed te klinken.",
        "price": "Vanaf € 600 excl. btw + reiskosten", "price_note": "Reis en verblijf worden apart vermeld", "price_amount": "600",
        "facts": [("Vanafprijs", "€ 600 excl. btw plus reis en verblijf"),
                  ("Landen", "België, Nederland, Frankrijk, Duitsland, VK, Oostenrijk, Griekenland"),
                  ("Materiaal in het buitenland", "Licht reizen met lokale apparatuur, of volledige productie dicht bij België"),
                  ("Griekse eilanden", "Elke zomer op Mykonos — vraag naar de seizoensdata"),
                  ("Talen", "Grieks, Engels, Frans, Nederlands")],
        "service_type": "DJ voor destination events",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Eén DJ, zes landen</h2>
      <p>Sommige evenementen vragen om een DJ die een specifiek publiek begrijpt — een Griekse bruiloft in Duitsland, een diasporagala in Wenen, een zakelijk zomerfeest in Amsterdam, een viering op Mykonos zelf. Voor precies zulke evenementen reis ik nu al: de <strong>Griekse studentengemeenschap van Wenen</strong>, de <strong>Griekse gemeenschappen van Leuven en Rijsel</strong>, en elke zomer <strong>gastoptredens op Mykonos</strong>, waar ik drie volledige seizoenen in het nachtleven van het eiland werkte.</p>
      <ul class="ticks">
        <li><strong>Eenvoudige logistiek</strong> — reis en verblijf worden transparant bij de offerte opgeteld; al het overige werkt precies zoals bij een boeking in Brussel.</li>
        <li><strong>Compacte of volledige opstelling</strong> — ik kan licht reizen en met lokale apparatuur werken, of volledige productie voorzien voor evenementen dicht bij België.</li>
        <li><strong>Mykonos-ervaring</strong> — voor destination weddings en feesten in Griekenland krijgt u een DJ die die zalen werkelijk heeft gedraaid en het ritme van het eiland kent.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Typische boekingen in het buitenland</h2>
    <div class="card-grid">
      <div class="card"><h3>Destination weddings</h3><p>Griekse en internationale bruiloften in Griekenland, Frankrijk en verder — inclusief Mykonos en de eilanden.</p></div>
      <div class="card"><h3>Diaspora-evenementen</h3><p>Gala's, nationale feestdagen en studentenfeesten voor Griekse gemeenschappen in heel Europa.</p></div>
      <div class="card"><h3>Zakelijke off-sites</h3><p>Bedrijfsretraites en zomerfeesten waar het team beter verdient dan een playlist.</p></div>
      <div class="card"><h3>Mykonos &amp; Griekenland</h3><p>Villafeesten, pre-weddingevenementen en gastoptredens in zalen tijdens het zomerseizoen.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Plant u een evenement in het buitenland?</h2>
    <p>Geef mij de stad en de datum — u ontvangt één heldere offerte, reis inbegrepen.</p>
    <a class="btn btn-gold" href="{link:contact}">Offerte aanvragen</a>
  </div>
</section>
""",
        "faq": [
            ("Welke landen bestrijkt u?",
             "België is mijn thuisbasis; ik draai regelmatig in Nederland, Frankrijk, Duitsland, het VK, Oostenrijk en Griekenland. Andere bestemmingen zijn mogelijk — vraag het gerust."),
            ("Hoe werkt de prijs voor evenementen buiten België?",
             "Hetzelfde honorarium als voor een Belgische boeking, plus transparante reis- en verblijfskosten die apart in de offerte staan. Voor Griekenland in de zomer ben ik vaak al ter plaatse — vraag naar mijn seizoensdata op Mykonos."),
            ("Kunt u draaien op een destination wedding op Mykonos of de Griekse eilanden?",
             "Ja — daar leerde ik het vak. Ik ken de locaties, het ritme van een trouwdag op een eiland, en hoe ik het Griekse repertoire combineer met een internationaal publiek."),
        ],
    },

    # ---------------------------------------------------------------- MUSIC
    "music": {
        "title": "Muziek & Sets — Grieks, Electronic, Afro, Latin & RnB | DJ Orestis",
        "desc": "Beluister DJ Orestis: vijf muziekwerelden — Grieks, electronic, Afro, Latin en RnB — gemixt voor bedrijfsfeesten, bruiloften en feesten in Brussel en heel Europa.",
        "kicker": "Beluister",
        "h1": "Vijf muziekwerelden, <span class='gold'>één DJ</span>",
        "sub": "De reikwijdte is het punt: wat uw publiek ook is, er is een set voor.",
        "body": """
<section class="section">
  <div class="wrap">
    <div class="card-grid">
      <div class="card"><h3>Grieks</h3><p>Laïkà, éntekhna, nisiótika, rebetiko, klassiekers uit de jaren 90 en de hitlijsten van vandaag — het volledige spectrum, met de culturele feeling om te weten wat wanneer juist is.</p></div>
      <div class="card"><h3>Electronic</h3><p>House, deep en melodieuze sets, gevormd door drie seizoenen op Mykonos — van zonsondergangelegantie tot peak-time energie.</p></div>
      <div class="card"><h3>Afro</h3><p>Afrobeats, afro house en amapiano — de sound die de moderne Europese dansvloeren beheerst.</p></div>
      <div class="card"><h3>Latin</h3><p>Reggaeton, salsa, bachata en Latin pop — gegarandeerde dansvloervullers voor internationale publieken.</p></div>
      <div class="card"><h3>RnB</h3><p>Klassieke en hedendaagse RnB en hiphop — het bindweefsel van elke goede open-format set.</p></div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Sets &amp; aftermovies</h2>
    <p class="center muted">Nieuwe opnames zijn onderweg — in tussentijd kunt u mij elke maand live horen bij Papillon Schuman in Brussel.</p>
    <div class="media-grid">
      {PLACEHOLDER_VIDEO}
      {PLACEHOLDER_VIDEO}
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Wilt u deze sound op uw evenement?</h2>
    <a class="btn btn-gold" href="{link:contact}">Offerte aanvragen</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- EVENTS
    "events": {
        "title": "Eerdere Evenementen & Residenties — DJ Orestis | Brussel & Europa",
        "desc": "Een selectie van evenementen van DJ Orestis: residentie bij Papillon Schuman, Brussels Greek Food Festival, bedrijfsfeesten voor Freshfields en BCG, Griekse gemeenschapsfeesten in Wenen, Leuven en Rijsel, gastoptredens op Mykonos.",
        "kicker": "Referenties",
        "h1": "Eerdere evenementen &amp; <span class='gold'>residenties</span>",
        "sub": "Negen jaar, honderden avonden. Een selectie.",
        "body": """
<section class="section">
  <div class="wrap">
    <div class="events-cols">
      <div>
        <h2>Residenties &amp; zalen</h2>
        <ul class="event-list">
          <li><strong>Papillon Schuman</strong> — resident DJ, 4e jaar <span class="muted">· Brussel</span></li>
          <li><strong>La Place 33</strong> <span class="muted">· Brussel</span></li>
          <li><strong>Capital</strong> <span class="muted">· Brussel</span></li>
          <li><strong>Kosmos</strong> <span class="muted">· Brussel</span></li>
          <li><strong>YAYA</strong> <span class="muted">· Brussel</span></li>
          <li><strong>Meatropolis</strong> <span class="muted">· Brussel</span></li>
          <li><strong>Machina</strong> <span class="muted">· Brussel</span></li>
          <li><strong>AKT</strong> <span class="muted">· Brussel</span></li>
          <li><strong>Mykonos</strong> — jaarlijkse gastoptredens; 3 volledige seizoenen in het nachtleven van het eiland</li>
        </ul>
      </div>
      <div>
        <h2>Zakelijk</h2>
        <ul class="event-list">
          <li><strong>Freshfields</strong> — bedrijfsevenementen <span class="muted">· Brussel</span></li>
          <li><strong>Boston Consulting Group</strong> — bedrijfsevenementen <span class="muted">· Brussel</span></li>
          <li>Andere grote bedrijven in Brussel <span class="muted">· referenties op aanvraag</span></li>
        </ul>
        <h2>Festivals &amp; gemeenschap</h2>
        <ul class="event-list">
          <li><strong>Brussels Greek Food Festival</strong> — huis-DJ, twee edities</li>
          <li><strong>Dames Hellènes</strong> — evenementen &amp; vieringen</li>
          <li><strong>Grieks Koor van Brussel</strong></li>
          <li><strong>Griekse studentengemeenschap Wenen</strong> — feesten <span class="muted">· Oostenrijk</span></li>
          <li><strong>Griekse gemeenschap Leuven</strong> — feesten</li>
          <li><strong>Griekse gemeenschap Rijsel</strong> — feesten <span class="muted">· Frankrijk</span></li>
          <li><strong>Griekse Gemeenschap van Brussel</strong> — pro bono</li>
          <li><strong>Hellenic United Women</strong> — pro bono</li>
          <li><strong>Argo Hellenic Diplomat Network, AHEPA</strong> — samenwerkingen</li>
        </ul>
      </div>
    </div>
    <p class="muted">Meer evenementengeschiedenis vindt u bij <a href="https://soundsgreekevents.be" rel="noopener">Sounds Greek Events</a>, dat ik mee oprichtte.</p>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Uw evenement kan het volgende zijn</h2>
    <a class="btn btn-gold" href="{link:contact}">Offerte aanvragen</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- CONTACT
    "contact": {
        "title": "Boek DJ Orestis — Offerte Aanvragen | Brussel, België & Europa",
        "desc": "Boek DJ Orestis voor uw bedrijfsfeest, bruiloft of feest in Brussel, België of waar dan ook in Europa. Vul het offerteformulier in en ontvang een persoonlijk voorstel, meestal binnen 48 uur.",
        "kicker": "Laten we praten",
        "h1": "Vraag een <span class='gold'>offerte</span> aan",
        "sub": "Hoe meer u mij vertelt, hoe preciezer het voorstel. Meestal antwoord binnen 48 uur — altijd geheel vrijblijvend.",
        "body": """
<section class="section">
  <div class="wrap split-form">
    <div>
      {FORM}
    </div>
    <aside class="contact-aside">
      <h2>Rechtstreeks contact</h2>
      <p><a href="mailto:info@djorestis.com">info@djorestis.com</a></p>
      <p class="muted">Gevestigd in Brussel, België.<br>Beschikbaar in België, Nederland, Frankrijk, Duitsland, het VK en Griekenland — voor evenementen in het buitenland worden reis en verblijf bij de offerte opgeteld.</p>
      <h2>Talen</h2>
      <p class="muted">Grieks · Engels · Frans · Nederlands</p>
    </aside>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- PRIVACY
    "privacy": {
        "title": "Privacybeleid | DJORESTIS",
        "desc": "Privacybeleid van DJORESTIS.com: welke persoonsgegevens via het contactformulier worden verzameld, hoe ze worden gebruikt, en uw rechten onder de AVG (GDPR).",
        "h1": "Privacybeleid",
        "sub": "Kort, eerlijk en conform de AVG.",
        "body": """
<section class="section">
  <div class="wrap narrow legal">
    <h2>Wie ik ben</h2>
    <p>Deze website, djorestis.com, wordt beheerd door Orestis Vasileiadis (DJ Orestis), Brussel, België — btw BE 0785.520.639 ("ik", "mij"). Contact: <a href="mailto:info@djorestis.com">info@djorestis.com</a>.</p>
    <h2>Welke gegevens ik verzamel</h2>
    <p>Wanneer u het offerteformulier gebruikt, ontvang ik de informatie die u invult: uw naam, e-mailadres, optioneel telefoonnummer en de details van uw evenement. Ik gebruik deze voor één doel: uw aanvraag beantwoorden en een voorstel opstellen.</p>
    <h2>Wat ik niet doe</h2>
    <p>Ik verkoop of deel uw gegevens niet met derden voor marketingdoeleinden. Ik verstuur geen nieuwsbrieven tenzij u daar uitdrukkelijk om vraagt. Deze site plaatst geen advertentiecookies.</p>
    <h2>Statistieken</h2>
    <p>Deze site kan privacyvriendelijke bezoekersstatistieken gebruiken om te begrijpen welke pagina's nuttig zijn. Wanneer statistieken worden gebruikt waarvoor toestemming vereist is, wordt u eerst om toestemming gevraagd.</p>
    <h2>Hoe lang ik uw gegevens bewaar</h2>
    <p>E-mails met aanvragen worden bewaard zolang dat nodig is om uw evenement af te handelen en voor een redelijke administratie, en worden op verzoek verwijderd.</p>
    <h2>Uw rechten</h2>
    <p>Onder de AVG kunt u op elk moment inzage, correctie of verwijdering van uw persoonsgegevens vragen — één e-mail volstaat. U kunt ook een klacht indienen bij de Belgische Gegevensbeschermingsautoriteit (<a href="https://www.gegevensbeschermingsautoriteit.be" rel="noopener">gegevensbeschermingsautoriteit.be</a>).</p>
  </div>
</section>
""",
    },
}
