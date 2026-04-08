from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class NivelesCiclos(Base):
    __tablename__ = "nivelesCiclos"

    id_nivel = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_ciclo = Column(Integer, ForeignKey('ciclos.id_ciclo'), nullable=True)
    nivel = Column(Integer, nullable=True)
    finalizado = Column(Boolean, default=False)
    tiempo_nivel = Column(Integer, nullable=True) #En segundos
    cancelaciones = Column(JSON, nullable=True)
    seleccionado = Column(Boolean, default=False)