from tkinter import *
#from tkinter.ttk import *
import sqlite3

conn = sqlite3.connect("Datab.db")
c = conn.cursor()


fen = Tk()
fen.title('Utilitaire Admin')


def codeSQL(table):                                                             #RAJOUTER LES EXCEPTIONS DE SQLITE3 POUR UN MAXIMUM DE SWAG
    commande = "CREATE TABLE IF NOT EXISTS "+'"'+table+'"'+'"'"""" (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL
                                );"""
    return commande

frame_creation = LabelFrame(fen, text='Création de tables')
frame_creation.grid(row=0, column=0)

top_message_creation = Label(frame_creation, text='Entrez le nom de la table à créer!')
top_message_creation.grid(row=0,column=0)

entree_creation = Entry(frame_creation, width=30)
entree_creation.grid(row=1,column=0,padx=30,pady=10)

bottom_message_creation = Label(frame_creation, text='blank',fg='grey',font='Helvetica 7 italic')
bottom_message_creation.grid(row=3,column=0,padx=0,pady=5)

def ajouterTable(table):
    global bottom_message_creation
    c.execute(codeSQL(table))
    c.commit()
    str_creation = 'La table '+entree_creation.get()+' a été créée'
    bottom_message_creation.config(text=str_creation)

bouton_valider_creation = Button(frame_creation, text='Créer', command=ajouterTable(entree_creation.get()))
bouton_valider_creation.grid(row=2,column=0,padx=30,pady=10)

fen.mainloop()






##nom_table = input('Entrez un nom de table à créer : ')
##
##c.execute(ajouterTable(nom_table))
##conn.commit()
