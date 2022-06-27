from psycopg2 import pool
from . import DBconfig
import logging

log = logging.getLogger('DBCONNECTION')


class DBInitiateConnection(object):
    _instance = None

    def __init__(self):
        if DBInitiateConnection._instance is None:
            try:
                DBInitiateConnection._instance = pool.ThreadedConnectionPool(
                    10, 100, user=DBconfig.user,
                    password=DBconfig.db_pass,
                    host=DBconfig.host,
                    port=DBconfig.port,
                    database=DBconfig.database)

                log.info("Connected to the database!")
            except Exception as ex:
                log.error(ex)

    def __getattr__(self, aAttr):
        return getattr(self._instance, aAttr)

    def __setattr__(self, aAttr, aValue):
        return setattr(self._instance, aAttr, aValue)


class DBConnection:

    """Method to get the connection pool from the given instance."""
    def getConnectionPool(self):
        self.dbConnectionPool = DBInitiateConnection()._instance
        return self.dbConnectionPool

    """Method to get the connection from a given pool."""
    def getConnection(self):
        connectionPool = self.getConnectionPool()
        return connectionPool.getconn()

    """Method to commit the connection, given connection object as input.
    Mandatory to call this method after any insertion or updation
    or delete to ensure that data is persisted in database successfully.
    """
    def commit(self, connection):
        connection.commit()

    """Method to close the connection opened to execute respective queries,
    input is connection object"""
    def close(self, connection):
        connectionPool = self.getConnectionPool()
        connectionPool.putconn(connection, close=True)

    def closeAll(self):
        connectionPool = self.getConnectionPool()
        connectionPool.closeall()

    def delete(self, query, connection):
        cursor = connection.cursor()
        cursor.execute(query)
        self.commit(connection)
