import copy

# Prototype Interface
class Prototype:
    def clone(self):
        """Method to clone the object. Should be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement clone method.")

# Concrete Prototype 1: Car
class Car(Prototype):
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __str__(self):
        return f"Car(model={self.model}, color={self.color})"

    def clone(self):
        """Returns a deep copy of the Car object."""
        return copy.deepcopy(self)

# Concrete Prototype 2: Smartphone
class Smartphone(Prototype):
    def __init__(self, brand, model, os):
        self.brand = brand
        self.model = model
        self.os = os

    def __str__(self):
        return f"Smartphone(brand={self.brand}, model={self.model}, os={self.os})"

    def clone(self):
        """Returns a deep copy of the Smartphone object."""
        return copy.deepcopy(self)

# Concrete Prototype 3: House
class House(Prototype):
    def __init__(self, address, floors):
        self.address = address
        self.floors = floors

    def __str__(self):
        return f"House(address={self.address}, floors={self.floors})"

    def clone(self):
        """Returns a deep copy of the House object."""
        return copy.deepcopy(self)


if __name__ == "__main__":
    # Creating original objects
    car1 = Car("Toyota", "Red")
    phone1 = Smartphone("Apple", "iPhone 12", "iOS")
    house1 = House("123 Maple St", 2)

    # Cloning the objects
    car_clone = car1.clone()
    phone_clone = phone1.clone()
    house_clone = house1.clone()

    # Printing original and cloned objects
    print("Original Car:", car1)
    print("Cloned Car:", car_clone)

    print("Original Phone:", phone1)
    print("Cloned Phone:", phone_clone)

    print("Original House:", house1)
    print("Cloned House:", house_clone)
