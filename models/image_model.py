from pydantic import BaseModel

# Datos que ingresa el usuario
class Imagen(BaseModel):
    nombre: str
    alt: str
    categoria_id: int

