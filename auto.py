## Utility decorators

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        startTime = time.perf_counter()
        result = func(*args, **kwargs)
        totalTime = time.perf_counter()-startTime

        return (result,totalTime)
    return wrapper
