from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from services import dye_service

dye_ns = Namespace('dyes', description='Dye operations')

# Models for API documentation
dye_model = dye_ns.model('Dye', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the dye'),
    'commercial_name': fields.String(required=True, description='The commercial name of the dye'),
    'code': fields.String(required=True, description='The code of the dye'),
    'color_id': fields.Integer(description='The ID of the associated color') # Assuming a color_id field
})

dye_create_model = dye_ns.model('DyeCreate', {
    'commercial_name': fields.String(required=True, description='The commercial name of the dye'),
    'code': fields.String(required=True, description='The code of the dye'),
    'color_id': fields.Integer(description='The ID of the associated color')
})

dye_update_model = dye_ns.model('DyeUpdate', {
    'commercial_name': fields.String(description='The commercial name of the dye'),
    'code': fields.String(description='The code of the dye'),
    'color_id': fields.Integer(description='The ID of the associated color')
})

@dye_ns.route('/')
class DyeList(Resource):
    @dye_ns.doc('list_dyes')
    @dye_ns.marshal_list_with(dye_model)
    def get(self):
        '''List all dyes'''
        dyes = dye_service.get_all_dyes()
        return dyes

    @dye_ns.doc('create_dye')
    @dye_ns.expect(dye_create_model, validate=True)
    @dye_ns.marshal_with(dye_model, code=201)
    def post(self):
        '''Create a new dye'''
        data = request.get_json()
        if not data or not data.get('commercial_name') or not data.get('code'):
            dye_ns.abort(400, 'Missing required fields')
        new_dye = dye_service.create_dye(data)
        return new_dye, 201

@dye_ns.route('/<int:dye_id>')
@dye_ns.response(404, 'Dye not found')
class Dye(Resource):
    @dye_ns.doc('get_dye')
    @dye_ns.marshal_with(dye_model)
    def get(self, dye_id):
        '''Fetch a dye given its identifier'''
        dye = dye_service.get_dye_by_id(dye_id)
        if not dye:
            dye_ns.abort(404, 'Dye not found')
        return dye

    @dye_ns.doc('update_dye')
    @dye_ns.expect(dye_update_model, validate=True)
    @dye_ns.marshal_with(dye_model)
    def put(self, dye_id):
        '''Update a dye given its identifier'''
        data = request.get_json()
        updated_dye = dye_service.update_dye(dye_id, data)
        if not updated_dye:
            dye_ns.abort(404, 'Dye not found')
        return updated_dye

    @dye_ns.doc('delete_dye')
    @dye_ns.response(204, 'Dye deleted successfully')
    def delete(self, dye_id):
        '''Delete a dye given its identifier'''
        success = dye_service.delete_dye(dye_id)
        if not success:
            dye_ns.abort(404, 'Dye not found')
        return '', 204