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

helppo_kysymykset = [
    ("Mikä on Suomen pääkaupunki?", "helsinki"),
    ("Montako jalkaa kissalla on?", "4"),
    ("Mikä on maailman isoin maa?", "venäjä"),
    ("Viikon päivä jossa on eniten 'a'?", "maanantai"),
]
vaikea_kysymykset = [
    ("Missä maassa on Eiffel-torni?", "ranska"),
    ("Mikä on maailman pienin valtio pinta-alaltaan?", "vatikaani"),
    ("Mikä alkuaine on kemialliselta merkiltään W?", "volframi"),
    ("Kuka kirjoitti romaanin 1984?", "george orwell"),
    ("Mikä planeetta pyörii akselinsa ympäri nopeimmin?", "jupiter"),
    ("Kuinka monta luuta aikuisen ihmisen kehossa yleensä on?", "206"),
    ("Mikä on maailman syvin tunnettu valtameren kohta?", "challenger deep"),
    ("Minkä maan pääkaupunki on Ulaanbaatar?", "mongolia"),
    ("Mikä elin tuottaa insuliinia?", "haima"),
    ("Mikä on kemiallinen merkki kullalle?", "au"),
]


def kysy_kysymys():
    taso = input(
        "Haluatko helpon vai vaikean kysymyksen? (helppo/vaikea): "
    ).lower()
    if taso == "helppo":
        kysymys, oikea = random.choice(helppo_kysymykset)
    elif taso == "vaikea":
        kysymys, oikea = random.choice(vaikea_kysymykset)
    else:
        print("Kirjoita helppo tai vaikea.")
        return 0
    print("\nKysymys:", kysymys)
    vastaus = input("Vastauksesi: ")
    if vastaus.lower() == oikea.lower():
        if taso == "helppo":
            palkinto = random.randint(200, 400)
        else:
            palkinto = random.randint(400, 700)
        print("Oikein! Sait", palkinto, "catcoinia.")
        return palkinto
    else:
        print("Väärin!")
        print("Oikea vastaus oli:", oikea)
        return 0


def hae_lahimmat_maat(nykyinen):
    sql = """
          SELECT latitude_deg, longitude_deg
          FROM airport
          WHERE iso_country IN (SELECT iso_country \
                                FROM country \
                                WHERE LOWER(name) = LOWER(%s)) LIMIT 1 \
          """
    kursori.execute(sql, (nykyinen,))
    koordinaatit = kursori.fetchone()
    if koordinaatit is None:
        print("Nykyistä maata ei löytynyt.")
        return []
    sql = """
          SELECT country.name, airport.latitude_deg, airport.longitude_deg
          FROM airport
                   JOIN country
                        ON airport.iso_country = country.iso_country
          WHERE LOWER(country.name) != LOWER(%s) \
          """
    kursori.execute(sql, (nykyinen,))
    tulokset = kursori.fetchall()
    etaisyydet = []
    for nimi, lat, lon in tulokset:
        etaisyys = geodesic(
            koordinaatit,
            (lat, lon)
        ).kilometers
        etaisyydet.append((etaisyys, nimi))
    etaisyydet.sort()
    vaihtoehdot = []
    kaytetyt_maat = set()
    for etaisyys, nimi in etaisyydet:
        if nimi in kaytetyt_maat:
            continue
        kaytetyt_maat.add(nimi)
        hinta = int(etaisyys / 100) + 100
        vaihtoehdot.append((nimi, hinta))
        if len(vaihtoehdot) == 3:
            break
    return vaihtoehdot

def matkusta(nykyinen, raha, valinta, vaihtoehdot, kaydyt_maat):
    # Muutetaan käyttäjän numero kokonaisluvuksi
    try:
        numero = int(valinta)
    except ValueError:
        print("Kirjoita matkakohteen numero, esimerkiksi 1, 2 tai 3.")
        return nykyinen, raha

    if numero < 1 or numero > len(vaihtoehdot):
        print("Tuolla numerolla ei ole matkakohdetta.")
        return nykyinen, raha

    maa, hinta = vaihtoehdot[numero - 1]
    if raha < hinta:
        print("Ei oo tarpeeksi catcoinia tähän matkaan.")
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
    print("Saavuit maahan:", nykyinen)
    print("Matka maksoi", hinta, "catcoin.")
    print("Rahaa jäljellä:", raha, "catcoin.")

    return nykyinen, raha

# NÄYTÄ KÄYDYT MAAT

def nayta_kaydyt_maat(kaydyt_maat):
    print("\n=============================")
    print("        KÄYDYT MAAT")
    print("=============================")
    for numero, maa in enumerate(kaydyt_maat, 1):
        print(numero, ".", maa)
    print("=============================")


#peli looppi

print("""
       z
       z
   /\\_/\\
  ( -.- )
  /       \\
 (         )
  \\___/
""")

print("kissa on nukkumassa...")

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

print("Kissa haluaa matkustaa Thaimaahan!\n")

time.sleep(1)

print(
    "Tervetuloa kissa lentopeliin!\n"
    "Sulla on 0 catcoinia.\n"
    "Tavoite on päästä Thaimaahan.\n\n"
    "Jos tarvitset rahaa, kirjoita 'tarvin rahaa'.\n"
    "Jos haluat nähdä käydyt maat, kirjoita 'minun käydyt maat'.\n"
    "Kirjoita 'tauko', jos haluat lopettaa.\n"
)

time.sleep(3)

#pelin muuttuja

raha = 10000
nykyinen = "laos"
kaydyt_maat = []
kaydyt_maat.append(nykyinen)

# Päälooppi
while True:
    vaihtoehdot = hae_lahimmat_maat(nykyinen)
    print("\n-----------------------------")
    print("Olet nyt:", nykyinen)
    print("Rahaa jäljellä:", raha, "catcoin")
    print("-----------------------------")
    print("Voit lentää näihin maihin:")
    for numero, (maa, hinta) in enumerate(vaihtoehdot, 1):
        print(
            numero,
            ".",
            maa,
            "-",
            hinta,
            "catcoin"
        )
    print("\n1-3 = matkusta")
    print("tarvin rahaa = kysy kysymys")
    print("minun käydyt maat = näytä käydyt maat")
    print("tauko = lopeta peli")

    valinta = input("\nValintasi: ")
    if valinta == "tauko":
        print("\nPeli päättyy.")
        print("Oot nyt maassa:", nykyinen)
        print("Rahaa jäi:", raha, "catcoin.")

        break
    # Käydyt maat
    if valinta == "minun käydyt maat":
        nayta_kaydyt_maat(kaydyt_maat)

        continue

    # catcoin hankiminen
    if valinta == "tarvin rahaa":
        palkinto = kysy_kysymys()
        raha += palkinto
        print(
            "Nyt sulla on",
            raha,
            "catcoinia."
        )
        continue

    #matkustaa
    nykyinen, raha = matkusta(
        nykyinen,
        raha,
        valinta,
        vaihtoehdot,
        kaydyt_maat
    )
    #maali
    if nykyinen.lower() == "thailand":
        print("""

        🎉🎉🎉 ONNEKSI OLKOON! 🎉🎉🎉

        Kissa pääsi Thaimaahan! kissa voitti 2000 catcoin

             /\\_/\\
            ( ^.^ )
            /     \\
           (       )
            \\_____/

        Kissa voi nyt nauttia lomasta!

        PELI LÄPI!
        """)

        print("Rahaa jäi:", raha, "catcoin.")

        print("\nKäydyt maat:")
        nayta_kaydyt_maat(kaydyt_maat)

        break

# =========================
# SULJETAAN TIETOKANTA
# =========================

kursori.close()
yhteys.close()