
# funciones de orden superior, en lo mas alto de la jerarquia están.




def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value,f): # f es funcion
    return f(first_value + second_value)

print(sum_two_values_and_add_value(1, 2,sum_one))
print(sum_two_values_and_add_value(1, 2,sum_five))

# CLOSURES -> dentro de una funcion defino otra que hace algo y la retorno

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add


add_closure = sum_ten(5)  # es el original_value, se guarda como contexto
print(add_closure(5))
print(sum_ten(5)(5)) # es igual a lo de arriba, pero en una linea de codigo

# BUILT-IN, ya existen en el propio lenguaje

numbers = [2, 5, 10, 21, 3, 30]
#Funcion MAP
def multply_two(value):
    return value * 2

# le pasamos lista y lo que queremos hacer con cada elemento
print(list(map(multply_two,numbers))) 

print(list(map(lambda number: number * 2,numbers))) # igual a lo de arriba

#FILTER -> devuelve una lista con los elementos que cumplen una condicion

def filter_greater_that_ten(number):
    return number > 10 # false/true  


print(list(filter(filter_greater_that_ten,numbers)))
print(list(filter(lambda number: number > 10, numbers))) # igual a lo de arribas

# REDUCE -> reduce y une todos los elementos de una lista en un solo valor, mediante operaciones iterables

from functools import reduce # necesita esta importacion para funcionar.

def sum_numbers(a, b):
    return a + b

print(reduce(sum_numbers,numbers))
