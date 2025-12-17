from sqlalchemy.orm import scoped_session
from modelos.modelos import Usuario

class UsuarioDAO:

    def __init__(self, session: scoped_session):
        self.session = session

    def criar(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()

    def buscar_por_email(self, email: str):
        return self.session.query(Usuario).filter_by(email=email).first()

    def listar_usuarios(self):
        return self.session.query(Usuario).all()

    def autenticar(self, email: str, senha: str):
        usuario = self.buscar_por_email(email)
        if usuario is None:
            return None
        if usuario.senha == senha:
            return usuario

        return None
