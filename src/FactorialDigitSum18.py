# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

import math
import time

def factorialDigitSum(n):
    sum = 0
    for i in str(math.factorial(n)):
        sum += int(i)
    return sum


if __name__ == '__main__':
    print('Start!')
    start_time = time.time()
    print(factorialDigitSum(100))
    print(f'The sum of the digits in the number 100! is {factorialDigitSum(100)}')
    print("--- %s seconds ---" % (time.time() - start_time))

        
