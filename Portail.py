#-----------------------------------MODULES------------------------------------#
from tkinter import *
import datetime
import sqlite3
date = datetime.datetime.now()

#-----------------------------------FONCTIONS----------------------------------#
def TestPortail(lOut):
    #TEST DE STATUT
    Qualite=2
    conn = sqlite3.connect('Datab.db')
    c = conn.cursor()

    c.execute("SELECT interne FROM regimes")
    listeinterne = c.fetchall()

    c.execute("SELECT demip FROM regimes")
    listedemip = c.fetchall()

    c.execute("SELECT externe FROM regimes")
    listeexterne = c.fetchall()

    longueurdb = len(listedemip)
    for x in range (0,longueurdb-1):    #verifie le statue ( convertion de la base de donnné en liste)
        if(listeinterne[x][0]==lOut):
            Qualite=1
        if(listedemip[x][0]==lOut or listeexterne[x][0]==lOut ):
            Qualite=0
    
    #TEST DE L'HORAIRE
    date = datetime.datetime.now()
    Heure= int(date.strftime("%H"))+int(date.strftime("%M"))/60
    if  date.strftime("%A")==str('Saturday') or date.strftime("%A")==str('Sunday'):
        validite = 0
        
    elif Qualite == 0  and 7.5<Heure<18.5:
        validite = 1
    elif Qualite == 1  and 7.5<Heure<22:
        validite = 1    
    elif Qualite == 2:
        validite = 1
    else:
        validite = 0
    return validite #renvoit l'état du portail 1=ouvert , 0=fermé


#AFFICHAGE
def LCD(validite,lOut):
    #RECHERCHE DU NOM ET PRENOM DE L'INDIVIDU
    conn = sqlite3.connect('Datab.db')
    c = conn.cursor()
    c.execute("SELECT identifiant, nom, prenom FROM ids")
    listeindividus = c.fetchall()

    longueurdb = len(listeindividus)
    for x in range (0,longueurdb-1):
        if listeindividus[x][0]==lOut:
            profilUser = listeindividus[x][1]+' '+listeindividus[x][2]
    #Création de la fenétre
    fen=Tk()
    fen.title('afficheur LCD')
    fen.geometry('500x75')
    fen.configure(bg='black')

    #Module pour afficher l'heure
    Temps =str(date.strftime("%H"))+":"+str(date.strftime("%M"))


    #Partie test de l'affichage
    if validite == 0:
        NameUser=Label(fen, text=profilUser, fg='green', bg='black')
        NameUser.pack()
        EtatPortail=Label(fen, text='Le portail est fermé', fg='green', bg='black')
        EtatPortail.pack()
        HeureCourante=Label(fen, text=Temps, fg='green', bg='black')
        HeureCourante.pack()
    elif validite == 1:
        NameUser=Label(fen, text=profilUser, fg='green', bg='black')
        NameUser.pack()
        EtatPortail=Label(fen, text='Le portail est ouvert', fg='green', bg='black')
        EtatPortail.pack()
        HeureCourante=Label(fen, text=Temps, fg='green', bg='black')
        HeureCourante.pack()
    elif validite == -1:
        EtatPortail=Label(fen, text='Problème de carte', fg='green', bg='black')
        EtatPortail.pack()
        HeureCourante=Label(fen, text=Temps, fg='green', bg='black')
        HeureCourante.pack()
    else:
        EtatPortail=Label(fen, text='Passer votre carte', fg='green', bg='black')
        EtatPortail.pack()
        HeureCourante=Label(fen, text=Temps, fg='green', bg='black')
        HeureCourante.pack()
       
    fen.mainloop()

#-----------------------------------PARIE OPERATIVE------------------------------#
#lOut=str(1003920020)
#LCD(TestPortail(lOut),lOut)
