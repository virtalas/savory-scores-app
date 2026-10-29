# Finnish UI text for i18n/build.py. App terms match the iOS app's Localizable.xcstrings.


def data_note(n, m, of, stores, k, auth):
    about = {None: "", "dishes": " japanilaisista ruoista", "products": " japanilaisista tuotteista"}[of]
    where = "kaupassa" if stores else "paikassa"
    note = f"Perustuu {n} arvioon{about} {m} {where} Helsingin seudulla"
    if k:
        note += f"; mukana paikat, joilla on vähintään {k} {'autenttisuusarviota' if auth else 'arviota'}"
    return (note + ", tilanne lokakuussa 2026. Pisteet ja autenttisuus ovat keskiarvoja kymmenen pisteen asteikolla. "
            "Useimmilla annoksilla on toistaiseksi vain yksi tai kaksi arviota ja ruokalistat muuttuvat, joten katso "
            "ajantasainen järjestys sovelluksesta. Söitkö paikassa, jonka pitäisi olla tällä listalla? "
            "Arvioi se Savory Scoresissa.")


STRINGS = {
    "skip": "Siirry sisältöön",
    "icon_alt": "Savory Scores -sovelluksen kuvake",
    "nav_label": "Päävalikko",
    "nav_screenshots": "Kuvakaappaukset",
    "nav_how": "Näin se toimii",
    "nav_guides": "Oppaat",
    "nav_faq": "Kysymykset",
    "nav_cta": "Lataa sovellus",
    "languages": "Kieli",
    "footer_tag": "Helsingin aidon japanilaisen ruoan katalogi, arvioitu annos kerrallaan.",
    "footer_label": "Alatunniste",
    "footer_download": "Lataa App Storesta",
    "terms": "Käyttöehdot",
    "privacy": "Tietosuojaseloste",
    "made_in": "Tehty Helsingissä",
    "read_guide": "Lue opas",

    "home_title": "Savory Scores: löydä Helsingin paras japanilainen ruoka",
    "home_description": "Löydä Helsingin paras japanilainen ruoka annos kerrallaan. Vertaa kaupungin kaikkia katsudoneja, "
                        "rameneita ja sushia, arvioi ateriat yhdellä napautuksella ja kokoa oma top-listasi. "
                        "Ilmainen iPhonelle.",
    "app_ld_description": "Helsingin aidon japanilaisen ruoan katalogi. Hae ruokakategorian mukaan, arvioi annokset "
                          "yhdellä kysymyksellä (Tilaisitko sen uudestaan?), järjestä autenttisuuden mukaan ja kokoa "
                          "oma top-listasi.",

    "breadcrumb_label": "Murupolku",
    "home": "Etusivu",
    "article_meta": "Savory Scores -opas · Helsinki · Päivitetty lokakuussa 2026",
    "cta_strong": "Löydä suosikkisi Helsingistä.",
    "cta_text": "Savory Scores on ilmainen iPhonelle ja iPadille: hae annosta, vertaa kaikkia kaupungin versioita "
                "ja arvioi se yhdellä napautuksella.",
    "badge_alt": "Lataa Savory Scores App Storesta",
    "related": "Aiheeseen liittyvät oppaat",
    "colon": ": ",
    "more_guides": "Lisää oppaita",
    "back_home": "← Savory Scores -etusivu",
    "next": "Seuraavaksi: {name} →",

    "cities": {"Helsinki": "Helsinki", "Vantaa": "Vantaa"},
    "data": {
        "kicker": "Savory Scoresin datasta",
        "Photo": "Kuva",
        "#": "#",
        "Dish": "Annos",
        "Restaurant": "Ravintola",
        "Store": "Kauppa",
        "Product": "Tuote",
        "Score": "Pisteet",
        "Authenticity": "Autenttisuus",
        "Avg score": "Pisteet (ka.)",
        "Avg authenticity": "Autenttisuus (ka.)",
        "Ratings": "Arvioita",
        "Last rated": "Viimeksi arvioitu",
        "date": lambda month, year: f"{month}/{year}",
        "alt": lambda dish, place, city: f"{dish}, {place}, {city}. Kuva: Savory Scores -käyttäjä",
        "note": data_note,
    },

    "guides": {
        "japanese-restaurants-helsinki": {
            "name": "Japanilaiset ravintolat Helsingissä",
            "desc": "Näin löydät aidot paikat sushitiskeistä shokudōihin ja ohitat fuusiobuffetit.",
            "title": "Japanilaiset ravintolat Helsingissä: näin löydät aidot | Savory Scores",
            "description": "Etsitkö hyvää japanilaista ravintolaa Helsingistä? Näin erotat aidon japanilaisen "
                           "paikan fuusiosta ja vertaat kaupungin japanilaisia annoksia oikeiden arvioiden perusteella.",
        },
        "best-ramen-helsinki": {
            "name": "Paras ramen Helsingissä",
            "desc": "Tonkotsu, shio, shoyu vai vegaaninen: mitä kulhosta kannattaa katsoa ja miten löydät parhaan.",
            "title": "Paras ramen Helsingissä: näin löydät hyvän kulhon | Savory Scores",
            "description": "Missä on Helsingin paras ramen? Tutustu ramen-tyyleihin, opi tunnistamaan hyvä kulho "
                           "ja vertaa kaupungin rameneita oikeiden annosarvioiden perusteella.",
        },
        "best-sushi-helsinki": {
            "name": "Paras sushi Helsingissä",
            "desc": "Sushibaari, omakase vai buffet? Näin arvioit sushin laatua ja löydät parhaat palat.",
            "title": "Paras sushi Helsingissä: näin erotat hyvän sushin buffetrullista | Savory Scores",
            "description": "Etsitkö Helsingin parasta sushia? Näin arvioit riisin ja kalan laatua, erotat "
                           "sushitiskit buffeteista ja löydät annokset, joiden takia kannattaa palata.",
        },
        "authentic-japanese-restaurant": {
            "name": "Miten tunnistaa aito japanilainen ravintola",
            "desc": "Kahdeksan merkkiä ruokalistalla, pöydässä ja lautasella. Tarkista ne ennen kuin istut alas.",
            "title": "Miten tunnistaa aito japanilainen ravintola: 8 merkkiä | Savory Scores",
            "description": "Onko japanilainen ravintola aito vai fuusiota? Kahdeksan merkkiä ruokalistasta, "
                           "riisistä ja lautasesta sekä Helsingin autenttisimmiksi arvioidut paikat.",
        },
        "donburi-helsinki": {
            "name": "Katsudon, gyudon ja donburi Helsingissä",
            "desc": "Mitä kukin japanilainen riisikulho on, miten sen tilaat ja missä vertailet kaupungin kaikkia versioita.",
            "title": "Katsudon, gyudon ja donburi Helsingissä: opas japanilaisiin riisikulhoihin | Savory Scores",
            "description": "Mitä on katsudon tai gyudon, ja mistä Helsingistä saa parhaan? Opas japanilaisiin "
                           "riisikulhoihin ja Helsingin parhaiksi arvioidut donburit.",
        },
        "izakaya-helsinki": {
            "name": "Izakaya Helsingissä",
            "desc": "Mikä izakaya on, mitä tilata ja miten löydät japanilaistyylisen pubi-illan Helsingistä.",
            "title": "Izakaya Helsingissä: mitä tilata japanilaisessa pubissa | Savory Scores",
            "description": "Mikä on izakaya ja mitä siellä kannattaa tilata? Yakitori, karaage, takoyaki ja muut "
                           "pikkuannokset sekä Helsingin parhaiksi arvioidut izakaya-annokset.",
        },
        "japanese-lunch-helsinki": {
            "name": "Japanilainen lounas Helsingissä",
            "desc": "Bento, teishoku, ramen ja donburi: kun suomalainen lounaskulttuuri kohtaa japanilaiset setit.",
            "title": "Japanilainen lounas Helsingissä: bento, teishoku ja ramen | Savory Scores",
            "description": "Missä syödä japanilainen lounas Helsingissä? Mitä tilata (teishoku, donburi, ramen, "
                           "sushisetit) ja miten valitset päivän lounaan annosarvioiden perusteella.",
        },
        "japanese-grocery-helsinki": {
            "name": "Japanilaiset ruokakaupat Helsingissä",
            "desc": "Mistä ostaa japanilaisia raaka-aineita ja herkkuja, ja miten löydät uudelleen ostamisen arvoiset onigirit ja kastikkeet.",
            "title": "Japanilaiset ruokakaupat Helsingissä: mistä ostaa japanilaista ruokaa | Savory Scores",
            "description": "Mistä Helsingistä saa japanilaisia elintarvikkeita? Japanilaiset erikoisliikkeet, "
                           "aasialaiset marketit, perusostoslista ja parhaiksi arvioidut tuotteet.",
        },
        "japanese-food-finland": {
            "name": "Japanilainen ruoka Suomessa",
            "desc": "Mistä aitoa japanilaista ruokaa löytää Suomessa, mitä odottaa ja mistä aloittaa.",
            "title": "Japanilainen ruoka Suomessa: mistä löytää aitoa | Savory Scores",
            "description": "Mitä odottaa japanilaiselta ruoalta Suomessa? Missä japanilaiset ravintolat ovat, "
                           "mitä tilata ja miten Savory Scores auttaa löytämään aidot paikat.",
        },
        "rate-restaurant-dishes": {
            "name": "Miten arvioida ravintola-annoksia",
            "desc": "Miksi annoksen arvioiminen on parempi kuin ravintolan, ja yhden kysymyksen järjestelmä, jota oikeasti jaksaa käyttää.",
            "title": "Miten arvioida ravintola-annoksia (ja muistaa aina, mitä tilata) | Savory Scores",
            "description": "Unohdatko, mikä annos oli hyvä? Pidä ruokapäiväkirjaa yhdellä kysymyksellä: "
                           "Tilaisitko sen uudestaan? Arvioi annoksia, älä ravintoloita.",
        },
    },
}
