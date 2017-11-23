import sys
import logging
from heapq import heappush, nsmallest
import time
Logger = logging.getLogger()


def setup_debug_logger():
    handler = logging.StreamHandler()
    Logger.addHandler(handler)
    Logger.setLevel(logging.DEBUG)


def read_lines(file_name):
    with open(file_name) as f:
        return [int(line.strip()) for line in f]


def heap_median_maintanance(stream):
    median_list, heap = [], []
    for i in stream:
        median = find_median(i, heap)
        Logger.debug("Stream {0} heap {1} median {2}".format(i, heap, median))
        median_list.append(median)
    return sum(median_list) % 10000


def find_median(i, heap):
    heappush(heap, i)
    median_index = (len(heap) + 1) / 2
    median = max(nsmallest(median_index, heap))
    return median


if __name__ == "__main__":
    # setup_debug_logger()
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        int_stream = read_lines(file_name)
        start_time = time.time()
        median_mod = heap_median_maintanance(int_stream)
        print("Median maintainance mod: {0}".format(median_mod))
        print("Median maintainance using Heap: {0:.2f} seconds".format(
            time.time() - start_time))
    else:
        print("Please provide file name!")
