import sqlite3
from tkinter import *
from tkinter.ttk import *

conn = sqlite3.connect('Datab.db')
c = conn.cursor()

resultat = '0'
fen_validite = Tk()
fen_validite.title('Test de validité')
fen_validite.geometry('330x145')

greet_validite = Label(fen_validite, text='Entrez l\'identifiant à rechercher!', font='Helvetica 9')

tip_validite = Label(fen_validite, text='exemple : 1003920006', font='Helvetica 7 italic')

entree_validite_defaut = StringVar()
entree_validite_defaut.set('1003920000')
entree_validite = Entry(fen_validite, textvariable=entree_validite_defaut)

lignes_db_validite = Label(fen_validite, font='Helveltica 7 bold')



def rechercheIdentifiant():
    global lignes_db_validite
    global resultat_recherche_validite
    global entree_validite
    global entree_validite_defaut
    global resultat

    c.execute("SELECT identifiant, nom, prenom FROM ids")
    liste_ids = c.fetchall()
    str_lignes_db = 'La base de données comporte '+str(len(liste_ids))+' lignes.'
    try:
    lignes_db_validite.config(text=str_lignes_db)
    validite = True
    i = 0
    while liste_ids[i][0] != entree_validite.get():
        i+=1
    resultat = 'Identifiant : '+entree_validite.get()+' trouvé à la ligne '+str(i+1)+' : '+str(liste_ids[i][1])+' '+str(liste_ids[i][2])
    except IndexError:
         resultat = 'L\'identifiant n\'est pas présent dans la base de données'
         validite = False


bouton_validite = Button(fen_validite, text='Rechercher', command = rechercheIdentifiant())
resultat_recherche_validite = Label(fen_validite, text=resultat, font='Helvetica 8 bold')

greet_validite.pack()
tip_validite.pack()
entree_validite.pack()
lignes_db_validite.pack()
bouton_validite.pack()
resultat_recherche_validite.pack()

fen_validite.mainloop()
