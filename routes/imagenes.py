# Esenciales
from fastapi import APIRouter, File, UploadFile, Form
# Complementos
from datetime import datetime
# Personalizados
from services.imagenes_services import read_imagenes, read_imagen, create_imagen, update_imagen, delete_imagen

router = APIRouter()

# Obtener todas las imagenes
@router.get("/imagenes")
def leer_imagenes():
    imagenes = read_imagenes()

    return {"data": imagenes}

# Obtener una imagen
@router.get("/imagenes/{id_imagen}")
def leer_imagen(id_imagen: int):
    imagen = read_imagen(id_imagen)

    return {"data": imagen}

# Agregar una imagen
@router.post("/imagenes")
async def crear_imagen(
    nombre: str = Form(...),
    alt: str = Form(...),
    categoria_id: int = Form(...),
    file: UploadFile = File(...)
):
    file_location = f'assets/imagenes/{nombre.lower().replace(" ", "_")}.webp'

    imagen = create_imagen((
        nombre,
        alt,
        categoria_id,
        file_location,
        str(datetime.now())
    ))

    # TODO: Convertir las imagenes a webp desde acá, para facilitar al usuario la carga de imagenes en cualquier formato (jpg, png, etc)
    with open(file_location, "wb") as f:
        content = await file.read()
        f.write(content)
    
    return {"data": imagen}

# Modificar una imagen
@router.put("/imagenes/{id_imagen}")
# TODO: Chequear si se puede reemplazar todo este mamarracho por un model
def modificar_archivo(
    id_imagen: int,
    nombre: str = Form(...),
    alt: str = Form(...),
    categoria_id: int = Form(...)
):
    # Modifica el registro de una imagen por su id
    imagen = update_imagen(id_imagen, (nombre, alt, categoria_id))
    # TODO: Hacer que se modifique también el nombre de la imagen (archivo)

    # Retorna el archivo modificado
    return {"data": imagen}

# Eliminar una imagen
@router.delete("/imagenes/{id_imagen}")
def eliminar_archivo(id_imagen: int):
    # Elimina el registro de una imagen por su id
    delete_imagen(id_imagen)
    # TODO: Hacer que se elimine también el archivo de la imagen

    # Retorna "Not content" o "204"
    return {"Status": 204}
