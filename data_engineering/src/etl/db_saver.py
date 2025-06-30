import sqlite3
import pandas as pd
from src.etl.config import TABLE_1_CLEANED, TABLE_2_KPI

def save_to_sqlite(cleaned_df, kpi_df, db_path):
    """
            Save pd.DataFrame to SQLite

            Args: Cleaned pd.DataFrame, kpi pd.DataFrame, path to db

                """
    conn = sqlite3.connect(db_path)
    cleaned_df.to_sql(TABLE1_CLEANED, conn, if_exists="replace", index=False)
    kpi_df.to_sql(TABLE2_KPI, conn, if_exists="replace", index=False)

    for table in [TABLE1_CLEANED, TABLE2_KPI]:
        print(f"\n--- Preview: {table} ---")
        print(pd.read_sql(f"SELECT * FROM {table}", conn).head())
    conn.close()

