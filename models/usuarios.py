from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(100), nullable=True)
    usuario = Column(String(100), nullable=True, unique=True, index=True)
    nombre = Column(String(100), nullable=True)
    apellido = Column(String(100), nullable=True)
    rol = Column(String(100), nullable=True)
    password_hash = Column(String(255), nullable=True)
    habilitado = Column(Boolean, default=False)
    reporte = Column(Boolean, default=False)
    ultimo_envio = Column(DateTime, nullable=True)