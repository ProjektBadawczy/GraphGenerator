def construct_structure(adjacency_matrices):
    graphs_list = []
    for i in range(len(adjacency_matrices)):
        adjacency_matrix = adjacency_matrices[i]
        adjacency_list = [[] for _ in range(len(adjacency_matrix))]
        for j in range(len(adjacency_matrix)):
            for k in range(len(adjacency_matrix[j])):
                if adjacency_matrix[j][k] > 0:
                    adjacency_list[j].append({
                        "i": k,
                        "w": adjacency_matrix[j][k]
                    })

        graph = {
            "graph": {
                "id": i + 1,
                "numberOfVertices": len(adjacency_matrix),
                "adjacencyMatrix": adjacency_matrix
            },
            "directedGraph": {
                "id": i + 1,
                "numberOfVertices": len(adjacency_matrix),
                "adjacencyList": adjacency_list
            }
        }
        graphs_list.append(graph)
    return graphs_list
