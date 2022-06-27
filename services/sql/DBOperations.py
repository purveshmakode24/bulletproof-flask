import logging
from . import ConnectionManager
log = logging.getLogger('DBOPERATIONS')

class DBOperations:
    """Database Operations"""

    def runSelectQuery(self, query, params):
        """Execute Select Query"""
        result = None
        connection=None
        try:
            connection = ConnectionManager.DBConnection().getConnection()
            cursor = connection.cursor()

            # if params_map is None:
            #     cursor.execute(query)
            # else:
            #     cursor.execute(query, params_map)

            cursor.execute(query, params)

            if cursor.rowcount > 0:
                """cursor.fetchall() -> 
                Fetch all rows of a query result set and returns a list of tuples.
                If no more rows are available, it returns an empty list."""
                result = cursor.fetchall()

        except Exception as e:
            log.info("Some execption occured:"+str(e))

        finally:
            if connection is not None:
                ConnectionManager.DBConnection().close(connection)

        """Fetch all rows of a query result set and returns a list of tuples.
        If no more rows are available, it returns Null."""
        return result
    

    def runInsertQuery(self, query, params_map=None):
        pass


    def runUpdateQuery(self, query, params_map=None):
        pass


    def runDeleteQuery(self, query, params_map=None):
        pass

    