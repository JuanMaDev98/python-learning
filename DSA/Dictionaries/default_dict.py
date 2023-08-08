from collections import defaultdict

# En defaultdicts tratar de acceder a una clave que no existe simplemente inicializará su valor al dado
def_dict = defaultdict(lambda: 5)  # Hay que pasar una funcion y el valor retornado es en l que se inicializa

print(def_dict)
print(def_dict["number"])
print(def_dict)