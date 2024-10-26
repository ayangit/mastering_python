# Using simple performance counter
# import time
# from time import perf_counter
# from turtledemo.penrose import start
#
#
# def do_something():
#     for i in range(10**6):
#         pass
#     print("Doing Something")
#     time.sleep(1)
#
# def time_function(func):
#     start_time = perf_counter()
#     do_something()
#     end_time = perf_counter()
#     duration = end_time-start_time
#     print(duration)
#
# if __name__ == '__main__':
#     time_function(do_something)
import time
import timeit


# Using timeit module

def do_something():
    for i in range(10**2):
        pass
    # time.sleep(1)
    # print("doing something again !")

def do_calculation(a:int ,b:int):
    for i in range(10**2):
        pass
    print(a+b)

def measure_time(func:str,repeat:int,number:int):
    duration = min(timeit.repeat(func,repeat=repeat,number=number,globals=globals()))
    print(duration)

if __name__=="__main__":
    measure_time("do_something()",10,(10))
    measure_time("do_calculation(10,20)",10,(10))