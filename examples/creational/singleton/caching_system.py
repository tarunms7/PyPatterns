class Cache:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Cache, cls).__new__(cls)
            cls._instance.storage = {}
        return cls._instance

    def set(self, key, value):
        self.storage[key] = value
        print(f"Set {key}: {value}")

    def get(self, key):
        return self.storage.get(key, None)

# Example Usage
if __name__ == "__main__":
    cache1 = Cache()
    cache1.set("user_1", "John Doe")

    cache2 = Cache()
    print(cache2.get("user_1"))  # Output: John Doe
    print(cache1 is cache2)  # True
