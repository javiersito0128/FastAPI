from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get ("/calculadora") # Metodo para crear un parametro de ruta de tipo GET
# Creacion de la funcion la cual servira en este path
def calcular (operando_1 : float, operando_2: float):
    return {'suma': operando_1 + operando_2}
