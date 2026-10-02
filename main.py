import mysql.connector
from geopy.distance import geodesic
import random
import time

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='fortnite06',
    autocommit=True
)

kursori = yhteys.cursor()

#kysymys kohdat
helppo_kysymykset = [
    ("Mikä on Suomen pääkaupunki?", "helsinki"),
    ("Montako jalkaa kissalla on?", "4"),
    ("mikä on maailman isoin maa?", "venäjä"),
    ("viikon päivä jossa on eniten 'a'", "maanantai"),

]
vaikea_kysymykset = [
    ("Mikä on Japanin pääkaupunki?", "tokyo"),
    ("Missä maassa on Eiffel-torni?", "ranska"),
]
def kysy_kysymys():
    taso = input("Haluatko helpon vai vaikean kysymyksen? (helppo/vaikea): ").lower()
    if taso == "helppo":
        if len(helppo_kysymykset) == 0:
            print("Ei oo helppoja kysymyksiä vielä.")
            return 0
        kysymys, oikea = random.choice(helppo_kysymykset)
    elif taso == "vaikea":
        if len(vaikea_kysymykset) == 0:
            print("Ei oo vaikeita kysymyksiä vielä.")
            return 0
        kysymys, oikea = random.choice(vaikea_kysymykset)
    else:
        print("Kirjota helppo tai vaikea.")
        return 0
    print("\nKysymys:", kysymys)
    vastaus = input("Vastauksesi: ")
    if vastaus.lower() == oikea.lower():
        palkinto = random.randint(200, 400)
        print("Oikein! Sait", palkinto, "catcoinia.")
        return palkinto
    else:
        print("Väärin! Oikea vastaus oli:", oikea)
        return 0
def hae_lahimmat_maat(nykyinen):
    sql = """
    SELECT latitude_deg, longitude_deg
    FROM airport
    WHERE iso_country IN (
        SELECT iso_country FROM country
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
    SELECT country.name, airport.latitude_deg, airport.longitude_deg
    FROM airport, country
    WHERE airport.iso_country = country.iso_country
    AND LOWER(country.name) != LOWER(%s)
    GROUP BY country.name
    """
    kursori.execute(sql, (nykyinen,))
    tulokset = kursori.fetchall()

    etaisyydet = []
    for nimi, lat, lon in tulokset:
        etaisyys = geodesic(koordinaatit, (lat, lon)).kilometers
        etaisyydet.append((etaisyys, nimi))

    etaisyydet.sort()

    vaihtoehdot = []
    for etaisyys, nimi in etaisyydet:
        hinta = random.randint(200, 300)
        vaihtoehdot.append((nimi, hinta))
        if len(vaihtoehdot) == 3:
            break

    return vaihtoehdot


def matkusta(nykyinen, raha, valinta, vaihtoehdot):
    for maa, hinta in vaihtoehdot:
        if maa.lower() == valinta.lower():
            if raha < hinta:
                print("Ei oo tarpeeksi catcoinia tähän matkaan.")
                return nykyinen, raha

            # lentokone animaatio
            print("\nLähdit lentoon...")
            print("""
       __|__
--@--@--(_)--@--@--
""")
            time.sleep(3)
            print("""
__|__
\___/
 | |
 | |
_|_|______________
        /|\ 
      */ | \*
      / -+- \\
  ---o--(_)--o---
    /  0 " 0  \\
  */     |     \*
  /      |      \\
*/       |       \*
saavuit lentokentään
""")
            time.sleep(3)

            nykyinen = maa
            raha -= hinta
            print("Saavuit maahan:", nykyinen)
            print("Matka maksoi", hinta, "catcoin.")
            print("Rahaa jäljellä:", raha, "catcoin")
            return nykyinen, raha

    print("Ei tollasta vaihtoehtoa, kokeile uudestaan.")
    return nykyinen, raha
print("""
       z
       z
   /\\_/\\
  ( -.- )
  /       \\
 (         )
  \\___/
""")
print("kissa on nukkumasssa...")
time.sleep(2)

print("""
   /\\_/\\
  ( o.o )
  /        \\
 (          )
   \\___/
""")
print("Kissa heräsi...")
time.sleep(2)

print("""
   /\\_/\\
  ( ^.^ )
  /        \\
 (           )
   \\___/
""")
print("kissa halua matkustaa thaimaahan!\n")
time.sleep(1)

print("Tervetuloa kissa letopeliin\nSulla on 0 catcoinia. tavoiteet on päästä Thaimaahan.\n"
      "Jos tarvitset rahaa, kirjoita 'tarvin rahaa'")
print("Kirjoita 'tauko' kun haluut lopettaa.\n")
time.sleep(4)

raha = 0
nykyinen = "Egypt"

while True:
    vaihtoehdot = hae_lahimmat_maat(nykyinen)

    print("\nOlet nyt:", nykyinen)
    print("Rahaa jäljellä:", raha, "catcoin")
    print("Voit lentää näihin maihin:")
    for maa, hinta in vaihtoehdot:
        print("-", maa + "-" + str(hinta) + "catcoin")

    valinta = input("Mihin haluat mennä (tai tarvin rahaa / tauko): ")

    if valinta.lower() == "tauko":
        print("\nPeli päättyy.")
        print("Oot nyt maassa:", nykyinen)
        print("Rahaa jäi:", raha, "catcoin")
        break

    if valinta.lower() == "tarvin rahaa":
        palkinto = kysy_kysymys()
        raha += palkinto
        print("Nyt sulla on", raha, "catcoinia.")
        continue

    nykyinen, raha = matkusta(nykyinen, raha, valinta, vaihtoehdot)