import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    """Classe que representa um grafo."""

    def __init__(self):
        """Construtor da classe. Inicializa a lista de adjacência do grafo."""
        self.adjacency_list = {}

    @property
    def num_nodes(self):
        """Obtém o número de nós do grafo."""
        return len(self.adjacency_list)

    @property
    def num_edges(self):
        """
        Obtém o número de arestas do grafo.

        Como o grafo é não-direcionado, a soma dos tamanhos das listas de adjacências
        é dividida por 2.
        """
        return sum(len(edges) for edges in self.adjacency_list.values()) // 2

    def add_edge(self, node1, node2, weight=1):
        """
        Adiciona uma aresta entre dois vértices com um peso opcional.
        """
        self.adjacency_list.setdefault(node1, {})
        self.adjacency_list.setdefault(node2, {})
        self.adjacency_list[node1][node2] = weight
        self.adjacency_list[node2][node1] = weight

    def __str__(self):
        """Retorna uma representação em string do grafo."""
        result = ""
        for node, edges in self.adjacency_list.items():
            result += f"{node} -> "
            for edge, weight in edges.items():
                result += f"({edge}, {weight}) "
            result += "\n"
        return result

    def is_complete(self):
        """
        Verifica se um grafo é completo.
        """
        node_count = len(self.adjacency_list)
        for edges in self.adjacency_list.values():
            if len(edges) != node_count - 1:
                return False
        return True

    # def dfs(self, current_node, visited=None, is_initial_call=True):
    #     # Inicializa o dicionário de visitados se ele for None
    #     if visited is None:
    #         visited = {}

    #     # Marca o nó atual como visitado
    #     visited[current_node] = True

    #     # Visita recursivamente todos os nós adjacentes que ainda não foram visitados
    #     for adjacent_node in self.adjacency_list.get(current_node, {}):
    #         if not visited.get(adjacent_node):
    #             # Passa False para as chamadas recursivas
    #             self.dfs(adjacent_node, visited, False)

    #     # Apenas imprime quando a busca inteira estiver concluída (na chamada inicial)
    #     if is_initial_call:
    #         print("DFS: ", list(visited.keys()))
    #         return list(visited.keys())
    
    def dfs(self, current_node, visited=None, is_initial_call=True):
        if visited is None:
            visited = {}
        result_edges = []
        
        for adjacent_node in self.adjacency_list.get(current_node, {}):
            if not visited.get(adjacent_node):
                result_edges.append((current_node, adjacent_node, self.adjacency_list[current_node][adjacent_node]))
                visited[adjacent_node] = True
                result_edges.extend(self.dfs(adjacent_node, visited, False))

        if is_initial_call:
            print("Arestas DFS: ", result_edges)
            return result_edges
        else:
            return result_edges


    def get_degree_connections(graph):
        degree_connections = {}
        for node in graph.adjacency_list:
            node_degree = len(graph.adjacency_list[node])
            connected_degrees = set()
            for adjacent_node in graph.adjacency_list[node]:
                connected_degrees.add(len(graph.adjacency_list[adjacent_node]))
            degree_connections.setdefault(node_degree, set()).update(connected_degrees)
        return degree_connections


    def is_isomorphic(g, h):
        # Verifica se os grafos têm o mesmo número de nós e arestas
        if g.num_nodes != h.num_nodes or g.num_edges != h.num_edges:
            return False

        # Obtém as conexões de graus dos dois grafos
        g_degree_connections = Graph.get_degree_connections(g)
        h_degree_connections = Graph.get_degree_connections(h)

        # Compara as conexões de graus
        if g_degree_connections == h_degree_connections:
            # print("Os grafos são isomórficos.")
            return True
        else:
            # print("Os grafos não são isomórficos.")
            return False


    def prim(self, start_vertex):
        """Computes the Minimum Spanning Tree (MST) using Prim's algorithm."""
        if not self.adjacency_list:
            print("O grafo está vazio.")
            return None  # Return None if the graph is empty

        # Check if the start_vertex is in the graph
        if start_vertex not in self.adjacency_list:
            print(f"Vértice inicial '{start_vertex}' não está presente no grafo.")
            return None

        # Initialize all vertices as not in MST
        in_mst = {node: False for node in self.adjacency_list}

        # Priority queue: (weight, vertex, parent)
        priority_queue = [(0, start_vertex, None)]
        mst_edges = []

        while priority_queue:
            weight, vertex, parent = heapq.heappop(priority_queue)

            if in_mst[vertex]:
                continue  # Skip if vertex is already in MST

            in_mst[vertex] = True  # Include vertex in MST
            if parent is not None:
                mst_edges.append((parent, vertex, weight))  # Add edge to MST

            for adjacent, edge_weight in self.adjacency_list[vertex].items():
                if not in_mst[adjacent]:
                    heapq.heappush(priority_queue, (edge_weight, adjacent, vertex))

        if not mst_edges:
            print("O grafo não é conexo. Não é possível calcular a MST.")
            return None

        print("Arestas da MST:", mst_edges)
        return mst_edges


    def visualize_generic_graph(self, graph, edges=None):
            if not graph.adjacency_list:
                print("O grafo está vazio.")
                return

            G = nx.Graph()

            for node, node_edges in graph.adjacency_list.items():
                G.add_node(node)
                for neighbor, weight in node_edges.items():
                    G.add_edge(node, neighbor, weight=weight)

            if edges:
                for edge in edges:
                    G.add_edge(edge[0], edge[1], weight=edge[2])

            pos = nx.spring_layout(G, k=1.5)
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw(G, pos, with_labels=True, font_weight='bold')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

            plt.show()

    