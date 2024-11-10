import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo CSV limpio
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Proyecto-Algoritmos-Vs-final/refs/heads/main/data/final_csv/bases_unificadas_ok.csv"

# Cargar el archivo CSV
df = pd.read_csv(archivo_csv)

# Contar la cantidad de documentos por tipo
conteo_tipos = df['Tipo'].value_counts().reset_index()
conteo_tipos.columns = ['Tipo', 'Cantidad']

# Crear la gráfica de barras
plt.figure(figsize=(12, 6))
plt.barh(conteo_tipos['Tipo'], conteo_tipos['Cantidad'], color='lightblue')
plt.xlabel('Cantidad de Documentos')
plt.ylabel('Tipo de Documento')
plt.title('Distribución de Tipos de Documentos')
plt.gca().invert_yaxis()  # Invertir el eje para que el tipo con más documentos esté arriba
plt.show()
