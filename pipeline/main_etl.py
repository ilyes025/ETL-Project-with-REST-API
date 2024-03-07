import os
import logging
import sys
from datetime import datetime

from src.application.calculate_revenue import calculate_revenue
from src.infra.csv_reader import CSVHelper
from src.infra.infra_utils import check_create_dir
from src.infra.sql_server_connector import DatabaseHelper
from config import (
    REVENUE_TABLE,
    NUMBER_PRODUCT_TABLE,
    MSSQL_SERVER,
    MSSQL_DB,
    PORT,
    DATA_DIR
)  # noqa: E402

logFormatter = logging.Formatter("%(asctime)s [%(module)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)
check_create_dir(DATA_DIR)
fileHandler = logging.FileHandler(f"{os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')}/log.log")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)
logger = logging.getLogger()


def main(sql_username, sql_password):
    """main"""
    logger.info("Connecting to sql server...")
    connection_string_remote = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver=SQL+Server'.format(sql_username, sql_password,
                                                                                        MSSQL_SERVER,
                                                                                        PORT, MSSQL_DB)
    data_connector_remote = DatabaseHelper(connection_string=connection_string_remote)
    logger.info("Sql server is ready")

    logger.info("Extracting csv files...")
    csv_reader_orders = CSVHelper(f"{os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data-access')}\\orders_data.csv")
    csv_reader_prices = CSVHelper(f"{os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data-access')}\\product_prices.csv")
    df_orders = csv_reader_orders.read_csv_to_dataframe()
    df_prices = csv_reader_prices.read_csv_to_dataframe()
    logger.info("Csv files are extracted successfully!")

    logger.info("Calculating the revenue and the number of sold products...")
    production_sold_df, monthly_revenue = calculate_revenue(df_prices, df_orders)
    logger.info("Revenue and number of sold products are calculated successfully!")

    logger.info("Loading calculated data in database...")
    data_connector_remote.insert_dataframe(production_sold_df, NUMBER_PRODUCT_TABLE)
    data_connector_remote.insert_dataframe(monthly_revenue, REVENUE_TABLE)
    logger.info("Robot files paths are retrieved successfully!")


if __name__ == '__main__':
    sql_username = sys.argv[1]
    sql_password = sys.argv[2]
    main(sql_username, sql_password)

