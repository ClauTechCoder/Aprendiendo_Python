
# Como gestionar los paquetes en Python. Usamos para ello la herramienta pip.

#pip es un package installer para Python.Desde consola podemos controlarlo.

import numpy
# numpy sirve para hacer cálculos numéricos

print(numpy.version.version) # Imprime la versión de numpy

numpy_array = numpy.array([35, 24, 65,83,24]) # Crea un array de numpy con los valores dados 
print(numpy_array) # y con ello puedo nhacer todas las operaciones validas de los arrays

import pandas 
# pandas es una librería para manejar datos estructurados de manera fácil y eficiente

import requests # requests sirve para hacer peticiones HTTP, a un api...

request = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151") # Ejemplo de cómo hacer una pet a una api
print(request)
print(request.status_code) # Imprime el código de estado HTTP de la respuesta
print(request.json()) # Imprime la respuesta en formato JSON

# Ahora con nuestro apquete propio de operaciones aritméticas -> arithmetics.py
# Tenemos que importar nuestro paquete para usar sus funciones

from mypackage import arithmetics # Importamos el módulo arithmetics para usar sus funciones

print(arithmetics.sumar(3, 5)) # Probamos la función sumar

