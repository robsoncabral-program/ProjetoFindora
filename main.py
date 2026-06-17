import urllib.parse
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

# --- CONFIGURAÇÃO DA SENHA ---
# O quote_plus garante que o '@' não quebre a conexão
minha_senha = "Maranata1978@"
senha_segura = urllib.parse.quote_plus(minha_senha)

# --- CONEXÃO COM O MYSQL ---
# Substitui 'root' se usares outro utilizador, e 'findora_db' pelo nome da tua base
DB_URL = f"mysql+mysqlconnector://root:{senha_segura}@localhost/findora_db"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# --- MODELO DE DADOS ---
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)

# Cria as tabelas automaticamente
Base.metadata.create_all(engine)

# --- REPOSITÓRIO (Lógica) ---
class UsuarioRepository:
    def __init__(self, session):
        self.session = session

    def adicionar(self, nome, email):
        user = Usuario(nome=nome, email=email)
        self.session.add(user)
        self.session.commit()

    def listar_todos(self):
        return self.session.query(Usuario).all()

# --- INTERFACE CLI (Menu) ---
def main():
    session = Session()
    repo = UsuarioRepository(session)
    
    while True:
        print("\n--- FINDORA CLI ---")
        print("1. Listar Usuários | 2. Adicionar Usuário | 0. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            usuarios = repo.listar_todos()
            for u in usuarios:
                print(f"ID: {u.id} | Nome: {u.nome} | Email: {u.email}")
        elif opcao == "2":
            n = input("Nome: ")
            e = input("Email: ")
            repo.adicionar(n, e)
            print("Usuário adicionado com sucesso!")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()