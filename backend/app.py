from flask import Flask, jsonify
from config import Config
from models import db
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
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

@app.cli.command("create-all")
def create_all():
    """Creates all database tables."""
    with app.app_context():
        db.create_all()
    print("Database tables created!")

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Backend API!"})

if __name__ == '__main__':
    app.run(debug=True)
