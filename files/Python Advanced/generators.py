"""
def generate_list(n:int):
    for i in range(n):
        yield i

if __name__ == '__main__':
    generator = generate_list(10**100)
    list_1 : list[int] = []
    for i in range(10):
        list_1.append(next(generator))
    print(list_1)

    #OR
    list_1_1 : list[int]=[]
    index : int =0
    for i in generator:
        if(index==10):
            break
        index+=1
        list_1_1.append(i)

    print(list_1_1)


    list_2: list[int] =[]
    for j in range(10):
        list_2.append(next(generator))

    print(list_2)
"""

# Yield comprehension

if __name__ == '__main__':
    yield_comprehention = (i for i in range(10**100))
    #Note if we directly cast it into a list a below , it defeats the purpose of lazy loading
    yield_comprehention = list((i for i in range(10**100)))

    print(next(yield_comprehention))
    print(next(yield_comprehention))
    print(next(yield_comprehention))
    print(next(yield_comprehention))
    print(next(yield_comprehention))


