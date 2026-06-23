from sqlalchemy import Column, Integer, String
from config.database import Base

class Tecnico(Base):
    __tablename__ = 'tecnicos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    especialidade = Column(String(100))