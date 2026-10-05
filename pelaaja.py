def hae_pelaaja(kursori, nimi):
    sql = """
    SELECT nykyinen_maa, raha
    FROM pelaaja
    WHERE nimi = %s
    """

    kursori.execute(sql, (nimi,))
    return kursori.fetchone()


def poista_pelaaja(kursori, nimi):
    sql = """
    DELETE FROM pelaaja
    WHERE nimi = %s
    """

    kursori.execute(sql, (nimi,))


def luo_pelaaja(kursori, nimi):
    nykyinen = "Egypt"
    raha = 0

    sql = """
    INSERT INTO pelaaja (nimi, nykyinen_maa, raha)
    VALUES (%s, %s, %s)
    """

    kursori.execute(sql, (nimi, nykyinen, raha))

    return nykyinen, raha


def tallenna_pelaaja(kursori, nimi, nykyinen, raha):
    sql = """
    UPDATE pelaaja
    SET nykyinen_maa = %s,
        raha = %s
    WHERE nimi = %s
    """

    kursori.execute(sql, (nykyinen, raha, nimi))

    return nykyinen, raha


def tallenna_pelaaja(kursori, nimi, nykyinen, raha):
    sql = """
    UPDATE pelaaja
    SET nykyinen_maa = %s,
        raha = %s
    WHERE nimi = %s
    """

    kursori.execute(sql, (nykyinen, raha, nimi))