from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class Alarmas(Base):
    __tablename__ = "alarmas"

    id_alarma = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_diccionario_alarmas = Column(Integer, ForeignKey('diccionarioAlarmas.id_diccionario_alarmas'), nullable=True)
    fecha = Column(DateTime, nullable=True)