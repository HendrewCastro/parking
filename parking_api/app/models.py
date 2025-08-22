from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from .database import Base
from datetime import datetime
#Descreve como ficam as tabelas do banco

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True, index=True)
    plate = Column(String, unique=True, index=True)
    entry_time = Column(DateTime, default=datetime.utcnow)
    exit_time = Column(DateTime, nullable=True)
    payment_amount = Column(Float, nullable=True)
    is_paid = Column(Boolean, default=False)
