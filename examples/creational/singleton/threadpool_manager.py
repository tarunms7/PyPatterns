import threading

class ThreadPool:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ThreadPool, cls).__new__(cls)
            cls._instance.pool = cls._create_thread_pool()
        return cls._instance

    @staticmethod
    def _create_thread_pool():
        # Simulate creation of a thread pool
        return [threading.Thread() for _ in range(5)]

    def get_pool(self):
        return self.pool

# Example Usage
if __name__ == "__main__":
    pool1 = ThreadPool()
    print(pool1.get_pool())  # Outputs list of threads

    pool2 = ThreadPool()
    print(pool1 is pool2)  # True
