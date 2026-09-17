#6.Create a simple class hierarchy involving a Vehicle class as the base class
#  and two subclasses Car and Bike
# Base class
class Vehicle:

    def move(self):
        print("The vehicle is moving.")


# Subclass: Car
class Car(Vehicle):

    def move(self):
        print("The car is driving on the road.")


# Subclass: Bike
class Bike(Vehicle):

    def move(self):
        print("The bike is riding on two wheels.")


# Create objects
vehicle = Vehicle()
car = Car()
bike = Bike()

# Call methods
vehicle.move()
car.move()
bike.move()