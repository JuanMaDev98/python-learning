# Al tratar de acceder a una variable Python trata de buscarla siempre dentro de la función actual, si
# no la encuentra busca en la función mas externa en caso de haberla y si no la encuentra ahi tampoco
# busca en el scope global (todo el código)

# En esta función, si comentamos las asignaciones a variables podemos darnos cuenta de la prioridad que
# Python da a la hora de buscar estas variables

def outer():    
    # Non-Local scope
    x = "outer"
    def inner():
        # Local Scope
        x = "inner"  
        print(x)
    inner()

x = "global"
outer()

print("Segundo Ejemplo -------------------------------------------------------------------------------------")

a = 10
b = 20
c = 30

def print_globals():
    print(a, b, c)
    c = 100
    print(c)

# Si llamamos a la funcion anterior obtendremos un UnboundLocalError, ya que no podemos modificar los 
# valores de las variables desde un scope mas pequeño

#print_globals()  # Descomenta esta linea para que ocurra el UnboundLocalError

"""En este caso anterior al poner:

c = 100

Python cree que estás creando una nueva variable con nombre c en el scope global, en vez de modificar
la global c

Si quisieras modificar la variable global desde dentro de un scope local podrias usando la keyword 'global'
""" 

def print_globals():
    global c  # Defino la variable c como global, lo que me permite modificar esta variable globalmente
    print(a, b, c)
    c = 100
    print(c)


print_globals()

# La funcion built-in globals(), retorna un diccionario con todas las variables globales y el valor que almacenan
# Este diccionario se mutable po lo que puedes cambiar los valores de las variables globales y esto se reflejara en
# el programa
































































