from sqlalchemy.exc import IntegrityError
from models.usuario import Usuario

class UsuarioRepository:
    def __init__(self, session):
        self.session = session

    def adicionar(self, nome, email):
        try:
            user = Usuario(nome=nome, email=email)
            self.session.add(user)
            self.session.commit()
            return True
        except IntegrityError:
            self.session.rollback()  # Cancela a operação se der erro (ex: email duplicado)
            return False

    def listar_todos(self):
        try:
            return self.session.query(Usuario).all()
        except Exception as e:
            print(f"Erro ao listar: {e}")
            return []

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

    def atualizar_email(self, usuario_id, novo_email):
        try:
            user = self.session.query(Usuario).filter(Usuario.id == usuario_id).first()
            if user:
                user.email = novo_email
                self.session.commit()
                return True
            return False
        except IntegrityError:
            self.session.rollback()
            return False