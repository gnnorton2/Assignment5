import unittest
from FinonacciConversion import FibonacciConversion


class TestFibonacci(unittest.TestCase):
    def testFibonacci(self):
        self.assertEqual(FibonacciConversion(13), 233)
        self.assertEqual(FibonacciConversion(5), 5)

    def testFibonacciNegative(self):
        with self.assertRaises(ValueError):
            FibonacciConversion(-1)


if __name__ == "__main__":
    unittest.main()
