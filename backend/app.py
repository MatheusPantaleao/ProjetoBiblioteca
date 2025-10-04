# Este é o principal arquivo da aplicação. Nele que daremos RUN para iniciar os testes 

from flask_cors import CORS
from flask import Flask
from database import init_db, db
from routes.pessoas import pessoas_bp
from routes.livros import livros_bp
from routes.emprestimos import emprestimos_bp


app = Flask(__name__)
init_db(app)
CORS(app)

#cria a tabela no railway
with app.app_context():
    try:
        db.create_all()
        print("Tabelas criadas com sucesso")
    except Exception as e:
        print("Erro ao criar tabelas:", e)


app.register_blueprint(pessoas_bp)
app.register_blueprint(livros_bp)
app.register_blueprint(emprestimos_bp)

if __name__ == "__main__":
    app.run(debug=True) 