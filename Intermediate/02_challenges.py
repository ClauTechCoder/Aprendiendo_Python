
# Resolucion de unos cuantos retos de codigo para poner en marcha todos los conocimientos dados.

"""
 Ejercicio 1: Programa muestre por consola numeros del 1 al 100 sustituyendo:
 - Los multiplos de 3 por "Fizz"   
 - Los multiplos de 5 por "Buzz"
 - Los multiplos de 3 y de 5 a la vez por "FizzBuzz"
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


"""
Ejercicio 2: Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def my_anagram_function(word1, word2):
    if (word1 == word2):
        return False
    else:
        return True    

print(my_anagram_function("roma", "Roma"))
