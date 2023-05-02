import time

try:
    num = int(input("Dime un número: "))
except ValueError:
    print("Debes introducir un numero valido")
    quit()

count = 0
while num != 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = num * 3 +1
    print(num)
    count += 1
    #time.sleep(0.5)

print(f"Contó {count} números")