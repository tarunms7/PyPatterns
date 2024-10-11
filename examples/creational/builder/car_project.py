from abc import ABC, abstractmethod

# Product: Car
class Car:
    def __init__(self):
        self.engine = None
        self.seats = None
        self.gps = None

    def __str__(self):
        return f"Car with {self.engine} engine, {self.seats} seats, GPS: {self.gps}"

# Builder Interface
class CarBuilder(ABC):
    @abstractmethod
    def set_engine(self):
        pass

    @abstractmethod
    def set_seats(self):
        pass

    @abstractmethod
    def set_gps(self):
        pass

    @abstractmethod
    def get_car(self) -> Car:
        pass

# Concrete Builder: SportCarBuilder
class SportCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_engine(self):
        self.car.engine = "V8"

    def set_seats(self):
        self.car.seats = 2

    def set_gps(self):
        self.car.gps = True

    def get_car(self) -> Car:
        return self.car

# Concrete Builder: FamilyCarBuilder
class FamilyCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_engine(self):
        self.car.engine = "V4"

    def set_seats(self):
        self.car.seats = 5

    def set_gps(self):
        self.car.gps = False

    def get_car(self) -> Car:
        return self.car

# Director
class CarDirector:
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def construct_car(self):
        self.builder.set_engine()
        self.builder.set_seats()
        self.builder.set_gps()

    def get_car(self) -> Car:
        return self.builder.get_car()

# Example usage
if __name__ == "__main__":
    # Build a Sports Car
    sport_builder = SportCarBuilder()
    director = CarDirector(sport_builder)
    director.construct_car()
    car = director.get_car()
    print("Sports Car:", car)

    # Build a Family Car
    family_builder = FamilyCarBuilder()
    director = CarDirector(family_builder)
    director.construct_car()
    car = director.get_car()
    print("Family Car:", car)
