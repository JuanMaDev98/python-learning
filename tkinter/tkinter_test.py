from tkinter import *

root = Tk() #Inicializo la ventana principal que siempre se le pone el nombre root

myLabel1 = Label(root, text ="Hello World!") # creo un nuevo label en la ventana root
myLabel2 = Label(root, text ="My name is JuanMaDev")
myLabel3 = Label(root, text ="      /     ")

#myLabel1.pack() #inserta el label en cualquier slot disponible en la ventana
myLabel1.grid(row = 0, column = 0) # para insertar el label en formato de filas (row) y columnas (column)
myLabel2.grid(row = 1, column = 5)
myLabel3.grid(row = 3, column = 1)


root.mainloop()# loop principal donde se ejecuta la ventana

