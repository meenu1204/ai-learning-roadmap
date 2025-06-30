import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from src.etl.config import OUTPUT_PLOT_PATH

def visualise_data(db_path):
    conn = sqlite3.connect(db_path)
    plot_df = pd.read_sql(f"SELECT * FROM sales_kpis", conn)
    conn.close()

    plt.figure(figsize=(8, 5))
    plot_df.set_index("product")["total_sales"].sort_values().plot(kind='bar')
    plt.title("Total Sales per Product")
    plt.ylabel("Sales ($)")
    plt.xlabel("Product")
    plt.tight_layout()
    plt.savefig(OUTPUT_PLOT_PATH)
    plt.show()