import sqlite3

conn = sqlite3.connect("customer.db")# Conecta con el archivo de base de datos llamado customer.db, si no existe lo crea en blanco

#Crea un cursor para usar nuestra base de datos
c = conn.cursor()

#Rellena los valores de la tabla de nuestra base de datos
c.execute("SELECT * FROM customers") #Customers es el nombre de la tabla que creamos al inicio en create_SQLite.py

#fetch1 = c.fetchone() #Retorna el siguiente elemento de la lista (cada vez que se llama retornara un nuevo elemento, se usa para ciclar obviamente)
#fetch2 = c.fetchmany(X) #COmo fetchone pero retorna los elementos de x en x valores
fetch3 = c.fetchall() #Retorna todos los elementos de la lista, normalmente se almacena en una lista de tuplas o se usa en un ciclo

#print(fetch1, "\n")
#print(fetch2, "\n")
print(fetch3, "\n")

#No need to commit because you made no change
#conn.commit()
conn.close()













































































































