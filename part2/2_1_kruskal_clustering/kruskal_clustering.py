import sys
import logging
from heapq import heappush, heappop
Logger = logging.getLogger()


def setup_logger(level):
    handler = logging.StreamHandler()
    Logger.addHandler(handler)
    if level == 1:
        Logger.setLevel(logging.DEBUG)
    else:
        Logger.setLevel(logging.INFO)


class Graph(object):

    def __init__(self, node_num, edge_list):
        self.group_num = node_num
        self.edge_heap = []
        for start_node, end_node, weight in edge_list:
            heappush(self.edge_heap, (weight, start_node, end_node))
        self.parent = [i for i in range(node_num+1)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def union(self, x, y):
        # my wrong way to find root
        # x_parent, y_parent = self.parent[x], self.parent[y]
        # brute force to find and union without rank
        x_root, y_root = self.find(x), self.find(y)
        self.parent[x_root] = y_root
        self.group_num -= 1

    def check_circle(self, x, y):
        if self.find(x) == self.find(y):
            return True
        else:
            self.union(x, y)
            return False

    def kruskal_clustering(self, cluster_num):
        weight = -1
        while self.group_num >= cluster_num:
            weight, start_node, end_node = heappop(self.edge_heap)
            Logger.debug("parent: {0}".format(self.parent))
            circle = self.check_circle(start_node, end_node)
            Logger.debug("from {0} to {1} weight {2} has circle {3}".format(
                start_node, end_node, weight, circle))
        return weight


def build_graph(file_name):
    with open(file_name) as f:
        lines = [line.strip() for line in f]
        node_num = int(lines[0])
        edge_list = [map(int, line.split(' ')) for line in lines[1:]]
        graph = Graph(node_num, edge_list)
        return graph


if __name__ == "__main__":
    log_level = 1 if len(sys.argv) == 3 and sys.argv[2] == 'debug' else 0
    setup_logger(log_level)
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        graph = build_graph(file_name)
        cluster_num = 4
        cluster_weight = graph.kruskal_clustering(cluster_num)
        Logger.info("The max weight of {0}-cluster is {1}".format(
            cluster_num, cluster_weight))
    else:
        Logger.error("Please provide file name!")
