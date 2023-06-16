import sqlite3

#conn = sqlite3.connect(":memory:")# Crea una base de datos en la memoria RAM, que no se guarda una vez cerrado el programa

conn = sqlite3.connect("customer.db")# Conecta con el archivo de base de datos llamado customer.db, si no existe lo crea en blanco

#Creaun cursor para uasar nuestra base de datos
c = conn.cursor()

#Crea una tabla
#SQLite es case sensitive como Python asi que ojo con las mayusculas
c.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text
    )""")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#Asi es como se crearia la tabla normalmente, pero se usan las triples comillas como arriba porque es mas representativo visualmente y mas facil de leer
#c.execute("CREATE TABLE customers(first_name DATATYPE, last_name DATATYPE, email DATATYPE)")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

#hace commit de los cambios que hicimos a la database, algo asi como el commit de github
conn.commit()
#Cerramos la base de datos al terminar de usarla (best practices)
conn.close()













































































































