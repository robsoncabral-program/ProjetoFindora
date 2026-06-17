from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from config.database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)