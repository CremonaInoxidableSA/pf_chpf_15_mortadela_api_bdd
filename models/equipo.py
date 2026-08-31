from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class Equipo(Base):
    __tablename__ = "equipo"

    id_equipo = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_equipo = Column(String(255), nullable=True)