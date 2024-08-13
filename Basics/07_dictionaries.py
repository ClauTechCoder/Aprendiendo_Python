# Aprender cómo funcionan para qué sirven y cómo usarlos
# Estrucutra que relaciona datos.

my_dict = dict() # diccionario creado, ahora está vacio.
my_other_dict = {} # esto es un diccionario vacio tbn, NO ES UN SET.

# diccionario con valores, relacion clave-valor. key:value
my_other_dict = {
    "Nombre":"Raul", 
    "Apellido":"Rodriguez", 
    "Edad:":25, 
    "Lenguajes":{"Python","Java","C","Ruby"}, # le podemos pasar otras estructuras como el set
    1:1.85
    }

print(my_other_dict)
print(my_other_dict[1]) # imprime el valor de esa clave que le hemosd pasado. Facil acceso

print(len(my_other_dict)) # me da los elementos del diccionario
print(len(my_other_dict["Lenguajes"]))  # me da los elementos de ese elemento del diccionario

my_dict["Calle"] = "Pepinillo 14" # añadir campos a manos de esta manera
print(my_dict)

# Operaciones, métodos, funciones...
 
del my_dict["Calle"] # asi se elmina un solo elemento del diccionario
print(my_dict)

print("Lenguajes" in my_other_dict) # asi comprobamos si está una clave en el diccionario
print("Java" in my_other_dict) # no sale porque no es una , es un valor del set de Lenguajes
print("Java" in my_other_dict["Lenguajes"]) # ahora si sale bien porque estamos dentro de la key

print(my_other_dict.items()) # devuelve los elementos y veo bien la clave-valor
print(my_other_dict.keys()) # me devuelve listado las claves
print(my_other_dict.values()) # me devuelve listado los valores

# creamos un diccionario con esas claves pero sin valores. No vale de mucho porque da igual el diccionario que le pasemos. podemos hacer -> dict.fromkeys("Nombre",1,"Ciudad") que vale igual

my_new_dict = my_other_dict.fromkeys(("Nombre",1)) 
my_new_dict["Nombre"] = "Ana"
print(my_new_dict)

my_list = ["Nombre", 1, "Calle"] 
my_new_dict2 = dict.fromkeys(my_list) # Le hemos pasado una lista y da el mismo resultado
print(my_new_dict2)

# Si le paso directamente un diccionario ahora si cobra sentido esta funcionalidad
# dict.fromkeys(my_other_dict, "valor por defecto") -> mismo valor en all keys
my_new_dict3 = dict.fromkeys(my_other_dict)
print(my_new_dict3)

