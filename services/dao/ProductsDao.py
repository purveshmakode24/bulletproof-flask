import logging

from sql.DBOperations import DBOperations

log = logging.getLogger("DAO: ProductsDao")

# db = [{"id": 1000, "product_name": "ABC"},
#       {"id": 1001, "product_name": "XYZ"},
#       {"id": 1002, "product_name": "PQR"}]


def get_products_dao():
    query='''SELECT product_id, product_name, price from products'''
    params = []
    try:
        op = DBOperations().runSelectQuery(query, params)
        return op
    except Exception as e:
        log.error("Some exception occured: "+str(e))


def get_product_dao(product_id):
    query='''SELECT product_id, product_name, price from products where product_id=%s'''
    params = [product_id]
    try:
        op = DBOperations().runSelectQuery(query, params)
        return op
    except Exception as e:
        log.error("Some exception occured: "+str(e))
