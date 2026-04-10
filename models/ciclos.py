from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class Ciclos(Base):
    __tablename__ = "ciclos"

    id_ciclo = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fecha_inicio = Column(DateTime, nullable=True)
    fecha_fin = Column(DateTime, nullable=True)
    id_receta = Column(Integer, ForeignKey('recetas.id_receta'), nullable=True)
    id_rack = Column(Integer, ForeignKey('racks.id_rack'), nullable=True)
    id_equipo = Column(Integer, ForeignKey('equipo.id_equipo'), nullable=True)
    id_estado = Column(Integer, ForeignKey('diccionarioEstados.id_estado'), nullable=True)
    tiempo_total = Column(Integer, nullable=True) #En segundos
    tiempo_pausa = Column(Integer, nullable=True) #En segundos
    tiempo_ciclo = Column(Integer, nullable=True) #En segundos
    activo = Column(Boolean, nullable=True)
    peso_procesado = Column(Integer, nullable=True) #En kg