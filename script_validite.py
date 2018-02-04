# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:31:52 2018

@author: leo.gillet
"""

import sqlite3

conn = sqlite3.connect('Datab.db')
c = conn.cursor()

identifiant = input('Entrez l\'identifiant : ')

c.execute("SELECT identifiant, nom, prenom FROM ids")
liste_ids = c.fetchall()
print('La base de données comporte',len(liste_ids),'lignes.')

try:
    validite = True
    i = 0
    while liste_ids[i][0] != identifiant:
        i+=1
except IndexError:
    print("""!! L'identifiant n'est pas présent dans la base de données !!""")
    validite = False

print('')
print('Identifiant :',identifiant)
print('Trouvé à la ligne',i+1,':',liste_ids[i][1],liste_ids[i][2])
