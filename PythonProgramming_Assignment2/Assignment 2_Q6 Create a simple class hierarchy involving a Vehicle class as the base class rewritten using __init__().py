#6.Create a simple class hierarchy involving a Vehicle class as the base class
#  and two subclasses Car and Bike
# this program rewritten using __init__()
# Base class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def move(self):
        print(f"The {self.vehicle_type} is moving.")


# Subclass: Car
class Car(Vehicle):
    def __init__(self, vehicle_type):
        super().__init__(vehicle_type)

    def move(self):
        print(f"The {self.vehicle_type} is driving on the road.")


# Subclass: Bike
class Bike(Vehicle):
    def __init__(self, vehicle_type):
        super().__init__(vehicle_type)

    def move(self):
        print(f"The {self.vehicle_type} is riding on two wheels.")


# Create objects
vehicle = Vehicle("vehicle")
car = Car("car")
bike = Bike("bike")

# Call methods
vehicle.move()
car.move()
bike.move()