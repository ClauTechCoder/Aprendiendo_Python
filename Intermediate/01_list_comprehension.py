
# es tener listas de forma "comprimida". Manera de crear listas de manera rapida o a partir de otras listas

my_original_list = [35, 24, 62, 52, 30, 30, 17]

# recorro la lista y me quedo uno a uno sus elementos 
my_list = [i for i in my_original_list]
print(my_list)

my_original_list2 = [0, 1, 2, 3, 4, 5, 6, 7]

# tengo una lista de 8 elemnentos
my_list = [i for i in range(8)]
print(my_list)

# directamente con un rango puedo crear una lista. Analoga a la de arriba
my_range = range(8)
print(list(my_range))

# suma uno al elemento de la lista y lo guarda
my_list = [i + 1 for i in range(8)]
print(my_list)

# x2 al elemento de la lista y lo guarda
my_list = [i * 2 for i in range(8)]
print(my_list)

# multiplica por si mismo al elemento de la lista y lo guarda
my_list = [i * i for i in range(8)]
print(my_list)

# Pasandole una funcion ahora.
def sum_six(number):
    return number + 6

my_list = [sum_six(i) for i in range(8)]
print(my_list)
