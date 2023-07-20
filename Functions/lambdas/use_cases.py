# lambdas in map()
import functools

animals = ["cat", "dog", "turtle"]

# map aplica una función a todos los elementos de un iterable
print(list(map(lambda x: x.upper(), animals)))  # retorna un objeto de tipo map que puede ser convertido a lista


# lambdas in filter

# filter aplica una función a cada elemento de un iterable, si la funcion retorna True entonces ese elemento pasa a ser parte del objeto de tipo filter
print(list(filter(lambda x: "t" in x, animals)))  # retorna un objeto de tipo filter que puede ser convertido a lista

# lambdas in functools.reduce

# reduce aplica de manera acumulativa una función a los elementos de un iterable, reduciéndolo a un único valor.

import functools
nums = [1, 2, 3, 4, 5]
print(functools.reduce(lambda x, y: x + y, nums))  # 15

print(functools.reduce(lambda x, y: f"{x} - {y}", animals))  # cat - dog - turtle


