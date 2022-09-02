from flask import request
from flask_restx import Resource, reqparse
# from flask_restx import fields
from model.ProductsModel import ProductsModel
from service.ProductsService import get_product_or_products
import logging

log = logging.getLogger("Controller: ProductsController")
ns = ProductsModel.ns

# # Parser is not required if you are using Model for documentating Apis
# """ Model for documenting the POST API for the Payload"""
# posts_payload_resource = ns.model(
#     "posts_payload_resource",
#     {
#         "product_name": fields.String,
#         "price": fields.String
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

    # post_parser = reqparse.RequestParser()
    # post_parser.add_argument(
    #     'some-access-token',
    #     required=True, type=str, location='headers')
    # ## 'post_parser.add_argument()' is optional if you are
    # ## using payload_resource defined at the top above.
    # # post_parser.add_argument('payload',
    # # required=True, type=list, location='json')
    # @ns.response(403, 'Forbidden')
    # @ns.response(400, 'Unknown Exception')
    # # @ns.doc(parser = payload_resource)  # OR (optional)
    # # @ns.doc(parser = post_parser)  # OR (optional)
    # # @ns.expect(post_parser)  # OR (optional)
    # # @ns.expect(payload_resource) # OR (optional)

    # ## To use other arguments (headers, args, etc) and payload at a time
    # @ns.expect(post_parser, payload_resource)
    # def post(self):
    #     '''Post a product'''
    #     # Your POST method code goes here..
    #     pass
