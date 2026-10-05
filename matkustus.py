from geopy.distance import geodesic
import random

from animaatiot import lento_animaatio


def hae_lahimmat_maat(kursori, nykyinen):

    sql = """
    SELECT latitude_deg, longitude_deg
    FROM airport
    WHERE iso_country IN (
        SELECT iso_country
        FROM country
        WHERE LOWER(name) = LOWER(%s)
    )
    LIMIT 1
    """

    kursori.execute(sql, (nykyinen,))

    koordinaatit = kursori.fetchone()

    if koordinaatit is None:

        print("Maata ei löytynyt.")

        return []

    sql = """
    SELECT country.name,
           airport.latitude_deg,
           airport.longitude_deg
    FROM airport, country
    WHERE airport.iso_country = country.iso_country
    AND LOWER(country.name) != LOWER(%s)
    GROUP BY country.name
    """

    kursori.execute(sql, (nykyinen,))

    tulokset = kursori.fetchall()

    etaisyydet = []

    for nimi, lat, lon in tulokset:

        etaisyys = geodesic(
            koordinaatit,
            (lat, lon)
        ).kilometers

        etaisyydet.append(
            (etaisyys, nimi)
        )

    etaisyydet.sort()

    vaihtoehdot = []

    for etaisyys, nimi in etaisyydet:

        hinta = random.randint(200, 300)

        vaihtoehdot.append(
            (nimi, hinta)
        )

        if len(vaihtoehdot) == 3:
            break

    return vaihtoehdot
from geopy.distance import geodesic
import time


def hae_lahimmat_maat(kursori, nykyinen):

    sql = """
    SELECT latitude_deg, longitude_deg
    FROM airport
    WHERE iso_country IN (
        SELECT iso_country
        FROM country
        WHERE LOWER(name) = LOWER(%s)
    )
    LIMIT 1
    """

    kursori.execute(sql, (nykyinen,))

    koordinaatit = kursori.fetchone()

    if koordinaatit is None:
        print("Nykyistä maata ei löytynyt.")
        return []

    sql = """
    SELECT country.name,
           airport.latitude_deg,
           airport.longitude_deg
    FROM airport
    JOIN country
        ON airport.iso_country = country.iso_country
    WHERE LOWER(country.name) != LOWER(%s)
    """

    kursori.execute(sql, (nykyinen,))

    tulokset = kursori.fetchall()

    etaisyydet = []

    for nimi, lat, lon in tulokset:

        etaisyys = geodesic(
            koordinaatit,
            (lat, lon)
        ).kilometers

        etaisyydet.append(
            (etaisyys, nimi)
        )

    etaisyydet.sort()

    vaihtoehdot = []
    kaytetyt_maat = set()

    for etaisyys, nimi in etaisyydet:

        if nimi in kaytetyt_maat:
            continue

        kaytetyt_maat.add(nimi)

        hinta = int(etaisyys / 100) + 100

        vaihtoehdot.append(
            (nimi, hinta)
        )

        if len(vaihtoehdot) == 3:
            break

    return vaihtoehdot


def matkusta(
    nykyinen,
    raha,
    valinta,
    vaihtoehdot,
    kaydyt_maat
):

    try:
        numero = int(valinta)

    except ValueError:
        print(
            "Kirjoita matkakohteen numero, esimerkiksi 1, 2 tai 3."
        )

        return nykyinen, raha

    if numero < 1 or numero > len(vaihtoehdot):

        print(
            "Tuolla numerolla ei ole matkakohdetta."
        )

        return nykyinen, raha

    maa, hinta = vaihtoehdot[numero - 1]

    if raha < hinta:

        print(
            "Ei oo tarpeeksi catcoinia tähän matkaan."
        )

        return nykyinen, raha

    print("\nLähdit lentoon...")

    print("""
       __|__
--@--@--(_)--@--@--
""")

    time.sleep(2)

    print("""
       __|__
      \\___/
        | |
        | |
       _|_|______________
              /|\\ 
            */ | \\*
            /  -+-  \\
         ---o--(_)--o---
           /  0 " 0  \\
         */     |     \\*
        </      |      \\
       */       |       \\*

Saavuit lentokentälle!
""")

    time.sleep(2)

    nykyinen = maa
    raha -= hinta

    if maa not in kaydyt_maat:
        kaydyt_maat.append(maa)

    print(
        "Saavuit maahan:",
        nykyinen
    )

    print(
        "Matka maksoi",
        hinta,
        "catcoin."
    )

    print(
        "Rahaa jäljellä:",
        raha,
        "catcoin."
    )

    return nykyinen, raha


def nayta_kaydyt_maat(kaydyt_maat):

    print("\n=============================")
    print("        KÄYDYT MAAT")
    print("=============================")

    for numero, maa in enumerate(kaydyt_maat, 1):

        print(
            numero,
            ".",
            maa
        )

    print("=============================")