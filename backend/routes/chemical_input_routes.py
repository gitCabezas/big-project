from flask import Blueprint, request, jsonify
from services import chemical_input_service

chemical_input_bp = Blueprint('chemical_input_bp', __name__)

@chemical_input_bp.route('/', methods=['GET'])
def get_chemical_inputs():
    inputs = chemical_input_service.get_all_chemical_inputs()
    return jsonify(inputs)

@chemical_input_bp.route('/<int:input_id>', methods=['GET'])
def get_chemical_input(input_id):
    input = chemical_input_service.get_chemical_input_by_id(input_id)
    if not input:
        return jsonify({'error': 'Chemical input not found'}), 404
    return jsonify(input)

@chemical_input_bp.route('/', methods=['POST'])
def create_chemical_input():
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'error': 'Missing required fields'}), 400
    new_input = chemical_input_service.create_chemical_input(data)
    return jsonify(new_input), 201

@chemical_input_bp.route('/<int:input_id>', methods=['PUT'])
def update_chemical_input(input_id):
    data = request.get_json()
    updated_input = chemical_input_service.update_chemical_input(input_id, data)
    if not updated_input:
        return jsonify({'error': 'Chemical input not found'}), 404
    return jsonify(updated_input)

@chemical_input_bp.route('/<int:input_id>', methods=['DELETE'])
def delete_chemical_input(input_id):
    success = chemical_input_service.delete_chemical_input(input_id)
    if not success:
        return jsonify({'error': 'Chemical input not found'}), 404
    return '', 204
