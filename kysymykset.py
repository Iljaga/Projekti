import random


helppo_kysymykset = [
    ("Mikä on Suomen pääkaupunki?", "helsinki"),
    ("Montako jalkaa kissalla on?", "4"),
    ("Mikä on maailman isoin maa?", "venäjä"),
    ("Viikonpäivä jossa on eniten 'a'", "maanantai"),
]

vaikea_kysymykset = [
    ("Mikä on Japanin pääkaupunki?", "tokyo"),
    ("Missä maassa on Eiffel-torni?", "ranska"),
]


def kysy_kysymys():
    taso = input(
        "Haluatko helpon vai vaikean kysymyksen? (helppo/vaikea): "
    ).strip().lower()

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

    vastaus = input("Vastauksesi: ").strip()

    if vastaus.lower() == oikea.lower():

        palkinto = random.randint(200, 400)

        print("Oikein! Sait", palkinto, "catcoinia.")

        return palkinto

    else:

        print("Väärin! Oikea vastaus oli:", oikea)

        return 0