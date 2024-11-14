import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import imageio.v2 as imageio
import os

# Função para ler o arquivo .mtx e extrair o número de nós e lista de arestas
def ler_arquivo_mtx(arquivo_mtx):
    # Lê as linhas do arquivo
    with open(arquivo_mtx, 'r') as f:
        linhas = f.readlines()

    i = 0
    # Pula as linhas comentadas
    while linhas[i].startswith('%') or linhas[i].startswith('%%'):
        i += 1

    # Recebe as informações e monta uma lista de arestas
    n, _ , _ = map(int, linhas[i].split())
    arestas = [(int(v1), int(v2)) for v1, v2 in (linha.split() for linha in linhas[i+1:])]
    for linha in linhas[i+1:]:
        v1,v2 = map(int, linha.split())
        arestas.append((v1,v2))

    return n, arestas

# Função para gerar a matriz de adjacência formatada como tabela
def gerar_matriz_adjacencia(G):
    adj_matrix = nx.adjacency_matrix(G).todense()
    return adj_matrix

# Função para obter graus dos vértices
def obter_graus_vertices(G):
    # Dicionário para armazenar "vértice: grau"
    graus = {}
    for node, val in G.degree():
        graus[node] = val
    # Ordena os vértices/graus de 1 a n
    graus_ordenados = sorted(graus.items(), key=lambda x: (x[0], x[1]))
    return graus_ordenados

def bron_kerbosch(G, clique_atual, explorados, candidatos, cliques):
    # Caso base: quando não há mais vertices canditados nem explorados, o clique maximal é encontrado
    if not candidatos and not explorados:
        cliques.append(clique_atual)
        return

    copy_candidatos = candidatos.copy()
    # Para cada vértice 'v' em "candidatos", tenta expandir o cliqueAtual para incluir 'v'
    for v in copy_candidatos:
        novo_clique = clique_atual.copy()
        novo_clique.add(v)

        novos_candidatos = set()
        novos_explorados = set()
        # Restringe os vizinhos de 'v'
        for u in G[v]:
            if u in candidatos:
                novos_candidatos.add(u)
            if u in explorados:
                novos_explorados.add(u)

        # Chamada recursiva com o clique expandido e conjuntos atualizados
        bron_kerbosch(G, novo_clique, novos_explorados, novos_candidatos, cliques)

        # Marca o 'v' como explorado para que não seja processado novamente
        candidatos.remove(v)
        explorados.add(v)


# Função para encontrar cliques maximais
def encontrar_cliques_maximais(G, n):
    # Inicializa os conjuntos para o algoritmo de Bron-Kerbosch
    clique_atual = set()
    explorados = set()
    candidatos = set(range(1, n + 1))
    cliques = []
    bron_kerbosch(G, clique_atual, explorados, candidatos, cliques)

    # Ordena os cliques a partir do tamanho
    cliques.sort(key=len)

    # Cria uma lista para armazenar tamanho do clique e seus vértices
    cliques_e_tamanhos = []
    for clique in cliques:
        cliques_e_tamanhos.append((len(clique), clique))
    
    return cliques, cliques_e_tamanhos

# Função para calcular coeficiente de aglomeração
def calcular_coeficiente_aglomeracao(G):
    clustering = nx.clustering(G)

    # Ordena os vértices/coeficientes de 1 a n
    clustering_ordenado = sorted(list(clustering.items()), key= lambda x: (x[0], x[1]))
    return clustering_ordenado

# Função para calcular o coeficiente médio de aglomeração do grafo
def calcular_coeficiente_medio(G):
    coef_medio = nx.average_clustering(G)
    return f"Coeficiente médio de Aglomeração do Grafo: {coef_medio}"

# Função para criar GIF de cliques coloridos e salvar o último frame
def criar_gif_cliques(G, pos, cliques, output_gif="cliques.gif", final_frame="final_clique.png"):
    num_colors = len(cliques)
    colors = plt.colormaps['hsv'](np.linspace(0, 1, num_colors))  # Gerar cores para os cliques
    images = []
    node_colors = {node: "lightblue" for node in G.nodes}  # Cor inicial de todos os nós

    # Adiciona os cliques em sequência, mantendo as cores anteriores
    for i, clique in enumerate(cliques):
        # Para cada clique, define a cor para os nós pertencentes a esse clique
        for node in clique:
            node_colors[node] = colors[i]  # Atribui a cor do clique atual ao nó

        plt.figure()
        # Desenha o grafo com os nós coloridos conforme os cliques já processados
        node_color_list = [node_colors[node] for node in G.nodes]
        nx.draw(G, pos, with_labels=True, node_color=node_color_list, edge_color="gray", node_size=500, font_size=10)

        # Salva o frame temporário
        frame_path = f"/tmp/frame_{i}.png"
        plt.savefig(frame_path)
        images.append(imageio.imread(frame_path))  # Adiciona a imagem ao GIF
        os.remove(frame_path)  # Remove o arquivo temporário
        plt.close()  # Fecha a figura para o próximo frame

    # Salva o GIF
    imageio.mimsave(output_gif, images, duration=3.0)

# Leitura do arquivo e construção do grafo
arquivo_mtx = "soc-dolphins.mtx"
n, arestas = ler_arquivo_mtx(arquivo_mtx)

G = nx.Graph()
G.add_edges_from(arestas)

pos = nx.spring_layout(G)

print("Projeto 1 de Teoria e Aplicação de Grafos - Rede de Golfinhos")
print()

print("Matriz de Adjacência (parcial): ")
print(gerar_matriz_adjacencia(G))
print()

print("Vértices e seus respectivos graus: ")
print(obter_graus_vertices(G))
print()

print("Cliques maximais do grafo (tamanho, vértices): ")
cliques, cliques_e_tamanhos = encontrar_cliques_maximais(G,n)
print(cliques_e_tamanhos)
print()

print("Vértices e seus respectivos coeficientes de aglomeração: ")
print(calcular_coeficiente_aglomeracao(G))
print()

print(calcular_coeficiente_medio(G))

criar_gif_cliques(G, pos, cliques)
