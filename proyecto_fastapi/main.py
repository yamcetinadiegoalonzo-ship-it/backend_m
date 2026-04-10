from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

# "Base de datos" simulada
libros_db = {
    0: "El principito",
    1: "Cien años de soledad",
    2: "Don Quijote"
}

# 1️⃣ Endpoint GET básico
@app.get("/libros")
def obtener_libros():
    return {"mensaje": "Lista de libros disponible", "data": libros_db}


# 2️⃣ Endpoint con parámetro de ruta
@app.get("/libro/{id_libro}")
def obtener_libro(id_libro: int):
    return {"id": id_libro, "libro": libros_db[id_libro]}


# 3️⃣ Endpoint con validación 404
@app.get("/libro-validado/{id_libro}")
def obtener_libro_validado(id_libro: int):
    if id_libro in libros_db:
        return {"id": id_libro, "libro": libros_db[id_libro]}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "id": id_libro,
                "descripcion": "Libro no encontrado",
                "sugerencia": "Verifica el ID ingresado"
            }
        )


# 4️⃣ POST con parámetro simple
@app.post("/agregar-libro")
def agregar_libro(nombre_libro: str):
    nuevo_id = len(libros_db)
    libros_db[nuevo_id] = nombre_libro
    return {
        "mensaje": "Libro agregado correctamente",
        "id": nuevo_id,
        "nombre": nombre_libro
    }


# 5️⃣ Modelo con Pydantic
class LibroRespuesta(BaseModel):
    id: int
    nombre: str


# 6️⃣ POST con response_model
@app.post("/crear-libro", response_model=LibroRespuesta, status_code=status.HTTP_201_CREATED)
def crear_libro(nombre: str):
    nuevo_id = len(libros_db)
    libros_db[nuevo_id] = nombre
    return {"id": nuevo_id, "nombre": nombre}


# 7️⃣ Modelo con validaciones
class LibroValidado(BaseModel):
    id: int = Field(ge=0)
    nombre: str = Field(min_length=3)


# 8️⃣ Modelo para recibir datos
class LibroEntrada(BaseModel):
    nombre: str
    cantidad: int = Field(gt=0)


# 9️⃣ POST con body JSON
@app.post("/libro-body", response_model=LibroValidado, status_code=status.HTTP_201_CREATED)
def crear_desde_body(libro: LibroEntrada):
    nuevo_id = len(libros_db)
    libros_db[nuevo_id] = libro.nombre
    return {
        "id": nuevo_id,
        "nombre": libro.nombre
    }