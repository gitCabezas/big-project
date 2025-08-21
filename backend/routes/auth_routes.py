from flask import request, jsonify
from flask_restx import Namespace, Resource, fields # Import Namespace, Resource, fields
from services.auth_service import register_user, login_user

auth_ns = Namespace('auth', description='Authentication operations') # Use Namespace

# Define a model for the login request payload
login_model = auth_ns.model('Login', {
    'username': fields.String(required=True, description='User username'),
    'password': fields.String(required=True, description='User password')
})

@auth_ns.route('/login') # Use auth_ns.route
class Login(Resource): # Define a Resource class
    @auth_ns.expect(login_model, validate=True) # Document expected input
    @auth_ns.response(200, 'Login successful', auth_ns.model('LoginSuccess', {'message': fields.String, 'token': fields.String})) # Document success response
    @auth_ns.response(400, 'Validation Error', auth_ns.model('ValidationError', {'message': fields.String})) # Document validation error
    @auth_ns.response(401, 'Invalid credentials', auth_ns.model('AuthError', {'message': fields.String})) # Document auth error
    def post(self): # Define HTTP method as a method of the class
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # The validation is handled by @auth_ns.expect(login_model, validate=True)
        # but we keep this check for clarity or if validation fails before model parsing
        if not username or not password:
            auth_ns.abort(400, message="Username and password are required")

        token = login_user(username, password)
        if token:
            return jsonify({"message": "Login successful", "token": token}), 200
        auth_ns.abort(401, message="Invalid credentials") # Use abort for consistent error responses

# The register route remains commented out as per previous discussion
# @auth_ns.route('/register')
# class Register(Resource):
#     @auth_ns.expect(login_model, validate=True)
#     @auth_ns.response(201, 'User registered successfully')
#     @auth_ns.response(400, 'Validation Error')
#     @auth_ns.response(409, 'User already exists')
#     def post(self):
#         data = request.get_json()
#         username = data.get('username')
#         password = data.get('password')
#         if not username or not password:
#             auth_ns.abort(400, message="Username and password are required")
#
#         user = register_user(username, password)
#         if user:
#             return jsonify({"message": "User registered successfully", "user_id": user.id}), 201
#         auth_ns.abort(409, message="User already exists")
