# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")

my_dog = Labrador("Buddy")

# Call the methods
my_dog.display_name()  # Displays the dog's name
my_dog.sound()