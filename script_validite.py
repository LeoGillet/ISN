import sqlite3
from lectureCode1 import choixCode

conn = sqlite3.connect('Datab.db')
c = conn.cursor()

def rechercheIdentifiant(idCarte):
    c.execute("SELECT identifiant, nom, prenom FROM ids")
    liste_ids = c.fetchall()
    try:
        validite = True
        i = 0
        while liste_ids[i][0] != idCarte:
            i += 1
        sortie = 'IDENTIFIANT : '+str(idCarte)+' EST TROUVE A LA LIGNE : '+str(i+1)+' ASSOCIE A : '+str(liste_ids[i][1])+' '+str(liste_ids[i][2])
    except IndexError:
        validite = False
        sortie = """!! L'identifiant n'est pas présent dans la base de données !!"""
    print(sortie)
    return sortie

rechercheIdentifiant(choixCode())
