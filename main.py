# Esenciales
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
# Complementos
import os
from dotenv import load_dotenv
# Routers
from routes.archivos import router as archivos_router
from routes.login import router as login_router
from routes.imagenes import router as imagenes_router

load_dotenv()

app = FastAPI()

# Permite la conexión CORS, es decir, hacer llamadas a otros origins
origins = [
    "http://localhost:3000", # Next
    "http://localhost:5173", # Vite
    "https://eest2sn.edu.ar", # EEST2SN
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# Servir archivos e imagenes estáticas
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# ADMIN: Login
# Registra el login_router
app.include_router(login_router)

# ADMIN: ARCHIVOS
# Verifica si la carpeta "assets" existe, sino la crea
os.makedirs("assets", exist_ok=True) # (Es por las dudas)

# Registra el archivos_router
app.include_router(archivos_router)

# ADMIN: IMAGENES
# Verifica si la carpeta "assets" existe, sino la crea
os.makedirs("assets", exist_ok=True) # (Es por las dudas)

# Registra el imagenes_router
app.include_router(imagenes_router)
