from config.database import engine, Base, Session
from repositories.usuario_repo import UsuarioRepository
from repositories.tecnico_repo import TecnicoRepository
from repositories.ticket_repo import TicketRepository
from models.usuario import Usuario
from models.tecnico import Tecnico
from models.ticket import Ticket
import logging

# Configuração de Logs para Auditoria
logging.basicConfig(filename='sistema.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

Base.metadata.create_all(engine)

def menu():
    session = Session()
    repo_usuario = UsuarioRepository(session)
    repo_tecnico = TecnicoRepository(session)
    repo_ticket = TicketRepository(session)
    
    usuario_logado = {"nome": "Robson", "perfil": "admin"} 
    print(f"\nSessão iniciada como: {usuario_logado['nome']} (Perfil: {usuario_logado['perfil']})")
    logging.info(f"Sistema iniciado por {usuario_logado['nome']}.")
    
    while True:
        print("\n--- FINDORA: Sistema de Busca de Pessoas ---")
        print("1. Listar | 2. Registar | 3. Buscar | 4. Marcar 'Encontrado'")
        print("5. Eliminar [ADMIN] | 6. Reg. Técnico [ADMIN] | 7. Abrir Ticket | 8. Listar Tickets | 0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        try:
            if opcao == "1":
                for p in repo_usuario.listar_todos():
                    print(f"ID: {p.id} | Nome: {p.nome} | Status: {p.status}")
            
            elif opcao == "2":
                nome = input("Nome: ")
                idade = input("Idade: ")
                local = input("Última localização: ")
                desc = input("Descrição física: ")
                repo_usuario.adicionar(nome, idade, local, desc)
                print("Registo efetuado!")
                logging.info(f"Novo registo adicionado: {nome}")
            
            elif opcao == "3":
                loc = input("Localização: ")
                for p in repo_usuario.buscar_por_localizacao(loc):
                    print(f"{p.nome} - Visto em: {p.localizacao_vista}")
            
            elif opcao == "4":
                id_p = int(input("ID da pessoa encontrada: "))
                repo_usuario.atualizar_status(id_p, "Encontrado")
                print("Status atualizado!")
                logging.info(f"Status atualizado para 'Encontrado' (ID: {id_p})")

            elif opcao == "5":
                if usuario_logado["perfil"] == "admin":
                    id_p = int(input("ID a eliminar: "))
                    repo_usuario.remover(id_p)
                    print("Registo eliminado.")
                    logging.warning(f"Administrador {usuario_logado['nome']} eliminou o registo ID: {id_p}")
                else:
                    print("ACESSO NEGADO!")
                    logging.warning("Tentativa de acesso não autorizado à exclusão de dados.")
                
            elif opcao == "6":
                if usuario_logado["perfil"] == "admin":
                    nome = input("Nome do Técnico: ")
                    espec = input("Especialidade: ")
                    repo_tecnico.adicionar_tecnico(nome, espec)
                    print("Técnico registado!")
                    logging.info(f"Novo técnico registado: {nome}")
                else:
                    print("ACESSO NEGADO!")
            
            elif opcao == "7":
                desc = input("Descrição do Ticket: ")
                p_id = input("ID da pessoa: ")
                t_id = input("ID do técnico: ")
                repo_ticket.criar_ticket(desc, p_id, t_id)
                print("Ticket aberto com sucesso!")
            
            elif opcao == "0":
                logging.info("Sistema encerrado.")
                break
        
        except Exception as e:
            print(f"Erro inesperado no sistema: {e}")
            logging.error(f"Erro detetado: {e}")

if __name__ == "__main__":
    menu()