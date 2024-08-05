# Aprender lo básico de las tuplas. 
# NO CONFUNDIR CON LAS LISTAS, SE DIFERENCIAS MUY BIEN EN LA DEFINICION

my_tuple = tuple()
my_other_tuple = () # en listas era con []

my_tuple = (35,1.68, "juan", "fernandez") 
my_other_tuple = (40,1.85, "ana", "peleteiro")
print(my_tuple[0]) # me da el primer elemento
print(my_tuple[-1]) # me da el ultimo elemento

# Operaciones

print(my_tuple.count("juan")) # cuante el numero elementos que coinciden
print(my_tuple.index("juan")) # me da la posicion de ese elemento. Esto en listas no existe
# my_tuple[1] = "hello" --> DA ERROR, LAS TUPLAS SON CONSTANTES NO CAMBIAN SU VALOR

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) # tengo ambas tuplas en una "sumadas"

print(my_sum_tuple[1:4]) # veo los elementos de ese rango, el ultimo no lo tiene en cuenta

my_tuple = list(my_tuple) #convierto una tupla en una lista
print(type(my_tuple))

# del my_tuple -> esto lo que hace es eliminar la variable, no su contenido
# del my_tuple[2] -> esto tampoco es valido
