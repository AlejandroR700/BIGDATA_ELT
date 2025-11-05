FROM python:3.12-slim

WORKDIR /app

# Copiar el proyecto
COPY . /app

# Instalar dependencias necesarias para el ETL y EDA
RUN pip install --no-cache-dir pandas matplotlib seaborn

# Asegurar que exista la carpeta donde se almacenará la BD y gráficas
RUN mkdir -p /app/data

# Dar permisos al entrypoint (se creará junto al COPY)
RUN chmod +x /app/docker-entrypoint.sh || true

ENTRYPOINT ["/app/docker-entrypoint.sh"]
