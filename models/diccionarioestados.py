from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class DiccionarioEstados(Base):
    __tablename__ = "diccionarioEstados"

    id_estado = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(255), nullable=True)