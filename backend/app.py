from flask import Flask, jsonify
from config import Config
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp

app = Flask(__name__)
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(user_bp, url_prefix='/api/users')

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Backend API!"})

if __name__ == '__main__':
    app.run(debug=True)
