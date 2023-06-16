import sqlite3

conn = sqlite3.connect("customer.db")# Conecta con el archivo de base de datos llamado customer.db, si no existe lo crea en blanco

#Crea un cursor para usar nuestra base de datos
c = conn.cursor()

c.execute("SELECT rowid, * FROM customers") #Customers es el nombre de la tabla que creamos al inicio en create_SQLite.py

fetch = c.fetchall() #Retorna todos los elementos de la lista, normalmente se almacena en una lista de tuplas o se usa en un ciclo


for item in fetch:
    print(item)

#No need to commit because you made no change
#conn.commit()
conn.close()
