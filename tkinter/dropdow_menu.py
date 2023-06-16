from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Tkinter Checkboxes")
root.geometry("400x100")


clicked = StringVar()
clicked.set("Some Day")

def show():
    messagebox.showinfo('Day of the week', f"Today is {clicked.get()}")
    pass
dropdown = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")#clicked es la variable donde se van a poner uno de los siguientes argumentos (dias de la semana en este caso)
#dropdown = OptionMenu(root, clicked, *lista) #Se le puede poner una lista en vez de todos los valores asi en cola, mejor y mas bonito, notese el asterisco antes de la lista
dropdown.pack()

myButton = Button(root, text = "Show selection", command = show).pack()



root.mainloop()