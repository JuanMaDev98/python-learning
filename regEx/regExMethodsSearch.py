import re

#Busco con search en la linea la palabra come
text = open("regEx/file.txt")
for line in text:
    line = line.rstrip()
    if re.search("come", line):
        print(line + "\n")
        
#Busco con search al inicio de la linea la palabra come 
text = open("regEx/file.txt")
for line in text:
    line = line.rstrip()
    if re.search("^exp", line):
        print(line + "\n")


#Busco con search  
text = open("regEx/file.txt")     
for line in text:
    line = line.rstrip()
    if re.search("^a.*:", line): #una linea que empiece con a y luego tenga cualquier carácter repetido cualquier cantidad de veces y termine en :
        print(line)