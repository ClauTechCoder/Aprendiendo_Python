
# Aprender los principales, sus usos y estructura de los más comunes.
# Cuando necesito pasar por el mismo codigo varias veces.

# WHILE-- hay que pasarle una condicion

my_condition = 0

while my_condition < 10:
    print (my_condition)    
    my_condition += 2 # hay que modificar la condicion para no estar infinitamente en el bucle
else: #admite else pero no if ni elif
    print("mi condicion es mayor o igual a 10")   
    
while my_condition < 20: # empiezo a mezclar conceptos
    my_condition += 1
    if my_condition == 15:
        print("igual a 15")
    elif my_condition == 18:
        print("igual a 18")
        break # se detiene la ejecucion del bucle
    print(my_condition)

# FOR

my_list = [35, 24, 62, 52, 30, 30, 17]

# se repite tantas veces como elementos haya iterables, en este caso segun num elements de lista
for element in my_list: 
    print(element) # me salen todos los elementos en orden de la lista

my_set = {"Raul","Rodriguez", 25}
my_dict = {
    "Nombre":"Raul", 
    "Apellido":"Rodriguez", 
    "Edad:":25, 
    "Lenguajes":{"Python","Java","C","Ruby"}, 
    1:1.85
    }
for element in my_set:
    print(element) 
for element in my_dict:
    print(element) 