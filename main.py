from config.database import engine, Base, Session
from repositories.usuario_repo import UsuarioRepository
from repositories.tecnico_repo import TecnicoRepository
from repositories.ticket_repo import TicketRepository
from models.usuario import Usuario
from models.tecnico import Tecnico
from models.ticket import Ticket
import logging

# Configuração de Logs
logging.basicConfig(filename='sistema.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

Base.metadata.create_all(engine)

def autenticar():
    """Função simples de autenticação para proteger o sistema"""
    print("\n--- LOGIN NECESSÁRIO ---")
    user = input("Utilizador: ")
    senha = input("Password: ")
    
    # Simulação de base de dados de utilizadores
    if user == "admin" and senha == "admin123":
        return {"nome": "Administrador", "perfil": "admin"}
    elif user == "tecnico" and senha == "tec123":
        return {"nome": "Técnico de Campo", "perfil": "tecnico"}
    else:
        print("\n[ERRO] Credenciais inválidas!")
        logging.warning(f"Tentativa de login falhada para o utilizador: {user}")
        return None

def menu(usuario_logado):
    session = Session()
    repo_usuario = UsuarioRepository(session)
    repo_tecnico = TecnicoRepository(session)
    repo_ticket = TicketRepository(session)
    
    print(f"\nBem-vindo, {usuario_logado['nome']} (Perfil: {usuario_logado['perfil']})")
    logging.info(f"Sistema iniciado por {usuario_logado['nome']}.")
    
    while True:
        print("\n--- FINDORA: Sistema de Busca ---")
        print("1. Listar | 2. Registar | 3. Buscar | 4. Marcar 'Encontrado'")
        print("5. Eliminar [ADMIN] | 6. Reg. Técnico [ADMIN] | 7. Abrir Ticket | 0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        try:
            # [Lógica das opções permanece igual à tua, mantendo os teus ifs]
            if opcao == "1":
                for p in repo_usuario.listar_todos():
                    print(f"ID: {p.id} | Nome: {p.nome} | Status: {p.status}")
            
            elif opcao == "5" or opcao == "6":
                # Proteção por perfil (RBAC)
                if usuario_logado["perfil"] == "admin":
                    if opcao == "5":
                        id_p = int(input("ID a eliminar: "))
                        repo_usuario.remover(id_p)
                        print("Registo eliminado.")
                        logging.warning(f"Admin {usuario_logado['nome']} eliminou registo ID: {id_p}")
                    else:
                        nome = input("Nome do Técnico: ")
                        espec = input("Especialidade: ")
                        repo_tecnico.adicionar_tecnico(nome, espec)
                        print("Técnico registado!")
                else:
                    print("ACESSO NEGADO: Apenas administradores podem realizar esta ação.")
                    logging.warning(f"Utilizador {usuario_logado['nome']} tentou acesso restrito.")
            
            elif opcao == "0":
                break
                
        except Exception as e:
            print(f"Erro: {e}")
            logging.error(f"Erro no menu: {e}")

if __name__ == "__main__":
    usuario = autenticar()
    if usuario:
        menu(usuario)
    else:
        print("Sistema encerrado por segurança.")