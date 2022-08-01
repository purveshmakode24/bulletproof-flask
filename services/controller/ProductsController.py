from flask import request
from flask_restx import Resource, reqparse
from model.ProductsModel import ProductsModel
from service.ProductsService import get_product_or_products
import logging

log = logging.getLogger("Controller: ProductsController")
ns = ProductsModel.ns

# # Parser is not required if you are using Model for documentating Apis
# """ Model for documenting the POST API for the Payload"""
# payload_resource = ns.model(
#     "payload_resource",
#     {
#         "title": fields.String,
#         "description": fields.String,
#         "user_id": fields.Integer
#     }
# )


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

    # # post_parser = reqparse.RequestParser()
    # # post_parser.add_argument('payload', required=True, type=list, location='json')

    # @ns.response(403, 'Forbidden')
    # @ns.response(400, 'Unknown Exception')
    # @ns.doc(parser = payload_resource)  # OR
    # # @ns.doc(parser = post_parser)  # OR
    # # @ns.expect(post_parser)  # OR
    # # @ns.expect(payload_resource)
    # def post(self):
    #     '''Post a product'''
    #     pass
