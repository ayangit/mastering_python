#zip combines multiple tuples

#Set 1:
# names: tuple[str] = ("John","Harry","Doe")
# numbers: tuple[int] = (10,20,30)
#
# zipped = zip(names, numbers)
#
# #Type casting to tuple is needed before printing
# print(tuple(zipped))

#Set 2:
names: tuple[str] = ("John","Harry","Doe","Jenny")
numbers: tuple[int] = (10,20,30)

# zipped = zip(names, numbers)
#it will not throw error , and will just ignore jenny
#to make it throw error we need to make the strict property true
zipped = zip(names, numbers,strict=True)
print(tuple(zipped))

#zipped can take multiple tuples ( even more than two ) as input to concatenate

