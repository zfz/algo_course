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
            nodes = map(int, line.strip().split('\t'))
            g[nodes[0]].append(nodes[1])
    return g


def bfs(g, start_node):
    visited_nodes, queue = [], []

    # add start node
    queue.extend(g[start_node])
    visited_nodes.append(start_node)

    while queue:
        next_node = queue.pop(0)  # different with dfs
        if next_node not in visited_nodes:
            visited_nodes.append(next_node)
            queue.extend(g[next_node])

    return visited_nodes


if __name__ == "__main__":
    setup_debug_logger()
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        graph = read_lines(file_name)
        logger.debug("graph: {0}".format(graph))
        visited_nodes = bfs(graph, 0)
        print("BFS visited nodes: {0}".format(visited_nodes))
    else:
        print("Please provide file name!")
