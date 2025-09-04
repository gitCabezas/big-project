from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from services import color_service

color_ns = Namespace('colors', description='Color operations')

# Models for API documentation
color_model = color_ns.model('Color', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the color'),
    'name': fields.String(required=True, description='The name of the color'),
    'hex_code': fields.String(description='The hexadecimal code of the color (e.g., "#FFFFFF")') # Assuming a hex_code field
})

color_create_model = color_ns.model('ColorCreate', {
    'name': fields.String(required=True, description='The name of the color'),
    'hex_code': fields.String(description='The hexadecimal code of the color')
})

color_update_model = color_ns.model('ColorUpdate', {
    'name': fields.String(description='The name of the color'),
    'hex_code': fields.String(description='The hexadecimal code of the color')
})

@color_ns.route('/')
class ColorList(Resource):
    @color_ns.doc('list_colors')
    @color_ns.marshal_list_with(color_model)
    def get(self):
        '''List all colors'''
        colors = color_service.get_all_colors()
        return colors

    @color_ns.doc('create_color')
    @color_ns.expect(color_create_model, validate=True)
    @color_ns.marshal_with(color_model, code=201)
    def post(self):
        '''Create a new color'''
        data = request.get_json()
        if not data or not data.get('name'):
            color_ns.abort(400, 'Missing required fields')
        new_color = color_service.create_color(data)
        return new_color, 201

@color_ns.route('/<int:color_id>')
@color_ns.response(404, 'Color not found')
class Color(Resource):
    @color_ns.doc('get_color')
    @color_ns.marshal_with(color_model)
    def get(self, color_id):
        '''Fetch a color given its identifier'''
        color = color_service.get_color_by_id(color_id)
        if not color:
            color_ns.abort(404, 'Color not found')
        return color

    @color_ns.doc('update_color')
    @color_ns.expect(color_update_model, validate=True)
    @color_ns.marshal_with(color_model)
    def put(self, color_id):
        '''Update a color given its identifier'''
        data = request.get_json()
        updated_color = color_service.update_color(color_id, data)
        if not updated_color:
            color_ns.abort(404, 'Color not found')
        return updated_color

    @color_ns.doc('delete_color')
    @color_ns.response(204, 'Color deleted successfully')
    def delete(self, color_id):
        '''Delete a color given its identifier'''
        success = color_service.delete_color(color_id)
        if not success:
            color_ns.abort(404, 'Color not found')
        return '', 204