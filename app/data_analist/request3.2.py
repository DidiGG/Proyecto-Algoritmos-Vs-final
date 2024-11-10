import pandas as pd
from collections import defaultdict
import re, string
import nltk
from nltk.corpus import wordnet
from tqdm import tqdm  # Para mostrar progreso

# Descargar WordNet
print("Descargando WordNet...")
nltk.download("wordnet", quiet=True)

# Ruta del archivo CSV
archivo_csv = "https://raw.githubusercontent.com/DidiGG/Proyecto-Algoritmos-Vs-final/refs/heads/main/data/final_csv/bases_unificadas_ok.csv"

# Cargar el archivo CSV
print("Cargando datos...")
df = pd.read_csv(archivo_csv)

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
        "self efficacy",
        "self perceived",
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
        "ict",
        "competency test",
        "self-efficacy scale",
        "stem las",
    ],
    "Diseño de Investigación": [
        "experimental",
        "longitudinal research",
        "mixed methods",
        "post-test",
        "pre-test",
        "quasi-experiments",
        "no experimental",
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


def obtener_sinonimos(palabra):
    """Obtiene sinónimos de una palabra usando WordNet"""
    sinonimos = set()
    # Si la palabra tiene espacios, no buscar sinónimos
    if " " in palabra:
        return [palabra]

    for syn in wordnet.synsets(palabra):
        for lemma in syn.lemmas():
            # Agregar solo si no es la misma palabra
            if lemma.name().lower() != palabra.lower():
                sinonimos.add(lemma.name().lower())
    return list(sinonimos)


def clean_text(text):
    """Limpia y normaliza el texto"""
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", " ", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# Expandir keywords con sinónimos y crear nuevo diccionario
print("\nProcesando palabras clave y sus sinónimos...")
expanded_categories_keywords = {}

for categoria, palabras in categories_keywords.items():
    print(f"\nCategoría: {categoria}")
    expanded_palabras = []

    for palabra in palabras:
        expanded_palabras.append(palabra)  # Agregar palabra original
        sinonimos = obtener_sinonimos(palabra)

        # Imprimir palabra original y sus sinónimos
        print(f"\n{palabra}:")
        if sinonimos:
            for sinonimo in sinonimos:
                print(f"  -{sinonimo}")
                expanded_palabras.append(sinonimo)
        else:
            print("  No se encontraron sinónimos")

    expanded_categories_keywords[categoria] = expanded_palabras

# Inicializar conteos
category_counts = {
    category: defaultdict(int) for category in expanded_categories_keywords.keys()
}

# Procesar abstracts
print("\nAnalizando abstracts...")
for abstract in tqdm(df["Abstract"].dropna()):
    abstract_cleaned = clean_text(abstract)

    for category, keywords_list in expanded_categories_keywords.items():
        for term in keywords_list:
            # Buscar el término como palabra completa
            term_pattern = r"\b" + re.escape(term.lower()) + r"\b"
            term_count = len(re.findall(term_pattern, abstract_cleaned))
            if term_count > 0:
                category_counts[category][term] += term_count

# Imprimir resultados finales
print("\nResultados de conteo por categoría y término:")
for category, terms in category_counts.items():
    print(f"\n{category}:")
    if not terms:
        print("  No terms found.")
    else:
        # Ordenar términos por conteo
        sorted_terms = sorted(terms.items(), key=lambda x: x[1], reverse=True)
        for term, count in sorted_terms:
            # Identificar si es sinónimo (no está en la lista original)
            is_synonym = term not in categories_keywords[category]
            prefix = "-" if is_synonym else " "
            print(f"  {prefix}{term}: {count}")
