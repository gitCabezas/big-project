
# Este script permite redefinir a senha de um usuário existente.
import os
import sys
from flask import Flask
from models import db, User
from config import Config

# Adiciona o diretório raiz ao path para encontrar os módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- Configuração da Aplicação Flask ---
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app

app = create_app()

# --- Lógica do Script ---
def reset_user_password():
    username_to_reset = input("Digite o nome do usuário que terá a senha redefinida: ")
    
    with app.app_context():
        user = User.query.filter_by(username=username_to_reset).first()
        
        if not user:
            print(f"Erro: Usuário '{username_to_reset}' não encontrado.")
            return

        new_password = input(f"Digite a NOVA senha para o usuário '{username_to_reset}': ")
        
        if not new_password:
            print("Erro: A senha não pode ser vazia.")
            return

        user.set_password(new_password)
        db.session.commit()
        
        print(f"Sucesso! A senha para o usuário '{user.username}' foi redefinida.")

if __name__ == '__main__':
    reset_user_password()
