import heapq


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

        Se nenhum peso é fornecido, o peso padrão da aresta é 1.
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

        Um grafo é completo se todos os seus vértices são conectados entre si.
        Esta função verifica se cada vértice tem uma aresta para todos os outros vértices.

        Argumentos:
            - `graph`: Uma instância da classe `Graph`.

        Retorna `True` se o grafo é completo, `False` caso contrário.
        """
        node_count = len(self.adjacency_list)
        for edges in self.adjacency_list.values():
            if len(edges) != node_count - 1:
                return False
        print("O grafo é completo.")
        return True

    def dfs(self, current_node, visited=None, is_initial_call=True):
        """
        Realiza uma busca em profundidade (Depth-First Search - DFS) em um grafo a partir de um nó dado.

        Este método explora o grafo seguindo um caminho até o final antes de retroceder, o que é
        útil para muitas aplicações como ordenações topológicas, verificar conectividade, e encontrar
        componentes conectados.

        Argumentos:
            - `graph`: Uma instância da classe `Graph` na qual realizar a busca.
            - `current_node`: O vértice de início para a busca.
            - `visited`: (Opcional) Um dicionário para controlar os nós já visitados.
            - `is_initial_call`: (Opcional) Um booleano para indicar se a chamada atual é a chamada inicial.

        Retorna um iterável contendo todos os nós visitados durante a busca. Por padrão,
        quando a busca é iniciada pela primeira vez (ou seja, `is_initial_call` é `true`),
        a função imprimirá os nós visitados uma vez que a busca esteja completa.

        O argumento `visited` é usado internamente para marcar os nós que já foram explorados
        e deve ser passado como `None` quando chamar a função externamente.
        """
        # Inicializa o dicionário de visitados se ele for None
        if visited is None:
            visited = {}

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

    def get_degree_connections(graph):
        """
        Constrói um dicionário de conexões de graus para um grafo.

        Para cada nó do grafo, determina o grau (número de conexões) e mapeia esse grau
        para um conjunto de graus dos nós adjacentes. Este dicionário é usado para
        verificar o isomorfismo entre dois grafos.

        Argumentos:
            - `graph`: Uma instância da classe `Graph`.

        Retorna um dicionário que relaciona os graus dos nós a conjuntos dos graus dos
        nós adjacentes.
        """
        degree_connections = {}
        for node in graph.adjacency_list:
            node_degree = len(graph.adjacency_list[node])
            connected_degrees = set()
            for adjacent_node in graph.adjacency_list[node]:
                connected_degrees.add(len(graph.adjacency_list[adjacent_node]))
            degree_connections.setdefault(node_degree, set()).update(connected_degrees)
        return degree_connections

    def is_isomorphic(g, h):
        """
        Verifica se dois grafos são isomórficos.

        Dois grafos são isomórficos se eles têm uma correspondência de vértices que
        preserva a estrutura de conexão dos vértices. Esta função verifica se os grafos
        têm o mesmo número de vértices e arestas, e compara as conexões dos vértices
        para determinar se tal correspondência existe.

        Argumentos:
            - `g`: Uma instância da classe `Graph`, representando o primeiro grafo.
            - `h`: Uma instância da classe `Graph`, representando o segundo grafo.

        Retorna `True` se os grafos são isomórficos, ou seja, se eles têm o mesmo número
        de vértices e arestas e a mesma estrutura de conexões. Retorna `False` caso
        contrário.
        """
        # Verifica se os grafos têm o mesmo número de nós e arestas
        if g.num_nodes != h.num_nodes or g.num_edges != h.num_edges:
            return False

        # Obtém as conexões de graus dos dois grafos
        g_degree_connections = Graph.get_degree_connections(g)
        h_degree_connections = Graph.get_degree_connections(h)

        # Compara as conexões de graus
        if g_degree_connections == h_degree_connections:
            print("Os grafos são isomórficos.")
            return True
        else:
            print("Os grafos não são isomórficos.")
            return False

    def prim(self):
        """Computes the Minimum Spanning Tree (MST) using Prim's algorithm."""
        if not self.adjacency_list:
            return None  # Return None if the graph is empty

        # Initialize all vertices as not in MST
        in_mst = {node: False for node in self.adjacency_list}

        # Priority queue: (weight, vertex, parent)
        # We start with an arbitrary vertex, let's pick the first in adjacency list
        start_vertex = next(iter(self.adjacency_list))
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

        print(mst_edges)
        return mst_edges
