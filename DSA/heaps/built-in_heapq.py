import heapq

a = [3, 5, 1, 2, 6, 8, 7]
heapq.heapify(a)  # Convierte una lista en un Heap
# Nota: Una sorted list es un Heap
print(a)
print(heapq.heappop(a))  # Saca del Heap el root, o sea el elemento mas pequeño
print(a)
heapq.heappush(a, 4)  # Mete una valor al Heap sin alterar la Heap Property
print(a)

# Si tienes que meter un elemento y sacar otro a la vez puedes usar heappushpop()
# Y si tienes que hacerlo viceversa puedes usar heapreplace()
# Son útiles en algunos algoritmos porque son más eficientes que hacer las dos cosas por separado