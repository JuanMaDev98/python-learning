print("MÉTODOS PARA MANIPULAR LISTAS  \n")

print("len([Lista]) - devuelve la longitud de la lista \n")
print("max([Lista]) - devuelve el valor máximo de la lista \n")
print("min([Lista]) - devuelve el valor mínimo de la lista \n")

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
print("lista.append() - agrega un elemento al final de la lista \n")

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
print("lista.extend() - agrega los elementos de una lista a otra \n")

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
print("lista.insert(indice, elemento) - inserta un elemento en una posición específica \n")

#Parámetros:
'''
índice - El índice especifica el lugar donde se insertará el elemento.
elemento - El elemento es el valor que se insertará en la lista.
'''

#Ejemplo:

# Declaración de una lista
lista = [1, 2, 3]

# Uso de insert() para agregar un elemento a la lista
lista.insert(2, 4)

print(lista) # Devuelve [1, 2, 4, 3]

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
print("lista.remove(elemento) - elimina el primer elemento con el valor dado. \n")

#Parámetros:
'''
elemento - El elemento a eliminar.
'''
#Ejemplo:

lista = [1, 2, 3, 4]
lista.remove(3)
print(lista) #retorna [1, 2, 4]

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
print("lista.pop() - elimina el elemento en una posición específica \n")

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
print("lista.reverse() - invierte el orden de los elementos en la lista. \n")

#Ejemplo:

mi_lista = [1, 2, 3, 4]
print(mi_lista.reverse()) # retorna [4, 3, 2, 1]


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
print("lista.sort() - ordena los elementos de la lista. \n")

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
print("lista.clear() - remueve todos los elementos de una lista \n")

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
print("lista.copy(src, dest, depth, ignore_errors) - copia una lista \n")

#Parámetros:
'''
src - El objeto fuente que se va a copiar.
dest - El objeto destino al que se va a copiar el objeto fuente.
depth - La profundidad a la que se realizará la copia.
ignore_errors - Una bandera booleana que indica si se deben ignorar los errores durante la copia.
'''

#Ejemplo:
'''
from copy import copy

# Crear un objeto fuente
src = {'name': 'John', 'age': 30}

# Crear un objeto destino
dest = {}

# Copiar el objeto fuente al objeto destino
copy(src, dest, depth=2, ignore_errors=True)

print(dest) # {'name': 'John', 'age': 30}
'''
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
print("lista.count(elemento, start, end) - retorna el numero de elementos con el valor dado \n")

#Parámetros:
'''
elemento - El elemento que desea contar en la lista.
start (Opcional) - Un índice específico para comenzar a contar desde. Por defecto, este valor es 0.
end (Opcional) - Un índice específico para finalizar el conteo. Por defecto, este valor es el tamaño de la lista.
'''
#Ejemplo:

lista = [1, 2, 3, 4, 5, 1, 2, 3]
print(lista.count(1)) #El resultado sería 2, ya que hay dos instancias del número 1 en la lista

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
print("lista.index(elemento, start, end) - retorna el indice del primer elemento con el valor dado \n")

#Parámetros:
'''
elemento - elemento que se busca 
start - indice donde comienza
end - indice hasta en que busca, sin incluir este valor
'''
#Ejemplo:

mi_lista = [1, 2, 3, 4]

# Obtener el índice del elemento 2
indice = mi_lista.index(2)

print(indice) # Imprime 1

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
print("lista.sort() - organiza una lista \n")

#Ejemplo:

lista = [5, 3, 8, 6, 1]
lista.sort()
print(lista)
#El código anterior imprime: [1, 3, 5, 6, 8]

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
print("lista.sum(lista, start) - Suma todos los elementos de una lista \n")

#Parámetros:
'''
lista - lista a usar para la suma
start - indice donde comienza, 0 por defecto
'''
#Ejemplo:

# Sumando los elementos de una lista
números = [1, 2, 3, 4, 5]
resultado = sum(números)
print(resultado) # Output: 15

# Sumando los elementos de una tupla con un valor inicial
tupla_números = (1, 2, 3, 4, 5)
resultado = sum(tupla_números, 10)
print(resultado) # Output: 25





















