import sqlite3
from aggregator import *
import sys

sys.path.append("../")


def create_database():
    connection = sqlite3.connect("./static/odds.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS odds (
        team1 REAL,
        draw REAL,
        team2 REAL,
        result INTEGER
        )
    """
    )
    connection.commit()
    connection.close()


def fill_database():
    driver = create_webdriver()
    url = "https://www.oddsportal.com/football/france/ligue-1-2022-2023/results/"
    odds = get_all_content(driver=driver, base_url=url, n_pages=8)
    connection = sqlite3.connect("./static/odds.db")
    cursor = connection.cursor()
    for elt in odds:
        cursor.execute(
            """
            INSERT INTO odds (team1,draw,team2,result)
            VALUES 
            (?,?,?,?)
        """,
            (elt[0][0], elt[0][1], elt[0][2], elt[1]),
        )
    connection.commit()
    connection.close()


def delete_database():
    connection = sqlite3.connect("./static/odds.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        DELETE FROM IF EXISTS odds
    """
    )
    cursor.execute(
        """
        DROP TABLE IF EXISTS odds
    """
    )
    connection.commit()
    connection.close()


if __name__ == "__main__":
    delete_database()
    create_database()
    fill_database()
