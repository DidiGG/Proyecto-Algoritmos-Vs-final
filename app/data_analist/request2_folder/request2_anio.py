import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo CSV limpio
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Proyecto-Algoritmos-Vs-final/refs/heads/main/data/final_csv/bases_unificadas_ok.csv"

# Cargar el archivo CSV
df = pd.read_csv(archivo_csv)

# Agrupar por año de publicación y contar el número de artículos
articulos_por_ano = df['Publication Year'].value_counts().reset_index()
articulos_por_ano.columns = ['Año', 'Cantidad de Artículos']

# Ordenar por la cantidad de artículos y seleccionar los primeros 5 años
top_5_anos = articulos_por_ano.sort_values(by='Cantidad de Artículos', ascending=False).head(5)

# Crear la gráfica de barras
plt.figure(figsize=(10, 5))
plt.bar(top_5_anos['Año'].astype(str), top_5_anos['Cantidad de Artículos'], color='lightgreen')
plt.xlabel('Año de Publicación')
plt.ylabel('Cantidad de Artículos')
plt.title('Top 5 Años con Más Artículos Publicados')
plt.show()
