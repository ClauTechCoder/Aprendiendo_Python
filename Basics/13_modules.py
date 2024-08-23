
# Algo parecido a las librerias. Codigo externo a nuetro fichero actual que queremos usar.
# Lugar donde tenemos codigo "almacenado" y lo usamos. Solucion a problemas relacionados
# objetivo es realizar operaciones muy concretas que nos puedan servir en varios sitios

# importo ese fichero para poder usar su contenido. No admite los numeros first
import my_module as my_module 
# importo una sola funcionalidad del fichero (o varias), llamamos sum() direct
from my_module import sumValue 
# importo un modulo existente de python
import math

# funcion que esta codificada en el fichero importado, hay que poner el module. si o si
my_module.sumValue(1,4,5) # llamada a funcion
my_module.printValue("Holiiiii") 

print(math.pi) # accedo a la variable pi del modulo existente de python  
print(math.pow(2, 8)) # 2 elevado a 8
