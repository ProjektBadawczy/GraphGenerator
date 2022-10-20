import json


def create_json(graphs_list, output_filename, pretty=False):
    if pretty:
        indent = 4
    else:
        indent = None
    with open("graphs/{}".format(output_filename), 'w') as f:
        json.dump(graphs_list, f, indent=indent)
