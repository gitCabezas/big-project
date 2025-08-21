from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from services import chemical_input_service

chemical_input_ns = Namespace('chemical_inputs', description='Chemical Input operations')

# Models for API documentation
chemical_input_model = chemical_input_ns.model('ChemicalInput', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the chemical input'),
    'name': fields.String(required=True, description='The name of the chemical input'),
    'type': fields.String(description='The type of the chemical input (e.g., "acid", "base")'), # Assuming a type field
    'unit': fields.String(description='The unit of measurement for the chemical input (e.g., "kg", "L")') # Assuming a unit field
})

chemical_input_create_model = chemical_input_ns.model('ChemicalInputCreate', {
    'name': fields.String(required=True, description='The name of the chemical input'),
    'type': fields.String(description='The type of the chemical input'),
    'unit': fields.String(description='The unit of measurement for the chemical input')
})

chemical_input_update_model = chemical_input_ns.model('ChemicalInputUpdate', {
    'name': fields.String(description='The name of the chemical input'),
    'type': fields.String(description='The type of the chemical input'),
    'unit': fields.String(description='The unit of measurement for the chemical input')
})

@chemical_input_ns.route('/')
class ChemicalInputList(Resource):
    @chemical_input_ns.doc('list_chemical_inputs')
    @chemical_input_ns.marshal_list_with(chemical_input_model)
    def get(self):
        '''List all chemical inputs'''
        inputs = chemical_input_service.get_all_chemical_inputs()
        return inputs

    @chemical_input_ns.doc('create_chemical_input')
    @chemical_input_ns.expect(chemical_input_create_model, validate=True)
    @chemical_input_ns.marshal_with(chemical_input_model, code=201)
    def post(self):
        '''Create a new chemical input'''
        data = request.get_json()
        if not data or not data.get('name'):
            chemical_input_ns.abort(400, 'Missing required fields')
        new_input = chemical_input_service.create_chemical_input(data)
        return new_input, 201

@chemical_input_ns.route('/<int:input_id>')
@chemical_input_ns.response(404, 'Chemical input not found')
class ChemicalInput(Resource):
    @chemical_input_ns.doc('get_chemical_input')
    @chemical_input_ns.marshal_with(chemical_input_model)
    def get(self, input_id):
        '''Fetch a chemical input given its identifier'''
        input = chemical_input_service.get_chemical_input_by_id(input_id)
        if not input:
            chemical_input_ns.abort(404, 'Chemical input not found')
        return input

    @chemical_input_ns.doc('update_chemical_input')
    @chemical_input_ns.expect(chemical_input_update_model, validate=True)
    @chemical_input_ns.marshal_with(chemical_input_model)
    def put(self, input_id):
        '''Update a chemical input given its identifier'''
        data = request.get_json()
        updated_input = chemical_input_service.update_chemical_input(input_id, data)
        if not updated_input:
            chemical_input_ns.abort(404, 'Chemical input not found')
        return updated_input

    @chemical_input_ns.doc('delete_chemical_input')
    @chemical_input_ns.response(204, 'Chemical input deleted successfully')
    def delete(self, input_id):
        '''Delete a chemical input given its identifier'''
        success = chemical_input_service.delete_chemical_input(input_id)
        if not success:
            chemical_input_ns.abort(404, 'Chemical input not found')
        return '', 204