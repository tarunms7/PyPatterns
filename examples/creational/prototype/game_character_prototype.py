import copy
from creational.prototype import Prototype

class GameCharacter(Prototype):
    def __init__(self, name, level, inventory):
        self.name = name
        self.level = level
        self.inventory = inventory  # Dictionary of items

    def __str__(self):
        return f"GameCharacter(name={self.name}, level={self.level}, inventory={self.inventory})"

    def clone(self):
        """Perform deep copy of the GameCharacter object."""
        return copy.deepcopy(self)

if __name__ == "__main__":
    # Create a character with inventory
    character1 = GameCharacter("Hero", 10, {"sword": 1, "shield": 1, "potion": 5})

    # Cloning the character
    character_clone = character1.clone()

    # Modify the clone's inventory
    character_clone.inventory["potion"] += 5

    print("Original Character:", character1)
    print("Cloned Character:", character_clone)
