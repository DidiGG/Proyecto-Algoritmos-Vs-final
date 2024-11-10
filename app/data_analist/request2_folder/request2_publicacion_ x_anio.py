import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo CSV limpio
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Proyecto-Algoritmos-Vs-final/refs/heads/main/data/final_csv/bases_unificadas_ok.csv"

# Cargar el archivo CSV
df = pd.read_csv(archivo_csv)

# Asegúrate de que la columna 'Autores' esté separada correctamente
df["Autores"] = df["Autores"].str.split(", ")

# Expandir los autores en filas individuales
df_exploded = df.explode("Autores")

# Contar el número de publicaciones por autor
conteo_publicaciones = df_exploded['Autores'].value_counts().head(15).index

# Filtrar el DataFrame para solo incluir los 15 autores más prolíficos
df_top_autores = df_exploded[df_exploded['Autores'].isin(conteo_publicaciones)]

# Contar las publicaciones por autor y año
publicaciones_por_autor_ano = df_top_autores.groupby(['Autores', 'Publication Year']).size().unstack(fill_value=0)

# Crear la gráfica de líneas
plt.figure(figsize=(14, 8))
for autor in publicaciones_por_autor_ano.index:
    plt.plot(publicaciones_por_autor_ano.columns, publicaciones_por_autor_ano.loc[autor], marker='o', label=autor)

plt.xlabel('Año de Publicación')
plt.ylabel('Cantidad de Publicaciones')
plt.title('Cantidad de Publicaciones a lo Largo de los Años')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
