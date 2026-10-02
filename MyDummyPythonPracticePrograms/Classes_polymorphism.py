#Classes_polymorphism
class Animal:
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Function that demonstrates polymorphism
def animal_sound(animal):
    print(animal.sound())

# Create instances of Dog and Cat
my_dog = Dog()
my_cat = Cat()

# Call the function with different animal types
animal_sound(my_dog)  # Output: Woof!
animal_sound(my_cat)  # Output: Meow!