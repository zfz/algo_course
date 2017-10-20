import sys
import logging
logger = logging.getLogger()
inversion_count = 0


def setup_debug_logger():
    handler = logging.StreamHandler()
    global logger
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def read_lines(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    int_array = [int(line.strip()) for line in lines]
    return int_array


def merge_sort_count(l):
    if len(l) > 1:
        mid = len(l) / 2
        left, right = l[:mid], l[mid:]
        # logger.debug("split left: {0}, right {1}".format(left, right))

        sorted_left = merge_sort_count(left)
        sorted_right = merge_sort_count(right)
        # logger.debug("sorted left: {0}, sorted right {1}".format(
        #     sorted_left, sorted_right))

        return merge_count(sorted_left, sorted_right)
    else:
        return l


def merge_count(left, right):
    merged_list = []
    while left and right:
        if left[0] < right[0]:
            element = left.pop(0)
            merged_list.append(element)
        else:
            element = right.pop(0)
            merged_list.append(element)
            global inversion_count
            inversion_count += len(left)  # Point 3
            logger.debug("inversion_count: {0}".format(inversion_count))

        # logger.debug("merged_list: {0}".format(merged_list))

    # logger.debug("return merged list: {0}".format(merged_list + left + right))
    return merged_list + left + right


if __name__ == "__main__":
    setup_debug_logger()
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        int_array = read_lines(file_name)
        logger.debug("Int array: {0}, length: {1}".format(
            int_array, len(int_array)))
        merge_sort_count(int_array)
        print("Int array inversion count: {0}".format(inversion_count))
    else:
        print("Please provide file name!")
