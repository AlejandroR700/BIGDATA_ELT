#!/bin/sh
set -e

# Crear directorio data si no existe
mkdir -p /app/data
mkdir -p /app/Data

echo "Iniciando pipeline ETL..."
python Main.py
echo "Pipeline ETL finalizado. Ejecutando EDA..."
python eda.py
echo "EDA finalizado. Las gráficas están en la carpeta Data."

exit 0