from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Photo Viewer")
root.iconbitmap("icono.ico")

#Loading Photos
Photo1 = ImageTk.PhotoImage(Image.open("Photos/1.jpg"))
Photo2 = ImageTk.PhotoImage(Image.open("Photos/2.jpg"))
Photo3 = ImageTk.PhotoImage(Image.open("Photos/3.jpg"))
Photo4 = ImageTk.PhotoImage(Image.open("Photos/4.jpg"))
photo_index = 0
scroll_list = [Photo1, Photo2, Photo3, Photo4] #List of Photos for scrolling purposes

#Status bar
status = Label(root, text = f"{photo_index + 1} of {len(scroll_list)}",  bd = 1, pady = 1, relief = SUNKEN, anchor = E) #Anchor "ancla" el elemento a un polo, no permite combinacion
status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E) #Sticky "pega" al polo seleccionado(Norte, Sur, Este, Oeste) o una combinacion de varios (N+O)

#Picture Frame using Label
picture = Label(root, image = Photo1)
picture.grid(row = 0, column = 0, columnspan = 3)

#Button Comands
def remake_image_status():
    global picture
    global status
    picture.grid_forget() # Hace que el elemento "olvide" el grid en donde estaba y se descargue
    picture = Label(root, image = scroll_list[photo_index])
    picture.grid(row = 0, column = 0, columnspan = 3)

    status.grid_forget()
    status = Label(root, text = f"{photo_index + 1} of {len(scroll_list)}",  bd = 1, pady = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)

def forward():
    global picture
    global photo_index
    global my_button2
    global my_button1

    photo_index += 1

    my_button2.grid_forget()
    my_button1.grid_forget()

    my_button2 = Button(root, text = ">>", padx = 10, command = forward)
    my_button1 = Button(root, text = "<<", padx = 10, command = backward)
    if photo_index == len(scroll_list) - 1:
        my_button2 = Button(root, text = ">>", padx = 10, command = forward,state = "disable")

    my_button2.grid(row = 1, column = 2)
    my_button1.grid(row = 1, column = 0)

    remake_image_status()

def backward():
    global picture
    global photo_index
    global my_button2
    global my_button1

    photo_index -= 1
    my_button2.grid_forget()
    my_button1.grid_forget()

    my_button2 = Button(root, text = ">>", padx = 10, command = forward)
    my_button1 = Button(root, text = "<<", padx = 10, command = backward)

    if photo_index == 0:
        my_button1 = Button(root, text = "<<", padx = 10, command = backward,state = "disable")

    my_button2.grid(row = 1, column = 2)
    my_button1.grid(row = 1, column = 0)

    remake_image_status()

#Making buttons
my_button1 = Button(root, text = "<<", padx = 10, command = backward, state = "disable")
exit_button = Button(root, text = "X", padx = 5, command = root.quit)
my_button2 = Button(root, text = ">>", padx = 10, command = forward)

my_button1.grid(row = 1, column = 0)
exit_button.grid(row = 1, column = 1, pady = 10) # Puedes usar pady o padx para dejar espacios entre las columnas y filas
my_button2.grid(row = 1, column = 2)



#Main TKinter Loop
root.mainloop()