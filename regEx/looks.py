# Lookahead y lookbehind son como los if de los regEx
import re

# En este caso se usa el lookahead (?=)
# Aquí específicamente prueba que el próximo caracter sea uno entre la a y la z minúsculas
# Al retornar el objeto, el lookahead se ignora completamente en el match
x = re.search('foo(?=[a-z])', 'foobar')
print(x)  # Retorna un objeto porque si se cumple la condicion, ya que hace match con foo
y = re.search('foo(?=[a-z])', 'foo123')
print(y)  # Retorna None porque la condicion no se cumple

# ?! (en vez de ?=) es un lookahead negativo, como un if not

# ?< es un lookbehind assertion
# Es exactamente lo mismo que un lookahead, pero mira delante, no detrás del statement
# La única diferencia es que la línea evaluada en un lookbehind no puede ser de longitud indefinida  (usando * ó +)