from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class Torres(Base):
    __tablename__ = "torres"

    id_torre = Column(Integer, primary_key=True, index=True)
    nombre_torre = Column(String(100), nullable=True)
    niveles_torre = Column(Integer, nullable=True)
    filas_torre = Column(Integer, nullable=True)
    id_receta = Column(Integer, ForeignKey('recetas.id_receta'), nullable=True)
    correccion_busqueda = Column(Integer, nullable=True)
    correccion_guardado = Column(Integer, nullable=True)