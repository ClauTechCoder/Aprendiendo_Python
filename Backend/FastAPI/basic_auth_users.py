
# para autenticar users de manera muy basica esto

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool
    
class UserDb(User):
    passwprd: str

users_db = {
    "paco":{
        "username": "paco",
        "full_name": "Paco Lopez",
        "email": "paco@example.com",
        "disabled": False,
        "password": "123456"
    },
    "mercedes":{
        "username": "mercedes",
        "full_name": "Mercedes Martinez",
        "email": "mercedes@example.com",
        "disabled": True,
        "password": "654321"
    }
}
