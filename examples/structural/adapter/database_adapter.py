# Target Interface (Modern API expected by new code)
class DatabaseInterface:
    def connect(self):
        pass

    def query(self, sql):
        pass


# Adaptee (Legacy Database with a different interface)
class LegacyDatabase:
    def old_connect(self):
        print("Connecting to legacy database...")

    def old_execute(self, sql):
        print(f"Executing SQL in legacy database: {sql}")


# Adapter (Bridging LegacyDatabase to DatabaseInterface)
class LegacyDatabaseAdapter(DatabaseInterface):
    def __init__(self, legacy_db):
        self.legacy_db = legacy_db


