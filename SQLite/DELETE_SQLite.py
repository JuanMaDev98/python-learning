import sqlite3

conn = sqlite3.connect("customer.db")# Conecta con el archivo de base de datos llamado customer.db, si no existe lo crea en blanco

#Crea un cursor para usar nuestra base de datos
c = conn.cursor()

c.execute("DELETE from customers WHERE rowid = 6")#Elimina el elemento con rowid 6 en la lista customers

c.execute("SELECT * FROM customers")
print(c.fetchall())

conn.commit() #Se hacen cambios asi que hay que darle commit
conn.close()
