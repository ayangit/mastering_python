things : list[str,int] = ["John","Doe",10,20]

def is_str(element):
    return isinstance(element,str)

def is_int(element):
    return isinstance(element,int)

filtered_str_list : list[str] = list(filter(is_str,things))

print(filtered_str_list)

#Note : Filters and maps use lazy loading
filtered_int_list : list[str] = list(filter(is_int,things))

print(filtered_int_list)