from flask_restx import Namespace


class ProductsModel:
    ns = Namespace('products', description='Products related operations')
