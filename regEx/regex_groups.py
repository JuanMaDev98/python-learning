import re

s = re.search(r'(\w+),(\w+),(\w+)', 'foo,quux,baz')

# groups() retorna todos los grupos (los paréntesis) que se capturan en el regEx en una tupla
print(s.groups())

# group(n) retorna el n grupo (paréntesis) capturado por el regEx
# Se puede especificar mas de un valor y retorna todas esas posiciones en una tupla
print(s.group(2))

