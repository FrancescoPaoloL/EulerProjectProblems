'''
The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    ( 1 + 2 + ... + 9 + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

    3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''
import time

def findDiff():
    tmp = 0
    sm = 0

    for i in range(1, 101):
        tmp += i**2
        sm += i

    return (sm**2) - tmp

if __name__ == '__main__':
    print('Start!')
    start_time = time.time()
    print(f'The result is {findDiff()}')
    print("--- %s seconds ---" % (time.time() - start_time))
