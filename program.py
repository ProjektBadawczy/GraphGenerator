import ArgumentParser
from MatrixFiller import MatrixFiller as mF
import StructureConstructor
import JSONCreator


if __name__ == "__main__":
    number_of_graphs, min_num_of_vertices, max_num_of_vertices, if_pretty = ArgumentParser.parse_args()
    adjacency_matrix = mF.populate_matrices(number_of_graphs, min_num_of_vertices, max_num_of_vertices)
    graphs_list = StructureConstructor.construct_structure(adjacency_matrix)
    JSONCreator.create_json(graphs_list, if_pretty)
