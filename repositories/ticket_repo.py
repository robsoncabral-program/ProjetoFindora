from models.ticket import Ticket
from models.tecnico import Tecnico
from sqlalchemy import func

class TicketRepository:
    def __init__(self, session):
        self.session = session

    def criar_ticket_automatico(self, pessoa_id):
        """
        Automação: Seleciona o técnico com menos carga e cria o ticket (Takeover).
        """
        # 1. Encontra o técnico com menos tickets atribuídos
        # Faz um join entre Técnico e Ticket, agrupa e ordena pela contagem
        tecnico = self.session.query(Tecnico).\
            outerjoin(Ticket).\
            group_by(Tecnico.id).\
            order_by(func.count(Ticket.id)).\
            first()

        # 2. Cria o ticket automaticamente
        novo_ticket = Ticket(
            descricao="Busca automática - Atribuição por Takeover",
            pessoa_id=pessoa_id,
            tecnico_id=tecnico.id,
            status="Em Andamento"
        )
        
        self.session.add(novo_ticket)
        self.session.commit()
        
        return tecnico # Retorna o objeto técnico para ser exibido no main.py

    def listar_todos(self):
        return self.session.query(Ticket).all()