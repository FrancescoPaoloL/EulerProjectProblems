import unittest
from FibonacciProblem02 import sum_of_even_fibonacci_numbers

class TestSumOfEvenFibonacciNumbertres(unittest.TestCase):
    def test_limit_10(self):
        self.assertEqual(sum_of_even_fibonacci_numbers(10), 10)

    def test_limit_100(self):
        self.assertEqual(sum_of_even_fibonacci_numbers(100), 44)

    def test_limit_1000(self):
        self.assertEqual(sum_of_even_fibonacci_numbers(1000), 798)

    def test_limit_4000000(self):
        self.assertEqual(sum_of_even_fibonacci_numbers(4000000), 4613732)


if __name__ == '__main__':
    unittest.main()