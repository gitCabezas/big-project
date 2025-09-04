from models.user_model import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

def register_user(username, password):
    if User.query.filter_by(username=username).first():
        return None # User already exists

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        token = create_access_token(identity=str(user.id)) # Convert user.id to string
        return token
    return None
