import mysql.connector


def yhdista_tietokantaan():
    yhteys = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="root",
        password="Ilju4kaMetropol",
        autocommit=True
    )

    return yhteys