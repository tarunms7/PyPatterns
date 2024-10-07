"""
Singleton Design Pattern

Intent:
Ensure a class only has one instance and provide a global point of access to it.
"""

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Example Usage
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)  # True
