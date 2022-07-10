from flask_restx import Api
from controller.ProductsController import ns as products_ns

api = Api(
    title='Bulletproof Flask API',
    version='1.0',
    description='A simple, scalable, and powerful architecture \
    for building production ready Flask application API services.')

api.add_namespace(products_ns, '/service1')
