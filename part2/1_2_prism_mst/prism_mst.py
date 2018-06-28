import sys
import logging
from heapq import heappush, heappop
Logger = logging.getLogger()


def setup_logger(level):
    handler = logging.StreamHandler()
    Logger.addHandler(handler)
    Logger.setLevel(level)


def read_lines(file_name):
    with open(file_name) as f:
        lines = [line.strip() for line in f]
        node_num, edge_num = lines[0].split(' ')
        node_num, edge_num = int(node_num), int(edge_num)
        edge_list = [line.split(' ') for line in lines[1:]]
        return node_num, edge_num, edge_list


def prism_mst(edge_list):
    pass


if __name__ == "__main__":
    setup_logger(logging.DEBUG)
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        node_num, edge_num, edge_list = read_lines(file_name)
        Logger.debug("nodes_num: {0} edge_num: {1} edge_list: {2}".format(
            node_num, edge_num, edge_list[:100]))
    else:
        Logger.error("Please provide file name!")
