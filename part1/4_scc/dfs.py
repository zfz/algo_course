import sys
from collections import defaultdict
import logging
logger = logging.getLogger()


def setup_debug_logger():
    handler = logging.StreamHandler()
    global logger
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def read_lines(file_name):
    g = defaultdict(list)
    with open(file_name) as f:
        for line in f:
            nodes = map(int, line.strip().split(' '))
            g[nodes[0]].append(nodes[1])
    logger.debug("graph nodes number is {0}".format(len(g)))
    return g


def dfs(g, start_node, visited_nodes, trace):
    stack = []

    # add start node
    stack.extend(g[start_node])
    visited_nodes.add(start_node)
    trace.append(start_node)

    while stack:
        next_node = stack.pop()  # different with BFS
        if next_node not in visited_nodes:
            visited_nodes.add(next_node)
            for v in g[next_node]:
                if v not in visited_nodes:
                    stack.append(v)
            trace.append(next_node)

    return trace

def dfs_loop(g):
    # loop through the whole graph to deal with isolated nodes
    # use set is more efficient than list to remember nodes visited
    visited_nodes, trace = set(), []

    for k in g.keys():
        if k not in visited_nodes:
            dfs(g, k, visited_nodes, trace)

    # logger.debug("trace: {0}".format(trace))
    return trace


if __name__ == "__main__":
    setup_debug_logger()
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        graph = read_lines(file_name)
        trace = dfs_loop(graph)
        print("DFS visited nodes number is {0}".format(len(trace)))
    else:
        print("Please provide file name!")
