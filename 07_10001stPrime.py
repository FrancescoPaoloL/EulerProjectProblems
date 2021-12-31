'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime number?

---
I'm going to use the "sieve of Eratosthenes" that is one of the 
most efficient ways to find all primes smaller than 'n' when 'n' 
is smaller than 10 million or so.


'''
import time

def isPrime(nr):
    for i in range(2, nr - 1):
        if (nr % i) == 0:
            return False
    return True


print('Start!')
start_time = time.time()
kLimit = 10001
count = 1
countPN = 0
last = 0

while countPN < kLimit:
    count += 1
    if isPrime(count):
        last = count
        countPN += 1


print(f'The last PN is {last}, in {countPN} position')
print("--- %s seconds ---" % (time.time() - start_time))
