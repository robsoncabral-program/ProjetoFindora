from fastapi import FastAPI
from config.database import Session
from repositories.usuario_repo import UsuarioRepository

app = FastAPI(title="Findora API", description="API para gestão de utilizadores")

@app.get("/usuarios")
def ler_usuarios():
    session = Session()
    repo = UsuarioRepository(session)
    usuarios = repo.listar_todos()
    session.close()
    return [{"id": u.id, "nome": u.nome, "email": u.email} for u in usuarios]