'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

---
Numbers that read the same backwards and forwards.
    ex. "17371" is a Palindromic Number.
        "5" is also a Palindromic Number.
        But "1234" is NOT, because
            backwards it is "4321" (not the same).

Then
    10 x 10 = 100 -> not
    ...
    99 x 90 = 8910 --> not
    99 x 91 = 9009 --> OK
    99 x 92 = 9108 --> not
    etc

Find 3 digits:
    100 x 100 = 10000 -> not
    ...

'''
import time

class Max:
    i = 0

    def chkMax(self, nr):
        if nr > Max.i:
            Max.i = nr

def find_largest_palindrome():
    tmp = 0
    m = Max()

    for f1 in range(100, 1000):
        for f2 in range(100, 1000):
            tmp = f1 * f2
            if str(tmp) == str(tmp)[::-1]:
                m.chkMax(tmp)
    return Max.i

print('Start!')
start_time = time.time()
print(f'The largest palindrome number is {find_largest_palindrome()}')
print("--- %s seconds ---" % (time.time() - start_time))
