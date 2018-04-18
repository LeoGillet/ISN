#-----------------------------------MODULES------------------------------------#
from tkinter import *
import datetime
import sqlite3
date = datetime.datetime.now()
#-----------------------------------FONCTIONS----------------------------------#
def TestPortail(code):
    #TEST DE STATUE 
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
        if(listeinterne[x][0]==code):
            Qualite=1
        if(listedemip[x][0]==code or listeexterne[x][0]==code ):
            Qualite=0
    
    #TEST DE L'HORAIRE
    date = datetime.datetime.now()
    Heure= int(date.strftime("%H"))+int(date.strftime("%M"))/60
    if  date.strftime("%A")==str('Saturday') or date.strftime("%A")==str('Sunday'):
        Portail=0
        
    elif Qualite == 0  and 7.5<Heure<18.5:
        Portail=1

    elif Qualite == 1  and 7.5<Heure<22:
        Portail=1    
        
    elif Qualite == 2:
        Portail=1

    else:
        Portail=0
    return(Portail)#renvoi l'état du portail 1=ouvert , 0=fermer


#AFFICHAGE
def LCD(Portail):
    #RECHERCHE DU NOM ET PRENOM DE L'INDIVIDU
    conn = sqlite3.connect('Datab.db')
    c = conn.cursor()
    c.execute("SELECT identifiant, nom, prenom FROM ids")
    listeindividus = c.fetchall()

    longueurdb = len(listeindividus)
    for x in range (0,longueurdb-1):
        if(listeindividus[x][0]==code):
            profilUser = listeindividus[x][1]+' '+listeindividus[x][2]
    #Création de la fenétre
    fen=Tk()
    fen.title('afficheur LCD')
    fen.geometry('500x75')
    fen.configure(bg='black')

    #Module pour afficher l'heure
    Temps =str(date.strftime("%H"))+":"+str(date.strftime("%M"))


    #Partie test de l'affichage
    if Portail==0:
        NameUser=Label(fen, text=profilUser, fg='green', bg='black')
        NameUser.pack()
        EtatPortail=Label(fen, text='Le portail est fermé', fg='green', bg='black')
        EtatPortail.pack()
        HeureCourante=Label(fen, text=Temps, fg='green', bg='black')
        HeureCourante.pack()
    elif Portail==1:
        NameUser=Label(fen, text=profilUser, fg='green', bg='black')
        NameUser.pack()
        EtatPortail=Label(fen, text='Le portail est ouvert', fg='green', bg='black')
        EtatPortail.pack()
        HeureCourante=Label(fen, text=Temps, fg='green', bg='black')
        HeureCourante.pack()
    elif Portail ==-1:
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
code=str(1003920020)
LCD(TestPortail(code))
