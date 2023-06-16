import sqlite3

conn = sqlite3.connect("customer.db")# Conecta con el archivo de base de datos llamado customer.db, si no existe lo crea en blanco

#Crea un cursor para usar nuestra base de datos
c = conn.cursor()

c.execute("""UPDATE customers SET first_name = "Bob"
             WHERE last_name = 'Elder'
          """) #Cambia el first_name a "BOB" a las rows que tengan de last_name = "Elder"

c.execute("""UPDATE customers SET first_name = "Juan"
             WHERE rowid = '4'
          """) #Cambia el first_name a "Juan" al row con un rowid de 4


c.execute("SELECT * FROM customers")
print(c.fetchall())

conn.commit() #Se hacen cambios asi que hay que darle commit
conn.close()
