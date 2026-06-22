from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Substitui pela tua password se necessário
DB_URL = "mysql+mysqlconnector://root:Maranata1978@localhost/findora_db"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()