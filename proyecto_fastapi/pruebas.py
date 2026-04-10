import requests

BASE_URL = "http://127.0.0.1:8000"

# GET básico
def prueba_get():
    r = requests.get(BASE_URL + "/libros")
    print(r.json())
    print(r.status_code)

# ERROR 404
def prueba_error():
    r = requests.get(BASE_URL + "/libro-validado/99")
    
    if r.status_code == 404:
        detail = r.json()["detail"]
        print("ID:", detail["id"])
        print("Descripción:", detail["descripcion"])
    else:
        print(r.json())

# POST con params
def prueba_post_params():
    r = requests.post(
        BASE_URL + "/agregar-libro",
        params={"nombre_libro": "Nuevo Libro"}
    )
    print(r.json())
    print(r.status_code)

# POST con JSON
def prueba_post_json():
    r = requests.post(
        BASE_URL + "/libro-body",
        json={
            "nombre": "Libro JSON",
            "cantidad": 5
        }
    )
    print(r.json())
    print("status:", r.status_code)
    print("content-type:", r.headers.get("content-type"))
    print("text:", r.text)


# Ejecutar pruebas
prueba_get()
prueba_error()
prueba_post_params()
prueba_post_json()