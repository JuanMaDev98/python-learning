import sqlite3

conn = sqlite3.connect("customer.db")# Conecta con el archivo de base de datos llamado customer.db, si no existe lo crea en blanco

#Crea un cursor para usar nuestra base de datos
c = conn.cursor()

#Tabla con todos los clientes añadir a la database
many_customers = [
                ('Wes', 'Brown', 'wesbrown.com'),
                ('Steph', 'Kuewa', 'steph@kuewa.com'),
                ('Dan', 'Pas', 'dan@pas.com')
                 ]

#Rellena los valores usando una lista, los ? son placeholders para saber el formato a usar
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)



conn.commit()
conn.close()













































































































