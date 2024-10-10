# Shape Interface
class Shape:
    def draw(self):
        pass

# Concrete Classes
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"

# Shape Factory
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Example usage
if __name__ == "__main__":
    shape_type = input("Enter shape type (circle, square, rectangle): ").lower()
    shape = ShapeFactory.create_shape(shape_type)
    print(shape.draw())
