import sqlite3

conn = sqlite3.connect("customer.db")# Conecta con el archivo de base de datos llamado customer.db, si no existe lo crea en blanco

#Crea un cursor para usar nuestra base de datos
c = conn.cursor()

#Limita la recogida de dato a solo los 3 primeros valores encontrados
c.execute("SELECT rowid, * FROM customers LIMIT 3")

items = c.fetchall()

for item in items:
    print(item)




conn.commit() #Se hacen cambios asi que hay que darle commit
conn.close()
