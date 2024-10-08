
# Tutorial de instalacion de FastApi  correctamente y ver que funcione bien

# PETICION GET ES LA QUE EL EXPLORADOR LEE POR DEFECTO.

from fastapi import FastAPI
from routers import products,users # importamos el fichero a usar
from fastapi.staticfiles import StaticFiles # para poder usar recursos estaticos

app = FastAPI()

# AHORA LO QUE HACEMOS ES LLAMAR A OTRAS CLASES DENTRO DEL MISMO .PY PARA PODER HACER 
# # uvicorn nombre_app:app --reload SOLO UNA
app.include_router(products.router) # lo incluyo en mi main, y ya pueod usar todo lo suyo
app.include_router(users.router) 
app.mount("/static", StaticFiles(directory="static"), name="static")


# Creamos una funcion que devuelve un mensaje de bienvenida

@app.get("/") # esta linea indica que la ruta raiz de nuestra API va a responder con este metodo
async def root(): #async sirve para que la ejecucion del codigo sea asincrona   
    return {"message": "Hello, FastAPI!"} # mensaje de bienvenida al usuario en formato JSON


@app.get("/url") # esta linea indica que la ruta /url va a responder con este metodo
async def url(): #async sirve para que la ejecucion del codigo sea asincrona   
    return {"url": "Estoy dentro de la url",
            "google": "https://google.com"} # mensaje de bienvenida al usuario en formato JSON


# uvicorn main:app --reload -> este comando permite que el server se ejecute en el puerto 8000 y que 
# se reinicie automaticamente cuando se modifique el codigo de la server 
# PS C:\Users\claud\Desktop\Aprendiendo_Python> uvicorn main:app --reload -> CON ESTO LEVANTO EL SERVER EN LOCAL
# INFO:     Will watch for changes in these directories: ['C:\\Users\\claud\\Desktop\\Aprendiendo_Python']
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit) -> SERVER LOCAL DONDE CON EL GET VEMOS EL MSG
# INFO:     Started reloader process [23316] using StatReload
# INFO:     Started server process [34008]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.
# INFO:     127.0.0.1:56192 - "GET / HTTP/1.1" 200 OK


# http://127.0.0.1:8000/docs -> AQUI TENEMOS NUESTRA DOCUMENTACION HECHA, ES AUTOMATICO
# http://127.0.0.1:8000/redoc -> TBN  ES DOCUMENTACION HECHA ESTE LINK EN OTRO ESTANDAR, SE PUEDE DESCARGAR SU JSON
# USANDO POSTMAN TBN LE PUEDO PASAR ESA DIRECCION CON UN GET Y ME DEVUELVE LO MISMO
# USANDO EXTENSION VSCODE THUNDER CLIENT LO TENGO SIN SALIR DEL PROGRAMA


