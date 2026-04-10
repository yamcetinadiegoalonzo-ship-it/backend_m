import requests

#ejercicio 1

def alumnos():
    respuesta= requests.get("http://127.0.0.1:8000/alumnos/1")
    print(respuesta.json())

#alumnos()
#Ejercicio 2

def alumnos2():
    respuesta2 = requests.get("http://127.0.0.1:8000/alumnos2/1",
                            params={"bienvenida":False}
                             )
    print(respuesta2.json())

alumnos2()
def alumnos3():
    respuesta3= requests.get("http://127.0.0.1:8000/alumnos3/1",
                             params={"bienvenida":False},json={"materias":[1,2,3,4]}
                            )
    print(respuesta3.json())


alumnos3()

def persona():
    resp = requests.post(
        "http://127.0.0.1:8000/persona/1",
        params={"nombre":"Diego Yam"},
        json={
            "numeros":[7,1,4,0,2,9],
            "buscar":1

        }
    )
    print(resp.json())

persona()