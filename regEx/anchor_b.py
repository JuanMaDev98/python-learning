# r delante de un string (r"string") ignora los caracteres de escape y los interpreta
# como caracteres normales 

import re

s = "foo123 bar"

# Si la \b esta delante de la palabra, el pattern indica que lo buscado debe estar al inicio 
# de una palabra, si esta al final, debe estar al final de la palabra

# Si se usa \b se busca el pattern como una palabra suelta "texto {pattern} texto"
x = re.search(r"\bfoo", s)  
print(bool(x))  # True

# \B prueba lo contrario, que lo buscado no este al inicio o al final de una palabra, si se usa \B en
# el inicio y final de la palabra, la misma debe estar en el interior de una palabra