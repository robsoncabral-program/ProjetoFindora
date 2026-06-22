from sqlalchemy.exc import IntegrityError
from models.usuario import Usuario

class UsuarioRepository:
    def __init__(self, session):
        self.session = session

    # 1. Atualizado para receber os 5 parâmetros enviados pelo main.py
    def adicionar(self, nome, idade, localizacao_vista, descricao):
        try:
            user = Usuario(
                nome=str(nome),
                idade=int(idade) if idade else None,
                localizacao_vista=str(localizacao_vista),
                descricao=str(descricao),
                status="Desaparecido"  # Todo cadastro começa como desaparecido
            )
            self.session.add(user)
            self.session.commit()
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            self.session.rollback()
            return False

    # 2. Mantido para listar todas as pessoas na base de dados
    def listar_todos(self):
        try:
            return self.session.query(Usuario).all()
        except Exception as e:
            print(f"Erro ao listar: {e}")
            return []

    # 3. Adicionado: Permite o filtro por localização (Opção 3 do main.py)
    def buscar_por_localizacao(self, localizacao):
        try:
            return self.session.query(Usuario).filter(
                Usuario.localizacao_vista.like(f"%{localizacao}%")
            ).all()
        except Exception as e:
            print(f"Erro ao buscar por localização: {e}")
            return []

    # 4. Adicionado/Modificado: Atualiza o Status para 'Encontrado' (Opção 4 do main.py)
    def atualizar_status(self, usuario_id, novo_status):
        try:
            user = self.session.query(Usuario).filter(Usuario.id == usuario_id).first()
            if user:
                user.status = novo_status
                self.session.commit()
                return True
            return False
        except Exception:
            self.session.rollback()
            return False

    # 5. Mantido/Ajustado: Elimina o registo definitivamente (Opção 5 do main.py)
    def remover(self, usuario_id):
        try:
            user = self.session.query(Usuario).filter(Usuario.id == usuario_id).first()
            if user:
                self.session.delete(user)
                self.session.commit()
                return True
            return False
        except Exception:
            self.session.rollback()
            return False