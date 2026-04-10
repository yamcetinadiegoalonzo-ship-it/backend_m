from fastapi import FastAPI, Query,Body
from pydantic import BaseModel

app=FastAPI()
#@app.get("/Pet1")

#def pet1_wrapper(edad:int):
 #   return{"edad":edad}

#@app.get("/pet_2")
#def Pet_2_wrapper(edad:int,estado:str,estudiante:bool):
 #   return{"edad":edad,"estado":estado,"estudiante":estudiante}
#@app.get("/pet_3")
#def Pet_2_wrapper(edad:int,estado:str,estudiante:bool=True):
 #   return{"edad":edad,"estado":estado,"estudiante":estudiante}


#@app.get("/pet_4")
#def Pet_4_wrapper(estado:str,edad:int=Query(gt=0),estudiante:bool=True):
#    return{"edad":edad,"estado":estado,"estudiante":estudiante}

# @app.post("/body_1")
# def body_1_wrapper(edad:int=Body(gt=0),nombre:str=Body()):
#     return {"edad":edad,"nombre":nombre}
# @app.post("/body_2")
# def body_2_wrapper(edad:int=Body(embed=True, gt=0)):
#     return{"edad":edad}


class Estudiante(BaseModel):
    edad:int
    nombre:str

@app.post("/body_3")
def body_3_wrapper(estudiante:Estudiante):
    return{"edad":estudiante.edad,"nombre":estudiante.nombre}


@app.get("/alumno/{id_alumno}")
def alumno_wrapper(id_alumno:int, bienvenida:bool):
    if bienvenida:
        return {
            "id_alumno": id_alumno,
            "mensaje": "Bienvenido alumno"
        }
    else:
        return {
            "id_alumno": id_alumno,
            "mensaje": "Alumno sin mensaje de bienvenida"
        }