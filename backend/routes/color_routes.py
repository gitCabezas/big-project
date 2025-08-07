from flask import Blueprint, request, jsonify
from services import color_service

color_bp = Blueprint('color_bp', __name__)

@color_bp.route('/', methods=['GET'])
def get_colors():
    colors = color_service.get_all_colors()
    return jsonify(colors)

@color_bp.route('/<int:color_id>', methods=['GET'])
def get_color(color_id):
    color = color_service.get_color_by_id(color_id)
    if not color:
        return jsonify({'error': 'Color not found'}), 404
    return jsonify(color)

@color_bp.route('/', methods=['POST'])
def create_color():
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'error': 'Missing required fields'}), 400
    new_color = color_service.create_color(data)
    return jsonify(new_color), 201

@color_bp.route('/<int:color_id>', methods=['PUT'])
def update_color(color_id):
    data = request.get_json()
    updated_color = color_service.update_color(color_id, data)
    if not updated_color:
        return jsonify({'error': 'Color not found'}), 404
    return jsonify(updated_color)

@color_bp.route('/<int:color_id>', methods=['DELETE'])
def delete_color(color_id):
    success = color_service.delete_color(color_id)
    if not success:
        return jsonify({'error': 'Color not found'}), 404
    return '', 204
