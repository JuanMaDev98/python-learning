# Para qe un decorador acepte funciones con parámetros es necesario ponerle los argumentos *args y **kwargs, 
# asi aceptara multiples parámetros, o ninguno de ser necesario

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        # func(*args, **kwargs)   -->   Esta linea hay que eliminarla porque return también ejecuta la función y se ejecutaría triple
        return func(*args, **kwargs)  # Si le añades este return entonces la función base que decores seguiría retornando su valor
    return wrapper_do_twice

@do_twice
def suma(x, y):
    print(x + y)
    return x + y
    
    
print(f"Retornado de la función: {suma(5, 10)}")