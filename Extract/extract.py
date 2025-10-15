import pandas as pd

def extract_data(file_path):
    # Lee datos de un archivo CSV con encoding latin1 para evitar errores de decodificación
    df = pd.read_csv(file_path, encoding='latin1')
    return df