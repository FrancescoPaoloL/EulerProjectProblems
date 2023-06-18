'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

import time

print('Start!')
start_time = time.time()

def primes(n):  
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * ((n - i*i - 1)//(2*i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


if __name__ == '__main__':
    kLimit = 2000000
    listPN = primes(kLimit)

    print(f'The sum of first {kLimit} prime number is {sum(listPN)}')
    print("--- %s seconds ---" % (time.time() - start_time))
