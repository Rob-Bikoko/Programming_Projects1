# Classes and Objects
class Dog:
    species = "Canine"  # Class attribute

    # the init method is called when a new object of a class is created
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Tom", 8)

print(dog1.name)
print(dog1.species)
print(dog1.age)
print("\n")


print(dog2.name)
print(dog2.species)
print(dog2.age)