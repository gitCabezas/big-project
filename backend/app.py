from flask import Flask, jsonify
from config import Config
from models import db
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.client_routes import client_bp
from routes.raw_material_routes import raw_material_bp
from routes.dye_routes import dye_bp
from routes.chemical_input_routes import chemical_input_bp
from routes.color_routes import color_bp
from routes.recipe_routes import recipe_bp
from dotenv import load_dotenv

load_dotenv()
# Initialize Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(client_bp, url_prefix='/api/clients')
app.register_blueprint(raw_material_bp, url_prefix='/api/raw_materials')
app.register_blueprint(dye_bp, url_prefix='/api/dyes')
app.register_blueprint(chemical_input_bp, url_prefix='/api/chemical_inputs')
app.register_blueprint(color_bp, url_prefix='/api/colors')
app.register_blueprint(recipe_bp, url_prefix='/api/recipes')

@app.cli.command("create-all")
def create_all():
    """Creates all database tables."""
    with app.app_context():
        db.create_all()
    print("Database tables created!")

@app.cli.command("create-user")
def create_user_cli():
    """Cria um novo usuário administrador no banco de dados."""
    username = input("Digite o nome de usuário: ")
    email = input("Digite o email: ")
    password = input("Digite a senha: ")

    with app.app_context():
        # Importar o user_service aqui para evitar circular imports no topo
        from services.user_service import create_user
        try:
            user = create_user(username, email, password)
            print(f"Usuário '{user.username}' criado com sucesso! ID: {user.id}")
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Backend API!"})

if __name__ == '__main__':
    app.run(debug=True)
