import time
from functools import wraps


def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        print(f'Function {fn.__name__} is going to run')
        result = fn(*args, **kwargs)
        run_time = '{:.12f}'.format(time.perf_counter() - start_time)
        print(f'Function {fn.__name__} has finished running, run time is {run_time} seconds')
        return result

    return wrapper
