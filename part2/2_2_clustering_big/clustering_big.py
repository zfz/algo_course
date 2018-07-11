import sys
import logging
Logger = logging.getLogger()


def setup_logger(level):
    handler = logging.StreamHandler()
    Logger.addHandler(handler)
    if level == 1:
        Logger.setLevel(logging.DEBUG)
    else:
        Logger.setLevel(logging.INFO)


if __name__ == "__main__":
    log_level = 1 if len(sys.argv) == 3 and sys.argv[2] == 'debug' else 0
    setup_logger(log_level)
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        Logger.error("Please provide file name!")
