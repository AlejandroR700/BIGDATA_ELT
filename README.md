
# BIGDATA_ELT

DESCRIPCION
Este proyecto implementa un pipeline ETL (Extract, Transform, Load) y análisis exploratorio de datos (EDA) sobre un archivo CSV de noticias y etiquetas.

ESTRUCTURA
- Main.py: Ejecuta el pipeline ETL completo.
- eda.py: Genera y guarda 5 gráficas de análisis exploratorio en la carpeta `Data`.
- Data/: Carpeta donde se encuentra el archivo CSV y donde se almacenan las gráficas generadas.

REQUISITOS
- Python 3.12+
- Instalar dependencias:
	pip install pandas matplotlib seaborn

COMO SE USA?

1. Ejecutar el pipeline ETL
Ejecuta el archivo principal para extraer, transformar y cargar los datos en una base de datos SQLite:
python Main.py

2. Generar gráficas de análisis exploratorio (EDA)
Ejecuta el script de EDA para crear y guardar las gráficas en la carpeta `Data`:
```bash
python eda.py
```
Las gráficas se guardarán como archivos PNG en la carpeta `Data`.

RESULTADOS
Las gráficas generadas incluyen:
- Distribución de la columna Label
- Registros por año
- Registros por mes
- Suma de Label por año (si es numérica)
- Heatmap de correlación entre columnas numéricas
