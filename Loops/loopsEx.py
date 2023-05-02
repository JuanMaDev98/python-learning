numero = 0
total = 0
count = 0
average = 0
while numero != "done":
    numero = input("Dime un numero: ")
    try:
        numero = int(numero)
    except:
        print("Eso no es un numero")
        continue
    total += numero
    count += 1
average = total / count
print(total)
print(count)
print(average)