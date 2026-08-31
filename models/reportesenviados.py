from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class ReportesEnviados(Base):
    __tablename__ = "reportesEnviados"

    id_reporte = Column(Integer, primary_key=True, index=True, autoincrement=True)
    correo = Column(String(255), nullable=True)
    fecha_envio = Column(DateTime, nullable=True)
    estado = Column(Boolean, default=False)
    rol = Column(String(100), nullable=True)