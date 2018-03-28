# -*- coding: utf-8 -*-

from random import randint
from time import time
import os

tailleLigne = 12
file ='base_donnees.txt'

def choixCode():

    t1 = time()

    fichier = open(file,'r')#on ouvre le fichier en mode lecture
    nombreLigne = (os.path.getsize(file)+2)/12#on détermine le nombre de lignes du fichier
    random = randint(0,nombreLigne-1)#on génère aléatoirement un numéro de ligne
    fichier.seek(tailleLigne*random)#on change la position du curseur
    maLigne = fichier.readline().strip()#on enlève les caractères spéciaux en fin de ligne
    fichier.close

    print('temps =',time()-t1)#on affiche le temps d'exécution
    #print(random)
    #print(nombreLigne)
    return maLigne#on renvoie une ligne aléatoire du fichier .txt


##choixCode()
##print(choixCode())
