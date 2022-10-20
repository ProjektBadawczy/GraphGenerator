from ParametersGetter import ParametersGetter as pG
from MatrixFiller import MatrixFiller as mF
import StructureConstructor
import JSONCreator


if __name__ == "__main__":
    graphs_params, output_params = pG.get_parameters()
    adjacency_matrix = mF.populate_matrices(*graphs_params)
    graphs_list = StructureConstructor.construct_structure(adjacency_matrix)
    JSONCreator.create_json(graphs_list, *output_params)
