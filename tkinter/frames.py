from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap("icono.ico")
root.title("Tkinter Frames")

frame = LabelFrame(root, text = "MyFrame", padx = 50, pady = 50) #Crea un frame que es una subventana a la que poner elementos
frame.pack(padx = 10, pady = 10)

# Puedes mezclar pack y grid solo si lo haces en frames diferentes
b1 = Button(frame, text = "Dont click me Pls")
b1.grid(row = 0, column = 0)

b2 = Button(frame, text = "Do it!, Click it!")
b2.grid(row = 1, column = 1)

b3 = Button(root, text = "Help!, im out of frame")
b3.pack(pady = 5) # si aqui uso grid el codigo daria error


root.mainloop()