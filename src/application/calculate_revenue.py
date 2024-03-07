import pandas as pd


def calculate_revenue(df_price_product, df_orders):
    """
    calculate product sell per month and the toal revenue per month
    :param df_price_product: contains price of product.
    :type pandas.DataFrame
    :param df_orders: contains orders logs.
    :type pandas.DataFrame
    :return: production_sold_df : number of production sold each month.
    :rtype: pandas.DataFrame
    :return: monthly_revenue : the revenue per month.
    :rtype: pandas.DataFrame
    """
    # Merge dataframes based on product
    merged_df = pd.merge(df_orders, df_price_product, on='product')
    # Calculate revenue
    merged_df['revenue'] = merged_df['quantity'] * merged_df['price']

    # Convert order_date to datetime
    merged_df['order_date'] = pd.to_datetime(merged_df['order_date'])

    # Group by product and month and aggregate sum
    product_monthly_sales = merged_df.groupby(['product', merged_df['order_date'].dt.month]).agg({
        'quantity': 'sum',
        'revenue': 'sum'
    }).reset_index()

    # Rename month column
    product_monthly_sales.rename(columns={'order_date': 'month'}, inplace=True)

    # Separate dataframe for the number of productions sold in each month
    production_sold_df = product_monthly_sales[['product', 'month', 'quantity']].copy()

    # Separate dataframe for the revenue of each month
    monthly_revenue = product_monthly_sales[['month', 'revenue']].groupby(['month']).agg({
        'revenue': 'sum'
    }).reset_index()
    return production_sold_df, monthly_revenue



