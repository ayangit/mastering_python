alphabets: list[str] = ['A', 'b', 'C', 'd', 'E', 'f']

# .sort sorts it in place
# print(alphabets.sort())
# print(alphabets)

# sorted creates a new sorted list

# sorted_alphabets : list[str] = sorted(alphabets)
# print(sorted_alphabets)

# You can mention a key to sort in a particular order
# here while sorting it converts each element to lower case first. Also note its str.lower and not str.lower()
sorted_alphabets: list[str] = sorted(alphabets, key=str.lower)
print(sorted_alphabets)
