from models.user_model import User, db
from werkzeug.security import generate_password_hash, check_password_hash
# import jwt # Para JWT, você precisaria instalar PyJWT e configurar uma chave secreta
# from datetime import datetime, timedelta

def register_user(username, password):
    if User.query.filter_by(username=username).first():
        return None # User already exists

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def login_user(username, password):
    # Mocked user data for testing without a database
    allowed_users = [
        {'username': 'textilandina@uol.com.br', 'password': '270271'}
    ]

    for user in allowed_users:
        if user['username'] == username and user['password'] == password:
            return "dummy_token_for_testing"  # Return a dummy token for successful login

    return None  # Invalid credentials

    # Original database logic commented out for testing
    # user = User.query.filter_by(username=username).first()
    # if user and check_password_hash(user.password_hash, password):
    #     # Exemplo de geração de token JWT (requer PyJWT e SECRET_KEY em config.py)
    #     # token = jwt.encode({
    #     #     'user_id': user.id,
    #     #     'exp': datetime.utcnow() + timedelta(minutes=30)
    #     # }, app.config['SECRET_KEY'], algorithm='HS256')
    #     # return token
    #     return "dummy_token_for_now" # Retorna um token dummy por enquanto
    # return None
