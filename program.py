import json

from MatrixPopulator import MatrixPopulator as mp
import StructureConstructor

if __name__ == "__main__":
    adjacency_matrix = mp.populate_matrices(5)
    graphs_list = StructureConstructor.construct_structure(adjacency_matrix)
    with open('data.json', 'w') as f:
        json.dump(graphs_list, f)