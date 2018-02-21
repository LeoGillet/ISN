import sqlite3

conn = sqlite3.connect('Datab.db')
c = conn.cursor()

commande = """CREATE TABLE IF NOT EXISTS 'test' (
                                    entier integer PRIMARY KEY,
                                    texte text NOT NULL
                                );"""

c.execute(commande)
