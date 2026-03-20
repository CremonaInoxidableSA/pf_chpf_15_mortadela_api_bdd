from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class DiccionarioCancelaciones(Base):
    __tablename__ = "diccionarioCancelaciones"

    id_cancelaciones = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(255), nullable=True)
