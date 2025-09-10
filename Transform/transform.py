def transform_data(df):
    # Por ejemplo: eliminar filas con valores nulos
    df_clean = df.dropna()
    # Convertir columna 'fecha' a datetime si existe
    if 'fecha' in df_clean.columns:
        df_clean['fecha'] = pd.to_datetime(df_clean['fecha'])
    return df_clean