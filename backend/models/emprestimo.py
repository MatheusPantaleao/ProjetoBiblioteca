from database import db
from models.pessoa import Pessoa
from models.livro import Livro

class Emprestimo(db.Model):
    __tablename__ = "emprestimos"

    id = db.Column(db.Integer, primary_key=True)
    pessoa_id = db.Column(db.Integer, db.ForeignKey("pessoas.id"), nullable=False)
    livro_id = db.Column(db.Integer, db.ForeignKey("livros.id"), nullable=False)
    data_emprestimo = db.Column(db.String(20), nullable=False)

    # Relacionamentos
    pessoa = db.relationship("Pessoa", backref="emprestimos")
    livro = db.relationship("Livro", backref="emprestimos")

    def mostrar_dados(self):
        return {
            "id": self.id,
            "pessoa": self.pessoa.mostrar_dados(),
            "livro": self.livro.mostrar_dados(),
            "data_emprestimo": self.data_emprestimo
        }
