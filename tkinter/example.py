import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Crear un Label
label = ttk.Label(root, text="¡Hola, mundo!")
label.pack()

# Crear un Button
button = ttk.Button(root, text="Presióname")
button.pack()

# Crear un Entry
entry = ttk.Entry(root)
entry.pack()

# Crear un Text
text = tk.Text(root)
text.pack()

# Crear un Canvas
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Crear un Checkbutton
checkbutton = ttk.Checkbutton(root, text="Selecciona esto")
checkbutton.pack()

# Crear un Radiobutton
radio1 = ttk.Radiobutton(root, text="Opción 1")
radio1.pack()
radio2 = ttk.Radiobutton(root, text="Opción 2")
radio2.pack()

# Crear un Listbox
listbox = tk.Listbox(root)
listbox.insert(1, "Manzanas")
listbox.insert(2, "Plátanos")
listbox.insert(3, "Naranjas")
listbox.pack()

# Crear un Combobox
combo = ttk.Combobox(root)
combo['values'] = ("Rojo", "Verde", "Azul")
combo.pack()

# Crear un Menu
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Abrir")
file_menu.add_command(label="Guardar")
file_menu.add_separator()
file_menu.add_command(label="Salir")

# Crear un Frame
frame = ttk.Frame(root)
frame.pack()

root.mainloop()