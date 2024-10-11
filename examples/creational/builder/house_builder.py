from abc import ABC, abstractmethod

# Product: Represents the complex object that is being constructed
class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.windows = None
        self.doors = None

    def __str__(self):
        return f"House with {self.walls}, {self.roof}, {self.windows} windows, and {self.doors} doors"

# Abstract Builder: Defines the building steps
class HouseBuilder(ABC):
    def __init__(self):
        self.house = House()

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    def get_house(self):
        return self.house

# Concrete Builder: Implements the building steps for a Wooden House
class WoodenHouseBuilder(HouseBuilder):
    def build_walls(self):
        self.house.walls = "wooden walls"

    def build_roof(self):
        self.house.roof = "wooden roof"

    def build_windows(self):
        self.house.windows = 4

    def build_doors(self):
        self.house.doors = 2

# Concrete Builder: Implements the building steps for a Stone House
class StoneHouseBuilder(HouseBuilder):
    def build_walls(self):
        self.house.walls = "stone walls"

    def build_roof(self):
        self.house.roof = "stone roof"

    def build_windows(self):
        self.house.windows = 6

    def build_doors(self):
        self.house.doors = 3

# Director: Constructs the product using the builder interface
class Director:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_windows()
        self.builder.build_doors()
        return self.builder.get_house()

# Example usage
if __name__ == "__main__":
    # Constructing a wooden house
    wooden_builder = WoodenHouseBuilder()
    director = Director(wooden_builder)
    wooden_house = director.construct_house()
    print(wooden_house)

    # Constructing a stone house
    stone_builder = StoneHouseBuilder()
    director = Director(stone_builder)
    stone_house = director.construct_house()
    print(stone_house)
