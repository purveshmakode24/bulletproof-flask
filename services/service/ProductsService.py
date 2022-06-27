import logging
from msilib.schema import Error

from dao.ProductsDao import get_product_dao, get_products_dao

log = logging.getLogger("Service: ProductsService")

class NoDataFoundException(Exception):
    pass


def get_product_or_products(query_param_product_id):
    try:
        data = []
        columns = ['product_id', 'product_name', 'price']
        if query_param_product_id:
            op = get_product_dao(query_param_product_id)
        else:
            op = get_products_dao()

        if op is None:
            raise NoDataFoundException

        for row in op:
            obj = {}
            for i, col in enumerate(columns):
                obj[col] = row[i]

            data.append(obj)
            
        return {"status": "Successfully Fetched!", "data": data}, 200

    except NoDataFoundException as ndfe:
        log.error("Exception occured: "+str(ndfe))
        return {"error": "No Data found"}, 404
    except Exception as e:
        log.error("Some error occured: "+str(e))
        return {"error": "Some error occured"}, 400