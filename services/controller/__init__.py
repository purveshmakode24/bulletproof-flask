from flask_restx import Api
api = Api(title='API', version='1.0', 
    description='Test API'
)

from controller.ProductsController import ns as products_ns

api.add_namespace(products_ns, '/service1')