
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


