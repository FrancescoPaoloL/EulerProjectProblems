import unittest
from SumOfPrimes10 import primes

class TestPrimes(unittest.TestCase):
    
    def test_primes(self):
        self.assertEqual(primes(10), [2, 3, 5, 7])
        self.assertEqual(primes(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(primes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    
    def test_sum_primes(self):
        self.assertEqual(sum(primes(10)), 17)
        self.assertEqual(sum(primes(20)), 77)
        self.assertEqual(sum(primes(30)), 129)
    
if __name__ == '__main__':
    unittest.main()
