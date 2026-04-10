# Codigos de respuesta 

from fastapi import FastAPI,Body,Query

app=FastAPI()

# Ejercicio 1

@app.get("/alumnos/{id}")
def alumnos_wrapper(id:str):
    return{"id":id}

# Ejercicio 2

@app.get("/alumnos2/{id}")
def alumnos2_wrapper(id:str, bienvenida:bool):
    return{"id":id, "bienvenida":bienvenida}
#ejercicio 3
@app.get("/alumnos3/{id}")

def alumnos3_wrapper(id:str,bienvenida:bool,materias:list=Body(embed=True)):
    return{"id":id,"bienvenida":bienvenida,"materias":materias}


@app.post("/persona/{id}")
def persona_wrapper(
    id:str,
    nombre:str,
    datos:dict=Body()
):
    lista_ordenada = sorted(datos["numeros"])
    veces = datos["numeros"].count(datos["buscar"])
    nombre_pila = nombre.split(" ")[0]

    return {
        "lista_ordenada": lista_ordenada,
        "veces": veces,
        "nombre_pila": nombre_pila,
        "id": id
    }