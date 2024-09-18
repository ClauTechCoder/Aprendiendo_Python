
from fastapi import APIRouter, HTTPException 
from pydantic import BaseModel #sirve para validar y crear modelos de datos fácilmente

router = APIRouter() # para poder usarlo bien en el main

# Definimos entidad user 
class User(BaseModel): # ponemos ahi BaseModel para validar y crear 
    name: str
    email: str
    age: int
class UserId(BaseModel): # ponemos ahi BaseModel para validar y crear 
    id: int
    name: str
    email: str
    age: int
     
# imaginamos que esto es lo que tenemos en una BBDD (es ficticia)

users_list = [User(name="pepe",email="pepe@correo.es",age= 24),
         User(name="ana",email="ana@correo.es",age= 44),
         User(name="luis",email="luis@correo.es",age= 31)]

users_list_id = [UserId(id=1,name="pepe",email="pepe@correo.es",age= 24),
         UserId(id=2,name="ana",email="ana@correo.es",age= 44),
         UserId(id=3,name="luis",email="luis@correo.es",age= 31)]

# uvicorn users:app --reload -> este comando permite que el server se ejecute. Siempre es nombre_app:app

@router.get("/usersjson") # http://127.0.0.1:8000/usersjson para ver ahora esta nueva funcion el return 
async def usersjson():  
    #devuelve estructura en forma de json como se lo hemos puesto
    return [{"name": "pepe", "email": "pepe@correo.es", "age": 24},
            {"name": "ana", "email": "ana@correo.es", "age": 44},
            {"name": "luis", "email": "luis@correo.es", "age": 31},
            ]
    
@router.get("/users") # http://127.0.0.1:8000/users para ver ahora esta nueva funcion el return
async def users():
    return users_list

@router.get("/userswithid") # http://127.0.0.1:8000/users para ver ahora esta nueva funcion el return
async def userswithid():
    return users_list_id

@router.get("/usersid/{id}") # ahora vamos a psar parametros en la ruta  http://127.0.0.1:8000/users/paranetro
async def usersid(id:int): # encontramos el user a apartir del parametro de la path
    return search_user(id)
    
# llamar por query es que podemos empezar a igualar una clave a un valor dentro de la url.  ? en 1º parametro
# http://127.0.0.1:8000/userquery/?id=1 --> y me retorna el user 1
# http://127.0.0.1:8000/userquery/?id=1&name=pepe --> y me retorna el user 1

@router.get("/userquery/")
async def usersid(id:int): # encontramos el user a apartir del parametro de la path
    return search_user(id)
    

# HACEMOS UN POST -> vamos a añdir un nuevo user a nuestra BBDDs ficticia
@router.post("/userquery/",response_model= UserId, status_code=201) 
# tengo respuesta que me sale por defecto 201 y un response_model 
async def userpost(adduser:UserId): # cojo el de id porque lo quiero lo mas completo posibles
    if type(search_user(adduser.id)) == UserId:
        raise HTTPException(status_code=404, detail= "User already exists") # excepcion si ya existe
    
    users_list_id.append(adduser)
    return adduser


# HACEMOS UN PUT
@router.put("/userswithid") # vamos a actualizar los datos de un user en nuetra BBDD
async def userput(user: UserId):
    found = False
    for index, saved_user in enumerate(users_list_id):
        if saved_user.id == user.id:
            users_list_id[index] = user # actualizamos la info aqui
            found = True
    if not found:
        return {"error": "User not found"} # si el user no existe en la lista me salta este mensaje
    else:
        return user

# HACEMOS UN DELETE
@router.delete("/usersid/{id}") # vamos a eliminar un user en nuetra BBDD
async def userdelete(id:int):
    found = False
    for index, saved_user in enumerate(users_list_id):
        if saved_user.id == id:
            del users_list_id[index] # eliminamos user al encotnrarlo por su id 
            found = True
    if not found:
        return {"error": "User not found"} # si el user no existe en la lista me salta este mensaje
    
    

# busco user por id funcion
def search_user(id:int):
    # tenemos funcion de orden superior
    my_user = filter(lambda user: user.id == id,users_list_id)
    try:
        return list(my_user)[0] # accedemos al elemento de la lista que coincida con eso
    except:
        return {"error": "User not found"} # si el id no existe en la listra me salta este mensaje
    

