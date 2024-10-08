class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance.config = cls._load_configuration()
        return cls._instance

    @staticmethod
    def _load_configuration():
        # Simulate loading configuration from a file or environment
        return {"app_name": "SingletonApp", "version": "1.0.0"}

    def get_config(self):
        return self.config

# Example Usage
if __name__ == "__main__":
    config1 = ConfigurationManager()
    print(config1.get_config())  # Output: {'app_name': 'SingletonApp', 'version': '1.0.0'}

    config2 = ConfigurationManager()
    print(config1 is config2)  # True
