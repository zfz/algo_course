import sys
import logging
Logger = logging.getLogger()


def setup_debug_logger():
    handler = logging.StreamHandler()
    Logger.addHandler(handler)
    Logger.setLevel(logging.DEBUG)


def read_lines(file_name):
    d = {}
    with open(file_name) as f:
        for line in f:
            d[int(line.strip())] = 1
    return d


def two_sum(t, d):
    for x in d:
        if t - x in d:
            if x != (t-x):
                Logger.debug("two_sum true : {0}".format(t))
                return True
    return False


def count_two_sum(d):
    c = 0
    for t in range(-10000, 10001):
        Logger.debug("two_sum: {0}".format(t))
        if two_sum(t, d):
            c += 1
    return c


if __name__ == "__main__":
    # setup_debug_logger()
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        d = read_lines(file_name)
        c = count_two_sum(d)
        print("count_two_sum: {0}".format(c))
    else:
        print("Please provide file name!")
