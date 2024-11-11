import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo CSV limpio
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Proyecto-Algoritmos-Vs-final/refs/heads/main/data/final_csv/bases_unificadas_ok.csv"

# Cargar el archivo CSV
df = pd.read_csv(archivo_csv)

# Filtrar las filas donde la columna 'Author Affiliations' no sea nula, no esté vacía y no contenga 'NA' como texto
df = df[
    df["Author Affiliations"].notna() & 
    (df["Author Affiliations"].str.strip() != "") & 
    (df["Author Affiliations"].str.upper() != "NA")
]

# Contar la cantidad de autores por institución
conteo_instituciones = df["Author Affiliations"].value_counts().reset_index()
conteo_instituciones.columns = ["Author Affiliations", "Cantidad de Autores"]

# Filtrar solo las instituciones relevantes (excluyendo posibles 'NA' o vacíos)
conteo_instituciones = conteo_instituciones[
    ~conteo_instituciones["Author Affiliations"].str.upper().isin(["NA", ""])
]

# Tomar las 10 instituciones principales
conteo_instituciones = conteo_instituciones.head(10)

# Crear la gráfica de barras
plt.figure(figsize=(12, 6))
plt.barh(
    conteo_instituciones["Author Affiliations"],
    conteo_instituciones["Cantidad de Autores"],
    color="lightcoral",
)
plt.xlabel("Cantidad de Autores")
plt.ylabel("Institución")
plt.title("Top 10 Instituciones con Mayor Cantidad de Autores")
plt.gca().invert_yaxis()  # Invertir el eje para que la institución con más autores esté arriba
plt.show()
