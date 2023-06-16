import sqlite3

conn = sqlite3.connect("customer.db")# Conecta con el archivo de base de datos llamado customer.db, si no existe lo crea en blanco

#Crea un cursor para usar nuestra base de datos
c = conn.cursor()

#WHERE es como un if, solo para obtener los datos que cumplan cierto requisito
#El simbolo % "rellena" la parte del texto donde se encuentre para usarlo con WHWERE
c.execute("SELECT * FROM customers WHERE email LIKE '%.com'") #Recoge todos los datos de las rows cuyo email termine con .com

fetch = c.fetchall()


for item in fetch:
    print(item)


#No need to commit because you made no change
#conn.commit()
conn.close()
