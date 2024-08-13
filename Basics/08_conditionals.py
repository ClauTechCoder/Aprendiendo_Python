
# Aprender los principales, sus usos y estructura de los más comunes.
# Asi decido si algo de mi codigo se va a ejecutar o no. Control de flujos.

# CONDICIONAL IF -- ojo los saltos de linea!

my_condition = False

if my_condition:
    print("Se ejecuta la condicion")

print("continua el programa!")


# CONDICIONAL IF-ELSE IF -ELSE

my_condition = 5 * 2

if my_condition <= 5:
    print("Estoy en el if!") 
elif my_condition <=10:
    print("Estoy en el else if!")
else:
    print("Estoy en el else!")
    
# MAS COMPLEJO

my_condition = 5 * 2 + 1

if my_condition > 10 and my_condition < 20:
    print("mayor a diez y menor a veinte")
else:
    print("no esta entre diez y veinte")


# AHORA CON CADENAS DE TEXTO

my_string = "cadena de prueba"

if my_string == "hola":
    print("son iguales!") # como no lo son no entra
else:
    print("no son iguales!")

my_string = ""
if not my_string: # compruebo con el not que este vacio
    print("la cadena esta vacia")