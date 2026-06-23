from models.tecnico import Tecnico

class TecnicoRepository:
    def __init__(self, session):
        self.session = session

    def adicionar_tecnico(self, nome, especialidade):
        novo_tec = Tecnico(nome=nome, especialidade=especialidade)
        self.session.add(novo_tec)
        self.session.commit()
        return True