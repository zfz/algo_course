import sys
import random
import logging
from copy import deepcopy
logger = logging.getLogger()


def setup_debug_logger():
    handler = logging.StreamHandler()
    global logger
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def read_lines(file_name):
    g = {}
    with open(file_name) as f:
        lines = f.readlines()
    for line in lines:
        nodes = map(int, line.strip().split('\t'))
        g[nodes[0]] = nodes[1:]
    return g


def merge_nodes(n1, n2):
    if isinstance(n1, tuple) and isinstance(n2, tuple):
        return tuple(list(n1) + list(n2))
    elif isinstance(n1, tuple) and isinstance(n2, int):
        return tuple(list(n1) + [n2])
    elif isinstance(n1, int) and isinstance(n2, tuple):
        return tuple([n1] + list(n2))
    else:
        return (n1, n2)


def replace_node(g, node1, node2, new_node):
    g[new_node] = g[node1] + g[node2]
    for key in g:
        values = g[key]
        for (i, v) in enumerate(values):
            if v == node1 or v == node2:
                values[i] = new_node

    # remove self connected edges, list's pop method deos not work here!
    g[new_node] = [v for v in g[new_node] if v != new_node]

    # remove old nodes
    del g[node1]
    del g[node2]
    return g


def karger_cut(g):
    while len(g.keys()) > 2:
        node1 = random.choice(g.keys())
        node2 = random.choice(g[node1])
        logger.debug("node1: {0}, node2: {1}".format(node1, node2))
        new_node = merge_nodes(node1, node2)
        replace_node(g, node1, node2, new_node)

    # edges count should be devided by 2 for every edge is undirected
    return sum(map(len, g.values())) / 2


if __name__ == "__main__":
    # setup_debug_logger()
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        graph = read_lines(file_name)
        count_list = []
        for i in range(200):  # 200 nodes in the graph
            copied_graph = deepcopy(graph)  # copy graph
            edges_count = karger_cut(copied_graph)
            print("Karger cut {0}th time count: {1}".format(i+1, edges_count))
            count_list.append(edges_count)
        print("Final min cut: {0}".format(min(count_list)))
    else:
        print("Please provide file name!")
