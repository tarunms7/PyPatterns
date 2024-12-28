from abc import ABC, abstractmethod

# Product: House
class House:
    def __init__(self):
        self.walls = None
        self.doors = None
        self.windows = None
        self.roof = None

    def __str__(self):
        return f"House with {self.walls} walls, {self.doors} doors, {self.windows} windows, and {self.roof} roof"

# Builder Interface
#abstract
class HouseBuilder(ABC):
    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def get_house(self) -> House:
        pass

# Concrete Builder: BasicHouseBuilder
class BasicHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "wooden"

    def build_doors(self):
        self.house.doors = 1

    def build_windows(self):
        self.house.windows = 2

    def build_roof(self):
        self.house.roof = "simple"

    def get_house(self) -> House:
        return self.house

# Concrete Builder: LuxuryHouseBuilder
class LuxuryHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "brick"

    def build_doors(self):
        self.house.doors = 3

    def build_windows(self):
        self.house.windows = 5

    def build_roof(self):
        self.house.roof = "luxury"

    def get_house(self) -> House:
        return self.house

# Director
class Director:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_walls()
        self.builder.build_doors()
        self.builder.build_windows()
        self.builder.build_roof()

    def get_house(self) -> House:
        return self.builder.get_house()

# Example Usage
if __name__ == "__main__":
    # Build a Basic House
    basic_builder = BasicHouseBuilder()
    director = Director(basic_builder)
    director.construct_house()
    house = director.get_house()
    print("Basic House:", house)

    # Build a Luxury House
    luxury_builder = LuxuryHouseBuilder()
    director = Director(luxury_builder)
    director.construct_house()
    house = director.get_house()
    print("Luxury House:", house)
