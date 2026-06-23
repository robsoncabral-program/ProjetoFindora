from config.database import engine, Base, Session
from repositories.usuario_repo import UsuarioRepository
from repositories.tecnico_repo import TecnicoRepository
from repositories.ticket_repo import TicketRepository

# Importar modelos para que o SQLAlchemy os reconheça
from models.usuario import Usuario
from models.tecnico import Tecnico
from models.ticket import Ticket

# Cria todas as tabelas no MySQL (incluindo as novas)
Base.metadata.create_all(engine)

def menu():
    session = Session()
    repo_usuario = UsuarioRepository(session)
    repo_tecnico = TecnicoRepository(session)
    repo_ticket = TicketRepository(session)
    
    while True:
        print("\n--- FINDORA: Sistema de Busca de Pessoas ---")
        print("1. Listar pessoas | 2. Registar pessoa")
        print("3. Buscar local | 4. Marcar 'Encontrado' | 5. Eliminar pessoa")
        print("6. Registar Técnico | 7. Abrir Ticket de Busca | 8. Listar Tickets")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
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
        
        elif opcao == "3":
            loc = input("Localização: ")
            for p in repo_usuario.buscar_por_localizacao(loc):
                print(f"{p.nome} - Visto em: {p.localizacao_vista}")
        
        elif opcao == "4":
            id_p = int(input("ID da pessoa encontrada: "))
            repo_usuario.atualizar_status(id_p, "Encontrado")
            print("Status atualizado!")

        elif opcao == "5":
            id_p = int(input("ID a eliminar: "))
            repo_usuario.remover(id_p)
            print("Registo eliminado.")
            
        elif opcao == "6":
            nome = input("Nome do Técnico: ")
            espec = input("Especialidade: ")
            repo_tecnico.adicionar_tecnico(nome, espec)
            print("Técnico registado!")

        elif opcao == "7":
            desc = input("Descrição do Ticket: ")
            p_id = input("ID da pessoa: ")
            t_id = input("ID do técnico responsável: ")
            repo_ticket.criar_ticket(desc, p_id, t_id)
            print("Ticket aberto com sucesso!")

        elif opcao == "8":
            for t in repo_ticket.listar_tickets():
                print(f"Ticket ID: {t.id} | Desc: {t.descricao} | Status: {t.status} | Pessoa: {t.pessoa_id} | Tec: {t.tecnico_id}")
                
        elif opcao == "0":
            break

if __name__ == "__main__":
    menu()