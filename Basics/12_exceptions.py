
# Aprender el manejo de errores en Python para que no se rompa el programa

numberOne, numberTwo = 5, 1
print(numberOne + numberTwo) # esto evidentemente no da ningun tipo de error

numberTwo = "1" # he cambiado a un str, no se puede sumar hay que tratar el error

# Es posible anidarlos pero no tiene mucho sentido
try: # intentalo y si hay error salta al except, el programa no muere aunque se para
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except: # no se ejecuta si en el try no hay errores
    print("Se ha producido un error")
else: # parte opcional, se ejecuta si no hay excepcion
    print("La ejecucion continua correctamente")
finally: # aqui entras tanto si hay error como si no, siempre.
    print("La ejecucion continua")

# Capturamos las excepciones por tipo de excepcion

try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError as error: # se ejecuta solo si el error es TypeError
    # puedo ponerle una variable que capture la info del error
    print("Se ha producido un error TypeError")
    print(error)
except ValueError as error: # se ejecuta solo si el error es ValueError
    print("Se ha producido un error ValueError")
    print(error)
