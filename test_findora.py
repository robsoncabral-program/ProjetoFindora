import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.database import Base
from models.tecnico import Tecnico
from repositories.tecnico_repo import TecnicoRepository

class TestFindora(unittest.TestCase):
    def setUp(self):
        # Cria uma base de dados em memória para testes (não afeta a tua real)
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.repo = TecnicoRepository(self.session)

    def test_adicionar_tecnico(self):
        # Testa se a funcionalidade principal de adicionar técnico funciona
        self.repo.adicionar_tecnico("Robson", "Investigação Digital")
        tecnico = self.session.query(Tecnico).filter_by(nome="Robson").first()
        self.assertIsNotNone(tecnico)
        self.assertEqual(tecnico.nome, "Robson")

if __name__ == '__main__':
    unittest.main()