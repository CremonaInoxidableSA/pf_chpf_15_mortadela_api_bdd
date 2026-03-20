from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class Recetas(Base):
    __tablename__ = "recetas"

    id_receta = Column(Integer, primary_key=True, index=True)
    codigo_producto = Column(String(100), nullable=True)
    peso_producto = Column(Integer, nullable=True)
    tipo_corte = Column(Integer, nullable=True)
    alto_producto = Column(Integer, nullable=True)
    largo_producto = Column(Integer, nullable=True)
    ancho_producto = Column(Integer, nullable=True)
    productos_fila = Column(Integer, nullable=True)
    productos_columna = Column(Integer, nullable=True)