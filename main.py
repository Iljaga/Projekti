import time


from database import yhdista_tietokantaan

from pelaaja import (
    hae_pelaaja,
    luo_pelaaja,
    tallenna_pelaaja,
    poista_pelaaja
)

from kysymykset import kysy_kysymys

from matkustus import (
    hae_lahimmat_maat,
    matkusta,
    nayta_kaydyt_maat
)

from animaatiot import aloitus_animaatio


# =========================
# TIETOKANTA
# =========================

yhteys = yhdista_tietokantaan()
kursori = yhteys.cursor()


# =========================
# ALOITUSANIMAATIO
# =========================

aloitus_animaatio()


# =========================
# TERVETULOA
# =========================

print(
    "\nTervetuloa kissa lentopeliin!\n"
    "Tavoite on päästä Thaimaahan.\n\n"
    "Jos tarvitset rahaa, kirjoita 'tarvin rahaa'.\n"
    "Jos haluat nähdä käydyt maat, kirjoita "
    "'minun käydyt maat'.\n"
    "Kirjoita 'tauko', jos haluat lopettaa.\n"
)

time.sleep(2)


# =========================
# KÄYTTÄJÄNIMI
# =========================

nimi = input(
    "Anna käyttäjänimi: "
).strip()


# Katsotaan löytyykö pelaaja
tulos = hae_pelaaja(
    kursori,
    nimi
)


# =========================
# VANHA PELAAJA
# =========================

if tulos:

    nykyinen, raha = tulos

    print(
        "\nTervetuloa takaisin,",
        nimi
    )

    haluatko_poistaa = input(
        "Haluatko aloittaa alusta? (kyllä/ei): "
    ).strip().lower()

    if haluatko_poistaa == "kyllä":

        poista_pelaaja(
            kursori,
            nimi
        )

        nykyinen, raha = luo_pelaaja(
            kursori,
            nimi
        )

        print(
            "Vanha tallennus poistettu."
        )

        print(
            "Aloitat pelin alusta!"
        )


# =========================
# UUSI PELAAJA
# =========================

else:

    nykyinen, raha = luo_pelaaja(
        kursori,
        nimi
    )

    print(
        "\nUusi pelaaja luotu!"
    )

    print(
        "Aloitat maasta:",
        nykyinen
    )

    print(
        "Sinulla on",
        raha,
        "catcoinia."
    )


# =========================
# KÄYDYT MAAT
# =========================

# Pelaajan nykyinen maa on
# ensimmäinen käyty maa.

kaydyt_maat = [nykyinen]


# =========================
# PÄÄLOOPPI
# =========================

while True:

    vaihtoehdot = hae_lahimmat_maat(
        kursori,
        nykyinen
    )

    print("\n-----------------------------")

    print(
        "Olet nyt:",
        nykyinen
    )

    print(
        "Rahaa jäljellä:",
        raha,
        "catcoin"
    )

    print("-----------------------------")

    print(
        "Voit lentää näihin maihin:"
    )


    # Tulostetaan kolme matkavaihtoehtoa

    for numero, (maa, hinta) in enumerate(
        vaihtoehdot,
        1
    ):

        print(
            numero,
            ".",
            maa,
            "-",
            hinta,
            "catcoin"
        )


    print("\n1-3 = matkusta")

    print(
        "tarvin rahaa = kysy kysymys"
    )

    print(
        "minun käydyt maat = näytä käydyt maat"
    )

    print(
        "tauko = lopeta peli"
    )


    valinta = input(
        "\nValintasi: "
    ).strip()


    # =========================
    # TAUKO
    # =========================

    if valinta.lower() == "tauko":

        tallenna_pelaaja(
            kursori,
            nimi,
            nykyinen,
            raha
        )

        print(
            "\nPeli tallennettu."
        )

        print(
            "Peli päättyy."
        )

        print(
            "Oot nyt maassa:",
            nykyinen
        )

        print(
            "Rahaa jäi:",
            raha,
            "catcoin."
        )

        break


    # =========================
    # KÄYDYT MAAT
    # =========================

    if valinta.lower() == "minun käydyt maat":

        nayta_kaydyt_maat(
            kaydyt_maat
        )

        continue


    # =========================
    # RAHAN HANKKIMINEN
    # =========================

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


    # =========================
    # MATKUSTAMINEN
    # =========================

    nykyinen, raha = matkusta(
        nykyinen,
        raha,
        valinta,
        vaihtoehdot,
        kaydyt_maat
    )


    # Tallennetaan matkan jälkeen

    tallenna_pelaaja(
        kursori,
        nimi,
        nykyinen,
        raha
    )


    # =========================
    # MAALI
    # =========================

    if nykyinen.lower() == "thailand":

        print("""

        🎉🎉🎉 ONNEKSI OLKOON! 🎉🎉🎉

        Kissa pääsi Thaimaahan!

             /\\_/\\
            ( ^.^ )
            /     \\
           (       )
            \\_____/

        Kissa voi nyt nauttia lomasta!

        PELI LÄPI!
        """)

        print(
            "Rahaa jäi:",
            raha,
            "catcoin."
        )

        print(
            "\nKäydyt maat:"
        )

        nayta_kaydyt_maat(
            kaydyt_maat
        )

        # Tallennetaan vielä lopullinen tila

        tallenna_pelaaja(
            kursori,
            nimi,
            nykyinen,
            raha
        )

        break


# =========================
# SULJETAAN TIETOKANTA
# =========================

kursori.close()
yhteys.close()