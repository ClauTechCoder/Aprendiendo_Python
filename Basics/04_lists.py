# Aprendiendo el concepto, funcuiones y/o operaciones de las listas en Python.
# No es un tipo base. Es una estructura. Es parecido a un array, pero más "inteligente".

my_list = list()
my_other_list = []

my_list = [35, 24, 62, 52, 30, 30, 17]
my_other_list = [35, 1.77, "Claudia", "clacla"] # puedo "mexclar" tipos de datos

# Operaciones, métodos, funciones...

print(my_list) 
print(len(my_list)) # me dice los elementos que hay
print(type(my_other_list)) # me dice el tipo de dato que es lista

print(my_other_list[0]) # me da el dato de esa posicion
print(my_other_list[-1]) # me da el dato de la ultima posicion
print(my_other_list[1:4]) # se queda con ese rango/intervalo de la lista

print(my_other_list.count("Claudia")) # te da el num de veces del elemento que le pases

age, height, name, alias = my_other_list # una variable a el elemento de la lista
# tbn podemos hacerlo -> var, other_var = my_other_list[i], my_other_list[i+1]
print(name)

print(my_list + my_other_list) # concateno dos listas. No vale -,*,/

my_other_list.append("holaaaa") # añado un nuevo elemento al final de la lista
my_other_list.insert(1, "posicion uno") #inserto en una posicion concreta el elemento
my_other_list.remove("holaaaa") # elmina ese elemento en concreto

my_new_list = my_list.copy() # copiado hasta este punto en el que se encuentran los elementos
my_list.pop() # quita el ultimo y se lo "guarda", puedo almacenarlo en una variable
del my_list[3] # elimino ese elemento en concreto de la lista
my_list.clear() # limpio la lista, ahora no hay nada en ella

my_new_list.reverse() # le da la vuelta a la lista el ultimo pasa al primero, etc.
my_new_list.sort() # ordena la lista de menor a mayor
