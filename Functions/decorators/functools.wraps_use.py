import functools

def do_twice(func):
    # Necesitas usar en todos los decoradores este otro decorador para que 
    # mantenga los atributos (__name__, help, etc..) de la función a la que decoras
    @functools.wraps(func) 
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
