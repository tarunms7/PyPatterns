from abc import ABC, abstractmethod

# Product: Pizza
class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []

    def __str__(self):
        return f"Pizza size: {self.size}, crust: {self.crust}, toppings: {', '.join(self.toppings)}"

# Builder Interface
class PizzaBuilder(ABC):
    @abstractmethod
    def set_size(self):
        pass

    @abstractmethod
    def set_crust(self):
        pass

    @abstractmethod
    def add_topping(self, topping):
        pass

    @abstractmethod
    def get_pizza(self) -> Pizza:
        pass

# Concrete Builder: MargheritaPizzaBuilder
class MargheritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self):
        self.pizza.size = "Medium"

    def set_crust(self):
        self.pizza.crust = "Thin"

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)

    def get_pizza(self) -> Pizza:
        return self.pizza

# Concrete Builder: PepperoniPizzaBuilder
class PepperoniPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self):
        self.pizza.size = "Large"

    def set_crust(self):
        self.pizza.crust = "Thick"

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)

    def get_pizza(self) -> Pizza:
        return self.pizza

# Director
class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construct_pizza(self):
        self.builder.set_size()
        self.builder.set_crust()
        self.builder.add_topping("Cheese")
        self.builder.add_topping("Tomato")

    def get_pizza(self):
        return self.builder.get_pizza()
    
    
if __name__ == "__main__":
    #margerita pizza
    builder = MargheritaPizzaBuilder()
    director = PizzaDirector(builder=builder)
    director.construct_pizza()
    margerita_pizza = director.get_pizza()
    print("Margerita Pizza : ", margerita_pizza)
    
    #pepproni pizza
    builder = PepperoniPizzaBuilder()
    director = PizzaDirector(builder=builder)
    director.construct_pizza()
    pepproni_pizza = director.get_pizza()
    print("Pepproni Pizza : ", pepproni_pizza)