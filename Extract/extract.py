import pandas as pd

def extract_data(file_path):
    # Lee datos de un archivo CSV
    df = pd.read_csv(file_path)
    return df