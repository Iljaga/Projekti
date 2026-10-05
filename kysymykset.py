import random


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

        print(
            "Oikein! Sait",
            palkinto,
            "catcoinia."
        )

        return palkinto

    else:
        print("Väärin!")
        print("Oikea vastaus oli:", oikea)

        return 0