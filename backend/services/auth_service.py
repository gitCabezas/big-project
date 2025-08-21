from models.user_model import User, db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from flask import current_app

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
    print(f"Attempting login for user: {username}")
    if user:
        print(f"User found: {user.username}")
        print(f"Password from input: {password}")
        print(f"Stored hash: {user.password_hash}")
        password_match = check_password_hash(user.password_hash, password)
        print(f"Password match result: {password_match}")
        if password_match:
        payload = {
            'user_id': user.id,
            'username': user.username,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }
        token = jwt.encode(
            payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        return token
    return None