# Vehicle Interface
class Vehicle:
    def drive(self):
        pass

# Concrete Classes
class Car(Vehicle):
    def drive(self):
        return "Driving a car!"

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike!"

class Truck(Vehicle):
    def drive(self):
        return "Driving a truck!"

# Vehicle Factory
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

# Example usage
if __name__ == "__main__":
    vehicle_type = input("Enter vehicle type (car, bike, truck): ").lower()
    vehicle = VehicleFactory.create_vehicle(vehicle_type)
    print(vehicle.drive())
