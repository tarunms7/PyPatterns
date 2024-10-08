class DatabaseConnectionPool:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnectionPool, cls).__new__(cls)
            cls._instance.pool = cls._create_connection_pool()
        return cls._instance

    @staticmethod
    def _create_connection_pool():
        # Simulate creation of a connection pool
        return "Database Connection Pool Created"

    def get_connection(self):
        return f"Getting a connection from {self.pool}"

# Example Usage
if __name__ == "__main__":
    pool1 = DatabaseConnectionPool()
    print(pool1.get_connection())  # "Getting a connection from Database Connection Pool Created"

    pool2 = DatabaseConnectionPool()
    print(pool1 is pool2)  # True, both references point to the same instance
