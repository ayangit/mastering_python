class Fruit:
    def __init__(self,name:str,calorie:int):
        self.name = name
        self.calorie = calorie
    def __repr__(self):
        return  f'{self.name} : {self.calorie}'

def get_calorie(fruit : Fruit):
    return fruit.calorie

def get_name(fruit : Fruit):
    return fruit.name

fruits: list[Fruit] = []
fruits.append(Fruit("Apple",100))
fruits.append(Fruit("Bananna",50))
fruits.append(Fruit("Dragon",30))

#this will give  an error as it cannot find a way to compare
# sorted_fruits : list[Fruit] = sorted(fruits)

#now lets sort using a key
sorted_fruits : list[Fruit] = sorted(fruits,key=get_calorie)
print(sorted_fruits)

# Now sort my name
# sorted_fruits : list[Fruit] = sorted(fruits,key=get_name)
# print(sorted_fruits)


# We can also change the order to reverse
sorted_fruits : list[Fruit] = sorted(fruits,key=get_name,reverse=False)
print(sorted_fruits)
