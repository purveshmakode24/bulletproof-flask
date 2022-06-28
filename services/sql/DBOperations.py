import logging
from . import ConnectionManager
log = logging.getLogger('DBOPERATIONS')


class DBOperations:
    """Database Operations"""

    def runSelectQuery(self, query, params):
        """Execute Select Query"""
        result = None
        connection = None
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
                Fetch all rows of a query result set
                and returns a list of tuples.
                If no more rows are available, it returns an empty list."""
                result = cursor.fetchall()
        except Exception as e:
            log.error("Some execption occured:"+str(e))
        finally:
            if connection is not None:
                ConnectionManager.DBConnection().close(connection)

        """Fetch all rows of a query result set and returns a list of tuples.
        If no more rows are available, it returns Null."""
        return result

    def runInsertQuery(self, query, params):
        """Execute Insert Query"""
        result = True
        connection = None
        try:
            connection = ConnectionManager.DBConnection().getConnection()
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
        except Exception as e:
            log.error("Some execption occured:"+str(e))
            result = False
        finally:
            if connection is not None:
                ConnectionManager.DBConnection().close(connection)
        """Returns True if Insert Query successfully executed,
        else it returns False."""
        return result

    def runUpdateQuery(self, query, params):
        """Execute Update Query"""
        result = True
        connection = None
        try:
            connection = ConnectionManager.DBConnection().getConnection()
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
        except Exception as e:
            log.error("Some execption occured:"+str(e))
            result = False
        finally:
            if connection is not None:
                ConnectionManager.DBConnection().close(connection)
        """Returns True if Update Query successfully executed,
        else it returns False."""
        return result

    def runDeleteQuery(self, query, params):
        """Execute Delete Query"""
        result = True
        connection = None
        try:
            connection = ConnectionManager.DBConnection().getConnection()
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
        except Exception as e:
            log.error("Some execption occured:"+str(e))
            result = False
        finally:
            if connection is not None:
                ConnectionManager.DBConnection().close(connection)
        """Returns True if Delete Query successfully executed,
        else it returns False."""
        return result
