# File: main.py

# Import necessary libraries
from src.etl.csv_loader import load_csv
from src.etl.data_cleaner import clean_data
from src.etl.kpi_calculator import calculate_kpi
from src.etl.db_saver import save_to_sqlite
from src.etl.visualise_kpi_data import visualise_data
from src.etl.config import RAW_DATA_PATH, DB_PATH

if __name__ == "__main__":
    file_path = RAW_DATA_PATH
    df = load_csv(file_path)
    print("\n--- Preview of Loaded Data ---")
    print(df.head())

    cleaned_df = clean_data(df)
    print("\n--- Preview of Cleaned Data ---")
    print(cleaned_df.head())
    cleaned_df.to_csv("data/processed/cleaned_sales.csv", index=False)

    kpi_df = calculate_kpi(cleaned_df)
    print("\n--- Preview of Calculated KPIs ---")
    print(kpi_df.head())

    print("\n--- Preview of SQLite Data ---")
    db_path = DB_PATH
    save_to_sqlite(cleaned_df, kpi_df, db_path)

    visualise_data(db_path)
