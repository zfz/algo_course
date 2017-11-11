import sys
from collections import defaultdict
from heapq import heappop, heappush
import logging
Logger = logging.getLogger()


def setup_debug_logger():
    handler = logging.StreamHandler()
    Logger.addHandler(handler)
    Logger.setLevel(logging.DEBUG)


def read_lines(file_name):
    g = defaultdict(list)
    with open(file_name) as f:
        for line in f:
            items = line.strip().split('\t')
            src = int(items[0])
            for item in items[1:]:
                dst, weight = map(int, item.split(','))
                g[src].append((weight, dst))
    Logger.debug("graph: {0}".format(g[1]))
    return g


def shortest_paths(g, src):
    D = [0 for i in range(len(g) + 1)]
    queue = []
    heappush(queue, (0, src))
    while queue:
        weight, node = heappop(queue)
        if D[node] == 0:
            D[node] += weight
            for dst_weight, dst in g[node]:
                heappush(queue, (D[node] + dst_weight, dst))
    return D


if __name__ == "__main__":
    # setup_debug_logger()
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        graph = read_lines(file_name)
        dst_paths = shortest_paths(graph, 1)
        print("Shortest paths is {0}".format(dst_paths))
        dst_list = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
        for dst in dst_list:
            print("Vetex {0}'s path is {1}".format(dst, dst_paths[dst]))
    else:
        print("Please provide file name!")
