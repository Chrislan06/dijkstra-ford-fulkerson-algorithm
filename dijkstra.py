import heapq

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0 

    # Criando a fila de prioridade para armazenar o menor caminho entre os nós
    priority_queue = [(0,start_node)]
    # Loop para percorrer todos os nós com menor distância
    while priority_queue:
        # Pega o nó com menor distância da heap
        current_distance, current_node = heapq.heappop(priority_queue)
        # Percorre os nós adjacentes ao nó analisado
        for adj_node, weight in graph[current_node].items():
            # Pega o valor da distância atual e do no adjacente atualizado
            distance = current_distance + weight
            # Atualiza as distâncias para a menor distância
            if distance < distances[adj_node]:
                distances[adj_node] = distance
                # Coloca na heap para as próximas interações
                heapq.heappush(priority_queue, (distance, adj_node))
    
    return distances

# Exemplos

ex1 = {
     'A': {'B': 3, 'C': 8},
     'B': {'A': 3, 'C': 2, 'E': 5},
     'C': {'A': 8, 'B': 2, 'D': 1, 'E': 6},
     'D': {'C': 1, 'E': 2, 'F': 3},
     'E': {'B': 5, 'C': 6, 'D': 2, 'F': 5},
     'F': {'D': 3, 'E': 5}
}

# print(dijkstra(ex1, 'A'))
# Saida Esperada: {'A': 0, 'B': 3, 'C': 5, 'D': 6, 'E': 8, 'F': 9}

ex2 = {
    'A' : {'B': 5, 'C': 8},
    'B' : {'C': 4, 'D': 6},
    'C' : {'D': 2},
    'D' : {'D': 0}
}

# print(dijkstra(ex2, 'A'))
# Saida Esperada: {'A': 0, 'B': 5, 'C': 8, 'D': 10}