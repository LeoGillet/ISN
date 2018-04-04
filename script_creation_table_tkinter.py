import sqlite3
from tkinter import *

fen = Tk()
fen.geometry('500x300')
upper_frame = Frame(fen, cursor='pirate')
upper_frame.grid(row=0,column=0)
welcome = Label(upper_frame, text='Entrez le nom de la table')
welcome.grid(row=0,column=0)

conn = sqlite3.connect('Datab.db')
c = conn.cursor()

commande = """CREATE TABLE IF NOT EXISTS 'test' (
                                    entier integer PRIMARY KEY,
                                    texte text NOT NULL
                                );"""

c.execute(commande)
##fen.mainloop()
