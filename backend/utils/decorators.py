from functools import wraps
from flask import request, jsonify
# import jwt # Para JWT, você precisaria instalar PyJWT

# Exemplo de decorator para verificar token JWT
# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None
#         if 'x-access-token' in request.headers:
#             token = request.headers['x-access-token']
#         if not token:
#             return jsonify({'message': 'Token is missing!'}), 401
#         try:
#             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
#             current_user = User.query.get(data['user_id'])
#         except:
#             return jsonify({'message': 'Token is invalid!'}), 401
#         return f(current_user, *args, **kwargs)
#     return decorated
