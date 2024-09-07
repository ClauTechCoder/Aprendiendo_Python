
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
    'la clave es ordenar alfabeticamente las palabras y ya ahi comparas si son anagramas'
    return sorted(word1.lower()) == sorted(word2.lower())

print(my_anagram_function("Amor", "Roma"))


"""
Ejercicio 3: Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def my_fibonacci_function():
    prev = 0;
    next = 1;
    for index in range(0,51):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

my_fibonacci_function()


"""
Ejercicio 4: Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def my_number_is_prime():
    for n in range(1,101):
        if n >= 2:
            is_divisible = False
            for i in range(2, n):
                if (n % i) == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(n)
    

my_number_is_prime()
        

"""
Ejercicio 5: Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse_string(input_string):
    text_length = len(input_string)
    reverse_string = ""
    for i in range(0, text_length):
        reverse_string += input_string[text_length - i - 1]
    return reverse_string
    

print(reverse_string("Hola mundo"))
