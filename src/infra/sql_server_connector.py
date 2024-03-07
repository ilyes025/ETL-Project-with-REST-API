import logging
import pandas as pd
from sqlalchemy import create_engine

logger = logging.getLogger()


class DatabaseHelper:
    """ a class used for handling with sql server databases"""

    def __init__(self, connection_string):
        """
        Constructor for CSVHelper.

        :param connection_string: a connection string.
        :type connection_string: str
        """
        self.engine = create_engine(connection_string, use_setinputsizes=False, echo=True)

    def read_data(self, query):
        """
        Read logs from database.
        :param query: a sql query that contains filters.
        :type query: str
        :return: DataFrame containing the logs extracted from sql query.
        :rtype: pandas.DataFrame
        """
        data = pd.read_sql(query, self.engine)
        return data

    def insert_dataframe(self, data, table_name):
        """
        Insert into database table a dataframe.
        :param data: logs will be inserted.
        :type query: pandas.DataFrame
        """
        data.to_sql(table_name, self.engine, if_exists='append', index=False)
