from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from services import raw_material_service

raw_material_ns = Namespace('raw_materials', description='Raw Material operations')

# Models for API documentation
raw_material_model = raw_material_ns.model('RawMaterial', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the raw material'),
    'name': fields.String(required=True, description='The name of the raw material'),
    'type': fields.String(required=True, description='The type of the raw material (e.g., "dye", "chemical")'),
    'unit': fields.String(description='The unit of measurement for the raw material (e.g., "kg", "L")') # Assuming a unit field
})

raw_material_create_model = raw_material_ns.model('RawMaterialCreate', {
    'name': fields.String(required=True, description='The name of the raw material'),
    'type': fields.String(required=True, description='The type of the raw material (e.g., "dye", "chemical")'),
    'unit': fields.String(description='The unit of measurement for the raw material')
})

raw_material_update_model = raw_material_ns.model('RawMaterialUpdate', {
    'name': fields.String(description='The name of the raw material'),
    'type': fields.String(description='The type of the raw material (e.g., "dye", "chemical")'),
    'unit': fields.String(description='The unit of measurement for the raw material')
})

@raw_material_ns.route('/')
class RawMaterialList(Resource):
    @raw_material_ns.doc('list_raw_materials')
    @raw_material_ns.marshal_list_with(raw_material_model)
    def get(self):
        '''List all raw materials'''
        materials = raw_material_service.get_all_raw_materials()
        return materials

    @raw_material_ns.doc('create_raw_material')
    @raw_material_ns.expect(raw_material_create_model, validate=True)
    @raw_material_ns.marshal_with(raw_material_model, code=201)
    def post(self):
        '''Create a new raw material'''
        data = request.get_json()
        if not data or not data.get('name') or not data.get('type'):
            raw_material_ns.abort(400, 'Missing required fields')
        new_material = raw_material_service.create_raw_material(data)
        return new_material, 201

@raw_material_ns.route('/<int:material_id>')
@raw_material_ns.response(404, 'Raw material not found')
class RawMaterial(Resource):
    @raw_material_ns.doc('get_raw_material')
    @raw_material_ns.marshal_with(raw_material_model)
    def get(self, material_id):
        '''Fetch a raw material given its identifier'''
        material = raw_material_service.get_raw_material_by_id(material_id)
        if not material:
            raw_material_ns.abort(404, 'Raw material not found')
        return material

    @raw_material_ns.doc('update_raw_material')
    @raw_material_ns.expect(raw_material_update_model, validate=True)
    @raw_material_ns.marshal_with(raw_material_model)
    def put(self, material_id):
        '''Update a raw material given its identifier'''
        data = request.get_json()
        updated_material = raw_material_service.update_raw_material(material_id, data)
        if not updated_material:
            raw_material_ns.abort(404, 'Raw material not found')
        return updated_material

    @raw_material_ns.doc('delete_raw_material')
    @raw_material_ns.response(204, 'Raw material deleted successfully')
    def delete(self, material_id):
        '''Delete a raw material given its identifier'''
        success = raw_material_service.delete_raw_material(material_id)
        if not success:
            raw_material_ns.abort(404, 'Raw material not found')
        return '', 204