
# ETL Project with REST API

## Overview

This project is an Extract, Transform, Load (ETL) pipeline implemented in Python. It extracts data from CSV files containing order information and product prices, transforms the data to calculate monthly revenue and quantity of products sold, and loads the transformed data into SQL Server database tables. Additionally, a REST API is developed to retrieve data from the database tables.

## Components

1. **ETL Script**: The ETL script is responsible for extracting data from CSV files (`product_prices.csv` and `orders_data.csv`), transforming the data to calculate monthly revenue and quantity of products sold, and loading the transformed data into SQL Server database tables.

2. **CSV Files**:
   - `product_prices.csv`: Contains the prices of different products.
   - `orders_data.csv`: Contains order information including the date, product, and quantity sold during the year 2023.

3. **SQL Server Database Tables**:
   - `test_revenue_table`: Stores monthly revenue data.
   - `test_number_product`: Stores quantity of products sold per month.

4. **REST API**: The REST API is developed in Python using Flask. It provides endpoints to access data from the database tables. One of the endpoints returns the top 10 records from a specified table.

## Usage

1. **Setup Environment**:
   - Ensure Python and required libraries (`pandas`, `flask`, `pyodbc`) are installed.
   - Ensure SQL Server is installed and accessible.

2. **Data Extraction**:
   - Place `product_prices.csv` and `orders_data.csv` in the designated directory.
   - Run the ETL script to extract data from CSV files.

3. **Data Transformation**:
   - The ETL script transforms the extracted data to calculate monthly revenue and quantity of products sold.

4. **Data Loading**:
   - The transformed data is loaded into SQL Server database tables (`test_revenue_table` and `test_number_product`).

5. **REST API**:
   - Run the Flask application to start the REST API server.
   - Access the API endpoints to retrieve data from the database tables.

## API Endpoints

- `Get /read/first-chunck`: Returns the top 10 records from the specified table.

## Example

To retrieve the top 10 records from `test_revenue_table`, make a GET request to `http://127.0.0.1:5000/read/first-chunk`.

## Dependencies

- Python 3.9
- pandas
- Flask
- pyodbc


## How to run 
First of all, you have to install pipenv and create a virtual environment based on `pipfile`.
After that, you have to put your sql server parameters : `MSSQL_SERVER`, `MSSQL_DB` and `PORT` in the `config.py` file.
Finally, you have to run the main with parameters (`sql_username`, `sql_password`).

## Author
ILYES TRABELSI
