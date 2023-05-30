from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Tkinter Frames")

def open():
    global my_image
    #La siguente línea abre un popup preguntando por la selección de un documento y devuelve el path al mismo
    root.filename = filedialog.askopenfilename(initialdir = "tkinter\Photos", title = "Select a file", filetypes = (("png","*.png"),("all files", "*.*"),("jpg","*.jpg"))) 
    #initialdir cambia el directorio inicial en el que se abre el dialogo
    #title cambia el titulo duh!
    #filetypes pone los diferentes tipos de archivos que seremos capaces de abrir, en una lista de listas, donde el primer elemento es el texto que nos muestra el programa y el segundo es la extension que van a tener los archivos que nos va a mostrar
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image = my_image).pack()

my_button = Button(root, text = "Open Photo", command = open).pack()




root.mainloop()