import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-super-secret-key'
    
    # Configuração do banco de dados a partir das variáveis de ambiente
    DB_USER = os.environ.get('user')
    DB_PASSWORD = os.environ.get('password')
    DB_HOST = os.environ.get('host')
    DB_PORT = os.environ.get('port')
    DB_NAME = os.environ.get('dbname')
    
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
