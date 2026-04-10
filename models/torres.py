from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class Racks(Base):
    __tablename__ = "racks"

    id_rack = Column(Integer, primary_key=True, index=True)
    nombre_rack = Column(String(100), nullable=True)
    niveles_rack = Column(Integer, nullable=True)
    filas_rack = Column(Integer, nullable=True)
    id_receta = Column(Integer, ForeignKey('recetas.id_receta'), nullable=True)
    correccion_busqueda = Column(Integer, nullable=True)
    correccion_guardado = Column(Integer, nullable=True)