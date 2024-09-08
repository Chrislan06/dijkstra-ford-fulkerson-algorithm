

# Verifica se há um caminho entre o nó do começo e o final
def breadth_first_search(graph, start_node, end_node, parent):

    # Guarda os nós visitados
    visited = {node: False for node in graph}

    if end_node not in visited:
        visited[end_node] = False
    # Fila para passar entre os nós
    queue = []

    # Adiciona o nó inicial a fila
    queue.append(start_node)
    visited[start_node] = True

    # Percorre a fila em busca de encontrar um caminho entre os nós
    while queue:
        # Nó atual a ser analisado
        current_node = queue.pop(0)

        # Percorre todos os nós adjacentes
        for adj_node, capacity in graph[current_node].items():
            if visited[adj_node] == False and capacity > 0:
                queue.append(adj_node)
                visited[adj_node] = True
                parent[adj_node] =  current_node
                # Verifica se chegou no nó final
                if adj_node == end_node:
                    return True
    # Não conseguiu achar o nó final
    return False

def ford_fulkerson(graph, start_node, end_node):
    parent = {}
    max_flow = 0

    # Criando grafo residual
    residual_graph = {node: dict(neighbors) for node, neighbors in graph.items()}


    # Adiciona um nó final caso ele não tenha nem um nó de saída
    if end_node not in residual_graph:
        residual_graph[end_node] = {}

    # Verifica se existe um caminho entre o nó de começo e o nó final, enquanto houver atualiza o flow maximo
    while breadth_first_search(residual_graph, start_node, end_node, parent):
        # Encontra o fluxo máximo possível a partir do caminho encontrado
        path_flow = float('Inf')
        compare_node = end_node
        while compare_node != start_node:
            path_flow = min(path_flow, residual_graph[parent[compare_node]][compare_node])
            compare_node = parent[compare_node]
        compare_node = end_node
        # Atualiza as capacidades das arestas e das arestas reversas ao longo do caminho
        while compare_node != start_node:
            parent_node = parent[compare_node]
            # Atualiza a aresta reversa no grafo residual
            residual_graph[parent_node][compare_node] -= path_flow
            # Verifica se existe a aresta no grafo residual
            if parent_node in residual_graph[compare_node]:
                residual_graph[compare_node][parent_node] += path_flow
            else: # Adiciona a aresta no grafo residual
                residual_graph[compare_node][parent_node] = path_flow
            compare_node = parent[compare_node]
        
        max_flow += path_flow
    
    return max_flow



# Exemplos


graph1 = {
    'A' : {'B': 5, 'C': 8},
    'B' : {'C': 4, 'D': 6},
    'C' : {'D': 2},
}


graph2 = {
    'A': {'B': 10, 'D': 10},
    'B': {'C': 4, 'D': 2, 'E': 8},
    'C': {'F': 10}, 
    'D': {'E': 9},
    'E': {'C': 6, 'F': 10},
    'F': {}
}
# print(ford_fulkerson(graph1, 'A', 'D'))
# Saída Esperada: 7
# print(ford_fulkerson(graph2, 'A', 'F'))
# Saída esperada: 19