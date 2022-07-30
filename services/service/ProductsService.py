import logging
from dao.ProductsDao import (
    get_product_dao,
    get_products_dao,
    get_product_dao_with_orm,
    get_products_dao_with_orm)

log = logging.getLogger("Service: ProductsService")


class NoDataFoundException(Exception):
    pass


# Shared helper functions
def return_product_or_products_by_sql(query_param_product_id):
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

    return data


def return_product_or_products_by_orm(query_param_product_id):
    data = []
    if query_param_product_id:
        op_non_serialized = get_product_dao_with_orm(query_param_product_id)
    else:
        op_non_serialized = get_products_dao_with_orm()

    if len(op_non_serialized) == 0:
        raise NoDataFoundException

    for obj in op_non_serialized:
        data.append(obj.to_json())

    return data


# Main functions
def get_product_or_products(query_param_product_id, operation_perfomed_by):
    try:
        if operation_perfomed_by == 'sql':
            data = return_product_or_products_by_sql(query_param_product_id)
        elif operation_perfomed_by == 'orm':
            data = return_product_or_products_by_orm(query_param_product_id)

        return {
            "status": "Successfully Fetched!",
            "operaton_performed_by": operation_perfomed_by,
            "data": data
            }, 200
    except NoDataFoundException:
        log.error("Exception occured: No Data Found.")
        return {"error": "No Data found."}, 404
    except Exception as e:
        log.error("Some error occured: "+str(e))
        return {"error": "Some error occured."}, 400
