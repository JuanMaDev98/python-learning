archivo = open("E:/Proyectos/Python/I&O/file.txt","r")

for i in archivo:
    i = i.strip()
    print(i.upper())  