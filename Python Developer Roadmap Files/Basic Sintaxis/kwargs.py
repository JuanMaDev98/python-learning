# El uso adecuado de Kwargs en una función para desempaquetar un diccionario

# Es usado sobre t-odo para la creación de clases que pueden llevar X cantidad de argumentos
# como por ejemplo los widgets de tkinter
def car(**kwargs):
    """Docstring for this function lol"""
    color = kwargs.get("color", "red")
    speed = kwargs.get("speed", 100)
    brand = kwargs.get("brand", "Ford")
    return f"The car made by {brand} is {color} and reach a speed of {speed} KM/H"


print(car())
print(car(color="blue", speed=200, brand="Chevrolet"))
