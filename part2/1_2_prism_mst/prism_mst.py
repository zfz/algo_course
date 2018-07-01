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


def read_lines(file_name):
    with open(file_name) as f:
        lines = [line.strip() for line in f]
        node_num, edge_num = map(int, lines[0].split(' '))
        edge_list = [map(int, line.split(' ')) for line in lines[1:]]
        return node_num, edge_num, edge_list


def prism_mst(node_num, edge_list):
    # Nodes start from 1
    graph = [[0 for i in range(node_num+1)] for j in range(node_num+1)]
    for start_node, end_node, weight in edge_list:
        graph[start_node][end_node] = weight
        graph[end_node][start_node] = weight
    Logger.debug(graph)

    visited_nodes = set([1])
    heap = []
    for end_node, weight in enumerate(graph[1]):
        if weight:
            heappush(heap, (weight, 1, end_node))
    Logger.debug("{0} {1}".format(visited_nodes, heap))

    weight_sum = 0
    while len(visited_nodes) != node_num:
        weight, start_node, end_node = heappop(heap)
        if end_node not in visited_nodes:
            visited_nodes.add(end_node)
            weight_sum += weight
            Logger.debug("{0} {1} {2}".format(start_node, end_node, weight))
            Logger.debug("{0}".format(visited_nodes))
            for new_end_node, weight in enumerate(graph[end_node]):
                if weight:
                    heappush(heap, (weight, end_node, new_end_node))
    return weight_sum


def prism_mst_0(node_num, edge_list):
    # Nodes start from 0
    graph = [[0 for i in range(node_num)] for j in range(node_num)]
    for start_node, end_node, weight in edge_list:
        graph[start_node][end_node] = weight
        graph[end_node][start_node] = weight
    Logger.debug(graph)

    visited_nodes = set([0])
    heap = []
    for end_node, weight in enumerate(graph[0]):
        if weight:
            heappush(heap, (weight, 0, end_node))
    Logger.debug("{0} {1}".format(visited_nodes, heap))

    weight_sum = 0
    while len(visited_nodes) != node_num:
        weight, start_node, end_node = heappop(heap)
        if end_node not in visited_nodes:
            visited_nodes.add(end_node)
            weight_sum += weight
            Logger.debug("{0} {1} {2}".format(start_node, end_node, weight))
            Logger.debug("{0}".format(visited_nodes))
            for new_end_node, weight in enumerate(graph[end_node]):
                if weight:
                    heappush(heap, (weight, end_node, new_end_node))
    return weight_sum


if __name__ == "__main__":
    log_level = 1 if len(sys.argv) == 3 and sys.argv[2] == '1' else 0
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        setup_logger(log_level)
        node_num, edge_num, edge_list = read_lines(file_name)
        Logger.debug("node_num: {0} edge_num: {1} edge_list: {2}".format(
            node_num, edge_num, edge_list[:100]))
        weight_sum = prism_mst(node_num, edge_list)
        Logger.info("The overall cost of MST is: {0}".format(weight_sum))
    else:
        Logger.error("Please provide file name!")
