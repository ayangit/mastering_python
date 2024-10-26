numbers:list[int] = [1,2,3,4,5,6]

even:list[int] = list(filter(lambda x: x%2==0,numbers))
print(even)

display = lambda x: print(x)

display("Hello Display")