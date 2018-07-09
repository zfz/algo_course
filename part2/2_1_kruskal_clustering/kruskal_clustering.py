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
        node_num = int(lines[0])
        edge_list = [map(int, line.split(' ')) for line in lines[1:]]
        return node_num, edge_list


if __name__ == "__main__":
    log_level = 1 if len(sys.argv) == 3 and sys.argv[2] == '1' else 0
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        setup_logger(log_level)
        node_num, edge_list = read_lines(file_name)
        Logger.debug("node_num: {0} edge_list: {1}".format(
            node_num, edge_list[:100]))
    else:
        Logger.error("Please provide file name!")
