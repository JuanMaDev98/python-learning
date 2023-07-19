func = lambda x: x + 1

print(func(5))  # 6
print((lambda x: x + 1)(2))  # retorna 3, es la forma de invocar una lambda, el segundo parentesis es el parametro que se pasa

full_name = lambda first_name, last_name: f"{first_name} {last_name}"

print(full_name("Juan Manuel", "González Vega"))

print((lambda x: (x % 2 and 'odd' or 'even'))(3))