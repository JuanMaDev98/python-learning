# Importo el modulo built-in collections para hacer una linked list
from collections import deque

print(deque())  # crea una linked list vacía

linked1 = deque(["a", "b", "c"])
print(linked1)

linked2 = deque("abc")  # Un string es una lista de caracteres (kinda)
print(linked2)

linked3 = deque([{'data': 'a'}, {'data': 'b'}])
print(linked3)

