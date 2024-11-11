import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Ruta al archivo CSV
csv_url = "https://raw.githubusercontent.com/DidiGG/Proyecto-Algoritmos-Vs-final/refs/heads/main/data/final_csv/bases_unificadas_ok.csv"

# Cargar el archivo CSV
df = pd.read_csv(csv_url)

# Columnas a usar
journal_column = "Publication Title"  # O usa "Revista" si se ajusta mejor
citation_column = "Article Citation Count"
country_column = "Country"  # Asignaremos valores aleatorios para esta columna

# Identificar los 10 journals con mayor cantidad de artículos publicados
top_journals = df[journal_column].value_counts().nlargest(10).index
top_journals_df = df[df[journal_column].isin(top_journals)].copy()

# Asignar valores de citación de forma aleatoria donde falten
top_journals_df[citation_column] = top_journals_df[citation_column].fillna(pd.Series(np.random.randint(0, 250, size=len(top_journals_df))))

# Asignar países de forma aleatoria si faltan
top_journals_df[country_column] = top_journals_df.get(country_column, pd.Series(np.random.choice(['USA', 'UK', 'Germany', 'India', 'China'], size=len(top_journals_df))))

# Crear el grafo
G = nx.Graph()

# Añadir nodos y aristas al grafo
for journal in top_journals:
    journal_articles = top_journals_df[top_journals_df[journal_column] == journal]
    top_articles = journal_articles.nlargest(15, citation_column)
    
    for _, row in top_articles.iterrows():
        article = row['Document Title']  # Nombre del artículo
        country = row[country_column]  # País del primer autor
        citations = row[citation_column]  # Número de citas

        G.add_node(journal, type='journal')
        G.add_node(article, type='article', citations=citations)
        G.add_node(country, type='country')
        
        G.add_edge(journal, article)
        G.add_edge(article, country)

# Dibujar el grafo
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(12, 12))

# Colorear los nodos según el tipo
node_colors = ['lightblue' if G.nodes[n]['type'] == 'journal' else 'orange' if G.nodes[n]['type'] == 'article' else 'lightgreen' for n in G.nodes]
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=4)

# Mostrar la gráfica
plt.title("Relación entre Journals, Artículos y Países")
plt.show()


