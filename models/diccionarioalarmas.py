from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class DiccionarioAlarmas(Base):
    __tablename__ = "diccionarioAlarmas"

    id_diccionario_alarmas = Column(Integer, primary_key=True, index=True, autoincrement=True)
    descripcion = Column(String(255), nullable=True)
    id_equipo = Column(Integer, ForeignKey('equipo.id_equipo'), nullable=True)