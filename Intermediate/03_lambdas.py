
# Aprender su concepto, para que se usan ... 
# Una lambda es una función anónima que se puede definir en una sola línea. Lambda = funcion sin nombre

# Ejemplo de uso
sum_two_values = lambda first_value, second_value: first_value + second_value

print(sum_two_values(3,5)) # una variable que realmente es una función y le pasamos dos valores

# Ejemplo de uso 2
multiply_values = lambda first_value, second_value: first_value * second_value - 3

print(multiply_values(2,4))

# lambda dentro de una funcion, pero no como argumento
def sum_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_values(5)(3,5)) # (value)(first_value, second_value) es lo mismo que sum_values(5)(3,5)


