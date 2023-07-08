# los docstring deben documentarse asi si som de una linea, sino como abajo

def f():
    """Docstring de una linea siempre se cierra en la misma linea"""
    pass


def fx():
    """Docstring multilínea

    Los docstring multilínea en el caso de las funciones mas largas
    deben tener una línea de resumen sola arriba, seguidos por un espacio
    en blanco y luego el bloque de líneas más debajo
    """


print(fx.__doc__)  # Para ver el docstring de la funcion usando un dunder

# En la consola de Python se puede escribir help<function_name> para ver
# el docstring de dicha función
