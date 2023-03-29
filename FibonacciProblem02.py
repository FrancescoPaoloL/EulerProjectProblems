'''
Each new term in the Fibonacci sequence is generated by
adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose
values do not exceed four million, find the sum of the
even-valued terms.

ex
    1, 2, 3, 4, 5, 6, 7,  8,  9, 10 ...

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
    144, 233, 377, 610, 987, 1597, 2584, 4181,
    6765, 10946, 17711, 28657, 46368, 75025,
    121393, 196418, 317811, ...
'''

import time

def sum_of_even_fibonacci_numbers(limit):
    seq = [0, 1]
    mysum = 0

    while True:
        lng = len(seq)

        tmp = seq[lng - 1] + seq[lng - 2]
        if tmp > limit:
            break

        if (tmp % 2) == 0:
            mysum += tmp
        seq.append(tmp)

    return mysum


if __name__ == '__main__':
    start_time = time.time()
    print('Start!')
    limit = 4000000
    mysum = sum_of_even_fibonacci_numbers(limit)
    print(f'The sum is {mysum}')
    print("--- %s seconds ---" % (time.time() - start_time))