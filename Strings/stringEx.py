#Extrae el número después de los :
str = "X-DSPAM-Confidence: 0.8475"

print(float(str[(str.find(":") + 2):]))