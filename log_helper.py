import time
import logging
from pythonjsonlogger import jsonlogger

def setup_logging():

    logger = logging.getLogger()
    # Remove all handlers if any exist
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        milliseconds = int(elapsed_time * 1000)
        logging.info(f"{func.__name__} took {format(milliseconds, ',')} milliseconds to execute", extra={'elapsed_time': milliseconds})
        return result
    return wrapper
