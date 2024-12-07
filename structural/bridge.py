# Implementation Interface
class Color:
    def apply_color(self):
        pass


# Concrete Implementations
class RedColor(Color):
    def apply_color(self):
        return "Red"


class BlueColor(Color):
    def apply_color(self):
        return "Blue"


# Abstraction
class Shape:
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        pass


# Refined Abstractions
class Circle(Shape):
    def draw(self):
        print(f"Drawing Circle in {self.color.apply_color()} color")


class Square(Shape):
    def draw(self):
        print(f"Drawing Square in {self.color.apply_color()} color")


# Client Code
if __name__ == "__main__":
    # Create different colors
    red = RedColor()
    blue = BlueColor()

    # Draw shapes with different colors
    red_circle = Circle(red)
    blue_square = Square(blue)

    red_circle.draw()   # Output: Drawing Circle in Red color
    blue_square.draw()  # Output: Drawing Square in Blue color
