
from fastapi import APIRouter

# el nombre router es como app el nombre es el que queramos
router = APIRouter(prefix="/products",
                   tags=["products"], # lo agrupoa por asi decirlo
                   responses={404:{"message": "Not Found"}}) 
# prefix para el nombre router y asi en metodos llamamos a / solo
# uvicorn products:app --reload si solo fuera este fichero mi aplicación

products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products_list(id: int):
    return products_list[id]
