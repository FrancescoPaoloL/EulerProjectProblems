'''
The following iterative sequence is defined 
for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, 
we generate the following sequence:

13 is odd   --> n → 3n + 1  --> 3*13+1  = 40
40 is even  --> n → n/2     --> 40/2    = 20
20 is even  --> n → n/2     --> 20/2    = 10
10 is even  --> n → n/2     --> 10/2    = 5
5 is odd    --> n → 3n + 1  --> 3*5+1   = 16
16 is even  --> n → n/2     --> 16/2    = 8
8 is even   --> n → n/2     --> 8/2     = 4
4 is even   --> n → n/2     --> 4/2     = 2
2 is even   --> n → n/2     --> 2/2     = 1

So:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1


It can be seen that this sequence (starting at 13 
and finishing at 1) contains 10 terms. 

Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

note: Once the chain starts the terms are allowed to go above one million.

'''

import time

def doCollatz(nrSeq):
    maxItems = 0
    lst = []
    mynumber = 0

    for n in range(nrSeq, 1, -1):
        tmp = n
        # print(n)
        lst.clear()
        lst.append(n)
        while (n > 1):
            if (n % 2 > 0):
                n = 3*n + 1
            else:
                n = n / 2
            lst.append(int(n))
        lng = len(lst)
        if maxItems < lng:
            maxItems = lng
            mynumber = tmp
        # print(maxItems)
    return mynumber

if __name__ == '__main__':
    print('Start!')
    start_time = time.time()
    print(f'The starting number which produces the longest chain is {doCollatz(999999)}')
    print("--- %s seconds ---" % (time.time() - start_time))
