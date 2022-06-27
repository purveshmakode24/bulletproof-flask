from flask_restx import Api
from controller.ProductsController import ns as products_ns

api = Api(
    title='API',
    version='1.0',
    description='Test API')

api.add_namespace(products_ns, '/service1')
