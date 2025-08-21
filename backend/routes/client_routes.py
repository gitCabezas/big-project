from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from services import client_service

client_ns = Namespace('clients', description='Client operations')

# Models for API documentation
client_model = client_ns.model('Client', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a client'),
    'name': fields.String(required=True, description='The name of the client'),
    'cnpj_cpf': fields.String(required=True, description='The CNPJ or CPF of the client'),
    'is_active': fields.Boolean(description='Client active status')
})

client_create_model = client_ns.model('ClientCreate', {
    'name': fields.String(required=True, description='The name of the client'),
    'cnpj_cpf': fields.String(required=True, description='The CNPJ or CPF of the client')
})

client_update_model = client_ns.model('ClientUpdate', {
    'name': fields.String(description='The name of the client'),
    'cnpj_cpf': fields.String(description='The CNPJ or CPF of the client')
})

@client_ns.route('/')
class ClientList(Resource):
    @client_ns.doc('list_clients')
    @client_ns.marshal_list_with(client_model)
    def get(self):
        '''List all clients'''
        clients = client_service.get_all_clients()
        return clients

    @client_ns.doc('create_client')
    @client_ns.expect(client_create_model, validate=True)
    @client_ns.marshal_with(client_model, code=201)
    def post(self):
        '''Create a new client'''
        data = request.get_json()
        if not data or not data.get('name') or not data.get('cnpj_cpf'):
            client_ns.abort(400, 'Missing required fields')
        new_client = client_service.create_client(data)
        return new_client, 201

@client_ns.route('/<int:client_id>')
@client_ns.response(404, 'Client not found')
class Client(Resource):
    @client_ns.doc('get_client')
    @client_ns.marshal_with(client_model)
    def get(self, client_id):
        '''Fetch a client given its identifier'''
        client = client_service.get_client_by_id(client_id)
        if not client:
            client_ns.abort(404, 'Client not found')
        return client

    @client_ns.doc('update_client')
    @client_ns.expect(client_update_model, validate=True)
    @client_ns.marshal_with(client_model)
    def put(self, client_id):
        '''Update a client given its identifier'''
        data = request.get_json()
        updated_client = client_service.update_client(client_id, data)
        if not updated_client:
            client_ns.abort(404, 'Client not found')
        return updated_client

@client_ns.route('/<int:client_id>/deactivate')
@client_ns.response(404, 'Client not found')
class ClientDeactivate(Resource):
    @client_ns.doc('deactivate_client')
    @client_ns.marshal_with(client_model)
    def put(self, client_id):
        '''Deactivate a client given its identifier'''
        deactivated_client = client_service.deactivate_client(client_id)
        if not deactivated_client:
            client_ns.abort(404, 'Client not found')
        return deactivated_client