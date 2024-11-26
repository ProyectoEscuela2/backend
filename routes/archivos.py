# Esenciales
from fastapi import APIRouter, UploadFile, File, Form
# Complementos
from typing import Union
from datetime import datetime
# Personalizados
from services.archivos_services import read_archivos, read_archivo, create_archivo, update_archivo, delete_archivo


router = APIRouter()

# Obtener todos los archivos
@router.get("/archivos")
def leer_archivos():
    # Obtiene todos los registros de archivos
    archivos = read_archivos()

    return {"data": archivos}

# Obtener un archivo
@router.get("/archivos/{id_archivo}")
def leer_archivo(id_archivo: int):
    # Obtiene el registro de un archivo por su id
    archivo = read_archivo(id_archivo)
    
    return {"data": archivo}

# Agregar archivos
@router.post("/archivos")
async def crear_archivo(
    # Trabajamos con archivos (File), por lo cual debemos usar Form, ya que json no soporta Files 
    nombre: str = Form(...),
    descripcion: Union[str, None] = Form(None),
    activo: bool = Form(...),
    file: UploadFile = File(...)
):
    # Definimos la ubicación donde se guardan los archivos
    file_location = f"assets/archivos/{nombre.lower().replace(' ', '_')}.pdf"
    
    # 1. Se inserta el registro de un archivo en la base de datos
    archivo = create_archivo(( # Tuple ()
        nombre,
        descripcion,
        file_location,
        activo,
        str(datetime.now())
    ))

    # 2. Se guarda el archivo en la carpeta "assets"
    with open(file_location, "wb") as f: # "wb": Write + Binarie | Write permite sobrescribir archivos en caso de que existan. Por eso utilizamos write en vez de read
        content = await file.read() # Lee el contenido del archivo y lo guarda en content
        f.write(content) # Escribe el contenido en la carpeta "assets"

    # Retorna el archivo guardado
    return {"data": archivo}

# Modificar archivos
@router.put("/archivos/{id_archivo}")
def modificar_archivo(
    id_archivo: int,
    nombre: str = Form(...),
    descripcion: Union[str, None] = Form(None),
    activo: bool = Form(...)
):
    # Modifica el registro de un archivo por su id
    archivo = update_archivo(id_archivo, (nombre, descripcion, activo))
    # TODO: Hacer que se modifique también el nombre del archivo

    # Retorna el archivo modificado
    return {"data": archivo}

# Eliminar archivos
@router.delete("/archivos/{id_archivo}")
def eliminar_archivo(id_archivo: int):
    # Elimina el registro de un archivo por su id
    delete_archivo(id_archivo)
    # TODO: Hacer que se elimine también el archivo

    # Retorna "Not content" o "204"
    return {"Status": 204}
