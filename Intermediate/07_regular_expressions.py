
# Aprender sobre el manejo de las expresiones regulares, con todas las operaciones básicas que podamos usar.
# Las expresiones regulares son patrones de cadenas que se utilizan para buscar y manipular texto.

import re # importamos la libreria de expresiones regulares

my_string = "Esta es la leccion numero 7 -> \n Expresiones Regulares (esa es la Leccion)"
my_other_string = "Esta no es la leccion numero 6 -> Aprendiendo de Ficheros"

# MATCH

print(re.match("Esta es la leccion", my_string)) # encuentra la coincidencia exacta desde el principio de la cadena
print(re.match("Esta es la leccion", my_other_string)) 
print(re.match("Expresiones regulares", my_string)) # sale none porque no esta al principio de la cadena

match = re.match("Esta es la leccion", my_string, re.I) #busqueda sea insensible a mayúsculas y minusculas
print(match)

#Varias formas: not(match == None) |  match != None |  match is not None

if not(match == None): # si la coincidencia no es None, es decir, hay coincidencia
    start, end = match.span() # devuelve la posicion donde se encuentra la coincidencia en forma de rango
    print(my_string[start:end]) # imprime la parte de la cadena que coincide con la expresion regular

# SEARCH

search = re.search("leccion", my_string, re.I) # busca la coincidencia en cualquier parte de la cadena devuelve rango
print(search)

# FIND ALL

findall = re.findall("leccion", my_string, re.I) # busca todas las coincidencias en la cadena devuelve listado
print(findall) # hay mas de una coincidencia, entonces hay lista con [leccion, leccion]
 
 
# SPLIT

split = re.split("\n", my_string) # separa la cadena en subcadenas usando el separador que le hemos pasado
print(split) # nos sale la cadena separada que se ha dividido a partir del \n

#SUB

sub = re.sub("Expresiones Regulares", "RegEx", my_string)
sub = re.sub("Leccion|leccion", "LECCION", my_string) # cambio por uno u otro
print(sub) # nos sale la cadena con la expresion regular reemplazada 

# PATRONES MAS COMPLEJOS

pattern = r"[l|L]eccion|Expresiones" # patron que busca leccion Leccion o Expresiones
pattern2 = r"[a-z]" # patron que busca cualquier letra minuscula
pattern3 = r"[0-9]" # patron que busca cualquier numero
print(re.findall(pattern, my_string)) # si loo encuentra nos devuelve lista con ello

# Ejemplo: email regulation regular expression

email = "miemail@email.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email)) # si la coincidencia es None es que no es un email valido
print(re.search(pattern, email))
print(re.findall(pattern, email))
