from tkinter import *
from PIL import ImageTk,Image #para poder usar imagenes en python

root = Tk()
root.title("Naiz")
root.iconbitmap("icono.ico") #Cambia el icono

my_img = ImageTk.PhotoImage(Image.open("dibujo.png")) #Cargo la imagen
my_label = Label(image = my_img) #Asigno la imagen a un label
my_label.pack()












button_quit = Button(root, text="Exit Program", command = root.quit) #root.quit cierra la ventana de TKinter
button_quit.pack()

root.mainloop()


