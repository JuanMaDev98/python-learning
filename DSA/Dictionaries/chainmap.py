from collections import ChainMap

dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "four": 4}
# Chainmap une dos diccionarios entre si para buscar keys de izquierda a derecha
chain = ChainMap(dict1, dict2)