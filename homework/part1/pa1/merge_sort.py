import logging
logger = logging.getLogger()
inversion_count = 0


def setup_debug_logger():
    handler = logging.StreamHandler()
    global logger
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def merge_sort(l):
    if len(l) > 1:  # Point 1
        mid = len(l) / 2
        left, right = l[:mid], l[mid:]
        logger.debug("split left: {0}, right {1}".format(left, right))

        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        logger.debug("sorted left: {0}, sorted right {1}".format(
            sorted_left, sorted_right))

        return merge(sorted_left, sorted_right)
    else:
        return l


def merge(left, right):
    merged_list = []
    while left and right:
        element = left.pop(0) if left[0] < right[0] else right.pop(0)
        merged_list.append(element)

        logger.debug("merged_list: {0}".format(merged_list))

    logger.debug("return merged list: {0}".format(merged_list + left + right))
    return merged_list + left + right  # Point 2


def merge_sort_count(l):
    if len(l) > 1:
        mid = len(l) / 2
        left, right = l[:mid], l[mid:]
        logger.debug("split left: {0}, right {1}".format(left, right))

        sorted_left = merge_sort_count(left)
        sorted_right = merge_sort_count(right)
        logger.debug("sorted left: {0}, sorted right {1}".format(
            sorted_left, sorted_right))

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

        logger.debug("merged_list: {0}".format(merged_list))

    logger.debug("return merged list: {0}".format(merged_list + left + right))
    return merged_list + left + right


if __name__ == "__main__":
    setup_debug_logger()
    a = [7, 5, 3, 4, 2, 8, 6, 1]
    # print("original list: {0}\n sorted list: {1}".format(a, merge_sort(a)))
    print("original list: {0}\n sorted list: {1}".format(
        a, merge_sort_count(a)))
    print(" inversion count: {0}".format(inversion_count))
