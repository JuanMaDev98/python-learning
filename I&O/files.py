archivo = open("E:/Proyectos/Python/I&O/file.txt","r")
#texto = archivo.read()

for i in archivo:
    i = i.rstrip()
    #if i.startswith("Juan: "):
        #print(i)
    if not "Juan: " in i:
        continue
    print(i)