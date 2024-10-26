class Car:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name


if __name__ == "__main__":
    car1 : Car = Car("Toyota")
    car2 : Car = Car("Toyota")

    #Note:
    # As the id's are diffrent the is operator returns false
    # As the __eq__ compares the two names so the == operator returns true
    print(f'{id(car1)} , {id(car2)}')
    print(f'Car1 == Car 2 ', car1==car2)
    print(f'Car1 is Car 2 ', car1 is car2)