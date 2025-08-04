import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-super-secret-key'
    
    # Configuração do banco de dados a partir das variáveis de ambiente
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_NAME = os.environ.get('DB_NAME')
    
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
