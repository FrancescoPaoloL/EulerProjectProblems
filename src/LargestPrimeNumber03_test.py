import unittest
from LargestPrimeNumber03 import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):

    def test_largest_prime_factor(self):
        test_cases = [
            {'input': 10, 'expected_output': 5},
            {'input': 13195, 'expected_output': 29},
            {'input': 600851475143, 'expected_output': 6857}
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                input_value = test_case['input']
                expected_output = test_case['expected_output']
                actual_output = largest_prime_factor(input_value)
                print(f"\nInput: {input_value}, Expected Output: {expected_output}, Actual Output: {actual_output}")
                self.assertEqual(actual_output, expected_output)
