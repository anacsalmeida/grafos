from graph import Graph

def create_example_graph(graph_type):
    g = Graph()

    if graph_type == 'complete':
        g.add_edge("A", "B")
        g.add_edge("B", "C")
        g.add_edge("C", "A")
    elif graph_type == 'incomplete':
        g.add_edge("X", "Y")
        g.add_edge("Y", "Z")
        g.add_edge("Z", "X")
        g.add_edge("Z", "W")
    elif graph_type == 'isomorphic_complete':
        g.add_edge("X", "Y")
        g.add_edge("Y", "Z")
        g.add_edge("Z", "X")
    elif graph_type == 'complex':
        g.add_edge("A", "C", 6)
        g.add_edge("A", "E", 2)
        g.add_edge("B", "C", 9)
        g.add_edge("B", "G", 5)
        g.add_edge("C", "E", 1)
        g.add_edge("C", "F", 1)
        g.add_edge("D", "F", 5)
        g.add_edge("D", "H", 4)
        g.add_edge("E", "G", 2)
        g.add_edge("E", "H", 3)
        g.add_edge("G", "H", 1)
        
    return g

# Função para verificar se dois grafos são isomórficos
def check_isomorphism(g, h):
    return Graph.is_isomorphic(g, h)

# Função para verificar se um grafo é completo
def check_completeness(graph):
    return graph.is_complete()



def main():
    while True:
        print("\nMenu:")
        print("1. Verificar se um grafo é completo (Exemplo Completo)")
        print("2. Verificar se um grafo é completo (Exemplo Incompleto)")
        print("3. Verificar se dois grafos são isomórficos")
        print("4. Executar DFS em um grafo")
        print("5. Árvore geradora mínima (MST) usando o algoritmo de Prim")
        print("6. Sair")

        choice = input("Escolha uma opção (1-6): ")

        if choice == '1':
            graph = create_example_graph('complete')  # Criar o grafo completo
            completeness_result = check_completeness(graph)
            print("O grafo é completo: ", completeness_result)
        elif choice == '2':
            graph = create_example_graph('incomplete')  # Criar o grafo incompleto
            completeness_result = check_completeness(graph)
            print("O grafo é completo: ", completeness_result)
        elif choice == '3':
            graph_g = create_example_graph('complete')  # Criar o grafo G
            graph_h = create_example_graph('isomorphic_complete')  # Criar o grafo H
            isomorphism_result = check_isomorphism(graph_g, graph_h)
            print("Os grafos são isomórficos: ", isomorphism_result)
        elif choice == '4':
            graph = create_example_graph('complex')  # Criar o grafo P
            start_vertex = input("Digite o vértice de início para o DFS: ")
            dfs_edges = graph.dfs(start_vertex)
        elif choice == '5':
            graph = create_example_graph('complex')  # Criar o grafo P
            start_vertex = input("Digite o vértice de início para o algoritmo de Prim: ")
            mst_edges = graph.prim(start_vertex)
        elif choice == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()