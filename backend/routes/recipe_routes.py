from flask import Blueprint, request, jsonify
from services import recipe_service

recipe_bp = Blueprint('recipe_bp', __name__)

@recipe_bp.route('/', methods=['GET'])
def get_recipes():
    recipes = recipe_service.get_all_recipes()
    return jsonify(recipes)

@recipe_bp.route('/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = recipe_service.get_recipe_by_id(recipe_id)
    if not recipe:
        return jsonify({'error': 'Recipe not found'}), 404
    return jsonify(recipe)

@recipe_bp.route('/', methods=['POST'])
def create_recipe():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('client_id'):
        return jsonify({'error': 'Missing required fields: name and client_id'}), 400
    new_recipe = recipe_service.create_recipe(data)
    return jsonify(new_recipe), 201

@recipe_bp.route('/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    data = request.get_json()
    updated_recipe = recipe_service.update_recipe(recipe_id, data)
    if not updated_recipe:
        return jsonify({'error': 'Recipe not found'}), 404
    return jsonify(updated_recipe)

@recipe_bp.route('/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    success = recipe_service.delete_recipe(recipe_id)
    if not success:
        return jsonify({'error': 'Recipe not found'}), 404
    return '', 204
