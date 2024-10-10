from abc import ABC, abstractmethod

# Abstract Product: Chair
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

# Abstract Product: Table
class Table(ABC):
    @abstractmethod
    def place_item(self):
        pass

# Concrete Product: Modern Chair
class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a modern chair"

# Concrete Product: Modern Table
class ModernTable(Table):
    def place_item(self):
        return "Placing item on a modern table"

# Concrete Product: Victorian Chair
class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian chair"

# Concrete Product: Victorian Table
class VictorianTable(Table):
    def place_item(self):
        return "Placing item on a Victorian table"

# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass

# Concrete Factory: Modern Furniture Factory
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()

# Concrete Factory: Victorian Furniture Factory
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_table(self) -> Table:
        return VictorianTable()


"""
OUTPUT 

Modern Furniture:
Sitting on a modern chair
Placing item on a modern table

Victorian Furniture:
Sitting on a Victorian chair
Placing item on a Victorian table

"""