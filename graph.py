import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    # Classe que representa um grafo."""

    def __init__(self):
        # Construtor da classe. Inicializa a lista de adjacência do grafo."""
        self.adjacency_list = {}

    @property
    def num_nodes(self):
        # Obtém o número de nós do grafo."""
        return len(self.adjacency_list)

    @property
    def num_edges(self):
        # Obtém o número de arestas do grafo.
        # Como o grafo é não-direcionado, a soma dos tamanhos das listas de adjacências
        # é dividida por 2.
        
        return sum(len(edges) for edges in self.adjacency_list.values()) // 2

    def add_edge(self, node1, node2, weight=1):
        # Adiciona uma aresta entre dois vértices com um peso opcional.
        
        self.adjacency_list.setdefault(node1, {})
        self.adjacency_list.setdefault(node2, {})
        self.adjacency_list[node1][node2] = weight
        self.adjacency_list[node2][node1] = weight

    def __str__(self):
        # Retorna uma representação em string do grafo.
        result = ""
        for node, edges in self.adjacency_list.items():
            result += f"{node} -> "
            for edge, weight in edges.items():
                result += f"({edge}, {weight}) "
            result += "\n"
        return result

    def is_complete(self):
        # Verifica se um grafo é completo.
        
        node_count = len(self.adjacency_list)
        for edges in self.adjacency_list.values():
            if len(edges) != node_count - 1:
                return False
        return True

    def dfs(self, current_node, visited=None, is_initial_call=True):
        # Inicializa o dicionário de visitados se ele for None
        if visited is None:
            visited = {}

        # Verifica se o vértice inicial existe no grafo
        if current_node not in self.adjacency_list:
            print("O vértice inicial não existe no grafo. Observação: diferenciamos maiúsculas e minúsculas!")
            return []
        
        # Marca o nó atual como visitado
        visited[current_node] = True

        # Visita recursivamente todos os nós adjacentes que ainda não foram visitados
        for adjacent_node in self.adjacency_list.get(current_node, {}):
            if not visited.get(adjacent_node):
                # Passa False para as chamadas recursivas
                self.dfs(adjacent_node, visited, False)

        # Apenas imprime quando a busca inteira estiver concluída (na chamada inicial)
        if is_initial_call:
            print("DFS: ", list(visited.keys()))
            return list(visited.keys())
        

    def is_isomorphic(g, h):
        # Verifica se os grafos têm o mesmo número de nós e arestas
        if g.num_nodes != h.num_nodes or g.num_edges != h.num_edges:
            return False

        # Obtém as conexões de graus dos dois grafos
        g_degree_connections = Graph.get_degree_connections(g)
        h_degree_connections = Graph.get_degree_connections(h)

        # Compara as conexões de graus
        if g_degree_connections == h_degree_connections:
            return True
        else:
            return False


    def prim(self, initial_vertex):
        # Calcula a Árvore de Abrangência Mínima (MST) usando o algoritmo de Prim.
        if not self.adjacency_list:
            print("The graph is empty.")
            return None  # Retorna None se o grafo estiver vazio

        # Verifica se o vertice_inicial está no grafo
        if initial_vertex not in self.adjacency_list:
            print(f"Initial vertex '{initial_vertex}' is not present in the graph.")
            return None

        # Inicializa todos os vértices como não na MST
        in_mst = {vertex: False for vertex in self.adjacency_list}

        # Fila de prioridade
        priority_queue = [(0, initial_vertex, None)]
        mst_edges = []

        while priority_queue:
            weight, vertex, parent = heapq.heappop(priority_queue)

            if in_mst[vertex]:
                continue   # Pula se o vértice já estiver na MST

            in_mst[vertex] = True  # Inclui o vértice na MST
            if parent is not None:
                mst_edges.append((parent, vertex, weight))  # Adiciona a aresta à MST

            for adjacent, edge_weight in self.adjacency_list[vertex].items():
                if not in_mst[adjacent]:
                    heapq.heappush(priority_queue, (edge_weight, adjacent, vertex))

        if not mst_edges:
            print("The graph is not connected. Cannot calculate the MST.")
            return None

        print("Edges of the MST:", mst_edges)
        return mst_edges