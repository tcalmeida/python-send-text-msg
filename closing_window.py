import sys
import GUI
from tkinter import messagebox


def closing_window():
    if messagebox.askokcancel('Quit', 'Do you want do quit?'):
        GUI.window.destroy()

    sys.exit()
