import networkx as nx

def encontrar_no_central(grafo):
    # Calcula a distância total de um nó para todos os outros nós
    def calcular_distancia_total(n):
        distancia_total = 0
        for no in grafo.nodes:
            if no != n:
                distancia = nx.shortest_path_length(grafo, source=n, target=no)
                distancia_total += distancia
        return distancia_total

    # Inicializa a distância mínima como infinito
    distancia_minima = float('inf')

    # Itera sobre todos os nós do grafo
    for no in grafo.nodes:
        distancia_total = calcular_distancia_total(no)
        # Atualiza a distância mínima e o nó central, se necessário
        if distancia_total < distancia_minima:
            distancia_minima = distancia_total
            no_central = no

    return no_central

def encontrar_nos_conectados(grafo, no_inicial):
    nos_conectados = []

    # Função recursiva auxiliar para encontrar os nós conectados
    def encontrar_recursivamente(no_atual):
        nos_conectados.append(no_atual)
        vizinhos = grafo.neighbors(no_atual)
        for vizinho in vizinhos:
            if vizinho not in nos_conectados:
                encontrar_recursivamente(vizinho)

    # Chama a função auxiliar para encontrar os nós conectados
    encontrar_recursivamente(no_inicial)

    return nos_conectados