import os
import pandas as pd

# Directorio donde están los archivos CSV
directorio_csv = r"C:\Users\didie\OneDrive\Documents\GitHub\Proyecto-Algoritmos-Vs-final\data\inicial_csv"

# Ruta de destino donde se guardará el archivo CSV combinado
directorio_destino = r"C:\Users\didie\OneDrive\Documents\GitHub\Proyecto-Algoritmos-Vs-final\data\final_csv"

# Lista de todos los archivos CSV en el directorio
archivos_csv = [f for f in os.listdir(directorio_csv) if f.endswith(".csv")]

# Definir los encabezados estándar que quieres para todos los archivos
encabezados_estandar = [
    "Título",
    "Autores",
    "Revista",
    "ISSN",
    "Fecha Publicacion",
    "DOI",
    "Palabras Clave",
    "Volumen",
    "Asunto",
    "Primera Pagina",
    "Paginas",
    "Publisher",
    "Tipo",
    "Abstract",
    "Link",
]

# Diccionario de mapeo de nombres de columnas con listas de variantes
mapeo_columnas = {
    "Título": ["Title", "Article Title", "title"],
    "Autores": ["Author", "Authors"],
    "Revista": ["Journal Title", "Source title", "journal"],
    "ISSN": ["ISSN"],
    "Fecha Publicacion": ["Publication Date", "Year"],
    "Volumen": ["Volume", "volume"],
    "Asunto": ["Issue", "issn"],
    "Primera Pagina": ["First Page", "Page start"],
    "Paginas": ["Page Count", "Page count", "pages"],
    "DOI": ["DOI", "doi"],
    "Publisher": ["Publisher"],
    "Tipo": ["Doctype", "Document Type"],
    "Palabras Clave": ["Keywords", "Author Keywords", "keywords"],
    "Abstract": ["Abstract", "abstract"],
    "Link": ["PLink", "Link", "URL", "url"],
}

# Lista para almacenar los DataFrames de cada archivo CSV
dataframes = []

# Cargar cada archivo CSV y asegurar que tenga todas las columnas necesarias
for archivo in archivos_csv:
    ruta_completa = os.path.join(directorio_csv, archivo)
    df = pd.read_csv(ruta_completa)

    # Imprimir las columnas del archivo para verificar
    print(f"Columnas en {archivo}: {df.columns.tolist()}")

    # Renombrar columnas según el mapeo definido
    for estandar, variantes in mapeo_columnas.items():
        for variante in variantes:
            if variante in df.columns:
                df.rename(columns={variante: estandar}, inplace=True)
                break  # Solo renombrar la primera variante encontrada

    # Verificar si todas las columnas estándar están presentes
    columnas_presentes = [col for col in encabezados_estandar if col in df.columns]
    if len(columnas_presentes) == len(encabezados_estandar):
        df = df[columnas_presentes].dropna(
            how="all"
        )  # Elimina filas donde todas las columnas son NaN
    else:
        print(
            f"Advertencia: Algunas columnas estándar faltan en el archivo {archivo}. Columnas presentes: {columnas_presentes}"
        )

    # Agregar el DataFrame a la lista después de asegurarse que tenga solo las columnas deseadas
    if not df.empty:  # Solo agregar DataFrame no vacío
        dataframes.append(df)

# Combinar todos los DataFrames en uno solo
df_final = pd.concat(dataframes, ignore_index=True, sort=False)

# Definir la ruta completa del archivo final
ruta_destino_completa = os.path.join(directorio_destino, "archivo_csv_unificado.csv")

# Crear el directorio de destino si no existe
if not os.path.exists(directorio_destino):
    os.makedirs(directorio_destino)

# Guardar el DataFrame combinado en un nuevo archivo CSV
df_final.to_csv(ruta_destino_completa, index=False)

print(
    f"¡Todos los archivos CSV han sido combinados y guardados en '{ruta_destino_completa}'!"
)
