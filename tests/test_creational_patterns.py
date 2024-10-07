import unittest
from creational.singleton import Singleton

class TestSingleton(unittest.TestCase):

    def test_singleton_instance(self):
        s1 = Singleton()
        s2 = Singleton()
        self.assertIs(s1, s2)  # Both should be the same instance

if __name__ == '__main__':
    unittest.main()
