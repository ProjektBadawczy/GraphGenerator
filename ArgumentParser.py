import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number_of_graphs",
                        help="number of graphs to be generated",
                        type=int, default=10)
    parser.add_argument("-m", "--min_num_of_vertices",
                        help="number of graphs to be generated",
                        type=int, default=5)
    parser.add_argument("-M", "--max_num_of_vertices",
                        help="number of graphs to be generated",
                        type=int, default=30)
    parser.add_argument("-p", "--pretty",
                        help="write JSON in readable manner",
                        action="store_true")
    args = parser.parse_args()
    return args.number_of_graphs, args.min_num_of_vertices, args.max_num_of_vertices + 1, args.pretty
