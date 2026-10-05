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


def matkusta(nykyinen, raha, valinta, vaihtoehdot):

    for maa, hinta in vaihtoehdot:

        if maa.lower() == valinta.lower():

            if raha < hinta:

                print(
                    "Ei oo tarpeeksi catcoinia tähän matkaan."
                )

                return nykyinen, raha

            lento_animaatio()

            nykyinen = maa

            raha -= hinta

            print("Saavuit maahan:", nykyinen)

            print(
                "Matka maksoi",
                hinta,
                "catcoin."
            )

            print(
                "Rahaa jäljellä:",
                raha,
                "catcoin"
            )

            return nykyinen, raha

    print(
        "Ei tollasta vaihtoehtoa, kokeile uudestaan."
    )

    return nykyinen, raha