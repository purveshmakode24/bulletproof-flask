import logging

from dao.ProductsDao import get_product_dao, get_products_dao

log = logging.getLogger("Service: ProductsService")


def get_product_or_products(query_param_product_id):
    try:
        if query_param_product_id:
            op = get_product_dao(query_param_product_id)
            return {"status": "Successfully Fetched!", "data": op}, 200
        else:
            op = get_products_dao()
            return {"status": "Successfully Fetched!", "data": op}, 200
    except Exception as e:
        log.error("Some error occured: "+str(e))
        return {"error": "Some error occured"}, 400