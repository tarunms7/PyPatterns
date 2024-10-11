from abc import ABC, abstractmethod

# Product: Represents a Meal
class Meal:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(f"Item: {item.name()}, Price: {item.price()}")

    def get_cost(self):
        return sum(item.price() for item in self.items)

# Abstract Item
class Item(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def price(self):
        pass

# Concrete Item: Burger
class Burger(Item):
    def name(self):
        return "Burger"

    def price(self):
        return 5.0

# Concrete Item: Drink
class Drink(Item):
    def name(self):
        return "Drink"

    def price(self):
        return 2.0

# Builder for Meal
class MealBuilder:
    def __init__(self):
        self.meal = Meal()

    def add_burger(self):
        self.meal.add_item(Burger())

    def add_drink(self):
        self.meal.add_item(Drink())

    def get_meal(self):
        return self.meal

# Example usage
if __name__ == "__main__":
    meal_builder = MealBuilder()
    meal_builder.add_burger()
    meal_builder.add_drink()
    meal = meal_builder.get_meal()

    print("Meal items:")
    meal.show_items()
    print(f"Total Cost: {meal.get_cost()}")
