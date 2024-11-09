import pandas as pd
import os

# Cargar el archivo CSV a limpiar
archivo_csv = r"C:\Users\didie\OneDrive\Documents\GitHub\Proyecto-Algoritmos-Vs-final\data\final_csv\archivo_csv_unificado.csv"
df = pd.read_csv(archivo_csv)

# Eliminar registros duplicados
df_limpio = df.drop_duplicates(subset=["Título", "DOI"])

# Mostrar el número de filas antes y después de eliminar duplicados
print(f"Número de filas antes de eliminar duplicados: {len(df)}")
print(f"Número de filas después de eliminar duplicados: {len(df_limpio)}")

# Definir la ruta de destino para el archivo limpio, asegurándote de especificar el nombre completo
archivo_limpio = r"C:\Users\didie\OneDrive\Documents\GitHub\Proyecto-Algoritmos-Vs-final\data\final_csv\bases_unificadas_ok.csv"

# Guardar el DataFrame limpio en un nuevo archivo CSV
df_limpio.to_csv(archivo_limpio, index=False)

print(f"Dataset limpio guardado en '{archivo_limpio}'")
