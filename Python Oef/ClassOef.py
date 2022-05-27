# 1 Instantiate the Cat object with 3 cats
# 2 Create a function that finds the oldest cat
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2


class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
Cat1 = Cat("Chris", 5);
Cat2 = Cat("Arie", 6);
Cat3 = Cat("Amore", 7);

def get_oldest(*args):
    return max(*args);

print(f"The oldest cat is {get_oldest(Cat1.age, Cat2.age, Cat3.age)} years old.")