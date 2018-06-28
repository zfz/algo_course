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
        job_num = int(lines[0])
        job_list = [line.split(' ') for line in lines[1:]]
        return job_num, job_list


def schedule_job(job_list, method='differnce'):
    heap = []
    for weight, length in job_list:
        if method == 'differnce':
            greed = int(weight) - int(length)
        elif method == 'ratio':
            greed = float(weight) / float(length)
        heappush(heap, (-greed, -int(weight), int(length)))
    weighted_sum, finish_time = 0, 0
    while heap:
        greed, weight, length = heappop(heap)
        finish_time += length
        weighted_sum += -weight * finish_time
    return weighted_sum, finish_time


if __name__ == "__main__":
    setup_logger(logging.INFO)
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        job_num, job_list = read_lines(file_name)
        weighted_sum, finish_time = schedule_job(job_list, 'differnce')
        Logger.info("Difference weighted sum: {0} finish_time: {1}".format(
            weighted_sum, finish_time))
        weighted_sum, finish_time = schedule_job(job_list, 'ratio')
        Logger.info("Ratio weighted sum: {0} finish_time: {1}".format(
            weighted_sum, finish_time))
    else:
        Logger.error("Please provide file name!")
