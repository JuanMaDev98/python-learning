from tkinter import *

root = Tk()
root.title("TK-calculator")  # cambia el título de la ventana
list_sum = []


# Funciones de los botones


def button_click(num):
    # entry1.delete(0, END) #Borra todo lo escrito en el entry1
    entry1.insert(END, num)  # end inserta el número en la posición final


def button_clear_sign(lista):
    entry1.delete(0, END)
    lista.clear()


def button_add_sign(lista):
    lista.append(int(entry1.get()))
    entry1.delete(0, END)
    global sign
    sign = "+"
    # print(lista)
    '''if len(lista) == 2:
        value = sum(lista)
        entry1.insert(0,value)
        lista.clear()'''


def button_subtract_sign(lista):
    lista.append(int(entry1.get()))
    entry1.delete(0, END)
    global sign
    sign = "-"


def button_multiply_sign(lista):
    lista.append(int(entry1.get()))
    entry1.delete(0, END)
    global sign
    sign = "*"


def button_divide_sign(lista):
    lista.append(int(entry1.get()))
    entry1.delete(0, END)
    global sign
    sign = "/"


def button_equal_sign(lista):
    lista.append(int(entry1.get()))
    entry1.delete(0, END)
    if sign == "+":
        value = lista[0] + lista[1]
    elif sign == "-":
        value = lista[0] - lista[1]
    elif sign == "*":
        value = lista[0] * lista[1]
    elif sign == "/":
        value = lista[0] // lista[1]
    entry1.insert(0, value)
    lista.clear()


# Definiendo los componentes

entry1 = Entry(root, width=36, borderwidth=5)
button1 = Button(root, text="1", padx=30, pady=15, command=lambda: button_click(
    1))  # Lambda antes de la función permite que se le pasen parámetros a la función
button2 = Button(root, text="2", padx=30, pady=15, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=30, pady=15, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=30, pady=15, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=30, pady=15, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=30, pady=15, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=30, pady=15, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=30, pady=15, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=30, pady=15, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=30, pady=15, command=lambda: button_click(0))

button_equal = Button(root, text="=", padx=70, pady=15, command=lambda: button_equal_sign(list_sum))
button_clear = Button(root, text="Clear", padx=60, pady=15, command=lambda: button_clear_sign((list_sum)))
button_add = Button(root, text="+", padx=29, pady=15, command=lambda: button_add_sign(list_sum))
button_subtract = Button(root, text="-", padx=30, pady=15, command=lambda: button_subtract_sign(list_sum))
button_multiply = Button(root, text="*", padx=31, pady=15, command=lambda: button_multiply_sign(list_sum))
button_divide = Button(root, text="/", padx=30, pady=15, command=lambda: button_divide_sign(list_sum))

# Dibujando los componentes en pantalla

entry1.grid(row=0, column=0, columnspan=3, padx=10,
            pady=10)  # columnspan cambia la cantidad de columnas que usa el objeto para ocupar como espacio

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0, columnspan=1)
button_multiply.grid(row=6, column=1, columnspan=1)
button_divide.grid(row=6, column=2, columnspan=1)

root.mainloop()
