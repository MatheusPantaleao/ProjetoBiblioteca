from flask import Blueprint, request, jsonify
from database import db
from models.livro import Livro

livros_bp = Blueprint("livros", __name__)

# Criar livro
@livros_bp.route("/livros", methods=["POST"])
def criar_livro():
    data = request.json

    obrigatorios = ["nome", "autor", "isbn", "categoria", "data_aquisicao"]
    for campo in obrigatorios:
        if campo not in data or not data[campo]:
            return jsonify({"error": f"Campo '{campo}' é obrigatório"}), 400

    livro = Livro(
        nome=data["nome"],
        autor=data["autor"],
        isbn=data["isbn"],
        categoria=data["categoria"],
        data_aquisicao=data["data_aquisicao"]
    )
    db.session.add(livro)
    db.session.commit()
    return jsonify(livro.mostrar_dados()), 201

# Listar todos os livros
@livros_bp.route("/livros", methods=["GET"])
def listar_livros():
    livros = Livro.query.all()
    return jsonify([l.mostrar_dados() for l in livros]), 200

# Buscar livro por ID
@livros_bp.route("/livros/<int:id>", methods=["GET"])
def buscar_livro(id):
    livro = Livro.query.get(id)
    if not livro:
        return jsonify({"error": "Livro não encontrado"}), 404
    return jsonify(livro.mostrar_dados()), 200

# Atualizar livro
@livros_bp.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    livro = Livro.query.get(id)
    if not livro:
        return jsonify({"error": "Livro não encontrado"}), 404

    data = request.json
    livro.nome = data.get("nome", livro.nome)
    livro.autor = data.get("autor", livro.autor)
    livro.isbn = data.get("isbn", livro.isbn)
    livro.categoria = data.get("categoria", livro.categoria)
    livro.data_aquisicao = data.get("data_aquisicao", livro.data_aquisicao)

    db.session.commit()
    return jsonify(livro.mostrar_dados()), 200

# Deletar livro
@livros_bp.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro(id):
    livro = Livro.query.get(id)
    if not livro:
        return jsonify({"error": "Livro não encontrado"}), 404

    db.session.delete(livro)
    db.session.commit()
    return jsonify({"message": "Livro deletado com sucesso"}), 200