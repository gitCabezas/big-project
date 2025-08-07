from flask import Blueprint, request, jsonify
from services import raw_material_service

raw_material_bp = Blueprint('raw_material_bp', __name__)

@raw_material_bp.route('/', methods=['GET'])
def get_raw_materials():
    materials = raw_material_service.get_all_raw_materials()
    return jsonify(materials)

@raw_material_bp.route('/<int:material_id>', methods=['GET'])
def get_raw_material(material_id):
    material = raw_material_service.get_raw_material_by_id(material_id)
    if not material:
        return jsonify({'error': 'Raw material not found'}), 404
    return jsonify(material)

@raw_material_bp.route('/', methods=['POST'])
def create_raw_material():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('type'):
        return jsonify({'error': 'Missing required fields'}), 400
    new_material = raw_material_service.create_raw_material(data)
    return jsonify(new_material), 201

@raw_material_bp.route('/<int:material_id>', methods=['PUT'])
def update_raw_material(material_id):
    data = request.get_json()
    updated_material = raw_material_service.update_raw_material(material_id, data)
    if not updated_material:
        return jsonify({'error': 'Raw material not found'}), 404
    return jsonify(updated_material)

@raw_material_bp.route('/<int:material_id>', methods=['DELETE'])
def delete_raw_material(material_id):
    success = raw_material_service.delete_raw_material(material_id)
    if not success:
        return jsonify({'error': 'Raw material not found'}), 404
    return '', 204
