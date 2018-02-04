import sqlite3
from tkinter import *
from tkinter.ttk import *

conn = sqlite3.connect('Datab.db')
c = conn.cursor()

fen_validite = Tk()
fen_validite.title('Test de validité')
fen_validite.geometry('330x145')

greet_validite = Label(fen_validite, text='Entrez l\'identifiant à rechercher!', font='Helvetica 9')

tip_validite = Label(fen_validite, text='exemple : 1003920006', font='Helvetica 7 italic')

entree_validite = Entry(fen_validite, text='test')

lignes_db_validite = Label(fen_validite, font='Helveltica 7 bold')

resultat_recherche_validite = Label(fen_validite, font='Helvetica 8 bold')

def rechercheIdentifiant():
    global lignes_db_validite
    global resultat_recherche_validite
    global entree_validite

    c.execute("SELECT identifiant, nom, prenom FROM ids")
    liste_ids = c.fetchall()
    str_lignes_db = 'La base de données comporte '+str(len(liste_ids))+' lignes.'
    try:
        lignes_db_validite.config(text=str_lignes_db)
        validite = True
        i = 0
        while liste_ids[i][0] != entree_validite.get():
            i+=1
        str_resultat_recherche = 'Identifiant : '+entree_validite.get()+' trouvé à la ligne '+str(i+1)+' : '+str(liste_ids[i][1])+' '+str(liste_ids[i][2])
        resultat_recherche_validite.config(text=str_resultat_recherche)
    except IndexError:
        resultat_recherche_validite.config(text='L\'identifiant n\'est pas présent dans la base de données')
        validite = False
test = entree_validite.get()
bouton_validite = Button(fen_validite, text='Exécuter la recherche', command = rechercheIdentifiant())

testentree = Label(fen_validite, text=test)

greet_validite.pack()
tip_validite.pack()
entree_validite.pack()
lignes_db_validite.pack()
bouton_validite.pack()
testentree.pack()
resultat_recherche_validite.pack()

fen_validite.mainloop()
