from flask import Blueprint, request, jsonify
from database import db
from models.pessoa import Pessoa
from utils.validarCPF import validar_cpf

pessoas_bp = Blueprint("pessoas", __name__)

#criar pessoa
@pessoas_bp.route("/pessoas", methods=["POST"])
def criar_pessoa():
    data = request.json
    print("data recebido:", data)

    obrigatorios = ["cpf", "nome", "idade", "email", "numero", "tipo"]
    for campo in obrigatorios:
        if campo not in data or not data[campo]:
            return jsonify({"error": f"Campo '{campo}' é obrigatório"}), 400

    # Aqui usamos a função do utils
    if not validar_cpf(data["cpf"]):
        return jsonify({"error": "CPF inválido"}), 400

    if data["tipo"] not in ["cliente", "professor", "funcionario"]:
        return jsonify({"error": "Tipo deve ser cliente, professor ou funcionario"}), 400

    pessoa = Pessoa(
        cpf=data["cpf"],
        nome=data["nome"],
        idade=data["idade"],
        email=data["email"],
        numero=data["numero"],
        tipo=data["tipo"],
    )
    db.session.add(pessoa)
    db.session.commit()
    return jsonify(pessoa.mostrar_dados()), 201

# Listar todas as pessoas
@pessoas_bp.route("/pessoas", methods=["GET"])
def listar_pessoas():
    pessoas = Pessoa.query.all()
    return jsonify([p.mostrar_dados() for p in pessoas]), 200

# Buscar pessoa por ID
@pessoas_bp.route("/pessoas/<int:id>", methods=["GET"])
def buscar_pessoa(id):
    pessoa = Pessoa.query.get(id)
    if not pessoa:
        return jsonify({"error": "Pessoa não encontrada"}), 404
    return jsonify(pessoa.mostrar_dados()), 200

# Atualizar pessoa
@pessoas_bp.route("/pessoas/<int:id>", methods=["PUT"])
def atualizar_pessoa(id):
    pessoa = Pessoa.query.get(id)
    if not pessoa:
        return jsonify({"error": "Pessoa não encontrada"}), 404

    data = request.json
    pessoa.cpf = data.get("cpf", pessoa.cpf)
    pessoa.nome = data.get("nome", pessoa.nome)
    pessoa.idade = data.get("idade", pessoa.idade)
    pessoa.email = data.get("email", pessoa.email)
    pessoa.numero = data.get("numero", pessoa.numero)
    pessoa.tipo = data.get("tipo", pessoa.tipo)

    db.session.commit()
    return jsonify(pessoa.mostrar_dados()), 200

# Deletar pessoa
@pessoas_bp.route("/pessoas/<int:id>", methods=["DELETE"])
def deletar_pessoa(id):
    pessoa = Pessoa.query.get(id)
    if not pessoa:
        return jsonify({"error": "Pessoa não encontrada"}), 404

    db.session.delete(pessoa)
    db.session.commit()
    return jsonify({"message": "Pessoa deletada com sucesso"}), 200
