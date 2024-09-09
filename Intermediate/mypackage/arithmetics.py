
# Para lo de la simulacion y el hacer un pquete propio.
# Hacemos uno de operaciones aritméticas basicas

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError("No se puede dividir por cero")

