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

def f(L, nMax=45000):
    d = [0]*nMax
    for n in range(1, nMax):
        for j in range(n, nMax, n):
            d[j]+= 1
        nDiv = d[n-1]*d[n//2] if n%2==0 else d[(n-1)//2]*d[n]
        if nDiv > L: return (n-1)*n//2
for _ in range(int(input())):
    print (f(int(input())))


i = 0
kLimit = 500

# OK
def factors(x):
    i = 0
    q = 0
    lstFactor = []
    #print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            #print(i)
            lstFactor.append(i)
            q += 1
    #print(f'q = {q} and lstFactor={lstFactor}') 
    return lstFactor

print('Start!')
start_time = time.time()
seq = []
fct = []

# factors(40)


tmp = 0
i = 1
while True:
    lng = len(seq)

    tmp += i

    seq.append(tmp)
    
    fct = factors(seq[-1])
    print(seq[-1]) 
    if len(fct) >= kLimit:
        break
    i += 1

print(f'The value of the first triangle number with {kLimit} numbers is {seq[-1]}')
print(f'because {fct}')
print("--- %s seconds ---" % (time.time() - start_time))


''''''''''''

# rows, cols = 20, 20
# matrix = [([0]*cols) for i in range(rows)]
