import logging
import os
import sys

from flask import Flask, jsonify

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
fileHandler = logging.FileHandler(f"{os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')}/log_api.log")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)
logger = logging.getLogger()

sql_username = sys.argv[1]
sql_password = sys.argv[2]

app = Flask(__name__)

logger.info("Connecting to sql server...")
connection_string_remote = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver=SQL+Server'.format(sql_username, sql_password,
                                                                                    MSSQL_SERVER,
                                                                                    PORT, MSSQL_DB)
data_connector_remote = DatabaseHelper(connection_string=connection_string_remote)
logger.info("Sql server is ready")


# Endpoint to get the first chunk of logs
@app.route('/read/first-chunk')
def get_first_chunk():
    chunk_size = 10  # Define the chunk size
    first_chunk = data_connector_remote.read_data(f"select top({chunk_size}) * from {NUMBER_PRODUCT_TABLE}")
    return jsonify({"first_chunk": first_chunk.to_dict(orient='records')})


if __name__ == '__main__':
    app.run(debug=True)
