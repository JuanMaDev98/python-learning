archivo = open("E:/Proyectos/Python/I&O/file.txt","r")
texto = archivo.readlines()

for i in texto:
    i = i.rstrip()
    print(i)
