from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from services import recipe_service

recipe_ns = Namespace('recipes', description='Recipe operations')

# Models for API documentation
recipe_model = recipe_ns.model('Recipe', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the recipe'),
    'name': fields.String(required=True, description='The name of the recipe'),
    'client_id': fields.Integer(required=True, description='The ID of the client associated with the recipe'),
    'article': fields.String(description='The article related to the recipe'),
    'process': fields.String(description='The process type of the recipe'),
    'substrate': fields.String(description='The substrate used in the recipe'),
    'machine': fields.String(description='The machine used for the recipe'),
    'weight': fields.Float(description='The weight for the recipe'),
    'dyes': fields.List(fields.Nested(recipe_ns.model('RecipeDye', {
        'dye_id': fields.Integer(required=True),
        'quantity': fields.Float(required=True)
    }))),
    'chemical_inputs': fields.List(fields.Nested(recipe_ns.model('RecipeChemicalInput', {
        'chemical_input_id': fields.Integer(required=True),
        'quantity': fields.Float(required=True)
    })))
})

recipe_create_model = recipe_ns.model('RecipeCreate', {
    'name': fields.String(required=True, description='The name of the recipe'),
    'client_id': fields.Integer(required=True, description='The ID of the client associated with the recipe'),
    'article': fields.String(description='The article related to the recipe'),
    'process': fields.String(description='The process type of the recipe'),
    'substrate': fields.String(description='The substrate used in the recipe'),
    'machine': fields.String(description='The machine used for the recipe'),
    'weight': fields.Float(description='The weight for the recipe'),
    'dyes': fields.List(fields.Nested(recipe_ns.model('RecipeDyeCreate', {
        'dye_id': fields.Integer(required=True),
        'quantity': fields.Float(required=True)
    }))),
    'chemical_inputs': fields.List(fields.Nested(recipe_ns.model('RecipeChemicalInputCreate', {
        'chemical_input_id': fields.Integer(required=True),
        'quantity': fields.Float(required=True)
    })))
})

recipe_update_model = recipe_ns.model('RecipeUpdate', {
    'name': fields.String(description='The name of the recipe'),
    'client_id': fields.Integer(description='The ID of the client associated with the recipe'),
    'article': fields.String(description='The article related to the recipe'),
    'process': fields.String(description='The process type of the recipe'),
    'substrate': fields.String(description='The substrate used in the recipe'),
    'machine': fields.String(description='The machine used for the recipe'),
    'weight': fields.Float(description='The weight for the recipe')
})

@recipe_ns.route('/')
class RecipeList(Resource):
    @recipe_ns.doc('list_recipes')
    @recipe_ns.marshal_list_with(recipe_model)
    def get(self):
        '''List all recipes'''
        recipes = recipe_service.get_all_recipes()
        return recipes

    @recipe_ns.doc('create_recipe')
    @recipe_ns.expect(recipe_create_model, validate=True)
    @recipe_ns.marshal_with(recipe_model, code=201)
    def post(self):
        '''Create a new recipe'''
        data = request.get_json()
        if not data or not data.get('name') or not data.get('client_id'):
            recipe_ns.abort(400, 'Missing required fields: name and client_id')
        new_recipe = recipe_service.create_recipe(data)
        return new_recipe, 201

@recipe_ns.route('/<int:recipe_id>')
@recipe_ns.response(404, 'Recipe not found')
class Recipe(Resource):
    @recipe_ns.doc('get_recipe')
    @recipe_ns.marshal_with(recipe_model)
    def get(self, recipe_id):
        '''Fetch a recipe given its identifier'''
        recipe = recipe_service.get_recipe_by_id(recipe_id)
        if not recipe:
            recipe_ns.abort(404, 'Recipe not found')
        return recipe

    @recipe_ns.doc('update_recipe')
    @recipe_ns.expect(recipe_update_model, validate=True)
    @recipe_ns.marshal_with(recipe_model)
    def put(self, recipe_id):
        '''Update a recipe given its identifier'''
        data = request.get_json()
        updated_recipe = recipe_service.update_recipe(recipe_id, data)
        if not updated_recipe:
            recipe_ns.abort(404, 'Recipe not found')
        return updated_recipe

    @recipe_ns.doc('delete_recipe')
    @recipe_ns.response(204, 'Recipe deleted successfully')
    def delete(self, recipe_id):
        '''Delete a recipe given its identifier'''
        success = recipe_service.delete_recipe(recipe_id)
        if not success:
            recipe_ns.abort(404, 'Recipe not found')
        return '', 204