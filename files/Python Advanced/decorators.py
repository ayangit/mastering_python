from functools import wraps
from time import sleep,perf_counter

def get_time(func):
    @wraps(func) #This @wraps is important to  get the doc and name to the function and not the wrapper
    def wrapper(*args,**kwargs):
        start_time = perf_counter()
        func(*args,**kwargs)
        end_time = perf_counter()
        total_time = round(end_time-start_time,3)
        print(f'Total time = {total_time}')
    #make sure to return wrapper and not wrapper() as we are not calling the wrapper here
    return wrapper


@get_time
def do_something(args):
    """Do something important  """
    sleep(1)
    for i in range(1):
        sleep(1)
    print(f'{args} is doing Something')

if __name__ == '__main__':
    do_something("John")
    print(f'Name = {do_something.__name__}')
    print(f'DocString = {do_something.__doc__}')