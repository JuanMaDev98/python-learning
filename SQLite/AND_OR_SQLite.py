import sqlite3

conn = sqlite3.connect("customer.db")# Conecta con el archivo de base de datos llamado customer.db, si no existe lo crea en blanco

#Crea un cursor para usar nuestra base de datos
c = conn.cursor()

#Selecciona todos los valores que el email termine en .com y el nombre termine con "an"
c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%.com' AND first_name LIKE '%an'")

items = c.fetchall()

for item in items:
    print(item)

print("-----------------------------------------------------------------------")

#Selecciona todos los valores que el email termine en kuewa.com o el nombre sea "Wes"
c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%kuewa.com' OR first_name = 'Wes'")

items = c.fetchall()

for item in items:
    print(item)




conn.commit() #Se hacen cambios asi que hay que darle commit
conn.close()
