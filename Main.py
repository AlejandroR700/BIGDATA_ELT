from Config.config import DB_PATH
from Extract.extract import extract_data
from Transform.transform import transform_data
from Load.load import load_data

def main():
    # Ruta del archivo CSV
    file_path = "Data/stock_senti_analysis.csv"
    table_name = "mi_tabla"

    # ETL pipeline
    data = extract_data(file_path)
    data_transformed = transform_data(data)
    load_data(data_transformed, DB_PATH, table_name)
    print("ETL completado correctamente")

if __name__ == "__main__":
    main()
    