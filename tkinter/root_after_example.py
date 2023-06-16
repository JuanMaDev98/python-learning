import tkinter as tk
from tkinter import ttk
from random import randint

root = tk.Tk()
root.geometry('200x200')

lista = ["causa 1", "causa 2", "causa 3"]

opcion_seleccionada = tk.StringVar()
opcion_seleccionada.set(lista[0])

option_menu = tk.OptionMenu(root, opcion_seleccionada, *lista)
option_menu.pack()

def update():
    x = lista.index(opcion_seleccionada.get())
    option_menu['menu'].entryconfigure(x, label=str(randint(1,100)))
    root.after(1000, update)
    
update()
root.mainloop()