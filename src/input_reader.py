import pandas as pd
import os


def read_csv_file(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    try:
        data = pd.read_csv(file_path)
        return data

    except Exception as e:
        raise ValueError(f"Unable to read CSV: {e}")