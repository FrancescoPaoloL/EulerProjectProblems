'''
The sequence of triangle numbers is generated 
by adding the natural numbers. 
So the 7th triangle number would be 

    1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
    
The first ten terms would be:

    1, 
    (1 + 2) = 3, 
    (1 + 2 + 3) = 6, 
    (1 + 2 + 3 + 4) = 10, 
    (1 + 2 + 3 + 4 + 5) = 15, 
    (1 + 2 + 3 + 4 + 5 + 6) = 21, 
    (1 + 2 + 3 + 4 + 5 + 6 + 7) = 28, 
    ...36, 
    ...45, 
    ...55, 
    ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number 
to have over five divisors.

What is the value of the first triangle number 
to have over five hundred divisors?

---

answer = 76576500

'''
import time

def factor_count(number: int) -> int:
    factors = 0
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            factors += 2
        if int(number ** 0.5) ** 2 == number:
            factors -= 1
    return factors

def f(limit: int):
    triangle_number = 1
    count = 1
    while True:
        if factor_count(triangle_number) > limit:
            return triangle_number
        count += 1
        triangle_number += count

if __name__ == '__main__':
    print('Start!')
    start_time = time.time()
    limit = 500
    print(f'The value of the first triangle number with {limit} numbers is {f(limit)}')
    print("--- %s seconds ---" % (time.time() - start_time))

''''''''''''

# rows, cols = 20, 20
# matrix = [([0]*cols) for i in range(rows)]
