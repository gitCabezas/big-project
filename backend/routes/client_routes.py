from flask import Blueprint, request, jsonify
from services import client_service

client_bp = Blueprint('client_bp', __name__)

@client_bp.route('/', methods=['GET'])
def get_clients():
    clients = client_service.get_all_clients()
    return jsonify(clients)

@client_bp.route('/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = client_service.get_client_by_id(client_id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404
    return jsonify(client)

@client_bp.route('/', methods=['POST'])
def create_client():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('cnpj_cpf'):
        return jsonify({'error': 'Missing required fields'}), 400
    new_client = client_service.create_client(data)
    return jsonify(new_client), 201

@client_bp.route('/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.get_json()
    updated_client = client_service.update_client(client_id, data)
    if not updated_client:
        return jsonify({'error': 'Client not found'}), 404
    return jsonify(updated_client)

@client_bp.route('/<int:client_id>/deactivate', methods=['PUT'])
def deactivate_client(client_id):
    deactivated_client = client_service.deactivate_client(client_id)
    if not deactivated_client:
        return jsonify({'error': 'Client not found'}), 404
    return jsonify(deactivated_client)
