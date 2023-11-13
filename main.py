from graph import Graph


def main():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "A")

    h = Graph()
    h.add_edge("X", "Y")
    h.add_edge("Y", "Z")
    h.add_edge("Z", "X")

    p = Graph()
    p.add_edge("A", "B", 2)
    p.add_edge("A", "C", 3)
    p.add_edge("A", "D", 3)
    p.add_edge("B", "C", 4)
    p.add_edge("B", "E", 3)

    # # Verifica se os grafos `g` e `h` são isomorfos.
    g.is_isomorphic(h)

    # # Verifica se o grafo `g` é completo.
    g.is_complete()

    # # Realiza uma busca em profundidade (DFS) a partir do vértice 'A' no grafo `g`.
    g.dfs("A")

    # # Computa a árvore geradora mínima (MST) do grafo `p` usando o algoritmo de Prim.
    p.prim()
    
    # # Imprime o grafo `p`.
    print(p)


if __name__ == "__main__":
    main()
