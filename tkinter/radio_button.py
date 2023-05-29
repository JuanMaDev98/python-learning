from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap("icono.ico")
root.title("Tkinter Radio Buttons")

r = IntVar()# Crea una variable de Tkinter de tipo Int para los radios (StrVar crea la variable de tipo string)
r.set(1) #Iguala la variable de Tkinter en 2

def clicked(value):
    global myLabel
    myLabel.pack_forget()
    myLabel = Label(root, text = value) #r.get Obtiene el valor de la variable r de Tkinter
    myLabel.pack()

Radiobutton(root, text = "Option 1", variable = r, value = 1, command = lambda: clicked(r.get())).pack()
Radiobutton(root, text = "Option 2", variable = r, value = 2, command = lambda: clicked(r.get())).pack()

myLabel = Label(root, text = r.get()) #r.get Obtiene el valor de la variable r de Tkinter
myLabel.pack()


root.mainloop()