from models.ticket import Ticket
from models.tecnico import Tecnico

class TicketRepository:
    def __init__(self, session):
        self.session = session

    def criar_ticket(self, descricao, pessoa_id, tecnico_id):
        novo_ticket = Ticket(descricao=descricao, pessoa_id=pessoa_id, tecnico_id=tecnico_id)
        self.session.add(novo_ticket)
        self.session.commit()
        return True

    def listar_tickets(self):
        return self.session.query(Ticket).all()