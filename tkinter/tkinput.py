from tkinter import *

root = Tk() #Inicializo la ventana principal que siempre se le pone el nombre root

def my_click():
    text = myEntry1.get() #Obtiene el texto en el interior de un Entry
    myLabel = Label(root, text = text)
    myLabel.pack()


myButton1 = Button(root, text ="Click Me!", state = "normal", padx = 50, pady = 50, command = my_click, fg = "blue", bg = "red")
myButton1.pack()
myEntry1 = Entry(root, width = 50, bg = "blue", fg = "white", borderwidth = 10) #Crea un textbox
myEntry1.insert(0, "Escribe algo")
myEntry1.pack()

#width - cambia el ancho del objeto
#height - cambia el largo del objeto
#borderwidth - cambia el ancho del borde del objeto

root.mainloop()# loop principal donde se ejecuta la ventana

