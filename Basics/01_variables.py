
# Aprendo qué son y cómo trabajar con ellas
#por convencion se pone en minúscula y siguiendo snake case(con _)

my_variable = "esto es un string"
my_int_variable = 88
my_bool_vartiable  = True

int_to_str = str(my_int_variable) #aqui transformamos int -> string

print(my_variable)
print(my_int_variable)

#a print le podemos pasar diferentes argumentos, las concatenamos
print(my_variable,my_int_variable,my_bool_vartiable)
print(type(int_to_str))

print(len(my_variable)) #Longitud de una cadena

#Variables en una sola línea, ahorro de espacio, en orden cronologico
#ESW MU FACIL COMETER ERRORES CON ESTO
#Las variables en python pueden cambiar su tipo de dato sin problema

name, surname, alias, age = "Claudia", "Robles", "Clacla", 25
print(name, surname,alias, age)

your_name = input("Introduce tu nombre: ")
print(your_name)


address: str = "direaccion" #lo declaro inicialmente con str
address = 32
print(address) #como lo he cambiado ahora la variable es un int

#Concatenar cadenas de texto

saludo_python = "Hola" + " " + "Python"
print(saludo_python)

