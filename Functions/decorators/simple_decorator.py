# Un decorador toma una función y la ejecuta en su interior pero teniendo la posibilidad
# de ejecutar cierto código antes y después de llamarla, esto permite cambiar
# la funcionalidad de la función sin tener que modificarla

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

say_whee()

# Otro ejemplo de decorador que al aplicarlo a una función solo la ejecuta de día

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            print("Is night time")
            pass  # Hush, the neighbors are asleep
    return wrapper  # Retorno la nueva función que modifica el comportamiento de la función usada como parámetro

def scream():
    print("Gaaaaaaa")

scream = not_during_the_night(scream)  # Asigno como nuevo valor de scream el retorno de la función not_during_the_day
scream()














