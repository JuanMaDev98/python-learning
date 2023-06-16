import sqlite3

conn = sqlite3.connect("customer.db")# Conecta con el archivo de base de datos llamado customer.db, si no existe lo crea en blanco

#Crea un cursor para usar nuestra base de datos
c = conn.cursor()

#Rellena los valores de la tabla de nuestra base de datos
c.execute("SELECT * FROM customers") #Customers es el nombre de la tabla que creamos al inicio en create_SQLite.py

fila = c.fetchone() #Retorna el siguiente elemento de la lista (cada vez que se llama retornara el siguente elemento, se usa para ciclar obviamente)

#Ejemplo ciclando
while fila is not None:
    print(fila)
    fila = c.fetchone()

#No need to commit because you made no change
#conn.commit()
conn.close()













































































































