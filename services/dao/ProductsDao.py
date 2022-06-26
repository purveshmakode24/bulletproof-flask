import logging

log = logging.getLogger("DAO: ProductsDao")

db = [{"id": 1000, "product_name": "ABC"},
      {"id": 1001, "product_name": "XYZ"},
      {"id": 1002, "product_name": "PQR"}]


def get_products_dao():
    query=''''''
    params = []
    try:
        return db
    except Exception as e:
        log.error("Some exception occured: "+str(e))


def get_product_dao(product_id):
    query=''''''
    params = []
    try:
        for p in db:
            if p['id'] == int(product_id):
                return p
        return {}
    except Exception as e:
        log.error("Some exception occured: "+str(e))
