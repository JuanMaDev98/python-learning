# Para que un decorador acepte funciones con parámetros es necesario ponerle los argumentos *args y **kwargs,
# asi aceptará multiples parámetros, o ninguno de ser necesario

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def scream(text):
    print(text)
    
scream("Nooooo!")