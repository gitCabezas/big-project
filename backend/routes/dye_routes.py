from flask import Blueprint, request, jsonify
from services import dye_service

dye_bp = Blueprint('dye_bp', __name__)

@dye_bp.route('/', methods=['GET'])
def get_dyes():
    dyes = dye_service.get_all_dyes()
    return jsonify(dyes)

@dye_bp.route('/<int:dye_id>', methods=['GET'])
def get_dye(dye_id):
    dye = dye_service.get_dye_by_id(dye_id)
    if not dye:
        return jsonify({'error': 'Dye not found'}), 404
    return jsonify(dye)

@dye_bp.route('/', methods=['POST'])
def create_dye():
    data = request.get_json()
    if not data or not data.get('commercial_name') or not data.get('code'):
        return jsonify({'error': 'Missing required fields'}), 400
    new_dye = dye_service.create_dye(data)
    return jsonify(new_dye), 201

@dye_bp.route('/<int:dye_id>', methods=['PUT'])
def update_dye(dye_id):
    data = request.get_json()
    updated_dye = dye_service.update_dye(dye_id, data)
    if not updated_dye:
        return jsonify({'error': 'Dye not found'}), 404
    return jsonify(updated_dye)

@dye_bp.route('/<int:dye_id>', methods=['DELETE'])
def delete_dye(dye_id):
    success = dye_service.delete_dye(dye_id)
    if not success:
        return jsonify({'error': 'Dye not found'}), 404
    return '', 204
