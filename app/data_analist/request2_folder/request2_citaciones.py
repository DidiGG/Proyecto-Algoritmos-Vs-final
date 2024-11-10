import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo CSV limpio
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Proyecto-Algoritmos-Vs-final/refs/heads/main/data/final_csv/bases_unificadas_ok.csv"

# Cargar el archivo CSV
df = pd.read_csv(archivo_csv)

# Asegúrate de usar los nombres correctos de las columnas
df["Autores"] = df["Autores"].str.split(", ")

# Expandir los autores en filas individuales
df_exploded = df.explode("Autores")

# Agrupar por autor y sumar las citaciones
autores_citados = (
    df_exploded.groupby("Autores")["Article Citation Count"].sum().reset_index()
)

# Ordenar por citaciones en orden descendente
autores_citados = autores_citados.sort_values(
    by="Article Citation Count", ascending=False
)

# Mostrar los 15 autores más citados
top_15_autores = autores_citados.head(15)

# Crear la gráfica de barras
plt.figure(figsize=(12, 6))
plt.barh(
    top_15_autores["Autores"], top_15_autores["Article Citation Count"], color="skyblue"
)
plt.xlabel("Cantidad de Citaciones")
plt.ylabel("Autores")
plt.title("Top 15 Autores Más Citados")
plt.gca().invert_yaxis()
plt.show()
