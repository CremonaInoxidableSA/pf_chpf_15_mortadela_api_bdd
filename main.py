from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

from config import db
from config.sql_loader import cargar_datos_iniciales

from models.usuarios import Usuarios
from models.ciclos import Ciclos
from models.recetas import Recetas
from models.torres import Torres
from models.equipo import Equipo
from models.nivelesciclos import NivelesCiclos
from models.correccionesniveles import CorreccionesNiveles
from models.alarmas import Alarmas
from models.diccionarioalarmas import DiccionarioAlarmas
from models.diccionariocancelaciones import DiccionarioCancelaciones
from models.diccionarioestados import DiccionarioEstados
from models.reportesenviados import ReportesEnviados


load_dotenv()
# Crear la base de datos si no existe
with create_engine(f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}").connect() as connection:
    connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')}"))
    print(f"✓ Base de datos '{os.getenv('DB_NAME')}' verificada o creada exitosamente")

db.Base.metadata.drop_all(bind=db.engine)
db.Base.metadata.create_all(bind=db.engine)
cargar_datos_iniciales()

app = FastAPI(title="API Mortadela CORRECCIONES", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        f"http://{os.getenv('FRONTEND_IP')}:3000",
        "http://localhost:3000",
        "http://192.168.20.150:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    # Verificar estado de la base de datos
    try:
        with db.engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        estado_bdd = "Conectado"
    except Exception as e:
        estado_bdd = f"Desconectado - {str(e)}"
    
    return {
        "value": "API Mortadela CORRECCIONES", 
        "Estado BDD": estado_bdd,
        "version": "1.0.0"
    }