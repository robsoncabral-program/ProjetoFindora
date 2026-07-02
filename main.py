from config.database import engine, Base, Session
from repositories.usuario_repo import UsuarioRepository
from repositories.tecnico_repo import TecnicoRepository
from repositories.ticket_repo import TicketRepository
import logging

# Configuração de Logs
logging.basicConfig(filename='sistema.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

Base.metadata.create_all(engine)

def autenticar():
    print("\n--- LOGIN NECESSÁRIO ---")
    user = input("Utilizador: ")
    senha = input("Password: ")
    if user == "admin" and senha == "admin123":
        return {"nome": "Administrador", "perfil": "admin"}
    elif user == "tecnico" and senha == "tec123":
        return {"nome": "Técnico de Campo", "perfil": "tecnico"}
    return None

def menu(usuario_logado):
    session = Session()
    repo_usuario = UsuarioRepository(session)
    repo_tecnico = TecnicoRepository(session)
    repo_ticket = TicketRepository(session)
    
    print(f"\nBem-vindo, {usuario_logado['nome']} ({usuario_logado['perfil']})")
    
    while True:
        print("\n--- FINDORA: Sistema de Busca ---")
        print("1. Listar | 2. Registar Pessoa | 3. Buscar | 4. 'Encontrado'")
        print("5. Eliminar [ADM] | 6. Reg. Técnico [ADM] | 8. Listar Tickets | 0. Sair")
        
        opcao = input("Escolha: ")
        
        try:
            if opcao == "1":
                for p in repo_usuario.listar_todos():
                    print(f"ID: {p.id} | Nome: {p.nome} | Status: {p.status}")
            
            elif opcao == "2":
                nome = input("Nome: ")
                idade = input("Idade: ")
                local = input("Última localização: ")
                desc = input("Descrição: ")
                # Regista o utilizador
                nova_pessoa = repo_usuario.adicionar(nome, idade, local, desc)
                
                # AUTOMAÇÃO: O sistema assume a criação do ticket e o takeover
                # Vamos chamar uma função automática no repo_ticket (que criaremos a seguir)
                tecnico_responsavel = repo_ticket.criar_ticket_automatico(nova_pessoa.id)
                
                print(f"Registo efetuado com sucesso!")
                print(f"SISTEMA: Ticket de busca gerado. Técnico '{tecnico_responsavel.nome}' assumiu o caso automaticamente.")
                logging.info(f"Automação: Pessoa {nome} registada. Ticket atribuído a {tecnico_responsavel.nome}.")

            elif opcao == "8":
                for t in repo_ticket.listar_todos():
                    print(f"Ticket ID: {t.id} | Pessoa: {t.pessoa_id} | Técnico: {t.tecnico_id} | Status: {t.status}")

            elif opcao == "5" or opcao == "6":
                if usuario_logado["perfil"] == "admin":
                    # ... (mantém a tua lógica de eliminar/registar técnico aqui)
                    pass
                else:
                    print("ACESSO NEGADO.")
            
            elif opcao == "0": break
                
        except Exception as e:
            print(f"Erro: {e}")
            logging.error(f"Erro no menu: {e}")

if __name__ == "__main__":
    usuario = autenticar()
    if usuario: menu(usuario)