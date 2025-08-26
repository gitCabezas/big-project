from flask import request, jsonify
from flask_restx import Namespace, Resource, fields, reqparse # Import Namespace, Resource, fields, reqparse
from services.user_service import get_all_users, get_user_by_id, create_user, update_user, delete_user
# from utils.decorators import token_required # Exemplo de importação de decorator

user_ns = Namespace('users', description='User operations') # Use Namespace

# Models for API documentation
user_model = user_ns.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'username': fields.String(required=True, description='The username of the user'),
    'email': fields.String(required=True, description='The email of the user'), # Assuming email is part of user model
    'created_at': fields.DateTime(readOnly=True, description='The creation timestamp of the user')
})

user_create_model = user_ns.model('UserCreate', {
    'username': fields.String(required=True, description='The username of the user'),
    'email': fields.String(required=True, description='The email of the user'),
    'password': fields.String(required=True, description='The password of the user')
})

user_update_model = user_ns.model('UserUpdate', {
    'username': fields.String(description='The updated username of the user'),
    'email': fields.String(description='The updated email of the user'),
    'password': fields.String(description='The updated password of the user')
})

@user_ns.route('/')
class UserList(Resource):
    @user_ns.doc('list_users')
    @jwt_required
    @user_ns.marshal_list_with(user_model)
    def get(self):
        '''List all users'''
        users = get_all_users()
        return [user.to_dict() for user in users]

    @user_ns.doc('create_user')
    @user_ns.expect(user_create_model, validate=True)
    @user_ns.marshal_with(user_model, code=201)
    def post(self):
        '''Create a new user'''
        data = request.get_json()
        username = data.get('username')
        email = data.get('email') # Assuming email is part of user creation
        password = data.get('password')
        if not username or not email or not password: # Added email check
            user_ns.abort(400, message="Username, email and password are required")

        user = create_user(username, email, password) # Updated create_user call
        return user.to_dict(), 201

@user_ns.route('/<int:user_id>')
@user_ns.response(404, 'User not found')
class User(Resource):
    @user_ns.doc('get_user')
    @user_ns.marshal_with(user_model)
    def get(self, user_id):
        '''Fetch a user given its identifier'''
        user = get_user_by_id(user_id)
        if user:
            return user.to_dict()
        user_ns.abort(404, message="User not found")

    @user_ns.doc('update_user')
    @user_ns.expect(user_update_model, validate=True)
    @user_ns.marshal_with(user_model)
    def put(self, user_id):
        '''Update a user given its identifier'''
        data = request.get_json()
        updated_user = update_user(user_id, data)
        if updated_user:
            return updated_user.to_dict()
        user_ns.abort(404, message="User not found")

    @user_ns.doc('delete_user')
    @user_ns.response(204, 'User deleted successfully')
    def delete(self, user_id):
        '''Delete a user given its identifier'''
        if delete_user(user_id):
            return '', 204
        user_ns.abort(404, message="User not found")
