'''
A Pythagorean triplet is a set of three natural
numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example:

    3^2 + 4^2 = 9 + 16 = 25 = 5^2.

--> 3 4 5

There exists exactly one Pythagorean triplet
for which

    a + b + c = 1000.

Find the product abc.

---
Euclid's formula is the fundamental formula
for generating the Pythagorean Triplets (PT)

    a = m^2 - n^2
    b = 2 *m * n
    c = m^2 + n^2

This for every integer 'm' and 'n'.
'''

import time

print('Start!')
start_time = time.time()


def PythagoreanTriplets():
    m = 0
    n = 0
    while True:
        for n in range(1, m+1):
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n

            if (a == 0 or b == 0 or c == 0):
                break

            if (a + b + c) == 1000:
                return a, b, c
            # print(a, b, c)
        m += 1



if __name__ == '__main__':
    a, b, c = PythagoreanTriplets()
    print(f'The product is {a*b*c}')
    print("--- %s seconds ---" % (time.time() - start_time))
