# Al usar back references siempre usarlo como raw string (r"") para que el
# intérprete no lo confunda con un número octal
import re

# Usar \num donde num es un numero del 1 al 99, se llama backreference
# Esto hace referencia al grupo con el numero num que se encontro en el regEx
regex = r'(\w+),\1'
# EL regex anterior básicamente hace lo siguiente:
# Busca cualquier palabra de cualquier tamaño
# Que luego tenga una coma literal
# Y que luego repita el primer grupo, o sea, la primera palabra que se encontró
m = re.search(regex, 'foo,foo')
print(m)
print(m.group(1))



