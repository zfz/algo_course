import sys
import logging
logger = logging.getLogger()


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


def median_of_three(l, start, end):
    """Returns the index of the median of three values:
        the first one, the last one, and the middle one.
    l = input list/array
    start = start index
    end = end index"""

    mid = start + int((end - start) / 2)
    median = min(max(l[start], l[end]),
                 max(l[start], l[mid]), max(l[mid], l[end]))
    logger.debug("start: {0}, mid: {1}, end: {2}, median: {0}".format(
        l[start], l[mid], l[end], median))
    if median == l[start]:
        return start
    elif median == l[end]:
        return end
    else:
        return mid


def quick_sort_partition(l, start, end, compare_count, pivot_choice):
    """Partition the array/list l around a certain pivot choosing by way
    l = input list/array
    start = start index
    end = end index
    compare_count = mutable data struct to store the number of comparisons
    pivot_choice = which way to select the pivot"""

    if pivot_choice == 1:
        l[end], l[start] = l[start], l[end]
    elif pivot_choice == 2:
        m = median_of_three(l, start, end)
        l[m], l[start] = l[start], l[m]
    pivot = l[start]

    i = start + 1
    for j in range(start+1, end+1):
        if l[j] < pivot:
            l[j], l[i] = l[i], l[j]
            i += 1
    l[start], l[i-1] = l[i-1], l[start]
    compare_count[0] += (end - start)
    return i-1


def quick_sort(l, start, end, compare_count, pivot_choice):
    """The quick sort algorithm which runs in O(nlogn) time on average
    l = input list/array
    start = start index
    end = end index
    compare_count = mutable data struct to store the number of comparisons
    pivot_choice = which way to select the pivot"""

    if start < end:
        pivot_index = quick_sort_partition(l, start, end,
                                           compare_count, pivot_choice)
        quick_sort(l, start, pivot_index-1, compare_count, pivot_choice)
        quick_sort(l, pivot_index+1, end, compare_count, pivot_choice)


if __name__ == "__main__":
    #setup_debug_logger()
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        input_array = read_lines(file_name)
        logger.debug("Int array: {0}, length: {1}".format(
            input_array, len(input_array)))
        for i in range(3):
            int_array = input_array[:]
            compare_count = [0]
            quick_sort(int_array, 0, len(int_array)-1, compare_count, i)
            logger.debug("sorted list: {0}".format(int_array))
            print("choice {0} compare count: {1}".format(i, compare_count))
    else:
        print("Please provide file name!")
