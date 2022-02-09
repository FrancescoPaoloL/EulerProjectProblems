'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

'''
import time

print('Start!')
start_time = time.time()

exp = 1000 #15

result = pow(2, exp)
tmp = str(result)
sum = 0

for i in range(len(tmp)):
    sum += int(tmp[i])

print(f'The sum of the digits of the number 2^{exp} is: {sum}')
print("--- %s seconds ---" % (time.time() - start_time))
