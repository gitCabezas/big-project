from flask_restx import Namespace, Resource

# O primeiro argumento é o nome do namespace, não o caminho
home_ns = Namespace('home', description='Endpoint da página inicial e health check')

@home_ns.route('/')
class HomeResource(Resource):
    @home_ns.doc(description='Retorna uma mensagem de boas-vindas. Pode ser usado como um health check.')
    def get(self):
        """Endpoint de boas-vindas"""
        return {'message': 'Welcome to the Backend API!'}
