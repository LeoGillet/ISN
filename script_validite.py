from gi.repository import Gtk, Gdk, GLib, GdkPixbuf
import sqlite3
from lectureCode1 import choixCode

class PassageCarte:                                             #Définition de la classe PassageCarte
    global rechercheIdentifiant
    def __init__(self):
        global c
        conn = sqlite3.connect('Datab.db')
        c = conn.cursor()
        interface = Gtk.Builder()
        interface.add_from_file('script_validite.glade')
        self.Sortie = interface.get_object("Sortie")
        self.Entree = interface.get_object("Entree")
        interface.connect_signals(self)

    def rechercheIdentifiant(idCarte):
        global c
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

    def on_mainWindow_destroy(self, widget):
        Gtk.main_quit()

    def on_BoutonRandom_clicked(self, widget):
        global lOut
        lOut = choixCode()
        self.Sortie.set_text(rechercheIdentifiant(choixCode()))
        
    def on_BoutonEntree_clicked(self, widget):
        global lOut
        lOut = self.Entree.get_text()
        self.Sortie.set_text(rechercheIdentifiant(self.Entree.get_text()))
        
##if __name__ == "__main__":
##    PassageCarte()
##    Gtk.main()
