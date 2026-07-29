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
        "title": "DJ in Brussels — Corporate Events, Weddings & Greek Parties | DJ Orestis",
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
        "title": "DJ Services in Brussels & Belgium — Corporate, Weddings, Parties | DJ Orestis",
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
        "service_type": "Corporate event DJ",
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
        "title": "Wedding DJ in Brussels & Belgium — Greek & International Weddings | DJ Orestis",
        "desc": "Wedding DJ in Brussels and across Belgium for Greek, international and mixed weddings and baptisms. Tailored playlists, ceremony to last dance, sound & light included if needed. Also NL, FR, DE, UK, GR.",
        "kicker": "The most important party of your life",
        "h1": "Wedding DJ in <span class='gold'>Brussels &amp; Belgium</span>",
        "sub": "Greek, international and beautifully mixed weddings — one DJ who gets both sides of the room dancing to the same beat.",
        "service_type": "Wedding DJ",
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
        "title": "Party DJ in Brussels — Private Parties, Birthdays & Celebrations | DJ Orestis",
        "desc": "Private party DJ in Brussels: birthdays, anniversaries, graduations and celebrations with a professional open-format DJ. Electronic, Afro, Latin, RnB and Greek. Sound & light available. Belgium & Europe.",
        "kicker": "Your party, professionally loud",
        "h1": "Party DJ in <span class='gold'>Brussels</span>",
        "sub": "Birthdays, anniversaries, graduations, house parties — club-level energy, living-room friendly professionalism.",
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
        "title": "Full-Package Event Solutions — DJ, Sound, Light, Photo & Video | Brussels",
        "desc": "One partner for your whole event in Brussels and beyond: professional DJ, sound and lighting for up to 500 guests, plus photography and video. One contact, one setup, one invoice.",
        "kicker": "One partner, whole event",
        "h1": "Full-package <span class='gold'>event solutions</span>",
        "sub": "DJ + professional sound &amp; light + photography + video — for events and small shows up to 500 people.",
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
        "title": "Restaurant DJ in Brussels — Resident DJ & Themed Nights | DJ Orestis",
        "desc": "Resident DJ for restaurants and venues in Brussels: recurring Greek nights and themed evenings that build a loyal crowd. Four-year residency at Papillon Schuman. Sound & light included if needed.",
        "kicker": "For restaurants & venues",
        "h1": "Restaurant DJ in <span class='gold'>Brussels</span>",
        "sub": "Recurring nights that turn quiet evenings into fully booked ones — the formula behind my four-year residency at Papillon Schuman.",
        "service_type": "Restaurant resident DJ",
        "body": """
<section class="section">
  <div class="wrap split">
    <div>
      <h2>What a residency does for a venue</h2>
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
    <h2>Formats that work</h2>
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
    <h2>Run a restaurant or venue?</h2>
    <p>Let's talk about a pilot night — one evening, clear numbers, no long-term commitment.</p>
    <a class="btn btn-gold" href="{link:contact}">Propose a pilot night</a>
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
        "desc": "Listen to DJ Orestis: five music worlds — Greek, electronic, Afro, Latin and RnB — mixed for corporate events, weddings and parties in Brussels and across Europe.",
        "kicker": "Listen",
        "h1": "Five music worlds, <span class='gold'>one DJ</span>",
        "sub": "The range is the point: whatever your crowd, there's a set for it.",
        "body": """
<section class="section">
  <div class="wrap">
    <div class="card-grid">
      <div class="card"><h3>Greek</h3><p>Laïkà, éntekhna, nisiótika, rebetiko, 90s classics and today's charts — the full spectrum, with the cultural fluency to know which is right when.</p></div>
      <div class="card"><h3>Electronic</h3><p>House, deep and melodic sets shaped by three seasons in Mykonos — sunset elegance to peak-time drive.</p></div>
      <div class="card"><h3>Afro</h3><p>Afrobeats, afro house and amapiano — the sound that owns modern European dance floors.</p></div>
      <div class="card"><h3>Latin</h3><p>Reggaeton, salsa, bachata and Latin pop — instant floor-fillers for international crowds.</p></div>
      <div class="card"><h3>RnB</h3><p>Classic and contemporary RnB and hip-hop — the connective tissue of every great open-format set.</p></div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2>Sets &amp; aftermovies</h2>
    <p class="center muted">Fresh recordings are on the way — in the meantime, you can hear me live every month at Papillon Schuman in Brussels.</p>
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
