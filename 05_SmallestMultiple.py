'''
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any
remainder.

What is the smallest positive number that is
evenly divisible by all of the numbers from
1 to 20?

---
2520 / 1 = 2520
2520 / 2 = 1260
...
2520 / 7 = 360
...
2520 / 10 = 252

see:
    https://www.quora.com/What-is-the-least-number-divisible-by-all-numbers-between-1-and-11-inclusive-of-1-and11?share=1

'''
import time


def chkMod(nummber):
    for item in range(1, 21):
        if (x % item) != 0:
            return False
    return True


print('Start!')
start_time = time.time()

x = 0

while True:
    x += 20
    if chkMod(x):
        break

print(f'The smallest positive number is {x}')
print("--- %s seconds ---" % (time.time() - start_time))
