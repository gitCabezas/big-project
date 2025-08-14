import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-super-secret-key'
    
    DB_USER = os.environ.get('user')
    DB_PASSWORD = os.environ.get('password')
    DB_HOST = os.environ.get('host')
    DB_PORT = os.environ.get('port')
    DB_NAME = os.environ.get('dbname')
    
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

try:
    with app.app_context():
        db.session.execute(db.text("SELECT 1"))
        print("Conexão com o banco de dados estabelecida com sucesso!")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
