import re

#Extraigo cierta parte de la cadena de caracteres
text = open("regEx/file.txt")
text1 = text.read()
print(re.findall("[aeiou].n", text1))

#Si pongo () solo extraigo lo que esta entre los () pero si lle tiene que hacer match a toda la expresión
text = open("regEx/file.txt")
text1 = text.read()
print(re.findall("[aeiou].n", text1))