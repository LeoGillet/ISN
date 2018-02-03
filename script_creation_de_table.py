from tkinter import *
import sqlite3

conn = sqlite3.connect("Datab.db")
c = conn.cursor()


fen = Tk()
fen.title('Utilitaire Admin')


def codeSQL(table):                                                             #RAJOUTER LES EXCEPTIONS DE SQLITE3 POUR UN MAXIMUM DE SWAG
    commande = """CREATE TABLE IF NOT EXISTS """+table+""" (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL
                                );"""
    return commande

def ajouterTable(table):
    codeSQL(table)
    str_creation = 'La table'+entree_creation.get()+'a été créée'
    bottom_message_creation = Label(frame_creation, text='blank', fg='grey', font='Helvetica 9 italic')
    bottom_message_creation.pack()
    bottom_message_creation.config(text=str_creation)



#           FRAME CREATION DE TABLES
frame_creation = LabelFrame(fen, text='Création de tables', padx=20, pady=20, font='Helvetica 9 italic')
frame_creation.pack(fill='both', expand='yes')
#
top_message_creation = Label(frame_creation, text='Entrez le nom de la table à créer!', font='Helvetica 9')
top_message_creation.pack()
#
entree_creation = Entry(frame_creation, width=30, fg='grey', font='Helvetica 9')
entree_creation.pack()
#
bouton_valider_creation = Button(frame_creation, text='Créer', font='Helvetica 9', command=ajouterTable(entree_creation.get()))
bouton_valider_creation.pack()
#




fen.mainloop()






##nom_table = input('Entrez un nom de table à créer : ')
##
##c.execute(ajouterTable(nom_table))
##conn.commit()
