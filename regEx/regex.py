import re

s = "foo123bar"

x = re.search("\d{3}", s)  # Devuelve un objeto de tipo match
print(bool(x))  # Se convierte a bool para ver si el pattern hace match o no