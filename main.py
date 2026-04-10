# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/tarea-0")
# def tarea_0():
#     return {"respuesta": "Primer tarea realizada"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}

@app.get("/tarea-0")
def tarea_0():
    return {"respuesta": "Primer tarea realizada"}