import json


def create_json(graphs_list, pretty=False):
    if pretty:
        indent = 4
    else:
        indent = None
    with open("data.json", 'w') as f:
        json.dump(graphs_list, f, indent=indent)
