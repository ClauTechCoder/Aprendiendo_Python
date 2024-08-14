
# Aprender sus usos y las principales estructuras de estas.
# Manera de recoger/encapsular un bloque de código que resuelve un problema concreto.

# Declaración/Definición de la misma.
def my_function ():
    print("Esta es mi primera funcion")

my_function() # llamada a la funcion y ejecuta ese bloque de código

# Funcion pasandole parametros

def my_sum(a,b):
    print(a + b) # me devuelve en un print la suma de esos valores

my_sum(2,3)

# Funcion con return

def my_sum_with_return (a,b):
    return a + b

print(my_sum_with_return(4,6)) # o puedo asignar resultado a variable e imprimirla.

# Funciones algo más compleja

def print_name(name,surname):
    print(f"{name} {surname}") 
    # f es formateo, accedo a los valores en este caso que me llega por parametro

print_name("Alex","Segura")
print_name(surname = "Segura", name = "Alex") # puedo reordenar los parametros de esta manera

def print_name_with_default(name,surname,alias ="Sin alias"): # valor por defecto se hace así
    print(f"{name} {surname} mejor conocido como {alias}") 
    
print_name_with_default("Alejandro","Segura","Alex")
print_name_with_default("Alejandro","Segura") # no le pongo parametro y aun asi funciona.

def print_all_upper(*text): # le puedo pasar infinitos parametros de ese tipo con el *
    for t in text: # imprimo en cada linea todo lo que me pasen
        print(t.upper())

print_all_upper("hola","que","tal","?")


