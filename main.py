from config.database import engine, Base, Session
from repositories.usuario_repo import UsuarioRepository

# Cria a base de dados se não existir
Base.metadata.create_all(engine)

def menu():
    repo = UsuarioRepository(Session())
    
    while True:
        print("\n--- FINDORA: Sistema de Busca de Pessoas ---")
        print("1. Listar todas as pessoas em busca")
        print("2. Registar nova pessoa desaparecida")
        print("3. Buscar por localização")
        print("4. Marcar como 'Encontrado'")
        print("5. Eliminar registo de pessoa")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            lista = repo.listar_todos()
            for p in lista:
                print(f"ID: {p.id} | Nome: {p.nome} | Status: {p.status} | Local: {p.localizacao_vista}")
        
        elif opcao == "2":
            nome = input("Nome: ")
            idade = input("Idade: ")
            local = input("Última localização: ")
            desc = input("Descrição física: ")
            if repo.adicionar(nome, idade, local, desc):
                print("Registo efetuado com sucesso!")
            else:
                print("Erro ao registar.")
        
        elif opcao == "3":
            loc = input("Digite a localização para filtrar: ")
            lista = repo.buscar_por_localizacao(loc)
            for p in lista:
                print(f"{p.nome} - Visto em: {p.localizacao_vista}")
        
        elif opcao == "4":
            id_p = int(input("ID da pessoa que foi encontrada: "))
            if repo.atualizar_status(id_p, "Encontrado"):
                print("Status atualizado!")
            else:
                print("Pessoa não encontrada.")

        elif opcao == "5":
            id_p = int(input("Digite o ID da pessoa que deseja eliminar: "))
            if repo.remover(id_p):
                print("Registo eliminado com sucesso!")
            else:
                print("Erro: ID não encontrado ou falha ao eliminar.")
                
        elif opcao == "0":
            break

if __name__ == "__main__":
    menu()