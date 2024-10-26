from dataclasses import dataclass


@dataclass
class Animal:
    name: str
    age: int

if __name__ == '__main__':
    cat : Animal = Animal("Cat","3")
    print(cat)
