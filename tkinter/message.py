from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox #Importamos el messagebox

root = Tk()
root.iconbitmap("icono.ico")
root.title("Tkinter Messages")


def yesno():
    response = messagebox.askyesno("Yes or No", "Hello World!")# el showifo acepta de primer parametro el nombre de la ventana y de segundo el texto que trae
    #posibles messagebox(showinfo, showwarning, showerror, askquestion, askokcancel, askyesno)
    #podemos igualar una variable al messagebox ya que este retorna un valor dependiendo del messagebox
    print(response)

    if response == True:
        messagebox.showinfo("Info", "You clicked Yes")
    else:
        messagebox.showerror("Info", "You clicked No")

def question():
    response = messagebox.askquestion("Good", "Hello World!")
    print(response)

    if response == "yes":
        messagebox.showinfo("Info", "You clicked Yes")
    elif response == "no":
        messagebox.showerror("Info", "You clicked No")

def okcancel():
    response = messagebox.askokcancel("Good", "Hello World!")
    print(response)

    if response == True:
        messagebox.showinfo("Info", "You clicked Yes")
    elif response == False:
        messagebox.showerror("Info", "You clicked No")

###################                                          #####################
#showinfo, showwarning y showerror retornan "ok" si el usuario oprime el boton OK#
###################                                          #####################


Button(root, text = "askyesno", command = yesno).pack()# llamamos el messagebox usando un boton en este caso
Button(root, text = "askokcancel", command = okcancel).pack()
Button(root, text = "askquestion", command = question).pack()



root.mainloop()