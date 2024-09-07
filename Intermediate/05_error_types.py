
# SyntaxError -> error de sintaxis en el codigo. Esta mal escrito este.

# print "hola" INCORRECTO
print("hola") # CORRECTO

# NameError -> error de nombre de variable no definida
#print(name) INCORRECTO
name = "hola"
print(name) # CORRECTO

# IndexError -> error de indice de lista o tupla fuera de rango

my_list = [1,2,3]
# print(my_list[5]) INCORRECTO
print(my_list[2]) # CORRECTO

# ModuleNotFoundError -> error de modulo no encontrado
# import maths  INCORRECTO
import math # CORRECTO

# AttributeError -> error de atributo no encontrado en un objeto
# print(math.PI) INCORRECTO
print(math.pi) # CORRECTO


# KeyError -> error de atributo no encontrado en un objeto
my_dict = {
    "Nombre":"Raul", 
    "Apellido":"Rodriguez", 
    "Edad:":25, 
    1:"Python",
    }
# print(my_dict["Asignatura"]) INCORRECTO
print(my_dict["Apellido"]) # CORRECTO

#TypeError -> error de tipos incompatibles

# print(my_list["Apellido"]) INCORRECTO
print(my_list[0]) # CORRECTO

# print(1 + "2") INCORRECTO
print(1 + 2) # CORRECTO

# ImportError -> error de importacion de prpiedad/metodo de modulo que no existe
# from math import PI INCORRECTO
from math import pi # CORRECTO

# ValueError -> error de valor incorrecto

# my_int = int("hola") INCORRECTO
my_int = int("10") # CORRECTO
print(my_int) 

# ZeroDivisionError -> error de division por cero
# print(10 / 0) INCORRECTO
print(10 / 2) # CORRECTO
