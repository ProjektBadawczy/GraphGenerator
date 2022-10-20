import random
import math
import statistics


class MatrixFiller:
    @staticmethod
    def populate_matrices(num_of_matrices, min_num_of_vertices, max_num_of_vertices, min_percent, max_percent):
        matrices_list = []
        for i in range(num_of_matrices):
            matrices_list.append(
                MatrixFiller.__populate_matrix(
                    random.randint(
                        min_num_of_vertices, max_num_of_vertices
                    ),
                    min_percent, max_percent
                )
            )
        return matrices_list

    @staticmethod
    def __populate_matrix(n, min_percent, max_percent):
        adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]
        nodes_vector = MatrixFiller.__prepare_nodes_vector(n, min_percent, max_percent)

        for i in nodes_vector:
            visited_set = set()
            unvisited_set = set(range(n))

            first_node = i
            unvisited_set.remove(first_node)
            visited_set.add(first_node)

            while len(unvisited_set) > 0:
                get_nodes_set = set()
                added_nodes_set = set()
                num_of_added_nodes = random.randint(1, len(unvisited_set))
                for _ in range(num_of_added_nodes):
                    added_node = random.choice(tuple(unvisited_set))
                    unvisited_set.remove(added_node)
                    get_nodes_set.add(added_node)
                for _ in range(num_of_added_nodes):
                    chosen_begin = random.choice(tuple(visited_set))
                    chosen_end = get_nodes_set.pop()
                    added_nodes_set.add(chosen_end)
                    adjacency_matrix[chosen_begin][chosen_end] = random.randint(1, 20)
                for _ in range(num_of_added_nodes):
                    visited_set.add(added_nodes_set.pop())
        return adjacency_matrix

    @staticmethod
    def __prepare_nodes_vector(n, min_percent, max_percent):
        nodes_vector = [i for i in range(n)]
        random.shuffle(nodes_vector)
        range_numbers = [
            int(statistics.median([1, math.ceil(n * min_percent / 100), n])),
            int(statistics.median([1, math.ceil(n * max_percent / 100), n]))
        ]
        range_numbers.sort()
        nodes_to_keep_num = random.randint(*range_numbers)
        return nodes_vector[0:nodes_to_keep_num]
