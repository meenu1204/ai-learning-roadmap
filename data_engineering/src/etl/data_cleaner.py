# File: data_cleaner.py

# Import needed libraries
import  pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
        Clean Pandas DataFrame.

        Args:
            pd.DataFrame.

        Returns:
            pd.DataFrame: Cleaned DataFrame.
        """
    cleaned_df = df.copy(deep=True)
    print("\n--- Handle missing prices ---")
    cleaned_df = cleaned_df.dropna(subset=["price"])

    print("\n--- Remove duplicates ---")
    cleaned_df = cleaned_df.drop_duplicates()

    print("\n--- Standardise data ---")
    cleaned_df["product"] = cleaned_df["product"].str.lower()

    print("\n--- Addition of new column ---")
    cleaned_df["quantity"] = np.random.randint(1, 6, size=len(cleaned_df))
    cleaned_df["total"] = cleaned_df["price"] * cleaned_df["quantity"]

    return cleaned_df
