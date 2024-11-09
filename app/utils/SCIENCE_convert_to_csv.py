import bibtexparser
import csv
import os


# Función para convertir y guardar un archivo .bib como .csv en una carpeta específica
def convertir_bib_a_csv(ruta_bib, carpeta_salida):
    # Leer el archivo .bib
    with open(ruta_bib, "r", encoding="utf-8") as bib_file:
        bib_database = bibtexparser.load(bib_file)

    # Definir la ruta del archivo .csv de salida
    nombre_csv = os.path.splitext(os.path.basename(ruta_bib))[0] + ".csv"
    ruta_csv = os.path.join(carpeta_salida, nombre_csv)

    # Escribir en formato .csv
    with open(ruta_csv, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        # Encabezados
        writer.writerow(
            [
                "title",
                "journal",
                "volume",
                "pages",
                "year",
                "issn",
                "doi",
                "url",
                "author",
                "keywords",
                "abstract",
            ]
        )

        # Escribir cada entrada del archivo .bib
        for entry in bib_database.entries:
            writer.writerow(
                [
                    entry.get("title", ""),
                    entry.get("journal", ""),
                    entry.get("volume", ""),
                    entry.get("pages", ""),
                    entry.get("year", ""),
                    entry.get("issn", ""),
                    entry.get("doi", ""),
                    entry.get("url", ""),
                    entry.get("author", ""),
                    entry.get("keywords", ""),
                    entry.get("abstract", ""),
                ]
            )

    print(f"Archivo .csv guardado en: {ruta_csv}")


# Función para recorrer todos los archivos .bib en una carpeta
def convertir_varios_bib_a_csv(carpeta_entrada, carpeta_salida="output"):
    # Verificar si la carpeta de salida existe; si no, crearla
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Recorrer los archivos en la carpeta de entrada
    for archivo in os.listdir(carpeta_entrada):
        if archivo.endswith(".bib"):
            ruta_bib = os.path.join(carpeta_entrada, archivo)
            convertir_bib_a_csv(ruta_bib, carpeta_salida)


# Llama a la función especificando la carpeta de entrada y la de salida
convertir_varios_bib_a_csv(
    r"C:\Users\didie\OneDrive\Documents\Bases de datos Algoritmos\bases vf\ScienceDirect",
    r"C:\Users\didie\OneDrive\Documents\GitHub\Proyecto-Algoritmos-Vs-final\data\inicial.csv",
)
