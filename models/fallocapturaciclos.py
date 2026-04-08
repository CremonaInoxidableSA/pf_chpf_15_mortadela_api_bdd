from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class FalloCapturaCiclos(Base):
    __tablename__ = "falloCapturaCiclos"

    id_fallo = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fecha = Column(DateTime, nullable=False)