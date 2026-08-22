# venues.py — Brussels venues where DJ Orestis has performed.
#
# All website and Instagram URLs below were verified by web search on 2026-08-22.
# Each entry was cross-checked against Brussels addresses (commune / postcode) to
# avoid matching a same-named venue in another city or country.
#
# Entries with confidence "unverified" have no link that could be confirmed as the
# Brussels venue — the owner needs to supply the correct link before these are used.
# Entries marked "likely" fit the Brussels profile but should be confirmed by the owner.
#
# No venue logos or brand images are included here: reproducing a venue's logo
# requires that venue's explicit permission. Text names only.

VENUES = [
    # --- Restaurants ---
    {
        "name": "Machina",
        "type": "Restaurant",
        "area": "Saint-Gilles",
        "url": "https://www.restomachina.be/",
        "instagram": "https://www.instagram.com/machina_resto_bar/",
        "confidence": "confirmed",
    },
    {
        "name": "Arion",
        "type": "Restaurant",
        "area": "Saint-Gilles",
        "url": "https://www.arionbrussels.be/",
        "instagram": "https://www.instagram.com/arion_restaurant/",
        "confidence": "confirmed",
    },
    {
        "name": "Greekit",
        "type": "Restaurant",
        "area": "EU Quarter",
        "url": "",
        "instagram": "https://www.instagram.com/greekit.be/",
        "confidence": "confirmed",
    },
    {
        "name": "Greek Yaya",
        "type": "Restaurant",
        "area": "Ixelles",
        "url": "https://greekyaya.be/",
        "instagram": "https://www.instagram.com/greek__yaya/",
        "confidence": "confirmed",
    },
    {
        "name": "Meatropolis Grill",
        "type": "Restaurant",
        "area": "Etterbeek",
        "url": "https://meatropolisgrill.com/",
        "instagram": "https://www.instagram.com/meatropolis_grill/",
        "confidence": "confirmed",
    },
    # --- Bars ---
    {
        "name": "Kosmos Place",
        "type": "Bar",
        "area": "Place Jourdan, Etterbeek",
        "url": "https://kosmosbrussels.com/",
        "instagram": "https://www.instagram.com/kosmos.brussels/",
        "confidence": "confirmed",
    },
    {
        "name": "Papillon",
        "type": "Bar",
        "area": "Schuman",
        "url": "https://papillon-brussels.com/",
        "instagram": "https://www.instagram.com/papillon_brussels/",
        "confidence": "confirmed",
    },
    {
        "name": "AKT",
        "type": "Bar",
        "area": "Schuman",
        "url": "https://www.akt.brussels/",
        "instagram": "",
        "confidence": "confirmed",
    },
    {
        "name": "Capital",
        "type": "Bar",
        "area": "Quartier Leopold",
        "url": "",
        "instagram": "https://www.instagram.com/capital_pym/",
        "confidence": "likely",
    },
    {
        "name": "To Meli",
        "type": "Bar",
        "area": "Schuman",
        "url": "https://tomelibrussels.wixsite.com/to-meli",
        "instagram": "https://www.instagram.com/to.meli.brussels/",
        "confidence": "confirmed",
    },
]
