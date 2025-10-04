# código para configurar o SQLAlchemy. Este arquivo define o objeto db (a instância de SQLAlchemy) e a função init_db para inicializar a extensão com a sua aplicação Flask.

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def init_db(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)