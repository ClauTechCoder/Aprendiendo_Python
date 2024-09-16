
from fastapi import FastAPI
from pydantic import BaseModel #sirve para validar y crear modelos de datos fácilmente

app = FastAPI()

# Definimos entidad user 
class User(BaseModel): # ponemos ahi BaseModel para validar y crear 
    name: str
    email: str
    age: int
    
# imaginamos que esto es lo que tenemos en una BBDD (es ficticia)
users = [User() ]

# uvicorn users:app --reload -> este comando permite que el server se ejecute. Siempre es nombre_app:app

@app.get("/usersjson") # http://127.0.0.1:8000/usersjson para ver ahora esta nueva funcion el return 
async def usersjson():  
    #devuelve estructura en forma de json como se lo hemos puesto
    return [{"name": "pepe", "email": "pepe@correo.es", "age": 24},
            {"name": "ana", "email": "ana@correo.es", "age": 44},
            {"name": "luis", "email": "luis@correo.es", "age": 31},
            ]
    


