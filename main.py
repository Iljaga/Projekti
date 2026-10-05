import time

from database import yhdista_tietokantaan
from pelaaja import hae_pelaaja, luo_pelaaja, tallenna_pelaaja, poista_pelaaja
from kysymykset import kysy_kysymys
from matkustus import hae_lahimmat_maat, matkusta
from animaatiot import aloitus_animaatio


# Yhdistetään tietokantaan
yhteys = yhdista_tietokantaan()
kursori = yhteys.cursor()


# Aloitusanimaatio
aloitus_animaatio()

print(
    "Tervetuloa kissa lentopeliin!\n"
    "Tavoite on päästä Thaimaahan.\n"
    "Jos tarvitset rahaa, kirjoita 'tarvin rahaa'."
)

print(
    "Kirjoita 'tauko' kun haluut lopettaa.\n"
)

time.sleep(2)


# Käyttäjänimi
nimi = input("Anna käyttäjänimi: ").strip()

tulos = hae_pelaaja(kursori, nimi)


# Jos käyttäjä löytyy
if tulos:
    nykyinen, raha = tulos

    print("\nTervetuloa takaisin,", nimi)

    haluatko_poistaa = input(
        "Haluatko aloittaa alusta? (kyllä/ei): "
    ).strip().lower()

    if haluatko_poistaa == "kyllä":

        poista_pelaaja(kursori, nimi)

        nykyinen, raha = luo_pelaaja(
            kursori,
            nimi
        )

        print("Vanha tallennus poistettu.")
        print("Aloitat pelin alusta!")


# Jos käyttäjää ei löydy
else:

    nykyinen, raha = luo_pelaaja(
        kursori,
        nimi
    )

    print("\nUusi pelaaja luotu!")


# Peli alkaa
while True:

    vaihtoehdot = hae_lahimmat_maat(
        kursori,
        nykyinen
    )

    print("\nOlet nyt:", nykyinen)

    print(
        "Rahaa jäljellä:",
        raha,
        "catcoin"
    )

    print("Voit lentää näihin maihin:")

    for maa, hinta in vaihtoehdot:

        print(
            f"- {maa} - {hinta} catcoin"
        )


    valinta = input(
        "\nMihin haluat mennä "
        "(tai tarvin rahaa / tauko): "
    ).strip()


    # Pelaaja haluaa lopettaa
    if valinta.lower() == "tauko":

        tallenna_pelaaja(
            kursori,
            nimi,
            nykyinen,
            raha
        )

        print("\nPeli tallennettu ja päättyy.")

        print(
            "Oot nyt maassa:",
            nykyinen
        )

        print(
            "Rahaa jäi:",
            raha,
            "catcoin"
        )

        break


    # Pelaaja tarvitsee rahaa
    if valinta.lower() == "tarvin rahaa":

        palkinto = kysy_kysymys()

        raha += palkinto

        tallenna_pelaaja(
            kursori,
            nimi,
            nykyinen,
            raha
        )

        print(
            "Nyt sulla on",
            raha,
            "catcoinia."
        )

        continue


    # Matkustaminen
    nykyinen, raha = matkusta(
        nykyinen,
        raha,
        valinta,
        vaihtoehdot
    )

    # Tallennetaan matkan jälkeen
    tallenna_pelaaja(
        kursori,
        nimi,
        nykyinen,
        raha
    )


    # Tarkistetaan voitto
    if nykyinen.lower() == "thailand":

        print("\n🐱 Kissa pääsi Thaimaahan!")
        print("Voitit pelin!")

        break


# Suljetaan tietokanta
kursori.close()
yhteys.close()