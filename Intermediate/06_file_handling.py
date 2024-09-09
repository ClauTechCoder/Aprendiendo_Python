
# Aprender el manejo de ficheros, con todas las operaciones básicas que podamos usar.

# TXT FILE

import os
# Abrir fichero
txt_file = open("Intermediate/my_file.txt", "r+") # leer y escribir. Si no existe el fichero lo crea
# print(txt_file.read()) # lee el contenido del fichero, si le pasamos un int me lee x caracteres
print(txt_file.readline()) # lee una linea del fichero
print(txt_file.readlines()) # lee todas las lineas del fichero y las devuelve en una lista

txt_file.write("\nEsto es una nueva linea") # escribo en el fichero, \n es salto de linea

txt_file.close() # cierro el fichero

#eliminar el fichero -> os.remove("Intermediate/my_file.txt")

#JSON FILE
import json # para poder trabajr con json adecuadamente

json_file = open("Intermediate/my_file.json", "w+")  # escribir y leer el fichero json, lo crea si no existe

json_test = {
    "name":"Raul", 
    "surname":"Rodriguez", 
    "Age:":25, 
    "Languages":"Python",
    "website":"https://www.example.com"
    }

json.dump(json_test,json_file,indent=2) # el indent=2 es para que el json sea más legible, son los espacios delante

json_file.close() # cierro el fichero

# hay que cerrar reviamente el fichero apra poder relizar esta operacion de lectura
with open("Intermediate/my_file.json") as file:
    for line in file.readlines():
        print(line)
        

#DE JSON A DICT
json_dict = json.load(open("Intermediate/my_file.json")) # carga el json y lo convierte en un diccionario
print(json_dict) # ahora tenemos el json guardado en un diccionario y se ve perfectamente


# CSV FILE

import csv # para trabajar con csv

csv_file = open("Intermediate/my_file.csv", "w") # abro el fichero csv para escribir

csv_writer = csv.writer(csv_file) # creo un writer para escribir en csv

csv_writer.writerow(["name", "surname", "Age", "Languages", "website"]) # escribo las cabeceras del csv (las columnas)
csv_writer.writerow(["Raul", "Rodriguez", 25, "Python","https://www.example.com"]) # escribo las filas del csv
csv_writer.writerow(["Roswell", "", 2, "COBOL",""]) # escribo las filas del csv

csv_file.close() # cierro el fichero

with open("Intermediate/my_file.csv") as file: # veo en la terminal los datos del csv
    for line in file.readlines():
        print(line)
   

# XLSX FILE

# XML FILE