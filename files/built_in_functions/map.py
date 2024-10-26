numbers: list[int] = [1, 2, 3, 4]
numbers2: list[int] = [10, 20, 30, 40]

def convert_to_str(element):
    element *= element
    return str(element)

converted_list: list[str] = list(map(convert_to_str,numbers))
print(converted_list)

