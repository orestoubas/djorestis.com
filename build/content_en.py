# English content for DJORESTIS.com
# Translators: translate every visible string; keep all HTML tags, class names
# and {link:...} / {FORM} / {PLACEHOLDER_PHOTO} / {PLACEHOLDER_VIDEO} markers intact.

LANG = "en"

STRINGS = {
    "tagline": "Your event as you dream it",
    "skip": "Skip to content",
    "cta_quote": "Request a quote",
    "cta_services": "View services",
    "faq_heading": "Frequently asked questions",
    "facts_heading": "At a glance",
    "testimonials_heading": "What clients say",
    "signup": {
        "wedding": {
            "title": "Free wedding music planning guide",
            "text": "The timeline that makes a wedding dance floor work, a must-play / never-play worksheet, and ten questions worth asking any DJ before you book.",
            "placeholder": "Your email address",
            "button": "Send me the guide",
            "note": "One email with the guide, then a few genuinely useful ones. Unsubscribe any time.",
        },
        "corporate": {
            "title": "Free corporate event music playbook",
            "text": "How to programme music around your agenda — arrival, dinner, speeches, and the transition to dancing that most events get wrong.",
            "placeholder": "Your work email address",
            "button": "Send me the playbook",
            "note": "One email with the playbook, then a few genuinely useful ones. Unsubscribe any time.",
        },
    },
    "photo_ph": "Photo coming soon",
    "video_ph": "Video coming soon",
    "footer_sge": "Co-founder of",
    "footer_services": "Services",
    "footer_explore": "Explore",
    "footer_contact": "Contact",
    "footer_based": "Based in Brussels, Belgium",
    "footer_areas": "Available in Belgium · Netherlands · France · Germany · UK · Greece",
    "footer_rights": "All rights reserved.",
    "whatsapp_label": "Chat on WhatsApp",
    "cookie": {
        "text": "This site uses cookies for anonymous visitor statistics only.",
        "accept": "Accept",
        "decline": "Decline",
    },
    "blog": {
        "index_title": "Blog — Stories & Guides from the Booth | DJ Orestis",
        "index_desc": "Event stories and practical guides from DJ Orestis: corporate parties, weddings and Greek nights in Brussels and across Europe.",
        "h1": "From the <span class='gold'>booth</span>",
        "sub": "Event stories, lessons learned and practical guides — weddings, corporate nights and Greek parties across Europe.",
        "read_more": "Read the story",
        "back": "All articles",
        "cta": "Planning something similar?",
    },
    "nav": {
        "home": "Home",
        "about": "About",
        "services": "Services",
        "corporate": "Corporate events",
        "wedding": "Weddings & baptisms",
        "greek": "Greek parties",
        "party": "Private parties",
        "fullpackage": "Full-package solutions",
        "restaurant": "Restaurant DJ",
        "mykonos": "DJ across Europe",
        "blog": "Blog",
        "weddingguide": "Wedding music guide",
        "corporateguide": "Corporate music playbook",
        "press": "Press & media",
        "music": "Music",
        "events": "Past events",
        "contact": "Contact",
        "privacy": "Privacy policy",
    },
    "form": {
        "name": "Your name *",
        "email": "Email *",
        "phone": "Phone / WhatsApp",
        "event_type": "Type of event",
        "event_types": ["Corporate event / reception", "Wedding", "Baptism", "Private party",
                        "Greek night / community event", "Club / venue booking", "Other"],
        "date": "Event date",
        "location": "Location",
        "location_ph": "City, country or venue",
        "guests": "Number of guests",
        "budget": "Indicative budget",
        "budget_ph": "Optional — helps me tailor the proposal",
        "extras": "Extra services needed",
        "x_sound": "Sound & light equipment",
        "x_photo": "Photography",
        "x_video": "Video",
        "message": "Tell me about your event",
        "message_ph": "The occasion, the atmosphere you want, music preferences…",
        "submit": "Send request",
        "note": "You will receive a personalised proposal — usually within 48 hours. No obligation.",
        "sent": "Thank you! Your request has been sent. I will get back to you shortly.",
        "error": "Something went wrong. Please email me directly instead.",
        "mailto_subject": "Quote request — DJORESTIS.com",
    },
}

PAGES = {
    # ---------------------------------------------------------------- HOME
    "home": {
        "title": "DJ in Brussels — Corporate Events, Weddings & Greek Parties",
        "desc": "Brussels-based DJ for corporate events, weddings and Greek parties across Belgium, the Netherlands, France, Germany, the UK and Greece. Greek, electronic, Afro, Latin & RnB. Your event as you dream it.",
        "kicker": "Brussels · Belgium · Europe",
        "h1": "Your event, <span class='gold'>as you dream it</span>",
        "sub": "DJ Orestis — Brussels-based DJ for corporate events, weddings and unforgettable parties. Greek, electronic, Afro, Latin and RnB, mixed for your crowd.",
        "body": """
<section class="section trustbar">
  <div class="wrap">
    <p class="kicker center">Trusted by</p>
    <ul class="client-list">
      <li>Freshfields</li><li>Boston Consulting Group</li><li>Brussels Greek Food Festival</li>
      <li>Papillon Schuman</li><li>AHEPA</li><li>Dames Hellènes</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>What I can do for <span class="gold">your event</span></h2>
    <div class="card-grid">
      <a class="card" href="{link:corporate}">
        <h3>Corporate events</h3>
        <p>Receptions, staff parties and brand moments for companies that expect polish — from background elegance to a packed dance floor.</p>
        <span class="card-more">Corporate event DJ →</span>
      </a>
      <a class="card" href="{link:wedding}">
        <h3>Weddings &amp; baptisms</h3>
        <p>Greek, international and mixed celebrations. One DJ who reads both sides of the family — and fills the floor for all of them.</p>
        <span class="card-more">Wedding DJ →</span>
      </a>
      <a class="card" href="{link:greek}">
        <h3>Greek parties</h3>
        <p>The Greek night done properly: from laïkà to island classics to modern hits, for communities and celebrations across Europe.</p>
        <span class="card-more">Greek DJ →</span>
      </a>
      <a class="card" href="{link:party}">
        <h3>Private parties</h3>
        <p>Birthdays, anniversaries and house parties with a professional open-format DJ — electronic, Afro, Latin, RnB and everything between.</p>
        <span class="card-more">Party DJ →</span>
      </a>
      <a class="card wide" href="{link:fullpackage}">
        <h3>Full-package event solutions</h3>
        <p>DJ, professional sound &amp; light, photography and video — one partner for events up to 500 guests. One contact, one invoice, zero stress.</p>
        <span class="card-more">Discover the full package →</span>
      </a>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap split">
    <div>
      <h2>Nine years behind the decks, <span class="gold">two music capitals</span></h2>
      <p>I learned my craft in the nightlife of Mykonos — three summer seasons reading some of the most demanding crowds in Europe — and refined it over six years in Brussels, where I hold a residency at Papillon Schuman, now in its fourth year.</p>
      <p>Today I play corporate receptions for firms like Freshfields and Boston Consulting Group, weddings across Europe, and the Greek community events that made my name — from the Brussels Greek Food Festival to student parties in Vienna, Leuven and Lille.</p>
      <a class="btn btn-ghost" href="{link:about}">More about me</a>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section">
  <div class="wrap stats">
    <div class="stat"><span class="stat-n">9+</span><span class="stat-l">years of experience</span></div>
    <div class="stat"><span class="stat-n">6</span><span class="stat-l">countries served</span></div>
    <div class="stat"><span class="stat-n">5</span><span class="stat-l">music worlds — Greek, electronic, Afro, Latin, RnB</span></div>
    <div class="stat"><span class="stat-n">500</span><span class="stat-l">guests — full production capacity</span></div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Planning something?</h2>
    <p>Tell me about your event and receive a tailored proposal — usually within 48 hours.</p>
    <a class="btn btn-gold" href="{link:contact}">Request a quote</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- ABOUT
    "about": {
        "title": "About DJ Orestis — Brussels-Based DJ, Trained in Mykonos Nightlife",
        "desc": "DJ Orestis: 3 years in Mykonos nightlife, 6 years in Brussels, resident DJ at Papillon Schuman and co-founder of Sounds Greek Events. Corporate events, weddings and Greek parties across Europe.",
        "kicker": "The person behind the decks",
        "h1": "About <span class='gold'>DJ Orestis</span>",
        "sub": "From Mykonos beach clubs to Brussels boardroom receptions — one constant: a dance floor that works.",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>The story</h2>
      <p>I started where DJs are forged the hard way: <strong>Mykonos</strong>. Three seasons in the island's nightlife taught me to read an international crowd in seconds — because on Mykonos, you don't get minutes.</p>
      <p>Six years ago I moved to <strong>Brussels</strong>, and the city became my home base. Today I hold a residency at <strong>Papillon Schuman</strong> — now in its fourth year — and I've played rooms across the city: La Place 33, Capital, Kosmos, YAYA, Meatropolis, Machina, AKT and more. Every summer I still return to Mykonos for guest sets.</p>
      <p>Alongside club work, I built a second specialty: <strong>events</strong>. I co-founded <a href="https://soundsgreekevents.be" rel="noopener">Sounds Greek Events</a>, hosted the <strong>Brussels Greek Food Festival</strong> twice, and became the go-to DJ for Greek communities across Europe — Vienna, Leuven, Lille and beyond. Companies followed: I've played corporate events for <strong>Freshfields</strong>, <strong>Boston Consulting Group</strong> and other major firms in Brussels.</p>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>How I work</h2>
    <div class="card-grid">
      <div class="card"><h3>Preparation first</h3><p>Every event starts with a conversation: the occasion, the guests, the moments that matter. The playlist is built for your room, not recycled from the last one.</p></div>
      <div class="card"><h3>Reading the floor</h3><p>A great set is a dialogue. I watch the floor constantly and adjust in real time — energy up when the room asks for it, elegance when the moment calls for restraint.</p></div>
      <div class="card"><h3>Five music worlds</h3><p>Greek, electronic, Afro, Latin and RnB — genuinely, not as tokens. That range is why mixed and international crowds are my speciality.</p></div>
      <div class="card"><h3>Professional, always</h3><p>Punctual, discreet, properly equipped and properly insured. The standard corporate clients expect — brought to every event, including private ones.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    <h2>Community &amp; culture</h2>
    <p>Music is also how I give back. I play <strong>pro bono</strong> for the Brussels Greek Community, Dames Hellènes and Hellenic United Women, support the Greek Choir of Brussels and local theatre groups — including with photography and video — and cooperate with the Argo Hellenic diplomat network, AHEPA and other organisations of the Greek diaspora.</p>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Let's talk about your event</h2>
    <a class="btn btn-gold" href="{link:contact}">Request a quote</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- SERVICES
    "services": {
        "title": "DJ Services in Brussels & Belgium — Corporate & Weddings",
        "desc": "Professional DJ services in Brussels and across Europe: corporate events, weddings and baptisms, Greek parties, private celebrations, plus full sound, light, photo and video packages for up to 500 guests.",
        "kicker": "What I offer",
        "h1": "Services",
        "sub": "One professional partner, five specialities — in Belgium, the Netherlands, France, Germany, the UK and Greece.",
        "body": """
<section class="section">
  <div class="wrap">
    <div class="svc-list">
      <a class="svc" href="{link:corporate}">
        <div><h2>Corporate events</h2>
        <p>Receptions, end-of-year parties, product launches and team events for companies in Brussels and beyond. Elegant background sets, seamless programme support and a dance floor that works when it's time.</p></div>
        <span class="card-more">Learn more →</span>
      </a>
      <a class="svc" href="{link:wedding}">
        <div><h2>Weddings &amp; baptisms</h2>
        <p>The most important parties of your life, handled with care: planning meetings, tailored playlists, ceremony and dinner sound, and a celebration that brings both families to the floor.</p></div>
        <span class="card-more">Learn more →</span>
      </a>
      <a class="svc" href="{link:greek}">
        <div><h2>Greek nights &amp; community events</h2>
        <p>The authentic Greek party — for communities, associations and celebrations across Europe. From zeibekiko moments to island summer sets.</p></div>
        <span class="card-more">Learn more →</span>
      </a>
      <a class="svc" href="{link:party}">
        <div><h2>Private parties</h2>
        <p>Birthdays, anniversaries, graduations and house parties with an open-format professional: electronic, Afro, Latin, RnB, Greek and the classics.</p></div>
        <span class="card-more">Learn more →</span>
      </a>
      <a class="svc" href="{link:fullpackage}">
        <div><h2>Full-package event solutions</h2>
        <p>DJ + professional sound &amp; light + photography + video, for events and small shows up to 500 people. One contact, one setup, one invoice.</p></div>
        <span class="card-more">Learn more →</span>
      </a>
      <a class="svc" href="{link:restaurant}">
        <div><h2>Restaurant &amp; venue nights</h2>
        <p>Recurring themed nights that build a loyal crowd — the formula behind my four-year residency at Papillon Schuman, available for your venue.</p></div>
        <span class="card-more">Learn more →</span>
      </a>
      <a class="svc" href="{link:mykonos}">
        <div><h2>Destination events across Europe</h2>
        <p>A Mykonos-trained Greek DJ for events in the Netherlands, France, Germany, the UK and Greece — including Mykonos itself.</p></div>
        <span class="card-more">Learn more →</span>
      </a>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap narrow center">
    <h2>Across borders</h2>
    <p>Based in Brussels, at home everywhere: I regularly play in the Netherlands, France, Germany, the UK and Greece. For events outside Belgium, travel and accommodation are simply added to the quote — everything else works exactly the same.</p>
    <a class="btn btn-gold" href="{link:contact}">Request a quote</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- CORPORATE
    "corporate": {
        "title": "Corporate Event DJ in Brussels & Belgium | DJ Orestis",
        "desc": "Corporate event DJ in Brussels: receptions, staff parties, product launches and business events for companies including Freshfields and BCG. Professional, discreet, full sound & light available. Belgium & Europe.",
        "kicker": "Business events, done right",
        "h1": "Corporate event DJ in <span class='gold'>Brussels</span>",
        "sub": "Music for companies that expect the same standard from their DJ as from their caterer: Freshfields, Boston Consulting Group and other leading firms already do.",
        "price": "From €600 excl. VAT", "price_note": "DJ only — sound &amp; lighting quoted separately", "price_amount": "600",
        "facts": [("Starting price", "€600 excl. VAT, DJ only"),
                  ("Typical set length", "4–6 hours, extendable"),
                  ("Guest capacity", "Up to 500 with full production"),
                  ("Languages", "Greek, English, French, Dutch"),
                  ("Base &amp; travel", "Brussels; all of Belgium, and Europe on request"),
                  ("Setup time", "2–3 hours before doors, discreetly")],
        "service_type": "Corporate event DJ",
        "signup": "corporate",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Why companies book me</h2>
      <p>A corporate event has two failure modes: music nobody notices going wrong, and music everybody notices going wrong. I've spent six years in Brussels making sure neither happens — at cocktail receptions, end-of-year parties, conference dinners and launches for international firms.</p>
      <ul class="ticks">
        <li><strong>Discretion and polish</strong> — appropriate dress, punctual setup, professional conduct with your guests and your leadership.</li>
        <li><strong>Programme awareness</strong> — speeches, awards and surprises land on time; the music breathes around your agenda, never over it.</li>
        <li><strong>Range</strong> — sophisticated background sets during dinner, international floor-fillers after; Greek, electronic, Afro, Latin and RnB for genuinely international teams.</li>
        <li><strong>Full production if needed</strong> — sound and light for up to 500 guests, plus photography and video through my <a href="{link:fullpackage}">full-package solutions</a>.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Typical formats</h2>
    <div class="card-grid">
      <div class="card"><h3>Cocktail receptions</h3><p>Elegant, conversation-friendly sets that raise the energy of the room without raising voices.</p></div>
      <div class="card"><h3>Staff &amp; end-of-year parties</h3><p>From dinner ambience to a full dance floor — the arc your team deserves after a long year.</p></div>
      <div class="card"><h3>Launches &amp; brand moments</h3><p>Sound identity matched to your brand, timed to your programme, coordinated with your agency.</p></div>
      <div class="card"><h3>Conferences &amp; dinners</h3><p>Walk-in and walk-out music, session stings, dinner sets — reliable AV support all day.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Planning a company event?</h2>
    <p>Send the date, venue and headcount — you'll receive a clear proposal, usually within 48 hours.</p>
    <a class="btn btn-gold" href="{link:contact}">Request a corporate quote</a>
    <p class="muted" style="margin-top:18px">Planning it yourself first? Read the free <a href="{link:corporateguide}">corporate event music playbook</a>, or see a <a href="/case-studies/corporate-year-end-reception-brussels/">year-end reception case study</a>.</p>
  </div>
</section>
""",
        "faq": [
            ("Do you provide sound and lighting equipment for corporate events?",
             "Yes. Through my full-package solutions I provide professional sound and lighting for events up to 500 guests, so you don't need a separate AV supplier. I can also work with your venue's installed system."),
            ("Can you play for an international, mixed-nationality audience?",
             "That is my speciality. I mix Greek, electronic, Afro, Latin and RnB and adapt in real time to the room — exactly what international teams in Brussels need."),
            ("Do you travel outside Brussels for business events?",
             "Yes — anywhere in Belgium, and to the Netherlands, France, Germany, the UK and Greece. For events abroad, travel and accommodation are added to the quote."),
            ("How far in advance should we book?",
             "For end-of-year season (November–December), 2–3 months ahead is wise. For other dates, 4–6 weeks is usually comfortable — but ask anyway; last-minute solutions are often possible."),
        ],
    },

    # ---------------------------------------------------------------- WEDDING
    "wedding": {
        "title": "Wedding DJ in Brussels & Belgium — Greek & International",
        "desc": "Wedding DJ in Brussels and across Belgium for Greek, international and mixed weddings and baptisms. Tailored playlists, ceremony to last dance, sound & light included if needed. Also NL, FR, DE, UK, GR.",
        "kicker": "The most important party of your life",
        "h1": "Wedding DJ in <span class='gold'>Brussels &amp; Belgium</span>",
        "sub": "Greek, international and beautifully mixed weddings — one DJ who gets both sides of the room dancing to the same beat.",
        "price": "From €600 excl. VAT", "price_note": "DJ only — sound &amp; lighting quoted separately", "price_amount": "600",
        "facts": [("Starting price", "€600 excl. VAT, DJ only"),
                  ("Covers", "Ceremony, dinner and party — one setup"),
                  ("Microphones", "Wireless mics for vows and speeches included"),
                  ("Guest capacity", "Up to 500 with full production"),
                  ("Languages", "Greek, English, French, Dutch"),
                  ("Planning", "A preparation meeting before every wedding")],
        "service_type": "Wedding DJ",
        "signup": "wedding",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Your wedding, your soundtrack</h2>
      <p>No two weddings should sound the same. We meet before the big day, walk through every moment — ceremony, entrance, dinner, first dance, party — and build the soundtrack around your story and your guests.</p>
      <ul class="ticks">
        <li><strong>Mixed &amp; international weddings</strong> — my home ground. Greek and Belgian, French and Latin, any combination: both families on the floor, together.</li>
        <li><strong>The Greek moments, done properly</strong> — kalamatianó that grandparents approve of, zeibekiko with the right gravity, island hits for the summer feeling.</li>
        <li><strong>Full coverage</strong> — ceremony sound, wireless microphones for speeches, dinner ambience and the party, one seamless flow.</li>
        <li><strong>Baptisms too</strong> — elegant family celebrations with the same care, scaled to the day.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>How it works</h2>
    <div class="card-grid">
      <div class="card"><h3>1 · We talk</h3><p>A relaxed planning conversation: your story, your must-plays, your never-plays, the timeline of the day.</p></div>
      <div class="card"><h3>2 · I prepare</h3><p>A tailored programme for every phase of the celebration, coordinated with your venue, photographer and planner.</p></div>
      <div class="card"><h3>3 · You celebrate</h3><p>On the day, everything simply works — you dance, I handle the rest. Sound and light included if you need it.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Getting married?</h2>
    <p>Tell me your date and your venue — I'll tell you honestly if I'm the right DJ for your wedding.</p>
    <a class="btn btn-gold" href="{link:contact}">Check my availability</a>
    <p class="muted" style="margin-top:18px">Still planning? The free <a href="{link:weddingguide}">wedding music planning guide</a> covers the timeline, and this <a href="/case-studies/greek-belgian-wedding-two-families/">Greek-Belgian wedding case study</a> shows how a mixed room works.</p>
  </div>
</section>
""",
        "faq": [
            ("Do you DJ both Greek and international weddings?",
             "Yes — and especially weddings that are both. I grew up in Greek music and spent years playing electronic, Afro, Latin and RnB for international crowds, so mixed weddings are where I'm strongest."),
            ("Can you provide music for the ceremony and speeches as well?",
             "Yes. I cover the full day: ceremony sound, wireless microphones for vows and speeches, dinner ambience and the evening party — one setup, one contact."),
            ("Do you play weddings outside Belgium?",
             "Regularly — in the Netherlands, France, Germany, the UK and Greece. Travel and accommodation are added to the quote; everything else stays the same."),
            ("Can we give you a playlist and a do-not-play list?",
             "Please do. Your must-plays and never-plays are the skeleton of the night; my job is to build the living set around them and keep the floor full."),
        ],
    },

    # ---------------------------------------------------------------- GREEK
    "greek": {
        "title": "Greek DJ in Brussels — Greek Parties Across Europe | DJ Orestis",
        "desc": "Greek DJ in Brussels: authentic Greek nights for communities, associations and private celebrations across Belgium and Europe. Host of the Brussels Greek Food Festival, resident at Papillon Schuman.",
        "kicker": "Ελληνικές βραδιές — the real thing",
        "h1": "Greek DJ in <span class='gold'>Brussels</span>",
        "sub": "From the Brussels Greek Food Festival to community parties in Vienna, Leuven and Lille — the Greek night, done the way it deserves.",
        "price": "From €400 excl. VAT", "price_note": "Within Brussels — travel added beyond", "price_amount": "400",
        "facts": [("Starting price", "€400 excl. VAT within Brussels, DJ only"),
                  ("Repertoire", "Laïkà, éntekhna, nisiótika, rebetiko, modern Greek hits"),
                  ("Mixed nights", "Greek hours blended with Afro, Latin, RnB and international"),
                  ("Hosting", "Announcements in Greek, English, French or Dutch"),
                  ("Track record", "Brussels Greek Food Festival ×2; Vienna, Leuven, Lille communities"),
                  ("Base &amp; travel", "Brussels; across Belgium, Europe and Greece")],
        "service_type": "Greek DJ",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>The DJ the Greek community already knows</h2>
      <p>For the Greek diaspora in Belgium and beyond, I'm probably not a new name: I've hosted the <strong>Brussels Greek Food Festival</strong> twice, played for <strong>Dames Hellènes</strong>, the <strong>Greek Choir of Brussels</strong> and the <strong>Vienna, Leuven and Lille Greek communities</strong>, and I play pro bono for the Brussels Greek Community and Hellenic United Women.</p>
      <p>My residency at <strong>Papillon Schuman</strong> — four years running — is where Brussels comes for its Greek nights. And every summer, I go home: guest sets in <strong>Mykonos</strong>, where I learned the craft.</p>
      <ul class="ticks">
        <li><strong>The full Greek spectrum</strong> — laïkà, éntekhna, nisiótika, rebetiko moments, 90s classics and today's hits.</li>
        <li><strong>Real zeibekiko culture</strong> — the space, the respect, the timing.</li>
        <li><strong>Mixed nights</strong> — Greek hours flowing into international sets, so every guest belongs.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Who books my Greek nights</h2>
    <div class="card-grid">
      <div class="card"><h3>Communities &amp; associations</h3><p>Annual balls, national holidays, fundraisers and student parties across Belgium and Europe.</p></div>
      <div class="card"><h3>Restaurants &amp; venues</h3><p>Recurring Greek nights that build a loyal crowd — the Papillon Schuman formula.</p></div>
      <div class="card"><h3>Families</h3><p>Weddings, baptisms and name-day celebrations where the Greek repertoire has to be right.</p></div>
      <div class="card"><h3>Companies</h3><p>Greek-themed corporate evenings — increasingly popular, surprisingly effective.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Πάμε;</h2>
    <p>Tell me about your Greek night — in Greek, English, French or Dutch.</p>
    <a class="btn btn-gold" href="{link:contact}">Request a quote</a>
  </div>
</section>
""",
        "faq": [
            ("Do you only play Greek music at Greek nights?",
             "Only if you want that. Most successful Greek nights breathe: strong Greek hours, with Afro, Latin, RnB and international hits woven in so every guest — Greek or not — stays on the floor."),
            ("Do you travel to Greek communities outside Belgium?",
             "Yes — I already play for the Vienna, Leuven and Lille Greek communities, and I'm available across the Netherlands, France, Germany, the UK and Greece. Travel and accommodation are added to the quote."),
            ("Can you also host or MC the event in Greek?",
             "Yes — announcements and hosting in Greek, English, French or Dutch, as your audience needs."),
        ],
    },

    # ---------------------------------------------------------------- PARTY
    "party": {
        "title": "Party DJ in Brussels — Private Parties & Birthdays",
        "desc": "Private party DJ in Brussels: birthdays, anniversaries, graduations and celebrations with a professional open-format DJ. Electronic, Afro, Latin, RnB and Greek. Sound & light available. Belgium & Europe.",
        "kicker": "Your party, professionally loud",
        "h1": "Party DJ in <span class='gold'>Brussels</span>",
        "sub": "Birthdays, anniversaries, graduations, house parties — club-level energy, living-room friendly professionalism.",
        "price": "From €400 excl. VAT", "price_note": "Within Brussels — travel added beyond", "price_amount": "400",
        "facts": [("Starting price", "€400 excl. VAT within Brussels, DJ only"),
                  ("Formats", "Birthdays, anniversaries, graduations, house parties"),
                  ("Scale", "From an apartment to a venue of 500 guests"),
                  ("Music", "Open format — electronic, Afro, Latin, RnB, Greek, pop"),
                  ("Equipment", "Compact apartment-friendly rig or full production"),
                  ("Base &amp; travel", "Brussels and all of Belgium")],
        "service_type": "Private party DJ",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>A real DJ makes the difference</h2>
      <p>A playlist can't see your dance floor. Nine years of club and event experience — Mykonos nightlife, Brussels residencies, hundreds of private events — means your party gets a professional who reads the room, takes requests gracefully and keeps the energy exactly where you want it.</p>
      <ul class="ticks">
        <li><strong>Open format</strong> — electronic, Afro, Latin, RnB, Greek, pop and the classics, mixed to your crowd.</li>
        <li><strong>Any scale</strong> — from a living-room birthday to a rented venue with 500 guests, with <a href="{link:fullpackage}">sound &amp; light included</a> if you need it.</li>
        <li><strong>Your rules</strong> — must-plays, never-plays, surprise moments: we plan it together beforehand.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Got a date in mind?</h2>
    <p>Tell me the occasion and the venue — I'll take care of the rest.</p>
    <a class="btn btn-gold" href="{link:contact}">Request a quote</a>
  </div>
</section>
""",
        "faq": [
            ("How much does a private party DJ cost in Brussels?",
             "It depends on duration, location and whether you need sound and lighting equipment. Send the basics through the contact form and you'll get a clear, personalised quote — usually within 48 hours, with no obligation."),
            ("Do you bring your own equipment for house parties?",
             "Yes — I can bring a complete, apartment-friendly setup, or full sound and light for a rented venue up to 500 guests. Tell me the space and I'll propose the right configuration."),
            ("Do you take song requests during the party?",
             "Gladly — requests are part of a good party. I weave them in when they serve the floor, and I'll always protect your never-play list."),
        ],
    },

    # ---------------------------------------------------------------- FULL PACKAGE
    "fullpackage": {
        "title": "Full-Package Events Brussels — DJ, Sound, Light & Video",
        "desc": "One partner for your whole event in Brussels and beyond: professional DJ, sound and lighting for up to 500 guests, plus photography and video. One contact, one setup, one invoice.",
        "kicker": "One partner, whole event",
        "h1": "Full-package <span class='gold'>event solutions</span>",
        "sub": "DJ + professional sound &amp; light + photography + video — for events and small shows up to 500 people.",
        "price": "From €1,000 excl. VAT", "price_note": "DJ, speakers, microphones and lighting", "price_amount": "1000",
        "facts": [("Starting price", "€1,000 excl. VAT for the full premium package"),
                  ("Maximum size", "500 guests"),
                  ("Included on request", "Sound, lighting, photography, video"),
                  ("Microphones", "Wireless mics for speeches and ceremonies"),
                  ("Coordination", "Venue technical planning handled directly"),
                  ("Billing", "One contact, one invoice for the whole event")],
        "service_type": "Event production (DJ, sound, light, photo, video)",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Why one partner beats four suppliers</h2>
      <p>Coordinating a DJ, an AV company, a photographer and a videographer means four contracts, four schedules and four people who've never worked together. I offer the alternative: one team, one technical plan, one person responsible for the whole evening working — me.</p>
      <ul class="ticks">
        <li><strong>Professional sound</strong> — scaled to your room, from 20 to 500 guests, with wireless microphones for speeches and ceremonies.</li>
        <li><strong>Lighting</strong> — elegant ambient design for receptions and dinners, full dance-floor lighting for the party.</li>
        <li><strong>Photography &amp; video</strong> — event coverage from a team that has supported cultural productions and theatre groups for years.</li>
        <li><strong>Small shows &amp; productions</strong> — stage sound and light for performances, community productions and showcases.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Perfect for</h2>
    <div class="card-grid">
      <div class="card"><h3>Corporate receptions</h3><p>One invoice and one accountable contact — the way procurement likes it.</p></div>
      <div class="card"><h3>Weddings &amp; baptisms</h3><p>Music, mics, light and memories, planned as one seamless production.</p></div>
      <div class="card"><h3>Community galas &amp; shows</h3><p>Stage productions, annual balls and cultural evenings up to 500 people.</p></div>
      <div class="card"><h3>Venue events</h3><p>Pop-up club nights and themed evenings, fully produced.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    <h2>What the full package actually costs</h2>
    <p>No mystery, and nothing bundled that you don't need. The package is built from three parts, and you can stop at any of them:</p>
    <dl class="fact-grid price-build">
      <div class="fact"><dt>DJ service</dt><dd>from €600</dd></div>
      <div class="fact"><dt>+ Standard speakers</dt><dd>+ €200</dd></div>
      <div class="fact"><dt>+ Microphones, stands &amp; lighting</dt><dd>+ €200</dd></div>
      <div class="fact total"><dt>Full premium package</dt><dd>around €1,000</dd></div>
    </dl>
    <p class="muted">All figures excl. VAT, for a standard event within Brussels. Larger rooms, longer hours, extra lighting or photo and video coverage are quoted on top — and I will tell you when you don't need them.</p>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Describe your event</h2>
    <p>Headcount, venue, date — you'll receive one clear proposal covering everything.</p>
    <a class="btn btn-gold" href="{link:contact}">Request a full-package quote</a>
  </div>
</section>
""",
        "faq": [
            ("What size of event can you fully produce?",
             "Up to 500 people with professional sound and lighting. Beyond the equipment, that includes technical planning with your venue and setup and teardown around your schedule."),
            ("Can I book only some parts of the package?",
             "Of course. DJ only, DJ + sound & light, or the complete package with photo and video — the quote is built around what you actually need."),
            ("Do you handle technical coordination with the venue?",
             "Yes — power, access, noise limits, timings: I speak with the venue directly so you don't have to translate between suppliers."),
        ],
    },

    # ---------------------------------------------------------------- RESTAURANT
    "restaurant": {
        "title": "Resident DJ for Restaurants & Bars in Brussels | DJ Orestis",
        "desc": "Hire a resident DJ for your restaurant or bar in Brussels. Recurring themed nights that fill quiet weekdays and lift bar revenue. Four-year residency at Papillon Schuman. Pilot night available.",
        "kicker": "For restaurants & venues",
        "h1": "Resident DJ for <span class='gold'>restaurants &amp; bars</span>",
        "sub": "For restaurant and bar owners in Brussels: a recurring themed night that fills a quiet weekday and lifts bar revenue — the formula behind my four-year residency at Papillon Schuman.",
        "price": "Per-night fee, quoted for the series", "price_note": "Pilot night available before any commitment",
        "facts": [("Engagement", "Weekly, monthly or seasonal residency"),
                  ("Trial", "One pilot night, no long-term commitment"),
                  ("Dinner service", "Conversation-level volume until service winds down"),
                  ("Equipment", "Compact system supplied, or your installed system used"),
                  ("Proven format", "Papillon Schuman, four consecutive years"),
                  ("Audience", "An established Greek and international following in Brussels")],
        "service_type": "Restaurant resident DJ",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>Why would a restaurant hire a resident DJ?</h2>
      <p>A good themed night is a business asset: it fills a slow weekday, builds a returning crowd that books tables in advance, and gives your venue a reputation beyond its menu. I've built exactly that at <strong>Papillon Schuman</strong> — four years and counting — and played rooms across Brussels: La Place 33, Capital, Kosmos, YAYA, Meatropolis, Machina, AKT.</p>
      <ul class="ticks">
        <li><strong>A concept, not just a DJ</strong> — we design the night together: Greek nights, Latin evenings, Afro &amp; RnB sessions, or an elegant dinner-to-dance format.</li>
        <li><strong>Volume discipline</strong> — dinner service stays conversational; the energy climbs when the plates leave.</li>
        <li><strong>A crowd that follows</strong> — my community following in Brussels comes with me, especially for Greek nights.</li>
        <li><strong>Zero infrastructure needed</strong> — I can bring compact, restaurant-appropriate sound and lighting.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Which residency format fits your venue?</h2>
    <div class="card-grid">
      <div class="card"><h3>Weekly or monthly residency</h3><p>A fixed, branded night your guests can plan around — the strongest crowd-builder.</p></div>
      <div class="card"><h3>Greek night launch</h3><p>A tested concept: Greek dinner service flowing into laïkà and island hits. Proven in Brussels for years.</p></div>
      <div class="card"><h3>Seasonal &amp; pop-up</h3><p>Terrace summers, festive December programming, one-off themed evenings.</p></div>
      <div class="card"><h3>Private venue hire</h3><p>Your restaurant hosts a private event? I handle the whole musical side, <a href="{link:fullpackage}">production included</a>.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Run a restaurant, bar or hotel in Brussels?</h2>
    <p>Let's talk about a pilot night — one evening, clear numbers, no long-term commitment.</p>
    <a class="btn btn-gold" href="{link:contact}">Propose a pilot night</a>
    <p class="muted" style="margin-top:18px">See how one worked in practice: the <a href="/case-studies/papillon-schuman-greek-night-residency/">four-year Papillon Schuman residency</a>.</p>
  </div>
</section>
""",
        "faq": [
            ("How does a restaurant DJ residency work commercially?",
             "Typically a fixed fee per night, agreed as a weekly or monthly series. We start with a pilot night so you can measure covers and bar revenue before committing to a series."),
            ("Will the music be too loud for dinner service?",
             "No — that's the craft. Dinner sets stay at conversation level with elegant programming; the volume and energy only climb once service winds down. I calibrate the system to your room."),
            ("Do you bring your own equipment?",
             "If needed, yes — compact, restaurant-appropriate sound and lighting that sets up discreetly. If your venue has an installed system, I work with that."),
        ],
    },

    # ---------------------------------------------------------------- MYKONOS / EUROPE
    "mykonos": {
        "title": "Greek DJ for Events Across Europe — Mykonos-Trained | DJ Orestis",
        "desc": "Book a Mykonos-trained Greek DJ for destination events across Europe: weddings, corporate events and Greek parties in the Netherlands, France, Germany, the UK and Greece — including Mykonos itself.",
        "kicker": "Brussels-based, Europe-wide",
        "h1": "Greek DJ across <span class='gold'>Europe</span>",
        "sub": "Trained in three seasons of Mykonos nightlife, based in Brussels, and regularly on the road: your event doesn't have to be in Belgium to sound right.",
        "price": "From €600 excl. VAT + travel", "price_note": "Travel and accommodation itemised separately", "price_amount": "600",
        "facts": [("Starting price", "€600 excl. VAT plus travel and accommodation"),
                  ("Countries served", "Belgium, Netherlands, France, Germany, UK, Austria, Greece"),
                  ("Equipment abroad", "Fly light and use local gear, or full production near Belgium"),
                  ("Greek islands", "Mykonos every summer — ask about season dates"),
                  ("Languages", "Greek, English, French, Dutch")],
        "service_type": "Destination event DJ",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>One DJ, six countries</h2>
      <p>Some events need a DJ who understands a specific crowd — a Greek wedding in Germany, a diaspora gala in Vienna, a corporate summer party in Amsterdam, a celebration on Mykonos itself. I already travel for exactly these: the <strong>Vienna Greek Student Community</strong>, the <strong>Leuven and Lille Greek communities</strong>, and every summer, <strong>guest sets in Mykonos</strong>, where I spent three full seasons in the island's nightlife.</p>
      <ul class="ticks">
        <li><strong>Simple logistics</strong> — travel and accommodation are added to the quote transparently; everything else works exactly like a Brussels booking.</li>
        <li><strong>Compact or full setup</strong> — I can fly light and use local equipment, or arrange full production for events near Belgium.</li>
        <li><strong>Mykonos experience</strong> — for destination weddings and parties in Greece, you get a DJ who has actually worked those rooms and knows the island's pace.</li>
      </ul>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Typical bookings abroad</h2>
    <div class="card-grid">
      <div class="card"><h3>Destination weddings</h3><p>Greek and international weddings in Greece, France and beyond — including Mykonos and the islands.</p></div>
      <div class="card"><h3>Diaspora community events</h3><p>Galas, national celebrations and student parties for Greek communities across Europe.</p></div>
      <div class="card"><h3>Corporate off-sites</h3><p>Company retreats and summer parties where the team deserves better than a playlist.</p></div>
      <div class="card"><h3>Mykonos &amp; Greece</h3><p>Villa parties, pre-wedding events and venue guest sets during the summer season.</p></div>
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Planning an event abroad?</h2>
    <p>Tell me the city and the date — you'll get one clear quote, travel included.</p>
    <a class="btn btn-gold" href="{link:contact}">Request a quote</a>
  </div>
</section>
""",
        "faq": [
            ("Which countries do you cover?",
             "Belgium is home base; I regularly play in the Netherlands, France, Germany, the UK, Austria and Greece. Other destinations are possible — ask."),
            ("How does pricing work for events outside Belgium?",
             "Same performance fee as a Belgian booking, plus transparent travel and accommodation costs listed separately in the quote. For Greece in summer, I'm often already there — ask about my Mykonos season dates."),
            ("Can you DJ a destination wedding in Mykonos or the Greek islands?",
             "Yes — that's where I learned the craft. I know the venues, the pace of an island wedding day, and how to combine the Greek repertoire with an international crowd."),
        ],
    },

    # ---------------------------------------------------------------- MUSIC
    "music": {
        "title": "Music & Sets — Greek, Electronic, Afro, Latin & RnB | DJ Orestis",
        "desc": "The five music worlds DJ Orestis mixes — Greek, electronic, Afro, Latin and RnB — how a set is actually built, and what that means for weddings, corporate events and Greek nights.",
        "kicker": "Listen",
        "h1": "Five music worlds, <span class='gold'>one DJ</span>",
        "sub": "The range is the point: whatever your crowd, there is a set for it — and the craft is knowing which one the room needs at 22:40.",
        "facts": [("Genres", "Greek, electronic, Afro, Latin, RnB"),
                  ("Format", "Open format, mixed live — never a fixed playlist"),
                  ("Requests", "Welcome, woven in when they serve the floor"),
                  ("Never-play list", "Always respected"),
                  ("Hosting", "Greek, English, French or Dutch"),
                  ("Typical set", "4–6 hours, extendable")],
        "body": """
<section class="section">
  <div class="wrap">
    <h2>The five worlds</h2>
    <div class="card-grid">
      <div class="card"><h3>Greek</h3><p>Laïkà and éntekhna, nisiótika for the summer feeling, rebetiko when the moment earns it, the 90s canon everyone over thirty knows by heart, and today's charts for everyone under it. The cultural fluency matters more than the catalogue — knowing that a zeibekiko needs space and silence around it, and that a kalamatianó early sets up the whole night.</p></div>
      <div class="card"><h3>Electronic</h3><p>House, deep and melodic, shaped by three seasons of Mykonos sunsets and peak-time rooms. This is what carries a corporate reception without dominating conversation, and what takes a wedding past midnight when the older guests have gone home.</p></div>
      <div class="card"><h3>Afro</h3><p>Afrobeats, afro house and amapiano — the sound that owns European dance floors right now, and the most reliable bridge between generations and nationalities in a mixed room.</p></div>
      <div class="card"><h3>Latin</h3><p>Reggaeton, salsa, bachata and Latin pop. Instant floor-fillers for international crowds, and the section of the night where people who claim they do not dance usually start.</p></div>
      <div class="card"><h3>RnB</h3><p>Classic and contemporary RnB and hip-hop. The connective tissue of any open-format set — what you use to move between worlds without the floor noticing the seam.</p></div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap split">
    <div>
      <h2>How a set is actually built</h2>
      <p>Almost every client starts the music conversation with a playlist. I read all of them properly, and they are genuinely useful — but a playlist is a list of songs, and an evening is a shape.</p>
      <p>What I plan is the shape. Where the energy sits during dinner, how long the first proper dance section runs before it needs air, which moment carries the emotional weight of the night, and what plays at 01:50 when you want people to leave happy rather than drift out.</p>
      <p>Then I abandon most of it. The room decides. A track that empties the floor at 21:00 fills it at 00:30 — same song, same people, different moment. Reading that in real time is the entire job, and it is the one thing a playlist cannot do.</p>
      <a class="btn btn-ghost" href="{link:weddingguide}">The full timeline, in the free guide</a>
    </div>
    {PLACEHOLDER_PHOTO}
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    <h2>What this means for your event</h2>
    <ul class="ticks">
      <li><strong>Mixed and international rooms</strong> — Brussels crowds are rarely one nationality. Five genuine repertoires means nobody stands at the edge waiting for something they recognise.</li>
      <li><strong>Greek celebrations</strong> — the Greek hours are real Greek hours, not three token songs, and they flow into international sets so every guest belongs all night.</li>
      <li><strong>Corporate events</strong> — sophisticated background programming during dinner and speeches, then a floor that fills when the plates leave. Two different skills, one evening.</li>
      <li><strong>Your list matters</strong> — must-plays get played, never-plays never do. That second list is more important than the first, and I ask for it every time.</li>
    </ul>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Sets &amp; aftermovies</h2>
    <p class="center muted">Recordings are on the way. In the meantime you can hear me live at Papillon Schuman in Brussels, where I have held the residency for four years.</p>
    <div class="media-grid">
      {PLACEHOLDER_VIDEO}
      {PLACEHOLDER_VIDEO}
    </div>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Want this sound at your event?</h2>
    <a class="btn btn-gold" href="{link:contact}">Request a quote</a>
  </div>
</section>
""",
        "faq": [
            ("Can I give you a playlist?",
             "Yes, and please do. Your must-plays are the skeleton of the night. I build the living set around them and adapt to the room as the evening goes — the list tells me who you are, the floor tells me what to do next."),
            ("Do you take requests during the event?",
             "Gladly. Requests are part of a good party and often the best moment of the night. I weave them in where they serve the floor, and I always protect your never-play list."),
            ("Can you cover several genres in one night?",
             "That is the whole point of an open format. A typical evening might move from elegant electronic during dinner into Greek hours, out through Latin and Afro, and finish on RnB and classics — with the joins invisible."),
            ("What if my guests are from many different countries?",
             "That is the most common situation in Brussels and my strongest ground. Five real repertoires and four spoken languages mean a mixed room is an advantage rather than a problem."),
        ],
    },

    # ---------------------------------------------------------------- EVENTS
    "events": {
        "title": "Past Events & Residencies — DJ Orestis | Brussels & Europe",
        "desc": "Selected events by DJ Orestis: Papillon Schuman residency, Brussels Greek Food Festival, corporate events for Freshfields and BCG, Greek community parties in Vienna, Leuven and Lille, Mykonos guest sets.",
        "kicker": "Track record",
        "h1": "Past events &amp; <span class='gold'>residencies</span>",
        "sub": "Nine years, hundreds of nights. A selection.",
        "body": """
<section class="section">
  <div class="wrap">
    <div class="events-cols">
      <div>
        <h2>Residencies &amp; venues</h2>
        <ul class="event-list">
          <li><strong>Papillon Schuman</strong> — resident DJ, 4th year <span class="muted">· Brussels</span></li>
          <li><strong>La Place 33</strong> <span class="muted">· Brussels</span></li>
          <li><strong>Capital</strong> <span class="muted">· Brussels</span></li>
          <li><strong>Kosmos</strong> <span class="muted">· Brussels</span></li>
          <li><strong>YAYA</strong> <span class="muted">· Brussels</span></li>
          <li><strong>Meatropolis</strong> <span class="muted">· Brussels</span></li>
          <li><strong>Machina</strong> <span class="muted">· Brussels</span></li>
          <li><strong>AKT</strong> <span class="muted">· Brussels</span></li>
          <li><strong>Mykonos</strong> — annual guest sets; 3 full seasons in the island's nightlife</li>
        </ul>
      </div>
      <div>
        <h2>Corporate</h2>
        <ul class="event-list">
          <li><strong>Freshfields</strong> — corporate events <span class="muted">· Brussels</span></li>
          <li><strong>Boston Consulting Group</strong> — corporate events <span class="muted">· Brussels</span></li>
          <li>Further major Brussels-based companies <span class="muted">· references on request</span></li>
        </ul>
        <h2>Festivals &amp; community</h2>
        <ul class="event-list">
          <li><strong>Brussels Greek Food Festival</strong> — host DJ, two editions</li>
          <li><strong>Dames Hellènes</strong> — events &amp; celebrations</li>
          <li><strong>Greek Choir of Brussels</strong></li>
          <li><strong>Vienna Greek Student Community</strong> — parties <span class="muted">· Austria</span></li>
          <li><strong>Leuven Greek Community</strong> — parties</li>
          <li><strong>Lille Greek Community</strong> — parties <span class="muted">· France</span></li>
          <li><strong>Brussels Greek Community</strong> — pro bono</li>
          <li><strong>Hellenic United Women</strong> — pro bono</li>
          <li><strong>Argo Hellenic Diplomat Network, AHEPA</strong> — cooperations</li>
        </ul>
      </div>
    </div>
    <p class="muted">More event history at <a href="https://soundsgreekevents.be" rel="noopener">Sounds Greek Events</a>, which I co-founded.</p>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Your event could be next</h2>
    <a class="btn btn-gold" href="{link:contact}">Request a quote</a>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- CONTACT
    "contact": {
        "title": "Book DJ Orestis — Request a Quote | Brussels, Belgium & Europe",
        "desc": "Book DJ Orestis for your corporate event, wedding or party in Brussels, Belgium or anywhere in Europe. Fill in the quote form and receive a personalised proposal, usually within 48 hours.",
        "kicker": "Let's talk",
        "h1": "Request a <span class='gold'>quote</span>",
        "sub": "The more you tell me, the more precise the proposal. Usually answered within 48 hours — always without obligation.",
        "body": """
<section class="section">
  <div class="wrap split-form">
    <div>
      {FORM}
    </div>
    <aside class="contact-aside">
      <h2>Direct contact</h2>
      <p><a href="mailto:info@djorestis.com">info@djorestis.com</a></p>
      <p class="muted">Based in Brussels, Belgium.<br>Available in Belgium, the Netherlands, France, Germany, the UK and Greece — for events abroad, travel and accommodation are added to the quote.</p>
      <h2>Languages</h2>
      <p class="muted">Greek · English · French · Dutch</p>
    </aside>
  </div>
</section>
""",
    },


    # ---------------------------------------------------------------- GUIDES
    "weddingguide": {
        "title": "Wedding Music Planning Guide — Timeline & Questions to Ask",
        "desc": "A free wedding music planning guide from a Brussels DJ: the day's timeline, a must-play worksheet, ten questions to ask any DJ, and honest Belgian pricing.",
        "kicker": "Free guide",
        "h1": "The wedding music <span class='gold'>planning guide</span>",
        "sub": "The timeline that makes a dance floor work, what to tell your DJ, and what a wedding DJ actually costs in Belgium — written from nine years of doing it.",
        "signup": "wedding",
        "body": """{GUIDE:WEDDING-GUIDE}

<section class="section cta-band">
  <div class="wrap center">
    <h2>Planning your wedding?</h2>
    <p>Tell me your date and venue — I'll tell you honestly whether I'm the right DJ for it.</p>
    <a class="btn btn-gold" href="{link:contact}">Check my availability</a>
  </div>
</section>
""",
    },

    "corporateguide": {
        "title": "Corporate Event Music Playbook — Brussels Event Organisers",
        "desc": "A free playbook for company event organisers: how to programme music around your agenda, handle the transition to dancing, and brief a DJ for a multinational room.",
        "kicker": "Free playbook",
        "h1": "The corporate event <span class='gold'>music playbook</span>",
        "sub": "How to programme music around speeches, awards and a room of fifteen nationalities — from a DJ who works Brussels corporate events.",
        "signup": "corporate",
        "body": """{GUIDE:CORPORATE-PLAYBOOK}

<section class="section cta-band">
  <div class="wrap center">
    <h2>Planning a company event?</h2>
    <p>Send the date, venue and headcount — you'll get a clear proposal, usually within 48 hours.</p>
    <a class="btn btn-gold" href="{link:contact}">Request a proposal</a>
  </div>
</section>
""",
    },


    # ---------------------------------------------------------------- PRESS
    "press": {
        "title": "Press & Media — DJ Orestis | Brussels DJ Press Kit",
        "desc": "Press resources for DJ Orestis: biographies in three lengths, a downloadable press kit, brand assets, fact sheet and direct media contact.",
        "kicker": "For journalists &amp; editors",
        "h1": "Press &amp; <span class='gold'>media</span>",
        "sub": "Everything you need to write about DJ Orestis, ready to copy. For interviews, comment or assets, email info@djorestis.com.",
        "body": """
<section class="section">
  <div class="wrap narrow guide-body">
    <h2>Biographies</h2>
    <p class="muted">Copy whichever length fits. No approval needed.</p>

    <h3>Short — 51 words</h3>
    <blockquote>DJ Orestis (Orestis Vasileiadis) is a Brussels-based Greek DJ with nine years behind the decks — three seasons in Mykonos nightlife, six in Brussels. He holds a four-year residency at Papillon Schuman, has twice been host DJ of the Brussels Greek Food Festival, and plays Greek, electronic, Afro, Latin and RnB.</blockquote>

    <h3>Medium — 98 words</h3>
    <blockquote>DJ Orestis (Orestis Vasileiadis) is a Brussels-based Greek DJ with nine years of professional experience: three seasons in Mykonos nightlife, followed by six years in Brussels. He holds a four-year residency at Papillon Schuman and has twice been host DJ of the Brussels Greek Food Festival. He works across weddings, private celebrations and corporate events for international organisations based in the city, and co-founded Sounds Greek Events. He plays regularly for Greek communities in Brussels, Vienna, Leuven and Lille. His sets move between Greek, electronic, Afro, Latin and RnB, and he works in Greek, English, French and Dutch.</blockquote>

    <h3>Long — 199 words</h3>
    <blockquote>Orestis Vasileiadis — DJ Orestis — is a Greek DJ based in Brussels, with nine years behind the decks. He learned the job in Mykonos, playing three seasons in one of the most demanding nightlife environments in Europe, where a room turns over every few days and no two crowds share a language. He has spent the six years since in Brussels, a city with the same mixture of nationalities but people who stay — and where the skill is not surprising a crowd but holding one together. He holds a four-year residency at Papillon Schuman, has twice been the host DJ of the Brussels Greek Food Festival, and plays weddings, private celebrations and corporate events for international organisations headquartered in the city. He is a co-founder of Sounds Greek Events. Alongside the paid work, he plays regularly for Greek communities across Europe — Brussels, Vienna, Leuven and Lille — and performs pro bono for the Brussels Greek Community, Dames Hellènes and Hellenic United Women, on the principle that diaspora cultural life runs on volunteer labour and stops when nobody volunteers. His sets move between Greek, electronic, Afro, Latin and RnB. He works in Greek, English, French and Dutch.</blockquote>
  </div>
</section>

<section class="section alt">
  <div class="wrap narrow">
    <h2>Fact sheet</h2>
    <dl class="fact-grid">
      <div class="fact"><dt>Name</dt><dd>Orestis Vasileiadis — DJ Orestis</dd></div>
      <div class="fact"><dt>Based</dt><dd>Brussels, Belgium</dd></div>
      <div class="fact"><dt>Experience</dt><dd>9 years — 3 seasons Mykonos, 6 years Brussels</dd></div>
      <div class="fact"><dt>Residency</dt><dd>Papillon Schuman, Brussels — 4th year</dd></div>
      <div class="fact"><dt>Genres</dt><dd>Greek, electronic, Afro, Latin, RnB</dd></div>
      <div class="fact"><dt>Languages</dt><dd>Greek, English, French, Dutch</dd></div>
      <div class="fact"><dt>Also</dt><dd>Co-founder, Sounds Greek Events</dd></div>
      <div class="fact"><dt>Media contact</dt><dd><a href="mailto:info@djorestis.com">info@djorestis.com</a></dd></div>
    </dl>
  </div>
</section>

<section class="section">
  <div class="wrap narrow guide-body">
    <h2>Assets</h2>
    <ul>
      <li><a href="/assets/press/djorestis-presskit.pdf">Press kit (PDF, one page)</a></li>
      <li><a href="/assets/branding/concept-2.svg">Logo — full wordmark (SVG)</a></li>
      <li><a href="/assets/branding/favicon.svg">Logo — monogram (SVG)</a></li>
      <li><a href="/assets/og-image.png">Brand image (PNG, 1200×630)</a></li>
    </ul>
    <p class="muted">Performance photography available on request — email and I will send high-resolution files with usage cleared.</p>

    <h2>Story angles</h2>
    <p>Happy to talk about any of these, on the record:</p>
    <ul>
      <li><strong>Greek diaspora nightlife in Brussels</strong> — how a community keeps its culture through music, and what happens on the floor when it works.</li>
      <li><strong>Reading a crowd</strong> — what three seasons in Mykonos nightlife teaches you, and how that translates to a Brussels corporate reception.</li>
      <li><strong>Building a four-year residency</strong> — what it takes to make one night of the week belong to a venue.</li>
      <li><strong>The multicultural wedding</strong> — four languages on one dance floor, and what that says about the city.</li>
      <li><strong>Playing for free</strong> — why community events get the same set as paying clients.</li>
    </ul>

    <h2>Availability for comment</h2>
    <p>Available as an expert source on wedding and event music, the Brussels nightlife and events industry, Greek music and diaspora culture, and what event suppliers actually cost in Belgium. Comment in Greek, English, French or Dutch.</p>
  </div>
</section>

<section class="section cta-band">
  <div class="wrap center">
    <h2>Media enquiries</h2>
    <p>Email <a href="mailto:info@djorestis.com">info@djorestis.com</a> — I answer quickly and I am comfortable on short deadlines.</p>
  </div>
</section>
""",
    },

    # ---------------------------------------------------------------- PRIVACY
    "privacy": {
        "title": "Privacy Policy | DJORESTIS",
        "desc": "Privacy policy of DJORESTIS.com: what personal data is collected through the contact form, how it is used, and your rights under the GDPR.",
        "h1": "Privacy policy",
        "sub": "Short, honest, GDPR-compliant.",
        "body": """
<section class="section">
  <div class="wrap narrow legal">
    <h2>Who I am</h2>
    <p>This website, djorestis.com, is operated by Orestis Vasileiadis (DJ Orestis), Brussels, Belgium — VAT BE 0785.520.639 ("I", "me"). Contact: <a href="mailto:info@djorestis.com">info@djorestis.com</a>.</p>
    <h2>What data I collect</h2>
    <p>When you use the quote request form, I receive the information you enter: your name, email address, optional phone number, and the details of your event. I use it for one purpose only: to answer your request and prepare a proposal.</p>
    <h2>What I don't do</h2>
    <p>I do not sell or share your data with third parties for marketing. I do not send newsletters unless you explicitly ask for updates. This site sets no advertising cookies.</p>
    <h2>Analytics</h2>
    <p>This site may use privacy-respecting visitor statistics to understand which pages are useful. Where analytics requiring consent are used, you will be asked first.</p>
    <h2>How long I keep your data</h2>
    <p>Enquiry emails are kept as long as needed to handle your event and for reasonable business records, and deleted on request.</p>
    <h2>Your rights</h2>
    <p>Under the GDPR you may request access to, correction of, or deletion of your personal data at any time — one email is enough. You may also lodge a complaint with the Belgian Data Protection Authority (<a href="https://www.dataprotectionauthority.be" rel="noopener">dataprotectionauthority.be</a>).</p>
  </div>
</section>
""",
    },
}
