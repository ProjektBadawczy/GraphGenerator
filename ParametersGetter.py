import argparse
import configparser
import os


class ParametersGetter:
    @staticmethod
    def get_parameters():
        path = ParametersGetter.__parse_args()
        graphs_params, output_params = None, None
        try:
            graphs_params, output_params = ParametersGetter.__read_ini(path)
        except KeyError:
            print("Error during reading config file. Check given path and parameters in config file")
            exit(1)
        except NameError:
            print("output name should only specify name of a file")
            exit(1)
        return graphs_params, output_params

    @staticmethod
    def __parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--path",
                            help="path to config file",
                            default="configs/random_config.ini")
        args = parser.parse_args()
        return args.path

    @staticmethod
    def __read_ini(file_path):
        config = configparser.ConfigParser()
        config.read(file_path)
        graphs_params = (
            config["APP"].getint("NUMBER_OF_GRAPHS"),
            config["APP"].getint("MIN_NUM_OF_VERTICES"),
            config["APP"].getint("MAX_NUM_OF_VERTICES"),
            config["APP"].getfloat("MIN_PERCENT_OF_EDGE_CREATION"),
            config["APP"].getfloat("MAX_PERCENT_OF_EDGE_CREATION")
        )
        output_params = (
            config["APP"]["OUTPUT_PATH"],
            config["APP"].getboolean("PRETTY")
        )
        if output_params[0] != os.path.basename(output_params[0]):
            raise NameError
        return graphs_params, output_params


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
