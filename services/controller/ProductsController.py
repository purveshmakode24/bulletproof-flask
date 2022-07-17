from flask import request
from flask_restx import Resource, reqparse
from model.ProductsModel import ProductsModel
from service.ProductsService import get_product_or_products
import logging

log = logging.getLogger("Controller: ProductsController")
ns = ProductsModel.ns


@ns.route('/products')
class Products(Resource):
    get_parser = reqparse.RequestParser()
    get_parser.add_argument('id', required=False, type=int, location='args')

    @ns.response(404, 'Not found')
    @ns.response(403, 'Forbidden')
    @ns.response(400, 'Unknown Exception')
    @ns.doc(parser=get_parser)  # OR
    # @ns.expect(get_parser)
    def get(self):
        '''Fetch product(s)'''
        try:
            log.info('--------------->Entered ProductsController.')
            query_param_product_id = request.args.get('id')

            op = get_product_or_products(query_param_product_id)
            return op
        except Exception as e:
            log.info("Unknown Exception"+str(e))
            return {"error": "Unknown Exception"}, 400

    # post_parser = reqparse.RequestParser()
    # post_parser.add_argument('id', required=False, type=int, location='args')

    # @ns.response(403, 'Forbidden')
    # @ns.response(400, 'Unknown Exception')
    # @ns.doc(parser=post_parser)  # OR
    # @ns.expect(post_parser)
    # def post(self):
    # '''Post a product'''
    #     pass
