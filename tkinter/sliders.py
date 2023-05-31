from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tkinter Radio Buttons")
root.geometry("400x400")#cambia el tamaño de la pantalla

def slide(var): #necesitas pasar un argumento para que funcione, ni el profesor sabe por que XD (solo con los Scale(slides))
    my_label = Label(root, text = horizontal.get()).pack()
    root.geometry(f"{horizontal.get()}x400")#smart

vertical = Scale(root, from_ =0, to = 400, command= slide)#Crea un slider vertical que empieza en 0 y termina en 200
vertical.pack()#No se puede usar seguido de la linea anterior

horizontal = Scale(root, from_ = 0, to = 400, orient = HORIZONTAL, command= slide)#orient cambia la orientación del widget
horizontal.pack()

my_label = Label(root, text = horizontal.get()).pack()

#Comentado porque uso un metodo mejor, este era presionar un boton para que la pantalla cambiara de tamaño, muy clunky XD
'''
my_btn = Button(root, text = "Click me!", command = slide).pack()
'''




root.mainloop()