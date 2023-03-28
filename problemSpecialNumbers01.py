'''
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

'''
import time

def listSpecialNumbers():
    n = 1000
    l = []
    for x in range(1, n):
        if (x % 3) == 0 or (x % 5) == 0:
            l.append(x)
    return l

if __name__ == '__main__':
    start_time = time.time()
    print('Start!')
    limit = 4000000
    l = listSpecialNumbers()
    print(f'The numbers are {l}')
    print(f'The sum is {sum(l)}')
    print("--- %s seconds ---" % (time.time() - start_time))
