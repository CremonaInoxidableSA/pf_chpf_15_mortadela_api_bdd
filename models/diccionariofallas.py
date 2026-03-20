from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class DiccionarioFallas(Base):
    __tablename__ = "diccionarioFallas"

    id_diccionario_fallas = Column(Integer, primary_key=True, index=True, autoincrement=True)
    descripcion = Column(String(255), nullable=True)