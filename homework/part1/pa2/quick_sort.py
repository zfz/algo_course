import logging
logger = logging.getLogger()
compare_count = 0


def setup_debug_logger():
    handler = logging.StreamHandler()
    global logger
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def quick_sort(l):
    if len(l) > 1:  # Point 1
        pivot = l[0]  # Choose the first element as the pivot
        logger.debug("pivot: {0}".format(pivot))
        small = [i for i in l if i < pivot]
        mid = [i for i in l if i == pivot]
        big = [i for i in l if i > pivot]
        logger.debug("small: {0}, mid: {1}, big: {2}".format(small, mid, big))

        global compare_count
        compare_count += (len(l) - 1)
        logger.debug("compare_count: {0}".format(compare_count))
        return quick_sort(small) + mid + quick_sort(big)
    else:
        return l


if __name__ == "__main__":
    setup_debug_logger()
    #a = [7, 5, 3, 4, 2, 8, 6, 1]
    a = [1, 3, 5, 2, 4, 6]
    print("original list: {0}\n sorted list: {1}".format(a, quick_sort(a)))
    print(" compare count: {0}".format(compare_count))
