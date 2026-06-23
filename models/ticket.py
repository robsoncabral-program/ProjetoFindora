from sqlalchemy import Column, Integer, String, ForeignKey
from config.database import Base

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(200))
    status = Column(String(50), default="Aberto")
    pessoa_id = Column(Integer, ForeignKey('usuarios.id'))
    tecnico_id = Column(Integer, ForeignKey('tecnicos.id'))