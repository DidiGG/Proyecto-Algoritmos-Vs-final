import pandas as pd
from collections import defaultdict
import re, string

# Ruta del archivo CSV limpio
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Proyecto-Algoritmos-Vs-final/refs/heads/main/data/final_csv/bases_unificadas_ok.csv"

# Cargar el archivo CSV
df = pd.read_csv(archivo_csv)

# Mostrar las primeras filas para asegurarnos de que las columnas son correctas
print("Primeras filas del archivo CSV:")
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
    "Herramienta": [
        "alice",
        "arduino",
        "scratch",
        "scratchJr",
        "blockly Games",
        "code.org",
        "codecombat",
        "CSUnplugged",
        "Robot Turtles",
        "Hello Ruby",
        "Kodable",
        "LightbotJr",
        "KIBO robots",
        "BEE BOT",
        "CUBETTO",
        "Minecraft",
        "Agent Sheets",
        "Mimo",
        "Py–Learn",
        "SpaceChem",
    ],
}

# Inicializar diccionario para guardar conteos de términos por categoría
category_counts = {
    category: defaultdict(int) for category in categories_keywords.keys()
}


# Función para limpiar y normalizar el texto
def clean_text(text):
    # Convertir a minúsculas
    text = text.lower()

    # Eliminar puntuación (se conserva solo alfabéticos y espacios)
    text = re.sub(f"[{string.punctuation}]", "", text)

    # Eliminar números si no son relevantes
    text = re.sub(r"\d+", "", text)

    # Eliminar espacios en blanco adicionales
    text = re.sub(r"\s+", " ", text).strip()

    return text


# Función para buscar de manera más flexible (tolerante a variaciones de formato)
def find_term_in_text(text, term):
    pattern = re.compile(r"\b" + re.escape(term) + r"\b", re.IGNORECASE)
    return len(re.findall(pattern, text))


# Procesar cada abstract para clasificarlo en las categorías
for abstract in data["Abstract"].dropna():
    abstract_cleaned = clean_text(abstract).lower()  # Convertir a minúsculas
    for category, keywords_list in categories_keywords.items():
        for term in keywords_list:
            term_lower = term.lower()

    # Recorrer cada categoría y sus palabras clave
    for category, keywords_list in categories_keywords.items():
        for term in keywords_list:
            # Buscar cuántas veces aparece el término de manera más flexible
            term_count = find_term_in_text(abstract_cleaned, term)
            if term_count > 0:
                category_counts[category][term] += term_count

# Imprimir los resultados de conteo
print("\nResultados de conteo por categoría y término:")
for category, terms in category_counts.items():
    print(f"\n{category}:")
    if not terms:  # Si no hay términos contados, imprimir un mensaje
        print("  No terms found.")
    else:
        for term, count in terms.items():
            print(f"  {term}: {count}")
