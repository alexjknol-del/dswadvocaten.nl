# dswadvocaten.nl (DSW Advocaten)

Statische site, gegenereerd met een Python-script. Geen frameworks nodig. Onafhankelijke advocatuur gids: rechtsgebieden uitgelegd in gewone taal, met een beperkt aantal uitgelichte advocatenkantoren.

## Bouwen
    python3 build.py
De site komt in `site/`.

## Deployen (Cloudflare Pages, via GitHub)
1. Maak een nieuwe GitHub-repository en zet de inhoud van deze map (behalve `site/`) in de root.
2. Koppel de repo aan Cloudflare Pages.
3. Instellingen:
   - Framework preset: None
   - Build command: `python3 build.py`
   - Build output directory: `site`
4. Voeg het domein `dswadvocaten.nl` toe onder Custom domains in Cloudflare Pages.

## Structuur
- Eigen huisstijl: navy met brons/goud op een warme papieren ondergrond, Newsreader (serif) voor koppen en Inter voor lopende tekst.
- Pagina's: home, over, rechtsgebieden (index + 15 detailpagina's), nieuws (index + 4 artikelen), aanbevolen advocatenkantoren (index + 12 profielen), schrijfster, contact, privacybeleid, cookiebeleid, 404.
- Contact bestaat bewust alleen uit een mailto-link naar info@dswadvocaten.nl, zonder formulier.
- De schrijfster (Nina Verschuur) is een bewust getekende, memoji-achtige illustratie, geen foto: `assets/img/schrijfster-avatar.svg`.

## Een advocatenkantoor toevoegen
1. Open `build.py` en voeg een blok toe aan de lijst `FIRMS`, met `slug`, `naam`, `plaats`, `domain`, `website`, adresgegevens, `usps`, `lead`, `secties` en `situaties`.
2. Koppel het kantoor aan een of meer rechtsgebieden via het veld `rechtsgebieden` (gebruik bestaande slugs uit `RECHTSGEBIEDEN`).
3. De link naar de eigen website van het kantoor wordt automatisch `rel="nofollow noopener"` (in `page_firm`), passend bij een uitgelichte, betaalde of samenwerkingsplaatsing.
4. Draai `python3 build.py` opnieuw.

## Een nieuwsartikel toevoegen
1. Open `build.py` en voeg een blok toe aan de lijst `ARTICLES`, met `slug`, `titel`, `cat`, `date`/`datum_nl`, `leestijd`, `excerpt` en `body`.
2. `body` is een lijst van tuples: `("h2", "Kop")`, `("p", "Tekst")`, `("ul", ["punt", "punt"])` of `("callout", "Tekst")`.
3. Draai `python3 build.py` opnieuw. Het artikel verschijnt automatisch op de homepage, in het nieuwsoverzicht en in de sitemap.

## Inhoud en bronnen
De profielen van Advocatenkantoor Appelman en HuygenLammers Advocaten zijn door de redactie geschreven op basis van publiek beschikbare informatie (eigen website van het kantoor en het register van de Nederlandse orde van advocaten). De nieuwsartikelen zijn originele, door de redactie geschreven achtergrondteksten met een disclaimer dat het geen juridisch advies betreft.
