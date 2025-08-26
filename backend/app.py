from flask import Flask
from flask_restx import Api, Namespace # Import Api and Namespace
from config import Config
from models import db
# Import namespaces instead of blueprints
from routes.auth_routes import auth_ns
from routes.user_routes import user_ns
from routes.client_routes import client_ns
from routes.raw_material_routes import raw_material_ns
from routes.dye_routes import dye_ns
from routes.chemical_input_routes import chemical_input_ns
from routes.color_routes import color_ns
from routes.recipe_routes import recipe_ns
from routes.home_routes import home_ns
from dotenv import load_dotenv

load_dotenv()
# Initialize Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)

# Initialize Flask-RESTX Api
api = Api(
    app,
    version='1.0',
    title='Fibras & Cores API',
    description='API para o sistema de gerenciamento de receitas e romaneios.',
    doc='/docs' # This sets the Swagger UI documentation endpoint
)

# Add namespaces to the API
api.add_namespace(home_ns, path='/')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(user_ns, path='/api/users')
api.add_namespace(client_ns, path='/api/clients')
api.add_namespace(raw_material_ns, path='/api/raw_materials')
api.add_namespace(dye_ns, path='/api/dyes')
api.add_namespace(chemical_input_ns, path='/api/chemical_inputs')
api.add_namespace(color_ns, path='/api/colors')
api.add_namespace(recipe_ns, path='/api/recipes')

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



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
