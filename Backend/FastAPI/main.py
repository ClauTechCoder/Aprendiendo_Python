
# Tutorial de instalacion de FastApi  correctamente y ver que funcione bien

from fastapi import FastAPI

app = FastAPI()

# Creamos una funcion que devuelve un mensaje de bienvenida

@app.get("/") # esta linea indica que la ruta raiz de nuestra API va a responder con este metodo
async def root(): #async sirve para que la ejecucion del codigo sea asincrona   
    return {"message": "Hello, FastAPI!"} # mensaje de bienvenida al usuario en formato JSON


@app.get("/url") # esta linea indica que la ruta /url va a responder con este metodo
async def url(): #async sirve para que la ejecucion del codigo sea asincrona   
    return {"message": "Estoy dentro de la url"} # mensaje de bienvenida al usuario en formato JSON


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
