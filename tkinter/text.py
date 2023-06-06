from tkinter import *

root = Tk()

# Creamos un widget Text y le damos un tamaño
text = Text(root, height=10)
text.grid(row =0, column = 0)

# Creamos un scrollbar y lo asociamos con el widget Text
scrollbar = Scrollbar(root, command=text.yview)
scrollbar.grid(row = 0,column = 1)
text.config(yscrollcommand=scrollbar.set)

root.mainloop()

#TODO: Add comments