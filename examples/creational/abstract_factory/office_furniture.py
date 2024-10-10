from creational.abstract_factory import Chair, Table, FurnitureFactory

# Additional Concrete Product: Office Chair
class OfficeChair(Chair):
    def sit_on(self):
        return "Sitting on an office chair"

# Additional Concrete Product: Office Table
class OfficeTable(Table):
    def place_item(self):
        return "Placing item on an office table"

# Additional Concrete Factory: Office Furniture Factory
class OfficeFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return OfficeChair()

    def create_table(self) -> Table:
        return OfficeTable()

# Example usage
def client_code(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    
    print(chair.sit_on())
    print(table.place_item())

if __name__ == "__main__":
    print("Office Furniture:")
    office_factory = OfficeFurnitureFactory()
    client_code(office_factory)
