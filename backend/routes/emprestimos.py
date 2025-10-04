from flask import Blueprint, request, jsonify
from database import db
from models.pessoa import Pessoa
from models.livro import Livro  
from models.emprestimo import Emprestimo


emprestimos_bp = Blueprint("emprestimos", __name__)

# Criar empréstimo
@emprestimos_bp.route("/emprestimos", methods=["POST"])
def criar_emprestimo():
    data = request.json

    if "pessoa_id" not in data or "livro_id" not in data or "data_emprestimo" not in data:
        return jsonify({"error": "Campos 'pessoa_id', 'livro_id' e 'data_emprestimo' são obrigatórios"}), 400

    pessoa = Pessoa.query.get(data["pessoa_id"])
    livro = Livro.query.get(data["livro_id"])

    if not pessoa:
        return jsonify({"error": "Pessoa não encontrado"}), 400
    if not livro:
        return jsonify({"erro": "livro não encontrado"}), 400

    emprestimo = Emprestimo(
        pessoa_id=pessoa.id,
        livro_id=livro.id,
        data_emprestimo=data["data_emprestimo"]
    )
    db.session.add(emprestimo)
    db.session.commit()
    return jsonify(emprestimo.mostrar_dados()), 201

# Listar todos os empréstimos
@emprestimos_bp.route("/emprestimos", methods=["GET"])
def listar_emprestimos():
    emprestimos = Emprestimo.query.all()
    return jsonify([e.mostrar_dados() for e in emprestimos]), 200

# Buscar empréstimo por ID
@emprestimos_bp.route("/emprestimos/<int:id>", methods=["GET"])
def buscar_emprestimo(id):
    emprestimo = Emprestimo.query.get(id)
    if not emprestimo:
        return jsonify({"error": "Empréstimo não encontrado"}), 404
    return jsonify(emprestimo.mostrar_dados()), 200

# Atualizar empréstimo
@emprestimos_bp.route("/emprestimos/<int:id>", methods=["PUT"])
def atualizar_emprestimo(id):
    emprestimo = Emprestimo.query.get(id)
    if not emprestimo:
        return jsonify({"error": "Empréstimo não encontrado"}), 404

    data = request.json
    # Permite alterar a data do empréstimo, pessoa ou livro
    if "pessoa_id" in data:
        pessoa = Pessoa.query.get(data["pessoa_id"])
        if pessoa:
            emprestimo.pessoa_id = pessoa.id
    if "livro_id" in data:
        livro = Livro.query.get(data["livro_id"])
        if livro:
            emprestimo.livro_id = livro.id
    emprestimo.data_emprestimo = data.get("data_emprestimo", emprestimo.data_emprestimo)

    db.session.commit()
    return jsonify(emprestimo.mostrar_dados()), 200

# Deletar empréstimo
@emprestimos_bp.route("/emprestimos/<int:id>", methods=["DELETE"])
def deletar_emprestimo(id):
    emprestimo = Emprestimo.query.get(id)
    if not emprestimo:
        return jsonify({"error": "Empréstimo não encontrado"}), 404

    db.session.delete(emprestimo)
    db.session.commit()
    return jsonify({"message": "Empréstimo deletado com sucesso"}), 200
