# -*- coding: utf8 -*-

import sqlite3
import time

def genBase():

    ''' Ecrit les codes de la base de donnees dans un fichier .txt '''

    global cursor
    
    #On se connecte à la base
    conn = sqlite3.connect('datab.db')
    cursor = conn.cursor()

    #On ouvre le fichier en mode ecriture
    Fichier = open('baseGen.txt','w')

    #On stock la base de donnees dans une liste
    cursor.execute("""SELECT identifiant, nom, prenom FROM ids""")
    liste = cursor.fetchall()

    #Pour chaque element de la liste
    for i in range(len(liste)):

        #Si on est pas au dernier element
        if 0 <= i < len(liste)-1:

            #On ecrit le code dans le .txt
            ligneBase = liste[i]
            Fichier.write(ligneBase[0]+'\n')

        #On est au dernier element   
        else:
            
            #On ecrit le dernier code sans sauter de ligne
            ligneBase = liste[i]
            Fichier.write(ligneBase[0])

    
