from gi.repository import Gtk, Gdk, GLib, GdkPixbuf
import sqlite3
from script_validite import PassageCarte
from TestPortail import TestPortail, LCD
from tkinter import *
import datetime
date = datetime.datetime.now()


def __init__(self):
    conn = sqlite3.connect('Datab.db')
    c = conn.cursor()

if __name__ == "__main__":
    PassageCarte()
    Gtk.main()
    LCD(TestPortail(lOut))
