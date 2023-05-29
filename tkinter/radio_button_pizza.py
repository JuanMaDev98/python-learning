from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap("icono.ico")
root.title("Tkinter Pizza Radio Buttons")

pizzas = [
    ("Pepperoni","1"),
    ("Cheese","2"),
    ("Mushroom","3"),
    ("Onion","4"),
]

pizza_var = IntVar()
pizza_var.set(2)

def clicked(value):
    global myLabel
    myLabel.pack_forget()
    myLabel = Label(root, text = value)
    myLabel.pack()
    pizza_var.set(value)

frame = LabelFrame(root, text = "Pizza Types", pady = 10, padx = 10)
frame.pack(pady = 10, padx = 10)


fila = 0
for text, var in pizzas: #Utilizo un ciclo para crear mulytiples radiobuttons basados en una lista
    Radiobutton(frame, text = text, variable = pizza_var, value = var, command = lambda: clicked(pizza_var.get())).grid(row = fila, column = 0, sticky = W)
    fila += 1

myLabel = Label(root, text = pizza_var.get())
myLabel.pack()







root.mainloop()