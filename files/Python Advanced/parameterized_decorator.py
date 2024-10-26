from functools import wraps
from typing import Callable

"""
    Start with the decorator name with the parameter 
    Inside that make a decorator function that takes a callable function as argument
    Inside that make the wrapper
    outside the wrapper define @wraps and pass the functino in that @wraps(func)
    Now make the wrapper function to do what you intent.
    The wrapper takes *args and **kwargs as  argument 
    Remember to return the wrapper and decorator
    
"""

def repeat(times:int):
    def decorator(func:Callable):
        @wraps(func)
        def wrapper(*args,**kwargs):
            value = None
            for i in range(times):
                value = func(*args,**kwargs)
            return value
        return wrapper
    return decorator

def repeatMessage(times:int,message:str):
    def decorator(func:Callable):
        @wraps(func)
        def wrapper(*args,**kwargs):
            value = None
            for i in range(times):
                value = func(*args,**kwargs)
                print(f'{message}')
            return value
        return wrapper
    return decorator

@repeat(2)
def func1():
    print("hello!")

@repeatMessage(2,"working")
def func2():
    print("hello!")



if __name__ == '__main__':
    # func1()
    func2()