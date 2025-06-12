import unittest
from FahrenheitToCelsius import FahrenheitToCelsius

class TestFahrenheitToCelsius(unittest.TestCase):
    def test_Celsius(self):
        self.assertEqual(FahrenheitToCelsius(32), 0)
        self.assertEqual(FahrenheitToCelsius(98.6), 37)


if __name__ == "__main__":
    unittest.main()
