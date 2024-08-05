# Aprender cómo funcionan para qué sirven y cómo usarlos

my_set = set()  # set creado, es un tipo de dato.
my_other_set = {} # inicialmente si vemos el tipo es un diccionario
print(type(my_other_set))

my_other_set = {"pepe","rodriguez",37} # cuando le pongo datos ya es un set
print(type(my_other_set))

#METODOS Y/O OPERACIONES

print(len(my_other_set)) # tengo la longitud del set
# print(my_other_set[2]) -> asi no se accede a un elemento, no es una lista

my_other_set.add("pepito") # guarda elementos sin orden.
my_other_set.add("pepito") # si esta repetido no lo añade. SET TIENE UNICIDAD
print(my_other_set) # si imprimo veo que NO ESTA ORDENADO, diferencia clave.

print("pepe" in my_other_set) # asi compruebo si un elemento existe dentro de un set
my_other_set.remove("pepito") # elimino un elemento concreto del set

my_other_set.clear() # asi "limpio el set", lo vacio.
my_list = list(my_set) # asi paso de set a lista
del my_set # asi elimino un set, no su contenido. Eliminas el objeto directamente

my_set = {"pepe","rodriguez",37}
my_other_set = {"Kotlin","Java","C", "Python"}

my_new_set = my_set.union(my_other_set) # mezcla ambas en un solo set. Lo repetido no sale
#si union no lo alamceno en una variable es como si no estuviese guradado en el set
print(my_new_set)

print(my_new_set.difference(my_set)) # de ese set quita lo que le pasemos del otro
