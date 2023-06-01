from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tkinter Checkboxes")
root.geometry("400x400")


var = IntVar()

def set_label():
    myLabel.config(text = var.get()) #Config cambia los valores sin hacer todas la cochinadas que hace el prosor en el video

checkbox = Checkbutton(root, text = "Check me pls", variable = var, command = set_label, onvalue = 1, offvalue = 0)# onvalue cambia el valor que retorna el checbox cuando esta marcado y offvalue cuando esta desmarcado
checkbox.select()#Marca la casilla del checkbox, deselect() hace lo contrario
checkbox.pack()

myLabel = Label(root, text = var.get())
myLabel.pack()






root.mainloop()