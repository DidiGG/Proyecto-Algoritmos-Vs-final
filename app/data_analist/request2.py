import pandas as pd
from collections import defaultdict
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
        "abstraction", "algorithm", "algorithmic thinking", "coding", "collaboration", "cooperation",
        "creativity", "critical thinking", "debug", "decomposition", "evaluation", "generalization",
        "logic", "logical thinking", "modularity", "pattern recognition", "problem solving", "programming",
        "representation", "reuse", "simulation",
    ],
    "Conceptos Computacionales": [
        "conditionals", "control structures", "directions", "events", "functions", "loops", "modular structure",
        "parallelism", "sequences", "software", "hardware", "variables",
    ],
    "Actitudes": [
        "emotional", "engagement", "motivation", "perceptions", "persistence", "self-efficacy", "self-perceived",
    ],
    "Propiedades Psicométricas": [
        "classical test theory", "confirmatory factor analysis", "exploratory factor analysis", "item response theory",
        "reliability", "structural equation model", "validity",
    ],
    "Herramienta de Evaluación": [
        "bctt", "escas", "cctt", "ctst", "cta-ces", "ctc", "ctls", "cts", "ctt-es", "ctt-lp", "capct", "ict competency test",
        "general self-efficacy scale", "stem-las",
    ],
    "Diseño de Investigación": [
        "experimental", "longitudinal research", "mixed methods", "post-test", "pre-test", "quasi-experiments",
        "non-experimental",
    ],
    "Nivel de Escolaridad": [
        "upper elementary education", "primary school", "early childhood education", "secondary school", "high school",
        "university", "college",
    ],
    "Medio": [
        "block programming", "mobile application", "pair programming", "plugged activities", "programming", "robotics",
        "spreadsheet", "stem", "unplugged activities",
    ],
    "Estrategia": [
        "construct-by-self mind mapping", "design-based learning", "gamification", "reverse engineering", "technology-enhanced learning",
        "collaborative learning", "cooperative learning", "flipped classroom", "game-based learning", "inquiry-based learning",
        "personalized learning", "problem-based learning", "project-based learning", "universal design for learning",
    ],
    "Herramienta": [
        "Alice", "Arduino", "Scratch", "ScratchJr", "Blockly Games", "Code.org", "Codecombat", "CSUnplugged", "Robot Turtles",
        "Hello Ruby", "Kodable", "LightbotJr", "KIBO robots", "BEE BOT", "CUBETTO", "Minecraft", "Agent Sheets", "Mimo",
        "Py–Learn", "SpaceChem",
    ],
}

# Inicializar diccionario para guardar conteos de términos por categoría
category_counts = {category: defaultdict(int) for category in categories_keywords.keys()}

# Procesar cada abstract para clasificarlo en las categorías
for abstract in data["Abstract"].dropna().str.lower():
    words = re.findall(r'\b\w+\b', abstract)  # Extraer todas las palabras

   # Recorrer cada categoría y sus palabras clave
for category, keywords_list in categories_keywords.items():
    for term in keywords_list:
        # Contar cuántas veces aparece el término
        term_count = words.count(term)
        if term_count > 0:
            category_counts[category][term] += term_count


# Mostrar resultados de conteo por categoría y término
for category, terms in category_counts.items():
    print(f"\n{category}:")
    for term, count in terms.items():
        print(f"  {term}: {count}")
