import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV con encoding latin1
file_path = "Data/stock_senti_analysis.csv"
df = pd.read_csv(file_path, encoding='latin1')

# 1. Conteo de valores de la columna Label (distribución de clases)
df['Label'].value_counts().plot(kind='bar', title='Distribución de la columna Label')
plt.xlabel('Label')
plt.ylabel('Cantidad')
plt.savefig('Data/eda_label_distribution.png')
plt.close()

# 2. Cantidad de registros por año
df['Date'] = pd.to_datetime(df['Date'])
df['Año'] = df['Date'].dt.year
df['Año'].value_counts().sort_index().plot(kind='bar', title='Cantidad de registros por año')
plt.xlabel('Año')
plt.ylabel('Cantidad')
plt.savefig('Data/eda_registros_por_ano.png')
plt.close()

# 3. Cantidad de registros por mes (acumulado)
df['Mes'] = df['Date'].dt.month
df['Mes'].value_counts().sort_index().plot(kind='bar', title='Cantidad de registros por mes')
plt.xlabel('Mes')
plt.ylabel('Cantidad')
plt.savefig('Data/eda_registros_por_mes.png')
plt.close()

# 4. Evolución temporal de la suma de Label por año (si Label es numérica)
if pd.api.types.is_numeric_dtype(df['Label']):
    df.groupby('Año')['Label'].sum().plot(title='Suma de Label por año')
    plt.xlabel('Año')
    plt.ylabel('Suma Label')
    plt.savefig('Data/eda_suma_label_por_ano.png')
    plt.close()
else:
    print('Label no es numérica, se omite gráfica de suma por año.')

# 5. Heatmap de correlación entre columnas numéricas
import seaborn as sns
num_cols = df.select_dtypes(include=['number'])
if not num_cols.empty:
    plt.figure(figsize=(10,6))
    sns.heatmap(num_cols.corr(), annot=True, cmap='coolwarm')
    plt.title('Heatmap de correlación entre columnas numéricas')
    plt.savefig('Data/eda_heatmap_correlacion.png')
    plt.close()
else:
    print('No hay columnas numéricas para mostrar correlación.')
