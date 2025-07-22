from flask import Blueprint, request, jsonify
from services.user_service import get_all_users, get_user_by_id, create_user, update_user, delete_user
# from utils.decorators import token_required # Exemplo de importação de decorator

user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['GET'])
# @token_required # Exemplo de uso de decorator
def get_users():
    users = get_all_users()
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({"message": "User not found"}), 404

@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400
    
    user = create_user(username, password)
    return jsonify({"message": "User created successfully", "user_id": user.id}), 201

@user_bp.route('/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    data = request.get_json()
    updated_user = update_user(user_id, data)
    if updated_user:
        return jsonify({"message": "User updated successfully", "user": updated_user.to_dict()})
    return jsonify({"message": "User not found"}), 404

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    if delete_user(user_id):
        return jsonify({"message": "User deleted successfully"}), 204
    return jsonify({"message": "User not found"}), 404
