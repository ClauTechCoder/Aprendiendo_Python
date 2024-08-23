
# Aprender las principales estructuras y todo lo básico y necesario.

class MyPerson: # asi de simple se define una clase. Las unicas que empiezan por mayuscula
    # pass -> como es clase vacia se pone esto apra que no de error y s epueda ejecutar fichero
    
    
    
    #construtor vacio usando el def,init y solo self.   + parametros ya no está vacio.
    # puedes no pasar propiedades en (self,...) si luego hacemos dentro self.
    # propiedad por defecto s epone como en la declaracion de alias
    # todas estas propiedades se pueden modificar y convertir en int por ej en un futuro
    def __init__(self, name, surname,alias ="Sin alias") -> None: 
        self.name = name # ya estamos asignado las propiedades con el nombre del constructor
        self.___surname = surname # ___ es propiedad privada
        self.alias = alias
        self.full_name = f"{name} {surname} ({alias})" # es valida perfectamente esta propiedad
    
    def walk(self): 
        # asi defino metodos/funciones de clase,pongo self y accedo a todo lo guardado en self
        print(f"Esta caminando...{self.full_name}")
    
    def getName(self): # puedo acceder al nombre pero no modificarlo, es como un getter
        return self.name
        
    
my_person = MyPerson("Pepe","Lopez", "Pepito")
print(f"{my_person.name} {my_person.surname}") # llamada a propiedades de la clase
print(my_person.full_name)
print(my_person.walk())

my_person.full_name = 35 # puedo convertirlo a otra cosa y no falla
print(my_person.full_name)
    



