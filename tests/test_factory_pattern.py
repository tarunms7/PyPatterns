import unittest
from creational.factory import VehicleFactory, Car, Truck

class TestFactoryPattern(unittest.TestCase):
    
    def test_car_creation(self):
        car = VehicleFactory.get_vehicle("car")
        self.assertIsInstance(car, Car)
        self.assertEqual(car.create(), "Car created!")
    
    def test_truck_creation(self):
        truck = VehicleFactory.get_vehicle("truck")
        self.assertIsInstance(truck, Truck)
        self.assertEqual(truck.create(), "Truck created!")
    
    def test_invalid_vehicle(self):
        with self.assertRaises(ValueError) as context:
            VehicleFactory.get_vehicle("bike")
        self.assertEqual(str(context.exception), "Unknown vehicle type: bike")

if __name__ == "__main__":
    unittest.main()
