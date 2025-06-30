# File: csv_loader.py

# Import needed libraries
import  pandas as pd
from typing import Union

def load_csv(input_file: Union[str, bytes]) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame with basic exploration.

    Args:
        input_file (str or bytes): Path to the input CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {input_file} not found")
    except ValueError:
        raise ValueError()

    print("\n--- CSV Loaded Successfully ---")
    # Explore structure
    print(f"Initial rows:\n {df.head()}")
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns}")
    print("\n--- Data Types ---")
    print(df.dtypes)
    # Identified missing data
    print("\n--- Missing Values ---")
    print(df.isnull().sum())
    return df
