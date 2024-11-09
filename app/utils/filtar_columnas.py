import pandas as pd

# Cargar el archivo CSV
archivo_csv_url = "https://raw.githubusercontent.com/DidiGG/Proyecto-Algoritmos-Vs-final/refs/heads/main/data/final_csv/bases_unificadas_ok.csv"
df = pd.read_csv(archivo_csv_url)

# Definir el umbral de datos no nulos mínimo (en este caso, el 30%)
umbral = 0.3

# Calcular el porcentaje de datos no nulos en cada columna
porcentaje_datos_no_nulos = df.count() / len(df)

# Mantener solo las columnas con un porcentaje de datos no nulos mayor o igual al umbral
df_filtrado = df.loc[:, porcentaje_datos_no_nulos >= umbral]

# Definir la ruta específica donde se desea guardar el archivo CSV
ruta_guardado = r"C:\Users\didie\OneDrive\Documents\GitHub\Proyecto-Algoritmos-Vs-final\data\final_csv\archivo_csv_filtrado_columnas.csv"

# Guardar el DataFrame filtrado en la ruta específica
df_filtrado.to_csv(ruta_guardado, index=False)

print(f"Archivo CSV filtrado guardado en '{ruta_guardado}'")
