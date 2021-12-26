'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


ex
    1, 2, 3, 4, 5, 6, 7,  8,  9, 10 ...

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, ...
'''

import time
import decimal



def formulaFib(n):
    decimal.getcontext().prec = 900000

    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)
    a = ((phi ** n) - ((-phi) ** -n)) / root_5
    return round(a)


print('Start calculating the sum of the even-valued terms (about 4G items!')
start_time = time.time()
limit = 4000001
mysum = 0

# print(formulaFib(limit))

for x in range(2, limit):
    tmp = formulaFib(x)
    if (tmp % 2) == 0:
        mysum += tmp

# print(f'The Fibonacci sequence is {l}')
# # print(f'The even list is {even}')
print(f'The sum is {mysum}')
print("--- %s seconds ---" % (time.time() - start_time))


