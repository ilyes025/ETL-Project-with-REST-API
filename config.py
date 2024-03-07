# MsSql pre_prod server
import os

MSSQL_SERVER = "****"
MSSQL_DB = "****"
PORT = "****"

# table
REVENUE_TABLE = 'test_revenue_table'
NUMBER_PRODUCT_TABLE = 'test_number_product'

# Data directory
DATA_DIR = os.path.join(os.path.dirname(__file__), "logs")
