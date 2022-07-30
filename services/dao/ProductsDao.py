"""
Data access objects using generic sql or by ORM
"""
import logging
from sql.DBOperations import DBOperations
from orm.models import Product

log = logging.getLogger("DAO: ProductsDao")

# db = [{"id": 1000, "product_name": "ABC"},
#       {"id": 1001, "product_name": "XYZ"},
#       {"id": 1002, "product_name": "PQR"}]


def get_products_dao():
    query = '''SELECT id, name, price from product'''
    params = []
    try:
        op = DBOperations().runSelectQuery(query, params)
        return op
    except Exception as e:
        log.error("Some exception occured: "+str(e))


def get_product_dao(product_id):
    query = '''SELECT id, name, price \
            from product where id=%s'''

    params = [product_id]
    try:
        op = DBOperations().runSelectQuery(query, params)
        return op
    except Exception as e:
        log.error("Some exception occured: "+str(e))


def get_products_dao_with_orm():
    try:
        op = Product.query.all()
        return op
    except Exception as e:
        log.error("Some exception occured: "+str(e))


def get_product_dao_with_orm(product_id):
    try:
        op = Product.query.filter_by(id=product_id).limit(1).all()
        return op
    except Exception as e:
        log.error("Some exception occured: "+str(e))
