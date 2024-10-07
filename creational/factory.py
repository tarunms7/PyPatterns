"""
Factory Design Pattern

Intent:
Define an interface for creating an object, but let subclasses decide which class to instantiate.
Factory Method lets a class defer instantiation to subclasses.
"""

from abc import ABC, abstractmethod

# Product Interface
class Vehicle(ABC):
    @abstractmethod
    def create(self):
        pass

# Concrete Products
class Car(Vehicle):
    def create(self):
        return "Car created!"

class Truck(Vehicle):
    def create(self):
        return "Truck created!"

# Factory Class
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

# Example usage
if __name__ == "__main__":
    factory = VehicleFactory()

    vehicle1 = factory.get_vehicle("car")
    print(vehicle1.create())  # Output: Car created!

    vehicle2 = factory.get_vehicle("truck")
    print(vehicle2.create())  # Output: Truck created!
