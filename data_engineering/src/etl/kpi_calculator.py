# File: kpi_calculator.py

# Import needed libraries
import pandas as pd

def calculate_kpi(cleaned_df):
    """
            Calculate KPIs: Total sales per product, Average price per product, Number of orders per product

            Args:
                Cleaned pd.DataFrame.

            Returns:
                KPI pd.DataFrame.
            """
    kpi_df = cleaned_df.groupby("product").agg(
        total_sales=("price", "sum"),
        avg_price=("price", "mean"),
        num_orders=("price", "count")
    ).reset_index()

    return kpi_df
