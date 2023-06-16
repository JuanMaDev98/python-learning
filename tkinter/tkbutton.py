from tkinter import *

root = Tk() #Inicializo la ventana principal que siempre se le pone el nombre root

def my_click():
    myLabel = Label(root, text ="Clickity!")
    myLabel.pack()


myButton1 = Button(root, text ="Click Me!", state = "normal", padx = 50, pady = 50, command = my_click, fg = "blue", bg = "red")
myButton1.pack()

#state cambia el estado del boton:
#1- Disable desactiva la opcion de tocar el boton
#2- active lo activa como si le hicieras clic
#3- normal es el estado por defecto del boton

# padx - aumenta el espacio del padding en el eje X
# pady - que tu crees...

#command ejecuta la funcion a la que esta igualado cuando le haces click al boton

#fg - cambia el color del texto del boton (Foreground)
#bg - cambia el color de fondo del boton (Background
#todos los colores en TKinter aceptan ademas de la representacion en string, la hexadecimal

root.mainloop()# loop principal donde se ejecuta la ventana

