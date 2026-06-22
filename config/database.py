import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Definição da senha original com o @ no final
senha_original = "Maranata1978@"

# 2. Codifica o '@' para um formato seguro (%40) que o SQLAlchemy entende
senha_segura = urllib.parse.quote_plus(senha_original)

# 3. Montagem da URL de conexão utilizando a senha mascarada
DB_URL = f"mysql+mysqlconnector://root:{senha_segura}@localhost/findora_db"

# Criação do motor e sessões do banco de dados
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()