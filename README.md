
# BIGDATA_ELT

## Descripción
Este proyecto implementa un pipeline ETL (Extract, Transform, Load) y análisis exploratorio de datos (EDA) sobre un archivo CSV de noticias y etiquetas.

## Estructura
- `Main.py`: Ejecuta el pipeline ETL completo.
- `eda.py`: Genera y guarda 5 gráficas de análisis exploratorio en la carpeta `Data`.
- `Data/`: Carpeta donde se encuentra el archivo CSV y donde se almacenan las gráficas generadas.

## Requisitos
- Python 3.12+
- Instalar dependencias:

```bash
pip install pandas matplotlib seaborn
```

## Uso local

### 1. Ejecutar el pipeline ETL
Ejecuta el archivo principal para extraer, transformar y cargar los datos en una base de datos SQLite:

```bash
python Main.py
```

### 2. Generar gráficas de análisis exploratorio (EDA)
Ejecuta el script de EDA para crear y guardar las gráficas en la carpeta `Data`:

```bash
python eda.py
```

Las gráficas se guardarán como archivos PNG en la carpeta `Data`.

## Uso con Docker

Se incluye un `Dockerfile` y `docker-compose.yml` para ejecutar el pipeline y el EDA dentro de un contenedor.

Construir la imagen:

```bash
docker build -t bigdata_elt:latest .
```

Ejecutar el contenedor (ejecuta ETL y EDA automáticamente):

```bash
docker run --rm -v "$(pwd)/Data:/app/Data" bigdata_elt:latest
```

O con docker-compose (útil para desarrollo):

```bash
docker-compose up --build
```

Nota: Se monta `./Data` para que las gráficas y la base de datos queden en tu máquina host.

## Resultados
Las gráficas generadas incluyen:
- Distribución de la columna `Label`
- Registros por año
- Registros por mes
- Suma de `Label` por año (si es numérica)
- Heatmap de correlación entre columnas numéricas

## Autor
AlejandroR700
