from fastapi import APIRouter, HTTPException
from models.loginRequest_model import LoginRequest
from services.login_services import read_hash
from bcrypt import checkpw

router = APIRouter()

@router.post("/login")
async def login(request: LoginRequest):
    # Obtener hash almacenado
    hash_almacenado = read_hash()

    # Compara la contraseña con el hash almacenado
    if checkpw(request.password.encode("utf-8"), hash_almacenado.encode("utf-8")):
        return {"success": True}
    else:
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")
