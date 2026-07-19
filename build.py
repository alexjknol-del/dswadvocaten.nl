#!/usr/bin/env python3
# Generator voor dswadvocaten.nl - DSW Advocaten, onafhankelijke advocatuur gids.
import os, json, html, hashlib

def _ver(relpath):
    try: return hashlib.md5(open(os.path.join(os.path.dirname(__file__),relpath),'rb').read()).hexdigest()[:8]
    except Exception: return "1"

BASE = "https://dswadvocaten.nl"
SITE = "DSW Advocaten"
TAGLINE = "de onafhankelijke gids voor juridische hulp"
EMAIL = "info@dswadvocaten.nl"
AUTHOR = "Nina Verschuur"
AUTHOR_ROLE = "Hoofdredacteur DSW Advocaten"
OUT = os.path.join(os.path.dirname(__file__), "site")
SRC = os.path.dirname(__file__)
CSS_VER = _ver("assets/css/style.css")

def esc(s): return html.escape(str(s), quote=True)

IC = {
 "check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "pin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "scale":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="3" x2="12" y2="21"/><line x1="5" y1="7" x2="19" y2="7"/><path d="M5 7 2 14a3.5 3.5 0 0 0 7 0z"/><path d="M19 7 16 14a3.5 3.5 0 0 0 7 0z"/><line x1="8" y1="21" x2="16" y2="21"/></svg>',
 "shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
 "search":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
 "users":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
 "doc":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>',
 "clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/></svg>',
 "euro":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 21a8 8 0 1 1 0-16"/><path d="M4 9h11"/><path d="M4 13h9"/></svg>',
 "heart":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-4.35-10-9.5C.5 7 3 3 7 3c2 0 3.5 1 5 3 1.5-2 3-3 5-3 4 0 6.5 4 5 8.5-3 5.15-10 9.5-10 9.5z"/></svg>',
 "compass":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>',
 "quill":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/><path d="M2 2l7.586 7.586"/><circle cx="11" cy="11" r="2"/></svg>',
 "menu":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>',
}

NAV = [("Home","/"),("Over","/over/"),("Rechtsgebieden","/rechtsgebieden/"),("Nieuws","/nieuws/"),("Aanbevolen kantoren","/advocatenkantoren/"),("Contact","/contact/")]

def head(title, desc, path, ld=None):
    can = BASE + path
    j = "".join('<script type="application/ld+json">'+json.dumps(b, ensure_ascii=False)+'</script>' for b in (ld or []))
    nav = "".join(f'<a class="navlink" href="{href}">{esc(label)}</a>' for label,href in NAV)
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{can}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{esc(SITE)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{can}">
<meta name="theme-color" content="#12213A">
<link rel="icon" href="/assets/icons/logo-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={CSS_VER}">
{j}
</head>
<body>
<header class="site-head">
  <nav class="nav" id="nav">
    <a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>DSW Advocaten</b><span>Advocatuur gids</span></span></a>
    {nav}
    <a class="btn btn-gold" href="/advocatenkantoren/">Vind een advocaat</a>
    <button class="menu-toggle" aria-label="Menu" onclick="document.getElementById('nav').classList.toggle('open')">{IC['menu']}</button>
  </nav>
</header>
"""

def footer():
    return f"""<footer class="foot">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="brand" href="/" style="color:#fff"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>DSW Advocaten</b><span style="color:#8B8878">Advocatuur gids</span></span></a>
        <p class="note">DSW Advocaten is een onafhankelijk redactioneel platform dat helpt bij het vinden van de juiste advocaat en bij het begrijpen van juridische onderwerpen in gewone taal. DSW Advocaten is zelf geen advocatenkantoor en geeft geen juridisch advies.</p>
      </div>
      <div>
        <h4>Op de site</h4>
        <a href="/over/">Over DSW Advocaten</a>
        <a href="/rechtsgebieden/">Rechtsgebieden</a>
        <a href="/nieuws/">Nieuws</a>
        <a href="/advocatenkantoren/">Aanbevolen kantoren</a>
        <a href="/schrijfster/">Over de redactie</a>
      </div>
      <div>
        <h4>Meer</h4>
        <a href="/contact/">Contact</a>
        <a href="/privacybeleid/">Privacybeleid</a>
        <a href="/cookiebeleid/">Cookiebeleid</a>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; 2026 {esc(SITE)}</span>
      <span><a href="/contact/">Contact</a> &middot; <a href="/privacybeleid/">Privacy</a> &middot; <a href="/cookiebeleid/">Cookies</a></span>
    </div>
  </div>
</footer>
</body>
</html>"""

def breadcrumb(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate(items)]}

def crumbs_html(items):
    out=[f'<a href="{u}">{esc(n)}</a>' for n,u in items[:-1]]
    out.append(f'<span>{esc(items[-1][0])}</span>')
    return '<div class="wrap"><nav class="crumbs">'+' / '.join(out)+'</nav></div>'

def write(path, content):
    full = os.path.join(OUT, "index.html") if path=="/" else os.path.join(OUT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full,"w",encoding="utf-8").write(content)

RECHTSGEBIEDEN = [
 {"slug":"personen-en-familierecht","naam":"Personen- en familierecht",
  "desc":"Alles rond echtscheiding, alimentatie, omgangsregelingen, gezag en adoptie. Dit rechtsgebied raakt vaak het persoonlijke leven direct.",
  "kantoren":["appelman"]},
 {"slug":"arbeidsrecht","naam":"Arbeidsrecht",
  "desc":"Geschillen over ontslag, arbeidscontracten, concurrentiebedingen en re-integratie tussen werkgever en werknemer.",
  "kantoren":["appelman"]},
 {"slug":"huurrecht","naam":"Huurrecht",
  "desc":"Conflicten tussen huurder en verhuurder, bijvoorbeeld over huurachterstand, onderhoud, opzegging of huurprijsherziening.",
  "kantoren":["appelman"]},
 {"slug":"strafrecht","naam":"Strafrecht",
  "desc":"Bijstand bij verdenking van een strafbaar feit, van verhoor tot rechtszitting, met aandacht voor de rechten van de verdachte.",
  "kantoren":["appelman"]},
 {"slug":"erfrecht","naam":"Erfrecht",
  "desc":"Vraagstukken rond nalatenschappen, testamenten, erfgenamen en verdeling, ook bij onderlinge geschillen tussen erfgenamen.",
  "kantoren":["appelman"]},
 {"slug":"verbintenissenrecht","naam":"Verbintenissenrecht",
  "desc":"De regels rond overeenkomsten en verplichtingen tussen partijen, bijvoorbeeld bij wanprestatie of een geschil over een contract.",
  "kantoren":["appelman"]},
 {"slug":"incassorecht","naam":"Incasso",
  "desc":"Het innen van openstaande vorderingen, van een eerste aanmaning tot een gerechtelijke procedure als betaling uitblijft.",
  "kantoren":["appelman"]},
 {"slug":"mediation","naam":"Mediation",
  "desc":"Een bemiddelde vorm van geschiloplossing waarbij partijen onder begeleiding zelf tot een oplossing proberen te komen, zonder rechtszaak.",
  "kantoren":["appelman"]},
 {"slug":"verzekeringsrecht","naam":"Verzekeringsrecht",
  "desc":"Geschillen met een verzekeraar, bijvoorbeeld over een afgewezen claim, de dekking van een polis of de hoogte van een uitkering.",
  "kantoren":["appelman"]},
 {"slug":"fiscaal-recht","naam":"Fiscaal recht en fiscaal strafrecht",
  "desc":"Procedures en geschillen met de Belastingdienst, van een boekenonderzoek tot fiscale vergrijpboetes en fiscaal-strafrechtelijke zaken.",
  "kantoren":["huygenlammers"]},
]

FIRMS = [
 {"slug":"advocatenkantoor-appelman","naam":"Advocatenkantoor Appelman","plaats":"Alkmaar",
  "domain":"appelman.nl","website":"https://www.appelman.nl/","badge":"Regionaal en breed inzetbaar",
  "adres":"Nieuwlandersingel 53, 1814 CK Alkmaar","tel":"072 512 32 29","tel_href":"tel:+31725123229","email":"info@appelman.nl",
  "tagline":"De advocaat in Alkmaar die cliënten als mens benadert, niet als dossiernummer.",
  "rechtsgebieden":["personen-en-familierecht","arbeidsrecht","huurrecht","strafrecht","erfrecht","verbintenissenrecht","incassorecht","mediation","verzekeringsrecht"],
  "usps":[
    "Klein kantoor met korte lijnen, zowel naar cliënten als binnen het team.",
    "Een gratis en vrijblijvend eerste kennismakingsgesprek.",
    "Ook gefinancierde rechtsbijstand, oftewel pro deo, is mogelijk.",
    "Meer dan dertig jaar ervaring in de regio Alkmaar en omstreken.",
  ],
  "lead":"Advocatenkantoor Appelman is een van de kleinere advocatenkantoren van Alkmaar. Een bewuste keuze: naast de kwaliteit van een groot kantoor biedt het de voordelen van een kleine organisatie, met korte lijnen en persoonlijk contact.",
  "secties":[
    ("Een persoonlijke aanpak","Het kantoor kent zijn cliënten en houdt de communicatie kort en helder. Doordat het team klein is, blijft er ruimte voor persoonlijke aandacht in elk dossier, van een eerste gesprek tot de afronding van een zaak."),
    ("Toegankelijke rechtshulp","Advocatenkantoor Appelman vindt dat goede juridische hulp voor iedereen toegankelijk moet zijn. Daarom houdt het kantoor de kosten bewust laag en behandelt het ook zaken via gefinancierde rechtsbijstand, oftewel pro deo."),
    ("Breed inzetbaar","Van echtscheiding en ontslag tot een huurconflict of een voornaamswijziging: het kantoor behandelt uiteenlopende situaties binnen het personen- en familierecht, arbeidsrecht, huurrecht, strafrecht, erfrecht, verbintenissenrecht, incasso, mediation en verzekeringsrecht."),
  ],
  "situaties":["Echtscheiding","Ontslag","Huurconflict","Voornaamswijziging"],
 },
 {"slug":"huygenlammers-advocaten","naam":"HuygenLammers Advocaten","plaats":"Amsterdam",
  "domain":"huygenlammersadvocaten.nl","website":"https://www.huygenlammersadvocaten.nl/","badge":"Specialist in fiscaal recht",
  "adres":"Willemsparkweg 100b, 1071 HM Amsterdam","tel":"020 226 90 18","tel_href":"tel:+31202269018","email":"info@huygenlammersadvocaten.nl",
  "tagline":"Gespecialiseerd in fiscaal recht en fiscaal strafrecht, met de cliënt centraal.",
  "rechtsgebieden":["fiscaal-recht"],
  "usps":[
    "Volledige specialisatie in fiscaal recht en fiscaal strafrecht.",
    "Opgeteld meer dan dertig jaar ervaring van de twee oprichters.",
    "Fungeert ook als sparringpartner voor de belastingadviseur of accountant.",
    "Persoonlijke aandacht en betrokkenheid gedurende het hele traject.",
  ],
  "lead":"HuygenLammers Advocaten is een Amsterdams kantoor dat zich volledig richt op fiscaal recht en fiscaal strafrecht. Het team combineert diepgaande fiscale kennis met een pragmatische aanpak, gericht op een oplossing die aansluit bij de situatie van de cliënt.",
  "secties":[
    ("Volledige specialisatie","Waar veel kantoren fiscaal recht als een van de vele rechtsgebieden voeren, doet HuygenLammers Advocaten uitsluitend dit. Die focus vertaalt zich in gedetailleerde kennis van steeds veranderende belastingwetgeving en fiscale procedures."),
    ("Van advies tot strafzaak","Het kantoor staat cliënten bij in het volledige spectrum van fiscale kwesties: van bezwaar tegen een belastingaanslag en begeleiding bij een boekenonderzoek, tot bijstand tijdens een verhoor door de FIOD in een fiscaal-strafrechtelijke zaak."),
    ("Sparringpartner voor adviseurs","Naast directe cliënten werkt HuygenLammers Advocaten ook samen met belastingadviseurs en accountants, die het kantoor inschakelen als juridische sparringpartner bij complexe fiscale vraagstukken."),
  ],
  "situaties":["Boekenonderzoek Belastingdienst","FIOD-verhoor","Fiscale vergrijpboete","Bezwaar belastingaanslag"],
 },
]
for _f in FIRMS:
    _f["rg_namen"] = [next(r["naam"] for r in RECHTSGEBIEDEN if r["slug"]==s) for s in _f["rechtsgebieden"]]

def firms_for(rg_slug):
    return [f for f in FIRMS if rg_slug in f["rechtsgebieden"]]

DISCLAIMER = "Dit artikel geeft algemene informatie en is geen juridisch advies. Voor een inschatting van een persoonlijke situatie is het raadzaam een advocaat te raadplegen."

ARTICLES = [
 {"slug":"wat-kost-een-advocaat","titel":"Wat kost een advocaat? Uurtarief, pro deo en gefinancierde rechtsbijstand uitgelegd",
  "cat":"Kosten en proces","datum":"2026-06-10","datum_nl":"10 juni 2026","leestijd":6,
  "excerpt":"De kosten van een advocaat lopen uiteen, en dat roept al snel drempelvrees op. Een overzicht van uurtarieven, pro deo en wat de prijs bepaalt.",
  "body":[
    ("p","De kosten van een advocaat zijn voor veel mensen reden om een probleem eerst maar te laten liggen. Dat is jammer, want de prijs van rechtsbijstand hangt af van meer factoren dan alleen een uurtarief, en er bestaan regelingen die de drempel aanzienlijk verlagen."),
    ("h2","Het uurtarief als uitgangspunt"),
    ("p","De meeste advocaten werken met een uurtarief. Dat tarief verschilt per kantoor, per regio en per rechtsgebied, en ligt doorgaans tussen de honderd en driehonderd euro exclusief btw. Gespecialiseerde kantoren, bijvoorbeeld in het fiscale recht, hanteren vaak een hoger tarief dan een algemene rechtswinkel, wat samenhangt met de complexiteit van de materie."),
    ("h2","Wat de einduitslag bepaalt"),
    ("ul",["De complexiteit van de zaak en de hoeveelheid werk die ermee gemoeid is.",
           "Of de zaak in overleg wordt opgelost of via een procedure bij de rechter loopt.",
           "De ervaring en specialisatie van de advocaat.",
           "Bijkomende kosten, zoals griffierecht bij een rechtszaak."]),
    ("h2","Gefinancierde rechtsbijstand: pro deo"),
    ("p","Voor mensen met een lager inkomen en vermogen bestaat gefinancierde rechtsbijstand, in de volksmond pro deo genoemd. De overheid vergoedt dan een deel van de kosten van rechtsbijstand, en de cliënt betaalt een eigen bijdrage die afhankelijk is van het inkomen. Niet elk kantoor voert pro deo-zaken; het is dus verstandig dit vooraf te vragen."),
    ("callout","Een gratis kennismakingsgesprek is bij veel kantoren gebruikelijk. Dat is het moment om de verwachte kosten, het te verwachten verloop en de slagingskans te bespreken, voordat er een verplichting ontstaat."),
    ("h2","Rechtsbijstandsverzekering"),
    ("p","Wie een rechtsbijstandsverzekering heeft, valt in bepaalde gevallen (deels) onder die dekking. De voorwaarden verschillen sterk per polis en per type geschil, en niet elke verzekeraar laat de vrije keuze van een advocaat toe. Navraag bij de verzekeraar voorkomt verrassingen achteraf."),
    ("h2","No cure no pay: geen gangbare praktijk"),
    ("p","In sommige landen is een beloning die afhankelijk is van het resultaat gebruikelijk. In Nederland is dat voor advocaten aan strikte regels gebonden en in de praktijk beperkt tot enkele specifieke situaties. De meeste zaken worden dan ook via een uurtarief of een vooraf afgesproken vaste prijs afgehandeld."),
    ("p",DISCLAIMER),
  ]},
 {"slug":"verplicht-advocaat-inschakelen","titel":"Is een advocaat verplicht? Dit zijn de regels",
  "cat":"Kosten en proces","datum":"2026-06-24","datum_nl":"24 juni 2026","leestijd":5,
  "excerpt":"Bij sommige procedures is een advocaat verplicht, bij andere niet. Een overzicht van wanneer procesvertegenwoordiging wettelijk nodig is.",
  "body":[
    ("p","Niet elke juridische stap vereist een advocaat. Bij sommige procedures is procesvertegenwoordiging door een advocaat echter wettelijk verplicht, terwijl iemand bij andere zaken zichzelf mag vertegenwoordigen. Het verschil hangt vooral af van het type procedure en de rechter die de zaak behandelt."),
    ("h2","Verplichte procesvertegenwoordiging"),
    ("p","Bij een procedure voor de rechtbank in een civiele zaak met een vordering boven een bepaald bedrag is een advocaat in de meeste gevallen verplicht. Ook bij hoger beroep en cassatie geldt vrijwel altijd een verplichting tot procesvertegenwoordiging. Bij deze procedures kan een partij niet zelfstandig optreden."),
    ("h2","Wanneer het niet verplicht is"),
    ("ul",["Bij de kantonrechter, bijvoorbeeld bij huurzaken, arbeidszaken of vorderingen tot een bepaald bedrag.",
           "Bij bestuursrechtelijke procedures, zoals een bezwaar tegen een besluit van een gemeente.",
           "Bij eenvoudige verzoekschriftprocedures die specifiek zijn vrijgesteld."]),
    ("h2","Verstandig, ook zonder verplichting"),
    ("p","Ook wanneer een advocaat niet verplicht is, kan bijstand verstandig zijn. Juridische procedures kennen termijnen, formele vereisten en argumentatielijnen die niet altijd voor de hand liggen. Een verkeerd ingediend stuk of een gemiste termijn kan een op zichzelf kansrijke zaak alsnog laten mislukken."),
    ("callout","Bij twijfel of een advocaat verplicht is, geeft de griffie van de rechtbank of een eerste gesprek met een advocaat vaak al duidelijkheid."),
    ("h2","Strafzaken: een aparte positie"),
    ("p","In het strafrecht ligt dit anders. Een verdachte is niet verplicht een advocaat te hebben, maar heeft daar wel recht op, ook als de kosten niet direct op te brengen zijn. Bij aanhouding is bijstand door een advocaat voorafgaand aan het eerste verhoor een vast onderdeel van de procedure."),
    ("p",DISCLAIMER),
  ]},
 {"slug":"mediation-of-rechtszaak","titel":"Mediation of een rechtszaak: de verschillen op een rij",
  "cat":"Mediation","datum":"2026-07-01","datum_nl":"1 juli 2026","leestijd":5,
  "excerpt":"Een geschil hoeft niet altijd bij de rechter te eindigen. Mediation biedt een alternatief traject, met een andere aanpak en andere uitkomst.",
  "body":[
    ("p","Een conflict, bijvoorbeeld bij een echtscheiding, een arbeidsgeschil of een zakelijk meningsverschil, kan op meerdere manieren worden opgelost. Een rechtszaak is de bekendste weg, maar mediation is in veel situaties een volwaardig alternatief, met een ander verloop en een andere uitkomst."),
    ("h2","Wat mediation inhoudt"),
    ("p","Bij mediation begeleidt een onafhankelijke mediator de partijen naar een eigen oplossing. De mediator neemt zelf geen beslissing, maar structureert het gesprek en helpt partijen hun belangen te verwoorden. Het traject is vertrouwelijk en de uitkomst wordt vastgelegd in een overeenkomst waar beide partijen mee instemmen."),
    ("h2","Wat een rechtszaak inhoudt"),
    ("p","Bij een rechtszaak leggen partijen het geschil voor aan een rechter, die na het horen van beide kanten een bindende beslissing neemt. Die uitspraak is afdwingbaar, ook als een van beide partijen het er niet mee eens is. Een procedure kent vaste termijnen en formele spelregels."),
    ("h2","De belangrijkste verschillen"),
    ("ul",["Bij mediation bepalen partijen zelf de uitkomst, bij een rechtszaak beslist de rechter.",
           "Mediation is doorgaans sneller en goedkoper dan een volledige procedure.",
           "Een rechterlijke uitspraak is afdwingbaar, een mediation-overeenkomst berust op wederzijdse instemming.",
           "Mediation laat meer ruimte voor een oplossing die verder gaat dan een juridisch geschilpunt, bijvoorbeeld bij een lopende samenwerking of ouderschap."]),
    ("callout","Mediation werkt het best wanneer beide partijen bereid zijn tot een gesprek. Is die bereidheid er niet, dan biedt een rechtszaak meer zekerheid over een uitkomst."),
    ("h2","Wanneer welke route past"),
    ("p","Bij een echtscheiding met kinderen kiezen veel mensen voor mediation, juist omdat er na de scheiding nog contact blijft. Bij een geschil waarbij snel duidelijkheid nodig is, of waarbij een van de partijen niet wil meewerken, ligt een rechtszaak eerder voor de hand. Een advocaat of mediator kan meedenken over welke route bij een specifieke situatie past."),
    ("p",DISCLAIMER),
  ]},
 {"slug":"ontslag-aangezegd-de-stappen","titel":"Ontslag aangezegd: dit zijn de stappen die volgen","cat":"Arbeidsrecht","datum":"2026-07-15","datum_nl":"15 juli 2026","leestijd":6,
  "excerpt":"Ontslag komt vaak onverwacht en roept meteen vragen op. Een overzicht van de mogelijke routes en de stappen die daarbij horen.",
  "body":[
    ("p","Ontslag komt zelden gelegen en roept al snel vragen op: mag dit zomaar, welke rechten zijn er, en wat gebeurt er nu. In Nederland is ontslag aan strikte regels gebonden, en de te volgen route hangt af van de reden voor het ontslag."),
    ("h2","De belangrijkste ontslagroutes"),
    ("ul",["Ontslag via het UWV, bij bedrijfseconomische redenen of langdurige arbeidsongeschiktheid.",
           "Ontslag via de kantonrechter, bijvoorbeeld bij een verstoorde arbeidsrelatie of disfunctioneren.",
           "Ontslag met wederzijds goedvinden, vastgelegd in een vaststellingsovereenkomst.",
           "Ontslag op staande voet, bij een dringende reden, wat een zware en uitzonderlijke maatregel is."]),
    ("h2","Een vaststellingsovereenkomst controleren"),
    ("p","Bij ontslag met wederzijds goedvinden krijgt de werknemer een vaststellingsovereenkomst voorgelegd. Daarin staan afspraken over de einddatum, een eventuele vergoeding en de reden van uitdiensttreding. Deze overeenkomst is niet zomaar bindend: er geldt een wettelijke bedenktermijn van veertien dagen waarbinnen de werknemer zonder opgaaf van reden kan terugkomen op de instemming."),
    ("callout","Een vaststellingsovereenkomst laten controleren, bijvoorbeeld door een advocaat arbeidsrecht, voorkomt dat er onnodig rechten worden prijsgegeven. Vaak zijn de kosten daarvan deels voor rekening van de werkgever."),
    ("h2","Transitievergoeding"),
    ("p","Bij onvrijwillig ontslag heeft een werknemer in veel gevallen recht op een transitievergoeding. De hoogte hangt af van het aantal dienstjaren en het salaris. Bij ernstig verwijtbaar handelen van de werkgever kan een rechter daarnaast een aanvullende vergoeding toekennen."),
    ("h2","Ontslag op staande voet"),
    ("p","Ontslag op staande voet is de zwaarste vorm van ontslag en vereist een dringende reden, zoals diefstal of ernstig wangedrag. Deze vorm van ontslag gaat direct in, zonder opzegtermijn. Een werknemer die het niet eens is met een ontslag op staande voet, kan dit binnen een korte termijn aanvechten bij de rechter."),
    ("p",DISCLAIMER),
  ]},
]
def article(slug): return next(a for a in ARTICLES if a["slug"]==slug)

def render_body(blocks):
    out=[]
    for b in blocks:
        if b[0]=="p": out.append(f"<p>{esc(b[1])}</p>")
        elif b[0]=="h2": out.append(f"<h2>{esc(b[1])}</h2>")
        elif b[0]=="ul": out.append("<ul>"+"".join(f"<li>{esc(x)}</li>" for x in b[1])+"</ul>")
        elif b[0]=="callout": out.append(f'<div class="callout"><p>{esc(b[1])}</p></div>')
    return "".join(out)

def news_card(a):
    return f"""<article class="news-card">
    <div class="nc-body">
      <span class="news-cat">{esc(a['cat'])}</span>
      <h3><a href="/nieuws/{a['slug']}/" style="color:inherit;text-decoration:none">{esc(a['titel'])}</a></h3>
      <p>{esc(a['excerpt'])}</p>
      <div class="news-meta">{esc(a['datum_nl'])} &middot; {a['leestijd']} min lezen</div>
    </div>
  </article>"""

def firm_card(f):
    usp="".join(f'<li>{IC["check"]}<span>{esc(u)}</span></li>' for u in f["usps"][:3])
    tags="".join(f'<span class="rg-tag">{esc(n)}</span>' for n in f["rg_namen"][:4])
    return f"""<article class="firm-card">
    <div class="fmain">
      <span class="firm-badge">{IC['shield']}{esc(f['badge'])}</span>
      <p class="fname">{esc(f['naam'])}</p>
      <p class="floc">{IC['pin']} {esc(f['plaats'])}</p>
      <p>{esc(f['tagline'])}</p>
      <ul class="firm-usp" style="margin-top:14px">{usp}</ul>
    </div>
    <div class="fside">
      <span class="for-who">Rechtsgebieden</span>
      <div class="firm-tags">{tags}</div>
      <div class="links">
        <a class="btn btn-navy" href="/advocatenkantoren/{f['slug']}/">Bekijk profiel {IC['arrow']}</a>
      </div>
    </div>
  </article>"""

def page_home():
    path="/"; crumbs=[("Home","/")]
    ld=[
      {"@context":"https://schema.org","@type":"WebSite","@id":BASE+"/#website","url":BASE+"/","name":SITE,"inLanguage":"nl-NL","description":"DSW Advocaten is een onafhankelijke gids voor het vinden van een advocaat en het begrijpen van juridische onderwerpen in gewone taal."},
      {"@context":"https://schema.org","@type":"Organization","@id":BASE+"/#org","name":SITE,"url":BASE+"/","email":EMAIL,"logo":BASE+"/assets/icons/logo-mark.svg"},
      breadcrumb(crumbs),
    ]
    stappen=[("search","Oriënteren","Lees op DSW Advocaten in gewone taal wat een rechtsgebied inhoudt en welke stappen bij een situatie horen."),
             ("users","Kantoor kiezen","Bekijk de aanbevolen advocatenkantoren en hun specialisaties, en kies wie bij de situatie past."),
             ("mail","Contact opnemen","Neem rechtstreeks contact op met het gekozen kantoor voor een kennismakingsgesprek.")]
    stap_html="".join(f'<div class="step"><div class="n">{i+1}</div><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></div>' for i,(ic,t,d) in enumerate(stappen))
    rg_html="".join(f'<div class="rg-card"><h3>{esc(r["naam"])}</h3><p>{esc(r["desc"])}</p></div>' for r in RECHTSGEBIEDEN[:6])
    firm_html="".join(firm_card(f) for f in FIRMS)
    news_html="".join(news_card(a) for a in ARTICLES[:3])
    h=head("DSW Advocaten | de onafhankelijke gids voor juridische hulp",
      "DSW Advocaten helpt bij het vinden van de juiste advocaat en legt rechtsgebieden uit in gewone taal. Onafhankelijk, met aanbevolen advocatenkantoren per specialisatie.",path,ld)
    h+=f"""<section class="hero">
  <div class="wrap hero-inner">
    <span class="eyebrow">{IC['compass']}Advocatuur gids</span>
    <h1>De weg vinden in het recht, <em>zonder</em> vakjargon</h1>
    <p class="lead">DSW Advocaten legt rechtsgebieden uit in gewone taal en brengt aanbevolen advocatenkantoren per specialisatie in beeld. Onafhankelijk, zodat de keuze voor een advocaat weloverwogen kan worden gemaakt.</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="/advocatenkantoren/">Bekijk aanbevolen kantoren {IC['arrow']}</a>
      <a class="btn btn-ghost-light" href="/rechtsgebieden/">Verken de rechtsgebieden</a>
    </div>
    <div class="hero-stats">
      <div><div class="n">10</div><div class="l">rechtsgebieden uitgelicht</div></div>
      <div><div class="n">2</div><div class="l">aanbevolen kantoren</div></div>
      <div><div class="n">0</div><div class="l">euro voor het gebruik van deze gids</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">{IC['compass']}Zo werkt het</span>
      <h2>In drie stappen bij de juiste advocaat</h2>
    </div>
    <div class="steps">{stap_html}</div>
  </div>
</section>

<section class="section panel">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['scale']}Rechtsgebieden</span>
      <h2>Veelvoorkomende rechtsgebieden</h2>
      <p class="lead">Een greep uit de onderwerpen waar mensen het vaakst mee te maken krijgen.</p>
    </div>
    <div class="grid cols-3">{rg_html}</div>
    <p style="margin-top:24px"><a class="more" href="/rechtsgebieden/">Alle rechtsgebieden bekijken {IC['arrow']}</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['users']}Aanbevolen</span>
      <h2>Advocatenkantoren in de spotlight</h2>
      <p class="lead">Twee kantoren die DSW Advocaten uitlicht vanwege hun specialisatie en aanpak.</p>
    </div>
    <div class="grid cols-2" style="align-items:stretch">{firm_html}</div>
  </div>
</section>

<section class="section panel">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['doc']}Nieuws</span>
      <h2>Laatste artikelen</h2>
    </div>
    <div class="grid cols-3">{news_html}</div>
    <p style="margin-top:24px"><a class="more" href="/nieuws/">Alle artikelen bekijken {IC['arrow']}</a></p>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <div class="cta-band">
      <h2>Op zoek naar een advocaat?</h2>
      <p>Bekijk de aanbevolen kantoren en hun specialisaties, en neem rechtstreeks contact op voor een kennismaking.</p>
      <a class="btn btn-gold" href="/advocatenkantoren/">Naar de aanbevolen kantoren {IC['arrow']}</a>
    </div>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_over():
    path="/over/"; crumbs=[("Home","/"),("Over",path)]
    ld=[{"@context":"https://schema.org","@type":"AboutPage","@id":BASE+path,"url":BASE+path,"name":"Over DSW Advocaten","inLanguage":"nl-NL"},breadcrumb(crumbs)]
    h=head("Over DSW Advocaten | de gedachte achter de gids | "+SITE,
      "DSW Advocaten is een onafhankelijk redactioneel platform dat rechtsgebieden uitlegt in gewone taal en advocatenkantoren uitlicht. Lees hoe het platform werkt.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap prose">
    <span class="eyebrow">{IC['compass']}Over het platform</span>
    <h1>Een gids, geen advocatenkantoor</h1>
    <p class="lead">DSW Advocaten is een onafhankelijke advocatuur gids. Het platform helpt mensen op weg wanneer ze met een juridische vraag zitten, door rechtsgebieden uit te leggen in gewone taal en door advocatenkantoren uit te lichten die daarin gespecialiseerd zijn.</p>
    <h2>Waarom deze gids bestaat</h2>
    <p>Een juridisch probleem komt zelden gelegen, en de stap naar een advocaat voelt voor veel mensen groot. Vaktaal, onduidelijkheid over kosten en de vraag welk kantoor bij een situatie past, zorgen voor drempelvrees. DSW Advocaten probeert die drempel te verlagen door heldere achtergrondinformatie te bieden en door een beperkt aantal kantoren voor te stellen, met uitleg over waar ze goed in zijn.</p>
    <h2>Hoe kantoren op de gids komen</h2>
    <p>DSW Advocaten licht bewust een beperkt aantal kantoren uit, in plaats van een lange, onoverzichtelijke lijst te tonen. Een kantoor wordt opgenomen op basis van een duidelijke specialisatie of een aanpak die opvalt, zoals een sterke regionale positie of een uitgesproken focus op één rechtsgebied. De profielen worden door de redactie geschreven en beschrijven het kantoor op basis van door het kantoor zelf gedeelde informatie.</p>
    <div class="callout"><p><strong>Onafhankelijke redactie, geen advies.</strong> DSW Advocaten is zelf geen advocatenkantoor, behandelt geen zaken en geeft geen juridisch advies over individuele situaties. De artikelen op deze site bieden algemene informatie; voor een concrete zaak blijft persoonlijk contact met een advocaat de aangewezen weg.</p></div>
    <h2>Wie er schrijft</h2>
    <p>De inhoud van DSW Advocaten wordt geschreven door de redactie, met als doel juridische onderwerpen begrijpelijk te maken zonder ze te versimpelen. Meer over de persoon achter de artikelen staat op de pagina over de redactie.</p>
    <p style="margin-top:18px"><a class="btn btn-navy" href="/schrijfster/">Over de redactie {IC['arrow']}</a> <a class="btn btn-ghost" href="/rechtsgebieden/">Verken de rechtsgebieden</a></p>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_rechtsgebieden_index():
    path="/rechtsgebieden/"; crumbs=[("Home","/"),("Rechtsgebieden",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Rechtsgebieden","inLanguage":"nl-NL"},
        {"@context":"https://schema.org","@type":"ItemList","name":"Rechtsgebieden","itemListElement":[{"@type":"ListItem","position":i+1,"name":r["naam"],"url":BASE+f"/rechtsgebieden/{r['slug']}/"} for i,r in enumerate(RECHTSGEBIEDEN)]},
        breadcrumb(crumbs)]
    cards="".join(f"""<div class="rg-card"><h3><a href="/rechtsgebieden/{r['slug']}/" style="color:inherit;text-decoration:none">{esc(r['naam'])}</a></h3><p>{esc(r['desc'])}</p><p style="margin-top:6px"><a class="more" href="/rechtsgebieden/{r['slug']}/">Meer lezen {IC['arrow']}</a></p></div>""" for r in RECHTSGEBIEDEN)
    h=head("Rechtsgebieden | overzicht in gewone taal | "+SITE,
      "Een overzicht van veelvoorkomende rechtsgebieden, van familierecht tot fiscaal recht, uitgelegd in gewone taal, met de aanbevolen kantoren per specialisatie.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['scale']}Rechtsgebieden</span>
      <h1>Rechtsgebieden in gewone taal</h1>
      <p class="lead">Het recht is opgedeeld in gebieden die elk hun eigen regels en procedures kennen. Dit overzicht legt de meest voorkomende rechtsgebieden kort uit.</p>
    </div>
    <div class="grid cols-3">{cards}</div>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_rechtsgebied(r):
    path=f"/rechtsgebieden/{r['slug']}/"; crumbs=[("Home","/"),("Rechtsgebieden","/rechtsgebieden/"),(r["naam"],path)]
    ld=[{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":r["naam"],"inLanguage":"nl-NL"},breadcrumb(crumbs)]
    fh="".join(firm_card(f) for f in firms_for(r["slug"]))
    h=head(f"{r['naam']} | rechtsgebied uitgelegd | {SITE}",
      f"{r['naam']} uitgelegd in gewone taal, met de aanbevolen advocatenkantoren die in dit rechtsgebied gespecialiseerd zijn.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap prose">
    <span class="eyebrow">{IC['scale']}Rechtsgebied</span>
    <h1>{esc(r['naam'])}</h1>
    <p class="lead">{esc(r['desc'])}</p>
  </div>
</section>

<section class="section panel">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['users']}Aanbevolen bij dit rechtsgebied</span>
      <h2>Kantoren gespecialiseerd in {esc(r['naam'].lower())}</h2>
    </div>
    <div class="grid cols-2" style="align-items:stretch">{fh if fh else '<p class="lead">Voor dit rechtsgebied wordt op dit moment nog geen kantoor uitgelicht.</p>'}</div>
    <p style="margin-top:22px"><a class="more" href="/rechtsgebieden/">Terug naar alle rechtsgebieden {IC['arrow']}</a></p>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_nieuws_index():
    path="/nieuws/"; crumbs=[("Home","/"),("Nieuws",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Nieuws","inLanguage":"nl-NL"},breadcrumb(crumbs)]
    cards="".join(news_card(a) for a in ARTICLES)
    h=head("Nieuws | juridische onderwerpen uitgelegd | "+SITE,
      "Artikelen over juridische onderwerpen in gewone taal: van de kosten van een advocaat tot ontslagrecht en mediation.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['doc']}Nieuws</span>
      <h1>Juridische onderwerpen uitgelegd</h1>
      <p class="lead">Achtergrondartikelen die juridische thema's toegankelijk maken, geschreven door de redactie van DSW Advocaten.</p>
    </div>
    <div class="grid cols-3">{cards}</div>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_artikel(a):
    path=f"/nieuws/{a['slug']}/"; crumbs=[("Home","/"),("Nieuws","/nieuws/"),(a["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":a["titel"],"description":a["excerpt"],"datePublished":a["datum"],"inLanguage":"nl-NL","author":{"@type":"Person","name":AUTHOR},"publisher":{"@type":"Organization","name":SITE}},breadcrumb(crumbs)]
    body=render_body(a["body"])
    related=[x for x in ARTICLES if x["slug"]!=a["slug"]][:2]
    rel_html="".join(news_card(x) for x in related)
    h=head(f"{a['titel']} | {SITE}", a["excerpt"], path, ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap prose">
    <span class="eyebrow">{IC['doc']}{esc(a['cat'])}</span>
    <h1>{esc(a['titel'])}</h1>
    <p class="news-meta" style="margin-bottom:26px">Door {esc(AUTHOR)} &middot; {esc(a['datum_nl'])} &middot; {a['leestijd']} min lezen</p>
    {body}
    <div class="byline">
      <img src="/assets/img/schrijfster-avatar.svg" alt="{esc(AUTHOR)}">
      <div class="who">{esc(AUTHOR)}<small>{esc(AUTHOR_ROLE)}</small></div>
    </div>
  </div>
</section>

<section class="section panel">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">{IC['doc']}Meer lezen</span><h2>Andere artikelen</h2></div>
    <div class="grid cols-2">{rel_html}</div>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_aanbieders_index():
    path="/advocatenkantoren/"; crumbs=[("Home","/"),("Aanbevolen kantoren",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Aanbevolen advocatenkantoren","inLanguage":"nl-NL"},
        {"@context":"https://schema.org","@type":"ItemList","name":"Aanbevolen advocatenkantoren","itemListElement":[{"@type":"ListItem","position":i+1,"name":f["naam"],"url":BASE+f"/advocatenkantoren/{f['slug']}/"} for i,f in enumerate(FIRMS)]},
        breadcrumb(crumbs)]
    cards="".join(firm_card(f) for f in FIRMS)
    h=head("Aanbevolen advocatenkantoren | "+SITE,
      "Een beperkt en uitgelicht aanbod advocatenkantoren, elk met een eigen specialisatie. Bekijk de profielen en kies het kantoor dat past.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['users']}Aanbevolen kantoren</span>
      <h1>Advocatenkantoren in de spotlight</h1>
      <p class="lead">DSW Advocaten licht bewust een beperkt aantal kantoren uit, elk met een eigen specialisatie of aanpak. Zo blijft de keuze overzichtelijk.</p>
    </div>
    <div class="grid cols-2" style="align-items:stretch">{cards}</div>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_firm(f):
    path=f"/advocatenkantoren/{f['slug']}/"; crumbs=[("Home","/"),("Aanbevolen kantoren","/advocatenkantoren/"),(f["naam"],path)]
    ld=[{"@context":"https://schema.org","@type":"LegalService","@id":BASE+path,"name":f["naam"],"url":f["website"],"telephone":f["tel"],"email":f["email"],"address":f["adres"]},breadcrumb(crumbs)]
    secs="".join(f"<h2>{esc(t)}</h2><p>{esc(d)}</p>" for t,d in f["secties"])
    usp="".join(f'<li>{IC["check"]}<span>{esc(u)}</span></li>' for u in f["usps"])
    tags="".join(f'<span class="rg-tag">{esc(n)}</span>' for n in f["rg_namen"])
    situ="".join(f'<span class="rg-tag">{esc(s)}</span>' for s in f["situaties"])
    h=head(f"{f['naam']} in {f['plaats']} | {SITE}",
      f"{f['naam']} in {f['plaats']}. {f['tagline']} Profiel met specialisaties, aanpak en contactgegevens.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap prose">
    <span class="firm-badge">{IC['shield']}{esc(f['badge'])}</span>
    <h1>{esc(f['naam'])}</h1>
    <p class="lead">{esc(f['lead'])}</p>
    <div class="firm-tags" style="margin:18px 0 4px">{tags}</div>
    <ul class="firm-usp" style="margin:18px 0">{usp}</ul>
    {secs}
    <h2>Veelvoorkomende situaties</h2>
    <div class="firm-tags">{situ}</div>
    <div class="callout" style="margin-top:26px">
      <p><strong>Contact met {esc(f['naam'])}</strong></p>
      <p style="margin:.3em 0">{esc(f['adres'])}</p>
      <p style="margin:.3em 0">Telefoon: <a href="{f['tel_href']}">{esc(f['tel'])}</a></p>
      <p style="margin:.3em 0">E-mail: <a href="mailto:{f['email']}">{esc(f['email'])}</a></p>
    </div>
    <p style="margin-top:22px"><a class="btn btn-navy" href="{f['website']}" target="_blank" rel="nofollow noopener">Naar {esc(f['domain'])} {IC['arrow']}</a> <a class="btn btn-ghost" href="/advocatenkantoren/">Terug naar alle kantoren</a></p>
    <p class="disclaimer" style="margin-top:18px">Dit profiel is een redactionele weergave op basis van door {esc(f['naam'])} gedeelde informatie en vormt geen juridisch advies.</p>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_schrijfster():
    path="/schrijfster/"; crumbs=[("Home","/"),("Over de redactie",path)]
    ld=[{"@context":"https://schema.org","@type":"Person","@id":BASE+"/#nina","name":AUTHOR,"jobTitle":AUTHOR_ROLE,"worksFor":{"@type":"Organization","name":SITE}},
        {"@context":"https://schema.org","@type":"ProfilePage","@id":BASE+path,"url":BASE+path,"name":"Over de redactie","inLanguage":"nl-NL"},breadcrumb(crumbs)]
    h=head(f"Over de redactie: {AUTHOR} | "+SITE,
      f"{AUTHOR} is {AUTHOR_ROLE.lower()} en schrijft de artikelen op DSW Advocaten, gericht op heldere uitleg van juridische onderwerpen.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap">
    <div class="persona-hero">
      <div class="persona-photo"><img src="/assets/img/schrijfster-avatar.svg" alt="{esc(AUTHOR)}"></div>
      <div>
        <span class="eyebrow">{IC['quill']}Over de redactie</span>
        <h1>{esc(AUTHOR)}</h1>
        <p class="lead">{esc(AUTHOR_ROLE)} bij DSW Advocaten. Nina schrijft de artikelen op deze site en stelt de profielen van de aanbevolen advocatenkantoren samen.</p>
      </div>
    </div>
  </div>
</section>

<section class="section panel">
  <div class="wrap prose">
    <h2>Waarom deze gids</h2>
    <p>Nina Verschuur werkte jarenlang als redacteur bij een juridisch vakblad, waar ze rechtbankuitspraken en wetswijzigingen vertaalde naar leesbare artikelen voor een breed publiek. Die ervaring vormt de basis van DSW Advocaten: juridische onderwerpen begrijpelijk maken, zonder de inhoud tekort te doen.</p>
    <h2>Geen advocaat, wel grondig</h2>
    <p>Nina is zelf geen advocaat. Voor elk artikel en elk kantoorprofiel op deze site baseert ze zich op openbare, betrouwbare bronnen en op informatie die kantoren zelf delen. Waar een onderwerp juridisch genuanceerd ligt, is dat in de tekst terug te lezen, inclusief een verwijzing naar professioneel advies waar dat past.</p>
    <h2>Contact met de redactie</h2>
    <p>Vragen, aanvullingen of een tip voor een artikel zijn welkom via <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_contact():
    path="/contact/"; crumbs=[("Home","/"),("Contact",path)]
    ld=[breadcrumb(crumbs),{"@context":"https://schema.org","@type":"ContactPage","@id":BASE+path,"url":BASE+path,"name":"Contact","inLanguage":"nl-NL"}]
    h=head("Contact | "+SITE,"Vraag, aanvulling of een kantoor aanmelden voor DSW Advocaten? Een e-mail naar de redactie is de snelste weg.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap prose">
    <span class="eyebrow">{IC['mail']}Contact</span>
    <h1>Contact met DSW Advocaten</h1>
    <p class="lead">Voor vragen over deze gids, een aanvulling op een artikel, of interesse om als kantoor onder de aandacht gebracht te worden, is e-mail de snelste weg. DSW Advocaten behandelt zelf geen juridische zaken en verwijst daarvoor naar de aanbevolen kantoren.</p>
    <div class="callout">
      <p><strong>E-mail de redactie</strong></p>
      <p style="margin:.3em 0"><a href="mailto:{EMAIL}" style="font-size:1.1rem;font-weight:700">{EMAIL}</a></p>
    </div>
    <p>Voor een juridische vraag over een persoonlijke situatie is rechtstreeks contact met een van de <a href="/advocatenkantoren/">aanbevolen advocatenkantoren</a> de aangewezen weg.</p>
  </div>
</section>"""
    h+=footer(); write(path,h)

def legal_page(path, title, blocks):
    crumbs=[("Home","/"),(title,path)]
    ld=[breadcrumb(crumbs),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":title,"inLanguage":"nl-NL"}]
    h=head(f"{title} | {SITE}", f"{title} van {SITE}.", path, ld)
    h+=crumbs_html(crumbs)
    h+=f'<section class="section"><div class="wrap prose"><h1>{esc(title)}</h1>{"".join(blocks)}</div></section>'
    h+=footer(); write(path,h)

def privacy():
    legal_page("/privacybeleid/","Privacybeleid",[
      "<p>DSW Advocaten is een redactioneel platform en verwerkt zo min mogelijk persoonsgegevens.</p>",
      "<h2>Welke gegevens</h2><p>Er is geen contactformulier op deze site. Wie via e-mail contact opneemt, deelt gegevens rechtstreeks met DSW Advocaten voor de afhandeling van die vraag. Wie via een link contact opneemt met een aanbevolen advocatenkantoor, deelt gegevens met dat kantoor, niet met DSW Advocaten.</p>",
      "<h2>Statistieken</h2><p>Indien bezoekstatistieken worden bijgehouden, gebeurt dat zo privacyvriendelijk mogelijk en zonder gegevens te verkopen aan derden.</p>",
      "<h2>Bewaartermijn</h2><p>E-mails die naar de redactie worden gestuurd, worden niet langer bewaard dan nodig is om de vraag te beantwoorden.</p>",
      f"<h2>Vragen</h2><p>Vragen over privacy kunnen per e-mail gesteld worden via {EMAIL}.</p>",
    ])

def cookies():
    legal_page("/cookiebeleid/","Cookiebeleid",[
      "<p>Deze site plaatst zo min mogelijk cookies en gebruikt geen advertentiecookies.</p>",
      "<h2>Functioneel</h2><p>Functionele cookies zorgen dat de site goed werkt en zijn noodzakelijk voor het bezoek.</p>",
      f"<h2>Vragen</h2><p>Vragen over cookies kunnen per e-mail gesteld worden via {EMAIL}.</p>",
    ])

def not_found():
    h=head("Pagina niet gevonden | "+SITE,"De opgevraagde pagina bestaat niet.","/404.html",None)
    h+=f"""<section class="section"><div class="wrap prose" style="text-align:center">
      <span class="eyebrow" style="justify-content:center">404</span>
      <h1>Deze pagina bestaat niet</h1>
      <p class="lead">Mogelijk is de link verouderd. Terug naar de startpagina of bekijk de aanbevolen advocatenkantoren.</p>
      <p><a class="btn btn-navy" href="/">Naar de homepage {IC['arrow']}</a> <a class="btn btn-ghost" href="/advocatenkantoren/">Aanbevolen kantoren</a></p>
    </div></section>"""
    h+=footer()
    open(os.path.join(OUT,"404.html"),"w",encoding="utf-8").write(h)

def extras():
    urls=["/","/over/","/rechtsgebieden/","/nieuws/","/advocatenkantoren/","/schrijfster/","/contact/","/privacybeleid/","/cookiebeleid/"]
    urls+=[f"/rechtsgebieden/{r['slug']}/" for r in RECHTSGEBIEDEN]
    urls+=[f"/nieuws/{a['slug']}/" for a in ARTICLES]
    urls+=[f"/advocatenkantoren/{f['slug']}/" for f in FIRMS]
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{u}</loc></url>\n" for u in urls)+"</urlset>\n"
    open(os.path.join(OUT,"sitemap.xml"),"w").write(sm)
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT,"_headers"),"w").write("/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    open(os.path.join(OUT,"_redirects"),"w").write("https://www.dswadvocaten.nl/* https://dswadvocaten.nl/:splat 301!\n")

def copy_assets():
    import shutil
    dst=os.path.join(OUT,"assets")
    if os.path.exists(dst): shutil.rmtree(dst)
    shutil.copytree(os.path.join(SRC,"assets"), dst)

def main():
    import shutil
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT, exist_ok=True)
    copy_assets()
    page_home(); page_over(); page_rechtsgebieden_index()
    for r in RECHTSGEBIEDEN: page_rechtsgebied(r)
    page_nieuws_index()
    for a in ARTICLES: page_artikel(a)
    page_aanbieders_index()
    for f in FIRMS: page_firm(f)
    page_schrijfster(); page_contact(); privacy(); cookies(); not_found(); extras()
    print("Build klaar in", OUT)

if __name__=="__main__":
    main()
