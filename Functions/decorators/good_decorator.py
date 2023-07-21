def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Asi es como se llama un decorador en python, básicamente esta linea ejecuta el código:
# say_whee = my_decorator(say_whee)
@my_decorator
def say_whee():
    print("Whee!")
