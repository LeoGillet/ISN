# -*- coding: utf-8 -*-

from random import randint
from time import time
import os

def choixCode():

    tailleLigne = 12
    file ='baseGen.txt'

    #ouvre le fichier en mode lecture
    fichier = open(file,'r')
    
    #determine le nombre de lignes du fichier
    nombreLigne = (os.path.getsize(file)+2)/tailleLigne

    #genere aleatoirement un numero de ligne
    random = randint(0,nombreLigne-1)

    #change la position du curseur
    fichier.seek(tailleLigne*random)

    #enleve les caracteres speciaux en fin de ligne
    maLigne = fichier.readline().strip()
    fichier.close

    #renvoie une ligne aleatoire du fichier .txt
    lOut = maLigne
    return lOut


