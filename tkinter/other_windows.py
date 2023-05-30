from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tkinter Frames")

def open():
    global my_img
    top = Toplevel() #Crea una ventana nueva como root pero secundaria
    top.iconbitmap("tkinter\icono.ico")
    top.title("Second Window")

    my_img = ImageTk.PhotoImage(Image.open("tkinter/Photos/1.jpg")) 
    my_label = Label(top, image = my_img).pack()
    btn2 = Button(top, text = "Close Window", command = top.destroy).pack()#destroy elimina la ventana emergente

# Button to open the second window panel
btn = Button(root, text = "Open Second Window", command = open)
btn.pack()


root.mainloop()