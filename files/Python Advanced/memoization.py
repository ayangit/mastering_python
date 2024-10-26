from collections.abc import Callable
from functools import wraps, cache
from time import perf_counter

def memoize(func:Callable):
    keys = {}
    @wraps(func)
    def wrapper(*args,**kwargs):
        key = str(*args)+ str(**kwargs)
        if key not in keys:
            keys[key]= func(*args,**kwargs)
        return keys[key]
    return wrapper

@memoize
def fibonachi(n:int):
    if n < 2:
        return n
    return fibonachi(n-1)+fibonachi(n-2)

# Or you can use the inbuilt cache in python
# In built cache is often more efficient
@cache
def fibonachi(n:int):
    if n < 2:
        return n
    return fibonachi(n-1)+fibonachi(n-2)

if __name__ == '__main__':
    start_time = perf_counter()
    print(fibonachi(70))
    end_time = perf_counter()
    print(end_time-start_time)