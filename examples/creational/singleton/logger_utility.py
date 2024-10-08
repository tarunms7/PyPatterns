class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_file = cls._create_log_file()
        return cls._instance

    @staticmethod
    def _create_log_file():
        # Simulate creation of a log file
        return "logfile.txt"

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(f"{message}\n")
        print(f"Logged: {message}")

# Example Usage
if __name__ == "__main__":
    logger1 = Logger()
    logger1.log("First log message")

    logger2 = Logger()
    logger2.log("Second log message")

    print(logger1 is logger2)  # True
