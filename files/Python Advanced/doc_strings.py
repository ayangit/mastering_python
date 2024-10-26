def add_numbers(a: int, b: int) -> int:
    """It adds two numbers:
        :param int a: 1st Integer Number to add
        :param int b: 2nd Integer Number to add
        :return : Returs the sum as integer
        :raises TypeError: If params are not string
    """
    if type(a)!= int or type(b)!=int:
        raise TypeError("Parameters  must be Integer")
    return a+b

if __name__ == '__main__':
    sum: int = add_numbers(10,"h")
    print(sum)

