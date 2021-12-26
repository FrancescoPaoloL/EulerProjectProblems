'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

To verify:
    https://www.calculatorsoup.com/calculators/math/prime-factors.php

'''

# In simple words, prime factor is finding which 
# prime numbers multiply together to make the 
# original number.
# Remember that: the largest prime factor 
# will never be larger than the square root of n

import time

print('Start!')
start_time = time.time()

nrStart = n = 600851475143
pf = 2


# pf < sqrt(n) --> pf^2 < n --> pf * pf  < n
while pf * pf < n:
    while n % pf == 0:
        n = n / pf
    pf = pf + 1

print(f'The largest prime factor of {nrStart} is {n}')
print("--- %s seconds ---" % (time.time() - start_time))