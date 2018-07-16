import sys
import logging
from heapq import heappush, heappop
from itertools import combinations, product
Logger = logging.getLogger()


def setup_logger(level):
    handler = logging.StreamHandler()
    Logger.addHandler(handler)
    if level == 1:
        Logger.setLevel(logging.DEBUG)
    else:
        Logger.setLevel(logging.INFO)


def process_node(file_name):
    with open(file_name) as f:
        lines = [line.strip() for line in f]
        node_num, digit_num = map(int, lines[0].split(' '))
        node_set = {int(line.replace(' ', ''), 2) for line in lines[1:]}
        return digit_num, node_set


def binary_combinations(length, ones):
    combination_list = []
    for position in combinations(range(length), ones):
        combination = ''.join(
            ['1' if _ in position else '0' for _ in range(length)])
        combination_list.append(combination)
    return combination_list


def binary_distance(digit_num, distance):
    distance_list = []
    for i in range(1, distance+1):
        distance_list += binary_combinations(digit_num, i)
    distance_list = [int(dist, 2) for dist in distance_list]
    return distance_list


def cluster_big(node_set, distance_list):
    cluster_num = 0
    while len(node_set) > 0:
        neighbor = {node_set.pop()}
        cluster_num += 1
        while len(neighbor) > 0:
            target = {x^y for x, y in product(neighbor, distance_list)}
            neighbor = target & node_set
            node_set.difference_update(neighbor)
    return cluster_num


if __name__ == "__main__":
    log_level = 1 if len(sys.argv) == 3 and sys.argv[2] == 'debug' else 0
    setup_logger(log_level)
    distance = 2
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        digit_num, node_set = process_node(file_name)
        distance_list = binary_distance(digit_num, distance)
        #Logger.debug("distance_list: {0}".format([int(str(i), 2) for i in distance_list]))
        cluster_num = cluster_big(node_set, distance_list)
        Logger.info("cluster num is {0}".format(cluster_num))
    else:
        Logger.error("Please provide file name!")
