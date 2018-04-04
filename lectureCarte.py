# -*- coding: utf-8 -*-

from tkinter import*
from tkinter.ttk import*
from lectureCode1 import choixCode
from script_validite import rechercheIdentifiant

def simulationPassage():
    global code
    code = choixCode()
    v.set(code) #on affiche le code dans le fenêtre
    print(v.get())
    rechercheIdentifiant(print(v.get()))
    return code

def outCode():
    global sortie
    global v

    root = Tk()#on ouvre une fenêtre
    root.title('Passage de carte')#on lui met un titre
    root.geometry('240x75')#on modifie sa taille

    consigne = Label(root, text = 'Cliquer pour simuler')
    consigne.grid(row=0, column=1, padx=10,pady=5)

    simuler = Button(root, text = 'Simuler',command = simulationPassage)#quand on clique on fait appelle à la procédure simulationPassage()
    simuler.grid(row=1, column=1, padx=10,pady=5)

    v = StringVar()
    sortie = Label(root, textvariable = v)#on affiche le code
    sortie.grid(row=1, column=3, padx=10,pady=5)




outCode()
simulationPassage()
