
# Aprendo qué son y las 'operaciones' más comunes en ellos

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string)) # calculo la longitud de la cadena de caractgeres
print(len(my_other_string))

print(my_other_string + " " + my_string) # concatenar strings 

#Strings usanco caracteres especiales, con \\ no hace caso
my_new_string = "aquí tengo un string \n con salto de linea"
print(my_new_string)

my_tab_string = "aquí tengo un string \t con una tabulacion"
print(my_tab_string)

my_scape_string = "\\taquí tengo un string \n escapado"
print(my_scape_string)

#Formateo de Strings

name, surname, age = "Claudia", "Robles", 24

#represento variables en un print %s -> string, %d -> int, %f -> float
#usando .format tenemos solo llaves {} representando la variable

print("Mi nombre es {} {} y tengo {} años".format(name, surname, age)) 
print("Mi nombre es %s %s y tengo %d años"%(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y tengo " + str(age) + " años")
print(f"Mi nombre es {name} {surname} y tengo {age} años")

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language 
#realmente lo que hace es asignar una variable a cada letra, si no hay num excacto da error

print(a)
print(b)

# División del string 

language_slice = language[1:3] # se queda con ese intervalo
print(language_slice)
language_slice = language[1:] # desde la pos uno hasta el final
print(language_slice)
language_slice = language[-2] # la segunda empezando por el final
print(language_slice)

reverse_language = language[::-1] # le damos la vuelta al string
print(reverse_language)

language_slice = language[0:6:2] # se queda el rango 0:6 y evita de dos en dos
print(language_slice)

# Funciones o metodos que podemos aplicar a los strings

print(language.capitalize()) # primer caracter a mayuscula
print(language.upper()) # todo a mayuscula
print(language.lower) # todo a minuscula
print(language.count("t")) # cuenta las veces que aparece ese caracter
print(language.isnumeric()) # dice si el estring es un numero 
print(language.upper().isupper()) # pasa a mayuscula y comprueba que lo sea, combo funciones.
print(language.startswith("Py")) # preguntas si empieza por ese string
