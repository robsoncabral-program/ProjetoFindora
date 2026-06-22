from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from config.database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    
    # Adicionado para suportar a idade (Opção 2)
    idade = Column(Integer, nullable=True)
    
    # Adicionado para suportar a última localização vista (Opção 2 e Opção 3)
    localizacao_vista = Column(String(255), nullable=True)
    
    # Alterado para TEXT: Permite textos longos, números, símbolos e quebras de linha na descrição física
    descricao = Column(Text, nullable=True)
    
    # Status para controlar se foi encontrado (Opção 4) - Começa como 'Desaparecido'
    status = Column(String(50), default="Desaparecido")
    
    criado_em = Column(DateTime, default=datetime.utcnow)