from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class CorreccionesNiveles(Base):
    __tablename__ = "correccionesNiveles"

    id_correccion = Column(Integer, primary_key=True, index=True, autoincrement=True)
    valor = Column(Integer, nullable=True)
    nivel = Column(Integer, nullable=True)
    tipo = Column(String(100), nullable=True)
    id_rack = Column(Integer, ForeignKey('racks.id_rack'), nullable=True)