from creational.abstract_factory import ModernFurnitureFactory, VictorianFurnitureFactory

def client_code(factory):
    chair = factory.create_chair()
    table = factory.create_table()
    
    print(chair.sit_on())
    print(table.place_item())

if __name__ == "__main__":
    print("Modern Furniture:")
    modern_factory = ModernFurnitureFactory()
    client_code(modern_factory)

    print("\nVictorian Furniture:")
    victorian_factory = VictorianFurnitureFactory()
    client_code(victorian_factory)
