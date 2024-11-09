import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import re

# Ruta del archivo CSV limpio
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Proyecto-Algoritmos-Vs-final/refs/heads/main/data/final_csv/bases_unificadas_ok.csv"

# Cargar el archivo CSV
df = pd.read_csv(archivo_csv)

# Mostrar las primeras filas para asegurarnos de que las columnas son correctas
print(df.head())

# Cargar la base de datos
file_path = archivo_csv
data = pd.read_csv(file_path)

# Definir palabras clave para cada categoría
categories_keywords = {
    "Habilidades": [
        "abstraction",
        "algorithm",
        "algorithmic thinking",
        "coding",
        "collaboration",
        "cooperation",
        "creativity",
        "critical thinking",
        "debug",
        "decomposition",
        "evaluation",
        "generalization",
        "logic",
        "logical thinking",
        "modularity",
        "pattern recognition",
        "problem solving",
        "programming",
        "representation",
        "reuse",
        "simulation",
    ],
    "Conceptos Computacionales": [
        "conditionals",
        "control structures",
        "directions",
        "events",
        "functions",
        "loops",
        "modular structure",
        "parallelism",
        "sequences",
        "software",
        "hardware",
        "variables",
    ],
    "Actitudes": [
        "emotional",
        "engagement",
        "motivation",
        "perceptions",
        "persistence",
        "self-efficacy",
        "self-perceived",
    ],
    "Propiedades Psicométricas": [
        "classical test theory",
        "confirmatory factor analysis",
        "exploratory factor analysis",
        "item response theory",
        "reliability",
        "structural equation model",
        "validity",
    ],
    "Herramienta de Evaluación": [
        "bctt",
        "escas",
        "cctt",
        "ctst",
        "cta-ces",
        "ctc",
        "ctls",
        "cts",
        "ctt-es",
        "ctt-lp",
        "capct",
        "ict competency test",
        "general self-efficacy scale",
        "stem-las",
    ],
    "Diseño de Investigación": [
        "experimental",
        "longitudinal research",
        "mixed methods",
        "post-test",
        "pre-test",
        "quasi-experiments",
        "non-experimental",
    ],
    "Nivel de Escolaridad": [
        "upper elementary education",
        "primary school",
        "early childhood education",
        "secondary school",
        "high school",
        "university",
        "college",
    ],
    "Medio": [
        "block programming",
        "mobile application",
        "pair programming",
        "plugged activities",
        "programming",
        "robotics",
        "spreadsheet",
        "stem",
        "unplugged activities",
    ],
    "Estrategia": [
        "construct-by-self mind mapping",
        "design-based learning",
        "gamification",
        "reverse engineering",
        "technology-enhanced learning",
        "collaborative learning",
        "cooperative learning",
        "flipped classroom",
        "game-based learning",
        "inquiry-based learning",
        "personalized learning",
        "problem-based learning",
        "project-based learning",
        "universal design for learning",
    ],
}

# Inicializar el conteo de cada categoría
category_counts = {category: 0 for category in categories_keywords.keys()}

# Procesar cada abstract para clasificarlo en las categorías
for abstract in data["Abstract"].dropna().str.lower():  # Ignorar valores nulos
    # Dividir en palabras y filtrar por cada categoría
    words = re.findall(r"\b\w+\b", abstract)  # Lista de palabras individuales
    for category, keywords in categories_keywords.items():
        # Contar cuántas palabras clave de cada categoría aparecen en el abstract
        if any(keyword in words for keyword in keywords):
            category_counts[category] += 1

# Mostrar el conteo por categoría
print("Conteo de artículos por categoría:", category_counts)

# Generar gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(category_counts.keys(), category_counts.values(), color="skyblue")
plt.xlabel("Categorías")
plt.ylabel("Número de artículos")
plt.title("Distribución de artículos por categorías de palabras clave")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
