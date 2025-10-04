from database import db

class Livro(db.Model):
    __tablename__ = "livros"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    data_aquisicao = db.Column(db.String(20), nullable=False)

    def mostrar_dados(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "autor": self.autor,
            "isbn": self.isbn,
            "categoria": self.categoria,
            "data_aquisicao": self.data_aquisicao
        }
