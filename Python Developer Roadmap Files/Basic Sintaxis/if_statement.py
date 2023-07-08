# Asi se puede usar un if tambien

x = 2

# Ejecuta todas las expresiones si es true y ninguna si es false
if x == 2: print(x); print(x + 10)  # Esto es funcional pero no se recomienda

# Asi también funciona, igual no recomendado
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

y = 3
# Ternary operator
# En este caso los paréntesis son innecesarios, ya que el operador coge tod-o el statement
z = (1 + x) if x > y else (y + 2)

# Asi harias si quieres evaluar en el operador ternario solo lo del medio
z = 1 + (x if x > y else y) + 2

# Uso correcto del operador ternario
x = 5 if y == 3 else 6

print("X", x)