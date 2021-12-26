'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

# In simple words, prime factor is finding which 
# prime numbers multiply together to make the 
# original number.
# Remember that: the largest prime factor 
# will never be larger than the square root of n

n = 840 #600851475143
pf = 2

while pf * pf < n:
    while n % pf == 0:
        n = n / pf
    pf = pf + 1

print (n)
